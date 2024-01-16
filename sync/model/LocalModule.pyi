from pathlib import Path
from typing import Dict, Type

from .AttrDict import AttrDict
from .TrackJson import TrackJson


class LocalModule(AttrDict):
    id: str
    name: str
    version: str
    versionCode: int
    author: str
    description: str

    @classmethod
    def load(cls, file: Path, track: TrackJson) -> LocalModule: ...
    @classmethod
    def expected_fields(cls, __type: bool = ...) -> Dict[str, Type]: ...
