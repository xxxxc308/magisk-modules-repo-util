from typing import Dict, Type

from .AttrDict import AttrDict


class ModuleFeatures(AttrDict):
    service: bool
    post_fs_data: bool
    # system.prop
    resetprop: bool
    sepolicy: bool
    zygisk: bool
    apks: bool
    
    # KernelSU
    webroot: bool
    post_mount: bool
    boot_completed: bool
    
    # MMRL
    modconf: bool

    @classmethod
    def expected_fields(cls, __type: bool = ...) -> Dict[str, Type]: ...
