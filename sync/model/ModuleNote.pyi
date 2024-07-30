from typing import Dict, Type

from .AttrDict import AttrDict


class ModuleNote(AttrDict):
    color: str
    title: str
    message: str

    @classmethod
    def expected_fields(cls, __type: bool = ...) -> Dict[str, Type]: ...
