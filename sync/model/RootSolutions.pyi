from .AttrDict import AttrDict
from typing import Dict, Type

class RootSolutions(AttrDict):
    magisk: str
    kernelsu: str
    apatch: str
    
    @classmethod
    def expected_fields(cls, __type=True) -> Dict[str, Type]: ...