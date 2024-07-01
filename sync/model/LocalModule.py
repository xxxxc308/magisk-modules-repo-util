import json

from zipfile import ZipFile

from .AttrDict import AttrDict
from ..error import MagiskModuleError

from ..utils import (
    Log,
)


class LocalModule(AttrDict):
    id: str
    name: str
    version: str
    versionCode: int
    author: str
    description: str
    added: int
    timestamp: float
    category: str
    categories: list[str]
    icon: str
    # antifeatures: list[str]
    homepage: str
    donate: str
    support: str
    cover: str
    screenshots: list[str]
    license: str
    screenshots: list[str]
    readme: str
    require: list[str]
    verified: bool

    @classmethod
    def load(cls, file, track):
        zipfile = ZipFile(file, "r")
        fields = cls.expected_fields()

        try:
            if (
                "#MAGISK" not in zipfile
                .read("META-INF/com/google/android/updater-script")
                .decode("utf-8")
            ):
                raise

            zipfile.read("META-INF/com/google/android/update-binary")
        except BaseException:
            msg = f"{file.name} is not a magisk module"
            raise MagiskModuleError(msg)

        try:
            props = zipfile.read("module.prop")
        except BaseException as err:
            raise MagiskModuleError(err.args)

        obj = AttrDict()
        for item in props.decode("utf-8").splitlines():
            prop = item.split("=", maxsplit=1)
            if len(prop) != 2:
                continue

            key, value = prop
            if key == "" or key.startswith("#") or key not in fields:
                continue

            _type = fields[key]
            obj[key] = _type(value)

        local_module = LocalModule()
        for key in fields.keys():
            local_module[key] = obj.get(key)

        try:
            raw_json = json.loads(zipfile.read("common/repo.json").decode("utf-8"))

            for item in raw_json.items():
                key, value = item
                
                _type = fields[key]
                obj[key] = _type(value)
                
                for key in fields.keys():
                    local_module[key] = obj.get(key)
        except BaseException:
            pass

        local_module.verified = track.verified or False
        local_module.added = track.added or 0
        local_module.timestamp = track.last_update

        return local_module

    @classmethod
    def expected_fields(cls, __type=True):
        if __type:
            return cls.__annotations__

        return {k: v.__name__ for k, v in cls.__annotations__.items()}
