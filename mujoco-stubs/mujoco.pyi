""" My generated .pyi file for MuJoCo """

# from mujoco import _specs
# from mujoco import _structs
# from mujoco._callbacks import *
# from mujoco._constants import *
# from mujoco._enums import *
# from mujoco._errors import *
# from mujoco._functions import *
# from mujoco._render import *
# from mujoco._specs import *
# from mujoco._structs import *
# from mujoco.gl_context import *
# from mujoco.renderer import Renderer

# --- mujoco._callbacks ---
def get_mjcb_act_bias() -> object:
    """get_mjcb_act_bias() -> object"""
def get_mjcb_act_dyn() -> object:
    """get_mjcb_act_dyn() -> object"""
def get_mjcb_act_gain() -> object:
    """get_mjcb_act_gain() -> object"""
def get_mjcb_contactfilter() -> object:
    """get_mjcb_contactfilter() -> object"""
def get_mjcb_control() -> object:
    """get_mjcb_control() -> object"""
def get_mjcb_passive() -> object:
    """get_mjcb_passive() -> object"""
def get_mjcb_sensor() -> object:
    """get_mjcb_sensor() -> object"""
def get_mjcb_time() -> object:
    """get_mjcb_time() -> object"""
def get_mju_user_free() -> object:
    """get_mju_user_free() -> object"""
def get_mju_user_malloc() -> object:
    """get_mju_user_malloc() -> object"""
def get_mju_user_warning() -> object:
    """get_mju_user_warning() -> object"""
def set_mjcb_act_bias(arg0: object) -> None:
    """set_mjcb_act_bias(arg0: object) -> None"""
def set_mjcb_act_dyn(arg0: object) -> None:
    """set_mjcb_act_dyn(arg0: object) -> None"""
def set_mjcb_act_gain(arg0: object) -> None:
    """set_mjcb_act_gain(arg0: object) -> None"""
def set_mjcb_contactfilter(arg0: object) -> None:
    """set_mjcb_contactfilter(arg0: object) -> None"""
def set_mjcb_control(arg0: object) -> None:
    """set_mjcb_control(arg0: object) -> None"""
def set_mjcb_passive(arg0: object) -> None:
    """set_mjcb_passive(arg0: object) -> None"""
def set_mjcb_sensor(arg0: object) -> None:
    """set_mjcb_sensor(arg0: object) -> None"""
def set_mjcb_time(arg0: object) -> None:
    """set_mjcb_time(arg0: object) -> None"""
def set_mju_user_free(arg0: object) -> None:
    """set_mju_user_free(arg0: object) -> None"""
def set_mju_user_malloc(arg0: object) -> None:
    """set_mju_user_malloc(arg0: object) -> None"""
def set_mju_user_warning(arg0: object) -> None:
    """set_mju_user_warning(arg0: object) -> None"""

# --- mujoco._constants ---
mjDISABLESTRING: tuple
mjENABLESTRING: tuple
mjFRAMESTRING: tuple
mjLABELSTRING: tuple
mjMAXCONPAIR: int
mjMAXIMP: float
mjMAXLIGHT: int
mjMAXLINE: int
mjMAXLINEPNT: int
mjMAXOVERLAY: int
mjMAXPLANEGRID: int
mjMAXVAL: float
mjMINIMP: float
mjMINMU: float
mjMINVAL: float
mjNBIAS: int
mjNDYN: int
mjNEQDATA: int
mjNGAIN: int
mjNGROUP: int
mjNIMP: int
mjNREF: int
mjNSOLVER: int
mjPI: float
mjRNDSTRING: tuple
mjTIMERSTRING: tuple
mjVERSION_HEADER: int
mjVISSTRING: tuple

# --- mujoco._enums ---
from typing import ClassVar, overload

class mjtAlignFree:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjALIGNFREE_AUTO: ClassVar[mjtAlignFree] = ...
    mjALIGNFREE_FALSE: ClassVar[mjtAlignFree] = ...
    mjALIGNFREE_TRUE: ClassVar[mjtAlignFree] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtAlignFree, value: int) -> None

        2. __init__(self: mujoco._enums.mjtAlignFree, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtAlignFree, value: int) -> None

        2. __init__(self: mujoco._enums.mjtAlignFree, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtAlignFree) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtAlignFree) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtAlignFree) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtAlignFree, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtAlignFree, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtBias:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjBIAS_AFFINE: ClassVar[mjtBias] = ...
    mjBIAS_MUSCLE: ClassVar[mjtBias] = ...
    mjBIAS_NONE: ClassVar[mjtBias] = ...
    mjBIAS_USER: ClassVar[mjtBias] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtBias, value: int) -> None

        2. __init__(self: mujoco._enums.mjtBias, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtBias, value: int) -> None

        2. __init__(self: mujoco._enums.mjtBias, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtBias, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtBias) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtBias) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtBias, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtBias) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtBias, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtBias, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtBias, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtBias, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtBias, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtBias, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtBias, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtBias, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtBias, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtBias, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtBuiltin:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjBUILTIN_CHECKER: ClassVar[mjtBuiltin] = ...
    mjBUILTIN_FLAT: ClassVar[mjtBuiltin] = ...
    mjBUILTIN_GRADIENT: ClassVar[mjtBuiltin] = ...
    mjBUILTIN_NONE: ClassVar[mjtBuiltin] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtBuiltin, value: int) -> None

        2. __init__(self: mujoco._enums.mjtBuiltin, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtBuiltin, value: int) -> None

        2. __init__(self: mujoco._enums.mjtBuiltin, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtBuiltin) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtBuiltin) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtBuiltin) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtBuiltin, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtBuiltin, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtButton:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjBUTTON_LEFT: ClassVar[mjtButton] = ...
    mjBUTTON_MIDDLE: ClassVar[mjtButton] = ...
    mjBUTTON_NONE: ClassVar[mjtButton] = ...
    mjBUTTON_RIGHT: ClassVar[mjtButton] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtButton, value: int) -> None

        2. __init__(self: mujoco._enums.mjtButton, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtButton, value: int) -> None

        2. __init__(self: mujoco._enums.mjtButton, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtButton, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtButton) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtButton) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtButton, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtButton) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtButton, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtButton, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtButton, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtButton, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtButton, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtButton, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtButton, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtButton, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtButton, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtButton, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtCamLight:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjCAMLIGHT_FIXED: ClassVar[mjtCamLight] = ...
    mjCAMLIGHT_TARGETBODY: ClassVar[mjtCamLight] = ...
    mjCAMLIGHT_TARGETBODYCOM: ClassVar[mjtCamLight] = ...
    mjCAMLIGHT_TRACK: ClassVar[mjtCamLight] = ...
    mjCAMLIGHT_TRACKCOM: ClassVar[mjtCamLight] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtCamLight, value: int) -> None

        2. __init__(self: mujoco._enums.mjtCamLight, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtCamLight, value: int) -> None

        2. __init__(self: mujoco._enums.mjtCamLight, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtCamLight, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtCamLight) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtCamLight) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtCamLight, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtCamLight) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtCamLight, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtCamLight, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtCamLight, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtCamLight, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtCamLight, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtCamLight, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtCamLight, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtCamLight, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtCamLight, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtCamLight, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtCamera:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjCAMERA_FIXED: ClassVar[mjtCamera] = ...
    mjCAMERA_FREE: ClassVar[mjtCamera] = ...
    mjCAMERA_TRACKING: ClassVar[mjtCamera] = ...
    mjCAMERA_USER: ClassVar[mjtCamera] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtCamera, value: int) -> None

        2. __init__(self: mujoco._enums.mjtCamera, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtCamera, value: int) -> None

        2. __init__(self: mujoco._enums.mjtCamera, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtCamera, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtCamera) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtCamera) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtCamera, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtCamera) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtCamera, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtCamera, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtCamera, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtCamera, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtCamera, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtCamera, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtCamera, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtCamera, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtCamera, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtCamera, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtCatBit:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjCAT_ALL: ClassVar[mjtCatBit] = ...
    mjCAT_DECOR: ClassVar[mjtCatBit] = ...
    mjCAT_DYNAMIC: ClassVar[mjtCatBit] = ...
    mjCAT_STATIC: ClassVar[mjtCatBit] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtCatBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtCatBit, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtCatBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtCatBit, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtCatBit, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtCatBit) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtCatBit) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtCatBit, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtCatBit) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtCatBit, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtCatBit, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtCatBit, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtCatBit, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtCatBit, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtCatBit, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtCatBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtCatBit, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtCatBit, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtCatBit, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtCone:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjCONE_ELLIPTIC: ClassVar[mjtCone] = ...
    mjCONE_PYRAMIDAL: ClassVar[mjtCone] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtCone, value: int) -> None

        2. __init__(self: mujoco._enums.mjtCone, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtCone, value: int) -> None

        2. __init__(self: mujoco._enums.mjtCone, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtCone, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtCone) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtCone) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtCone, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtCone) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtCone, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtCone, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtCone, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtCone, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtCone, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtCone, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtCone, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtCone, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtCone, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtCone, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtConstraint:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjCNSTR_CONTACT_ELLIPTIC: ClassVar[mjtConstraint] = ...
    mjCNSTR_CONTACT_FRICTIONLESS: ClassVar[mjtConstraint] = ...
    mjCNSTR_CONTACT_PYRAMIDAL: ClassVar[mjtConstraint] = ...
    mjCNSTR_EQUALITY: ClassVar[mjtConstraint] = ...
    mjCNSTR_FRICTION_DOF: ClassVar[mjtConstraint] = ...
    mjCNSTR_FRICTION_TENDON: ClassVar[mjtConstraint] = ...
    mjCNSTR_LIMIT_JOINT: ClassVar[mjtConstraint] = ...
    mjCNSTR_LIMIT_TENDON: ClassVar[mjtConstraint] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtConstraint, value: int) -> None

        2. __init__(self: mujoco._enums.mjtConstraint, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtConstraint, value: int) -> None

        2. __init__(self: mujoco._enums.mjtConstraint, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtConstraint, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtConstraint) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtConstraint) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtConstraint, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtConstraint) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtConstraint, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtConstraint, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtConstraint, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtConstraint, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtConstraint, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtConstraint, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtConstraint, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtConstraint, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtConstraint, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtConstraint, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtConstraintState:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjCNSTRSTATE_CONE: ClassVar[mjtConstraintState] = ...
    mjCNSTRSTATE_LINEARNEG: ClassVar[mjtConstraintState] = ...
    mjCNSTRSTATE_LINEARPOS: ClassVar[mjtConstraintState] = ...
    mjCNSTRSTATE_QUADRATIC: ClassVar[mjtConstraintState] = ...
    mjCNSTRSTATE_SATISFIED: ClassVar[mjtConstraintState] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtConstraintState, value: int) -> None

        2. __init__(self: mujoco._enums.mjtConstraintState, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtConstraintState, value: int) -> None

        2. __init__(self: mujoco._enums.mjtConstraintState, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtConstraintState) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtConstraintState) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtConstraintState) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtConstraintState, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtConstraintState, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtDataType:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjDATATYPE_AXIS: ClassVar[mjtDataType] = ...
    mjDATATYPE_POSITIVE: ClassVar[mjtDataType] = ...
    mjDATATYPE_QUATERNION: ClassVar[mjtDataType] = ...
    mjDATATYPE_REAL: ClassVar[mjtDataType] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtDataType, value: int) -> None

        2. __init__(self: mujoco._enums.mjtDataType, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtDataType, value: int) -> None

        2. __init__(self: mujoco._enums.mjtDataType, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtDataType, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtDataType) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtDataType) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtDataType, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtDataType) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtDataType, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtDataType, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtDataType, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtDataType, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtDataType, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtDataType, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtDataType, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtDataType, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtDataType, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtDataType, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtDepthMap:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjDEPTH_ZEROFAR: ClassVar[mjtDepthMap] = ...
    mjDEPTH_ZERONEAR: ClassVar[mjtDepthMap] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtDepthMap, value: int) -> None

        2. __init__(self: mujoco._enums.mjtDepthMap, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtDepthMap, value: int) -> None

        2. __init__(self: mujoco._enums.mjtDepthMap, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtDepthMap) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtDepthMap) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtDepthMap) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtDepthMap, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtDepthMap, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtDisableBit:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjDSBL_ACTUATION: ClassVar[mjtDisableBit] = ...
    mjDSBL_AUTORESET: ClassVar[mjtDisableBit] = ...
    mjDSBL_CLAMPCTRL: ClassVar[mjtDisableBit] = ...
    mjDSBL_CONSTRAINT: ClassVar[mjtDisableBit] = ...
    mjDSBL_CONTACT: ClassVar[mjtDisableBit] = ...
    mjDSBL_EQUALITY: ClassVar[mjtDisableBit] = ...
    mjDSBL_EULERDAMP: ClassVar[mjtDisableBit] = ...
    mjDSBL_FILTERPARENT: ClassVar[mjtDisableBit] = ...
    mjDSBL_FRICTIONLOSS: ClassVar[mjtDisableBit] = ...
    mjDSBL_GRAVITY: ClassVar[mjtDisableBit] = ...
    mjDSBL_LIMIT: ClassVar[mjtDisableBit] = ...
    mjDSBL_MIDPHASE: ClassVar[mjtDisableBit] = ...
    mjDSBL_NATIVECCD: ClassVar[mjtDisableBit] = ...
    mjDSBL_PASSIVE: ClassVar[mjtDisableBit] = ...
    mjDSBL_REFSAFE: ClassVar[mjtDisableBit] = ...
    mjDSBL_SENSOR: ClassVar[mjtDisableBit] = ...
    mjDSBL_WARMSTART: ClassVar[mjtDisableBit] = ...
    mjNDISABLE: ClassVar[mjtDisableBit] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtDisableBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtDisableBit, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtDisableBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtDisableBit, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtDisableBit) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtDisableBit) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtDisableBit) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtDisableBit, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtDisableBit, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtDyn:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjDYN_FILTER: ClassVar[mjtDyn] = ...
    mjDYN_FILTEREXACT: ClassVar[mjtDyn] = ...
    mjDYN_INTEGRATOR: ClassVar[mjtDyn] = ...
    mjDYN_MUSCLE: ClassVar[mjtDyn] = ...
    mjDYN_NONE: ClassVar[mjtDyn] = ...
    mjDYN_USER: ClassVar[mjtDyn] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtDyn, value: int) -> None

        2. __init__(self: mujoco._enums.mjtDyn, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtDyn, value: int) -> None

        2. __init__(self: mujoco._enums.mjtDyn, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtDyn, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtDyn) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtDyn) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtDyn, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtDyn) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtDyn, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtDyn, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtDyn, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtDyn, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtDyn, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtDyn, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtDyn, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtDyn, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtDyn, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtDyn, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtEnableBit:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjENBL_ENERGY: ClassVar[mjtEnableBit] = ...
    mjENBL_FWDINV: ClassVar[mjtEnableBit] = ...
    mjENBL_INVDISCRETE: ClassVar[mjtEnableBit] = ...
    mjENBL_ISLAND: ClassVar[mjtEnableBit] = ...
    mjENBL_MULTICCD: ClassVar[mjtEnableBit] = ...
    mjENBL_OVERRIDE: ClassVar[mjtEnableBit] = ...
    mjNENABLE: ClassVar[mjtEnableBit] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtEnableBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtEnableBit, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtEnableBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtEnableBit, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtEnableBit) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtEnableBit) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtEnableBit) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtEnableBit, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtEnableBit, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtEq:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjEQ_CONNECT: ClassVar[mjtEq] = ...
    mjEQ_DISTANCE: ClassVar[mjtEq] = ...
    mjEQ_FLEX: ClassVar[mjtEq] = ...
    mjEQ_JOINT: ClassVar[mjtEq] = ...
    mjEQ_TENDON: ClassVar[mjtEq] = ...
    mjEQ_WELD: ClassVar[mjtEq] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtEq, value: int) -> None

        2. __init__(self: mujoco._enums.mjtEq, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtEq, value: int) -> None

        2. __init__(self: mujoco._enums.mjtEq, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtEq, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtEq) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtEq) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtEq, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtEq) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtEq, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtEq, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtEq, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtEq, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtEq, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtEq, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtEq, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtEq, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtEq, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtEq, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtEvent:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjEVENT_FILESDROP: ClassVar[mjtEvent] = ...
    mjEVENT_KEY: ClassVar[mjtEvent] = ...
    mjEVENT_MOVE: ClassVar[mjtEvent] = ...
    mjEVENT_NONE: ClassVar[mjtEvent] = ...
    mjEVENT_PRESS: ClassVar[mjtEvent] = ...
    mjEVENT_REDRAW: ClassVar[mjtEvent] = ...
    mjEVENT_RELEASE: ClassVar[mjtEvent] = ...
    mjEVENT_RESIZE: ClassVar[mjtEvent] = ...
    mjEVENT_SCROLL: ClassVar[mjtEvent] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtEvent, value: int) -> None

        2. __init__(self: mujoco._enums.mjtEvent, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtEvent, value: int) -> None

        2. __init__(self: mujoco._enums.mjtEvent, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtEvent, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtEvent) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtEvent) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtEvent, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtEvent) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtEvent, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtEvent, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtEvent, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtEvent, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtEvent, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtEvent, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtEvent, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtEvent, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtEvent, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtEvent, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtFlexSelf:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjFLEXSELF_AUTO: ClassVar[mjtFlexSelf] = ...
    mjFLEXSELF_BVH: ClassVar[mjtFlexSelf] = ...
    mjFLEXSELF_NARROW: ClassVar[mjtFlexSelf] = ...
    mjFLEXSELF_NONE: ClassVar[mjtFlexSelf] = ...
    mjFLEXSELF_SAP: ClassVar[mjtFlexSelf] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFlexSelf, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFlexSelf, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFlexSelf, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFlexSelf, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtFlexSelf) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtFlexSelf) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtFlexSelf) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtFlexSelf, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtFlexSelf, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtFont:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjFONT_BIG: ClassVar[mjtFont] = ...
    mjFONT_NORMAL: ClassVar[mjtFont] = ...
    mjFONT_SHADOW: ClassVar[mjtFont] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFont, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFont, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFont, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFont, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtFont, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtFont) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtFont) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtFont, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtFont) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtFont, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtFont, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtFont, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtFont, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtFont, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtFont, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFont, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFont, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtFont, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtFont, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtFontScale:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjFONTSCALE_100: ClassVar[mjtFontScale] = ...
    mjFONTSCALE_150: ClassVar[mjtFontScale] = ...
    mjFONTSCALE_200: ClassVar[mjtFontScale] = ...
    mjFONTSCALE_250: ClassVar[mjtFontScale] = ...
    mjFONTSCALE_300: ClassVar[mjtFontScale] = ...
    mjFONTSCALE_50: ClassVar[mjtFontScale] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFontScale, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFontScale, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFontScale, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFontScale, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtFontScale, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtFontScale) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtFontScale) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtFontScale, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtFontScale) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtFontScale, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtFontScale, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtFontScale, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtFontScale, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtFontScale, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtFontScale, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFontScale, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFontScale, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtFontScale, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtFontScale, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtFrame:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjFRAME_BODY: ClassVar[mjtFrame] = ...
    mjFRAME_CAMERA: ClassVar[mjtFrame] = ...
    mjFRAME_CONTACT: ClassVar[mjtFrame] = ...
    mjFRAME_GEOM: ClassVar[mjtFrame] = ...
    mjFRAME_LIGHT: ClassVar[mjtFrame] = ...
    mjFRAME_NONE: ClassVar[mjtFrame] = ...
    mjFRAME_SITE: ClassVar[mjtFrame] = ...
    mjFRAME_WORLD: ClassVar[mjtFrame] = ...
    mjNFRAME: ClassVar[mjtFrame] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFrame, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFrame, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFrame, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFrame, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtFrame, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtFrame) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtFrame) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtFrame, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtFrame) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtFrame, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtFrame, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtFrame, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtFrame, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtFrame, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtFrame, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFrame, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFrame, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtFrame, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtFrame, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtFramebuffer:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjFB_OFFSCREEN: ClassVar[mjtFramebuffer] = ...
    mjFB_WINDOW: ClassVar[mjtFramebuffer] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFramebuffer, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFramebuffer, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtFramebuffer, value: int) -> None

        2. __init__(self: mujoco._enums.mjtFramebuffer, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtFramebuffer) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtFramebuffer) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtFramebuffer) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtFramebuffer, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtFramebuffer, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtGain:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjGAIN_AFFINE: ClassVar[mjtGain] = ...
    mjGAIN_FIXED: ClassVar[mjtGain] = ...
    mjGAIN_MUSCLE: ClassVar[mjtGain] = ...
    mjGAIN_USER: ClassVar[mjtGain] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtGain, value: int) -> None

        2. __init__(self: mujoco._enums.mjtGain, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtGain, value: int) -> None

        2. __init__(self: mujoco._enums.mjtGain, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtGain, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtGain) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtGain) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtGain, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtGain) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtGain, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtGain, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtGain, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtGain, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtGain, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtGain, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtGain, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtGain, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtGain, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtGain, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtGeom:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjGEOM_ARROW: ClassVar[mjtGeom] = ...
    mjGEOM_ARROW1: ClassVar[mjtGeom] = ...
    mjGEOM_ARROW2: ClassVar[mjtGeom] = ...
    mjGEOM_BOX: ClassVar[mjtGeom] = ...
    mjGEOM_CAPSULE: ClassVar[mjtGeom] = ...
    mjGEOM_CYLINDER: ClassVar[mjtGeom] = ...
    mjGEOM_ELLIPSOID: ClassVar[mjtGeom] = ...
    mjGEOM_FLEX: ClassVar[mjtGeom] = ...
    mjGEOM_HFIELD: ClassVar[mjtGeom] = ...
    mjGEOM_LABEL: ClassVar[mjtGeom] = ...
    mjGEOM_LINE: ClassVar[mjtGeom] = ...
    mjGEOM_LINEBOX: ClassVar[mjtGeom] = ...
    mjGEOM_MESH: ClassVar[mjtGeom] = ...
    mjGEOM_NONE: ClassVar[mjtGeom] = ...
    mjGEOM_PLANE: ClassVar[mjtGeom] = ...
    mjGEOM_SDF: ClassVar[mjtGeom] = ...
    mjGEOM_SKIN: ClassVar[mjtGeom] = ...
    mjGEOM_SPHERE: ClassVar[mjtGeom] = ...
    mjGEOM_TRIANGLE: ClassVar[mjtGeom] = ...
    mjNGEOMTYPES: ClassVar[mjtGeom] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtGeom, value: int) -> None

        2. __init__(self: mujoco._enums.mjtGeom, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtGeom, value: int) -> None

        2. __init__(self: mujoco._enums.mjtGeom, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtGeom, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtGeom) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtGeom) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtGeom, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtGeom) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtGeom, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtGeom, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtGeom, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtGeom, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtGeom, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtGeom, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtGeom, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtGeom, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtGeom, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtGeom, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtGeomInertia:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjINERTIA_SHELL: ClassVar[mjtGeomInertia] = ...
    mjINERTIA_VOLUME: ClassVar[mjtGeomInertia] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtGeomInertia, value: int) -> None

        2. __init__(self: mujoco._enums.mjtGeomInertia, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtGeomInertia, value: int) -> None

        2. __init__(self: mujoco._enums.mjtGeomInertia, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtGeomInertia) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtGeomInertia) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtGeomInertia) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtGeomInertia, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtGeomInertia, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtGridPos:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjGRID_BOTTOM: ClassVar[mjtGridPos] = ...
    mjGRID_BOTTOMLEFT: ClassVar[mjtGridPos] = ...
    mjGRID_BOTTOMRIGHT: ClassVar[mjtGridPos] = ...
    mjGRID_LEFT: ClassVar[mjtGridPos] = ...
    mjGRID_RIGHT: ClassVar[mjtGridPos] = ...
    mjGRID_TOP: ClassVar[mjtGridPos] = ...
    mjGRID_TOPLEFT: ClassVar[mjtGridPos] = ...
    mjGRID_TOPRIGHT: ClassVar[mjtGridPos] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtGridPos, value: int) -> None

        2. __init__(self: mujoco._enums.mjtGridPos, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtGridPos, value: int) -> None

        2. __init__(self: mujoco._enums.mjtGridPos, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtGridPos, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtGridPos) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtGridPos) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtGridPos, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtGridPos) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtGridPos, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtGridPos, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtGridPos, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtGridPos, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtGridPos, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtGridPos, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtGridPos, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtGridPos, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtGridPos, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtGridPos, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtInertiaFromGeom:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjINERTIAFROMGEOM_AUTO: ClassVar[mjtInertiaFromGeom] = ...
    mjINERTIAFROMGEOM_FALSE: ClassVar[mjtInertiaFromGeom] = ...
    mjINERTIAFROMGEOM_TRUE: ClassVar[mjtInertiaFromGeom] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtInertiaFromGeom, value: int) -> None

        2. __init__(self: mujoco._enums.mjtInertiaFromGeom, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtInertiaFromGeom, value: int) -> None

        2. __init__(self: mujoco._enums.mjtInertiaFromGeom, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtInertiaFromGeom) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtInertiaFromGeom) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtInertiaFromGeom) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtInertiaFromGeom, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtInertiaFromGeom, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtIntegrator:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjINT_EULER: ClassVar[mjtIntegrator] = ...
    mjINT_IMPLICIT: ClassVar[mjtIntegrator] = ...
    mjINT_IMPLICITFAST: ClassVar[mjtIntegrator] = ...
    mjINT_RK4: ClassVar[mjtIntegrator] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtIntegrator, value: int) -> None

        2. __init__(self: mujoco._enums.mjtIntegrator, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtIntegrator, value: int) -> None

        2. __init__(self: mujoco._enums.mjtIntegrator, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtIntegrator) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtIntegrator) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtIntegrator) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtIntegrator, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtIntegrator, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtItem:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjITEM_BUTTON: ClassVar[mjtItem] = ...
    mjITEM_CHECKBYTE: ClassVar[mjtItem] = ...
    mjITEM_CHECKINT: ClassVar[mjtItem] = ...
    mjITEM_EDITFLOAT: ClassVar[mjtItem] = ...
    mjITEM_EDITINT: ClassVar[mjtItem] = ...
    mjITEM_EDITNUM: ClassVar[mjtItem] = ...
    mjITEM_EDITTXT: ClassVar[mjtItem] = ...
    mjITEM_END: ClassVar[mjtItem] = ...
    mjITEM_RADIO: ClassVar[mjtItem] = ...
    mjITEM_RADIOLINE: ClassVar[mjtItem] = ...
    mjITEM_SECTION: ClassVar[mjtItem] = ...
    mjITEM_SELECT: ClassVar[mjtItem] = ...
    mjITEM_SEPARATOR: ClassVar[mjtItem] = ...
    mjITEM_SLIDERINT: ClassVar[mjtItem] = ...
    mjITEM_SLIDERNUM: ClassVar[mjtItem] = ...
    mjITEM_STATIC: ClassVar[mjtItem] = ...
    mjNITEM: ClassVar[mjtItem] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtItem, value: int) -> None

        2. __init__(self: mujoco._enums.mjtItem, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtItem, value: int) -> None

        2. __init__(self: mujoco._enums.mjtItem, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtItem, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtItem) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtItem) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtItem, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtItem) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtItem, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtItem, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtItem, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtItem, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtItem, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtItem, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtItem, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtItem, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtItem, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtItem, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtJacobian:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjJAC_AUTO: ClassVar[mjtJacobian] = ...
    mjJAC_DENSE: ClassVar[mjtJacobian] = ...
    mjJAC_SPARSE: ClassVar[mjtJacobian] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtJacobian, value: int) -> None

        2. __init__(self: mujoco._enums.mjtJacobian, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtJacobian, value: int) -> None

        2. __init__(self: mujoco._enums.mjtJacobian, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtJacobian, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtJacobian) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtJacobian) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtJacobian, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtJacobian) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtJacobian, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtJacobian, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtJacobian, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtJacobian, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtJacobian, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtJacobian, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtJacobian, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtJacobian, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtJacobian, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtJacobian, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtJoint:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjJNT_BALL: ClassVar[mjtJoint] = ...
    mjJNT_FREE: ClassVar[mjtJoint] = ...
    mjJNT_HINGE: ClassVar[mjtJoint] = ...
    mjJNT_SLIDE: ClassVar[mjtJoint] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtJoint, value: int) -> None

        2. __init__(self: mujoco._enums.mjtJoint, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtJoint, value: int) -> None

        2. __init__(self: mujoco._enums.mjtJoint, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtJoint, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtJoint) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtJoint) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtJoint, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtJoint) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtJoint, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtJoint, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtJoint, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtJoint, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtJoint, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtJoint, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtJoint, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtJoint, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtJoint, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtJoint, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtLRMode:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjLRMODE_ALL: ClassVar[mjtLRMode] = ...
    mjLRMODE_MUSCLE: ClassVar[mjtLRMode] = ...
    mjLRMODE_MUSCLEUSER: ClassVar[mjtLRMode] = ...
    mjLRMODE_NONE: ClassVar[mjtLRMode] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtLRMode, value: int) -> None

        2. __init__(self: mujoco._enums.mjtLRMode, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtLRMode, value: int) -> None

        2. __init__(self: mujoco._enums.mjtLRMode, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtLRMode, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtLRMode) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtLRMode) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtLRMode, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtLRMode) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtLRMode, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtLRMode, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtLRMode, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtLRMode, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtLRMode, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtLRMode, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtLRMode, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtLRMode, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtLRMode, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtLRMode, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtLabel:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjLABEL_ACTUATOR: ClassVar[mjtLabel] = ...
    mjLABEL_BODY: ClassVar[mjtLabel] = ...
    mjLABEL_CAMERA: ClassVar[mjtLabel] = ...
    mjLABEL_CONSTRAINT: ClassVar[mjtLabel] = ...
    mjLABEL_CONTACTFORCE: ClassVar[mjtLabel] = ...
    mjLABEL_CONTACTPOINT: ClassVar[mjtLabel] = ...
    mjLABEL_FLEX: ClassVar[mjtLabel] = ...
    mjLABEL_GEOM: ClassVar[mjtLabel] = ...
    mjLABEL_ISLAND: ClassVar[mjtLabel] = ...
    mjLABEL_JOINT: ClassVar[mjtLabel] = ...
    mjLABEL_LIGHT: ClassVar[mjtLabel] = ...
    mjLABEL_NONE: ClassVar[mjtLabel] = ...
    mjLABEL_SELECTION: ClassVar[mjtLabel] = ...
    mjLABEL_SELPNT: ClassVar[mjtLabel] = ...
    mjLABEL_SITE: ClassVar[mjtLabel] = ...
    mjLABEL_SKIN: ClassVar[mjtLabel] = ...
    mjLABEL_TENDON: ClassVar[mjtLabel] = ...
    mjNLABEL: ClassVar[mjtLabel] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtLabel, value: int) -> None

        2. __init__(self: mujoco._enums.mjtLabel, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtLabel, value: int) -> None

        2. __init__(self: mujoco._enums.mjtLabel, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtLabel, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtLabel) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtLabel) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtLabel, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtLabel) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtLabel, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtLabel, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtLabel, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtLabel, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtLabel, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtLabel, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtLabel, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtLabel, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtLabel, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtLabel, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtLimited:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjLIMITED_AUTO: ClassVar[mjtLimited] = ...
    mjLIMITED_FALSE: ClassVar[mjtLimited] = ...
    mjLIMITED_TRUE: ClassVar[mjtLimited] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtLimited, value: int) -> None

        2. __init__(self: mujoco._enums.mjtLimited, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtLimited, value: int) -> None

        2. __init__(self: mujoco._enums.mjtLimited, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtLimited, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtLimited) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtLimited) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtLimited, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtLimited) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtLimited, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtLimited, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtLimited, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtLimited, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtLimited, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtLimited, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtLimited, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtLimited, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtLimited, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtLimited, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtMark:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjMARK_CROSS: ClassVar[mjtMark] = ...
    mjMARK_EDGE: ClassVar[mjtMark] = ...
    mjMARK_NONE: ClassVar[mjtMark] = ...
    mjMARK_RANDOM: ClassVar[mjtMark] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtMark, value: int) -> None

        2. __init__(self: mujoco._enums.mjtMark, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtMark, value: int) -> None

        2. __init__(self: mujoco._enums.mjtMark, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtMark, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtMark) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtMark) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtMark, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtMark) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtMark, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtMark, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtMark, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtMark, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtMark, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtMark, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtMark, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtMark, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtMark, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtMark, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtMeshInertia:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjMESH_INERTIA_CONVEX: ClassVar[mjtMeshInertia] = ...
    mjMESH_INERTIA_EXACT: ClassVar[mjtMeshInertia] = ...
    mjMESH_INERTIA_LEGACY: ClassVar[mjtMeshInertia] = ...
    mjMESH_INERTIA_SHELL: ClassVar[mjtMeshInertia] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtMeshInertia, value: int) -> None

        2. __init__(self: mujoco._enums.mjtMeshInertia, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtMeshInertia, value: int) -> None

        2. __init__(self: mujoco._enums.mjtMeshInertia, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtMeshInertia) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtMeshInertia) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtMeshInertia) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtMeshInertia, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtMeshInertia, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtMouse:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjMOUSE_MOVE_H: ClassVar[mjtMouse] = ...
    mjMOUSE_MOVE_V: ClassVar[mjtMouse] = ...
    mjMOUSE_NONE: ClassVar[mjtMouse] = ...
    mjMOUSE_ROTATE_H: ClassVar[mjtMouse] = ...
    mjMOUSE_ROTATE_V: ClassVar[mjtMouse] = ...
    mjMOUSE_SELECT: ClassVar[mjtMouse] = ...
    mjMOUSE_ZOOM: ClassVar[mjtMouse] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtMouse, value: int) -> None

        2. __init__(self: mujoco._enums.mjtMouse, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtMouse, value: int) -> None

        2. __init__(self: mujoco._enums.mjtMouse, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtMouse, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtMouse) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtMouse) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtMouse, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtMouse) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtMouse, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtMouse, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtMouse, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtMouse, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtMouse, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtMouse, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtMouse, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtMouse, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtMouse, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtMouse, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtObj:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjNOBJECT: ClassVar[mjtObj] = ...
    mjOBJ_ACTUATOR: ClassVar[mjtObj] = ...
    mjOBJ_BODY: ClassVar[mjtObj] = ...
    mjOBJ_CAMERA: ClassVar[mjtObj] = ...
    mjOBJ_DOF: ClassVar[mjtObj] = ...
    mjOBJ_EQUALITY: ClassVar[mjtObj] = ...
    mjOBJ_EXCLUDE: ClassVar[mjtObj] = ...
    mjOBJ_FLEX: ClassVar[mjtObj] = ...
    mjOBJ_FRAME: ClassVar[mjtObj] = ...
    mjOBJ_GEOM: ClassVar[mjtObj] = ...
    mjOBJ_HFIELD: ClassVar[mjtObj] = ...
    mjOBJ_JOINT: ClassVar[mjtObj] = ...
    mjOBJ_KEY: ClassVar[mjtObj] = ...
    mjOBJ_LIGHT: ClassVar[mjtObj] = ...
    mjOBJ_MATERIAL: ClassVar[mjtObj] = ...
    mjOBJ_MESH: ClassVar[mjtObj] = ...
    mjOBJ_NUMERIC: ClassVar[mjtObj] = ...
    mjOBJ_PAIR: ClassVar[mjtObj] = ...
    mjOBJ_PLUGIN: ClassVar[mjtObj] = ...
    mjOBJ_SENSOR: ClassVar[mjtObj] = ...
    mjOBJ_SITE: ClassVar[mjtObj] = ...
    mjOBJ_SKIN: ClassVar[mjtObj] = ...
    mjOBJ_TENDON: ClassVar[mjtObj] = ...
    mjOBJ_TEXT: ClassVar[mjtObj] = ...
    mjOBJ_TEXTURE: ClassVar[mjtObj] = ...
    mjOBJ_TUPLE: ClassVar[mjtObj] = ...
    mjOBJ_UNKNOWN: ClassVar[mjtObj] = ...
    mjOBJ_XBODY: ClassVar[mjtObj] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtObj, value: int) -> None

        2. __init__(self: mujoco._enums.mjtObj, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtObj, value: int) -> None

        2. __init__(self: mujoco._enums.mjtObj, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtObj, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtObj) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtObj) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtObj, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtObj) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtObj, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtObj, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtObj, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtObj, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtObj, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtObj, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtObj, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtObj, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtObj, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtObj, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtOrientation:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjORIENTATION_AXISANGLE: ClassVar[mjtOrientation] = ...
    mjORIENTATION_EULER: ClassVar[mjtOrientation] = ...
    mjORIENTATION_QUAT: ClassVar[mjtOrientation] = ...
    mjORIENTATION_XYAXES: ClassVar[mjtOrientation] = ...
    mjORIENTATION_ZAXIS: ClassVar[mjtOrientation] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtOrientation, value: int) -> None

        2. __init__(self: mujoco._enums.mjtOrientation, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtOrientation, value: int) -> None

        2. __init__(self: mujoco._enums.mjtOrientation, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtOrientation, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtOrientation) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtOrientation) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtOrientation, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtOrientation) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtOrientation, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtOrientation, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtOrientation, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtOrientation, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtOrientation, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtOrientation, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtOrientation, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtOrientation, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtOrientation, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtOrientation, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtPertBit:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjPERT_ROTATE: ClassVar[mjtPertBit] = ...
    mjPERT_TRANSLATE: ClassVar[mjtPertBit] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtPertBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtPertBit, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtPertBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtPertBit, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtPertBit, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtPertBit) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtPertBit) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtPertBit, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtPertBit) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtPertBit, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtPertBit, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtPertBit, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtPertBit, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtPertBit, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtPertBit, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtPertBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtPertBit, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtPertBit, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtPertBit, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtPluginCapabilityBit:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjPLUGIN_ACTUATOR: ClassVar[mjtPluginCapabilityBit] = ...
    mjPLUGIN_PASSIVE: ClassVar[mjtPluginCapabilityBit] = ...
    mjPLUGIN_SDF: ClassVar[mjtPluginCapabilityBit] = ...
    mjPLUGIN_SENSOR: ClassVar[mjtPluginCapabilityBit] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtPluginCapabilityBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtPluginCapabilityBit, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtPluginCapabilityBit, value: int) -> None

        2. __init__(self: mujoco._enums.mjtPluginCapabilityBit, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtPluginCapabilityBit) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtPluginCapabilityBit) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtPluginCapabilityBit) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtPluginCapabilityBit, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtRndFlag:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjNRNDFLAG: ClassVar[mjtRndFlag] = ...
    mjRND_ADDITIVE: ClassVar[mjtRndFlag] = ...
    mjRND_CULL_FACE: ClassVar[mjtRndFlag] = ...
    mjRND_FOG: ClassVar[mjtRndFlag] = ...
    mjRND_HAZE: ClassVar[mjtRndFlag] = ...
    mjRND_IDCOLOR: ClassVar[mjtRndFlag] = ...
    mjRND_REFLECTION: ClassVar[mjtRndFlag] = ...
    mjRND_SEGMENT: ClassVar[mjtRndFlag] = ...
    mjRND_SHADOW: ClassVar[mjtRndFlag] = ...
    mjRND_SKYBOX: ClassVar[mjtRndFlag] = ...
    mjRND_WIREFRAME: ClassVar[mjtRndFlag] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtRndFlag, value: int) -> None

        2. __init__(self: mujoco._enums.mjtRndFlag, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtRndFlag, value: int) -> None

        2. __init__(self: mujoco._enums.mjtRndFlag, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtRndFlag) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtRndFlag) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtRndFlag) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtRndFlag, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtRndFlag, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtSameFrame:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjSAMEFRAME_BODY: ClassVar[mjtSameFrame] = ...
    mjSAMEFRAME_BODYROT: ClassVar[mjtSameFrame] = ...
    mjSAMEFRAME_INERTIA: ClassVar[mjtSameFrame] = ...
    mjSAMEFRAME_INERTIAROT: ClassVar[mjtSameFrame] = ...
    mjSAMEFRAME_NONE: ClassVar[mjtSameFrame] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtSameFrame, value: int) -> None

        2. __init__(self: mujoco._enums.mjtSameFrame, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtSameFrame, value: int) -> None

        2. __init__(self: mujoco._enums.mjtSameFrame, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtSameFrame) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtSameFrame) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtSameFrame) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtSameFrame, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtSameFrame, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtSection:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjSECT_CLOSED: ClassVar[mjtSection] = ...
    mjSECT_FIXED: ClassVar[mjtSection] = ...
    mjSECT_OPEN: ClassVar[mjtSection] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtSection, value: int) -> None

        2. __init__(self: mujoco._enums.mjtSection, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtSection, value: int) -> None

        2. __init__(self: mujoco._enums.mjtSection, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtSection, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtSection) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtSection) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtSection, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtSection) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtSection, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtSection, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtSection, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtSection, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtSection, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtSection, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtSection, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtSection, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtSection, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtSection, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtSensor:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjSENS_ACCELEROMETER: ClassVar[mjtSensor] = ...
    mjSENS_ACTUATORFRC: ClassVar[mjtSensor] = ...
    mjSENS_ACTUATORPOS: ClassVar[mjtSensor] = ...
    mjSENS_ACTUATORVEL: ClassVar[mjtSensor] = ...
    mjSENS_BALLANGVEL: ClassVar[mjtSensor] = ...
    mjSENS_BALLQUAT: ClassVar[mjtSensor] = ...
    mjSENS_CAMPROJECTION: ClassVar[mjtSensor] = ...
    mjSENS_CLOCK: ClassVar[mjtSensor] = ...
    mjSENS_E_KINETIC: ClassVar[mjtSensor] = ...
    mjSENS_E_POTENTIAL: ClassVar[mjtSensor] = ...
    mjSENS_FORCE: ClassVar[mjtSensor] = ...
    mjSENS_FRAMEANGACC: ClassVar[mjtSensor] = ...
    mjSENS_FRAMEANGVEL: ClassVar[mjtSensor] = ...
    mjSENS_FRAMELINACC: ClassVar[mjtSensor] = ...
    mjSENS_FRAMELINVEL: ClassVar[mjtSensor] = ...
    mjSENS_FRAMEPOS: ClassVar[mjtSensor] = ...
    mjSENS_FRAMEQUAT: ClassVar[mjtSensor] = ...
    mjSENS_FRAMEXAXIS: ClassVar[mjtSensor] = ...
    mjSENS_FRAMEYAXIS: ClassVar[mjtSensor] = ...
    mjSENS_FRAMEZAXIS: ClassVar[mjtSensor] = ...
    mjSENS_GEOMDIST: ClassVar[mjtSensor] = ...
    mjSENS_GEOMFROMTO: ClassVar[mjtSensor] = ...
    mjSENS_GEOMNORMAL: ClassVar[mjtSensor] = ...
    mjSENS_GYRO: ClassVar[mjtSensor] = ...
    mjSENS_JOINTACTFRC: ClassVar[mjtSensor] = ...
    mjSENS_JOINTLIMITFRC: ClassVar[mjtSensor] = ...
    mjSENS_JOINTLIMITPOS: ClassVar[mjtSensor] = ...
    mjSENS_JOINTLIMITVEL: ClassVar[mjtSensor] = ...
    mjSENS_JOINTPOS: ClassVar[mjtSensor] = ...
    mjSENS_JOINTVEL: ClassVar[mjtSensor] = ...
    mjSENS_MAGNETOMETER: ClassVar[mjtSensor] = ...
    mjSENS_PLUGIN: ClassVar[mjtSensor] = ...
    mjSENS_RANGEFINDER: ClassVar[mjtSensor] = ...
    mjSENS_SUBTREEANGMOM: ClassVar[mjtSensor] = ...
    mjSENS_SUBTREECOM: ClassVar[mjtSensor] = ...
    mjSENS_SUBTREELINVEL: ClassVar[mjtSensor] = ...
    mjSENS_TENDONLIMITFRC: ClassVar[mjtSensor] = ...
    mjSENS_TENDONLIMITPOS: ClassVar[mjtSensor] = ...
    mjSENS_TENDONLIMITVEL: ClassVar[mjtSensor] = ...
    mjSENS_TENDONPOS: ClassVar[mjtSensor] = ...
    mjSENS_TENDONVEL: ClassVar[mjtSensor] = ...
    mjSENS_TORQUE: ClassVar[mjtSensor] = ...
    mjSENS_TOUCH: ClassVar[mjtSensor] = ...
    mjSENS_USER: ClassVar[mjtSensor] = ...
    mjSENS_VELOCIMETER: ClassVar[mjtSensor] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtSensor, value: int) -> None

        2. __init__(self: mujoco._enums.mjtSensor, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtSensor, value: int) -> None

        2. __init__(self: mujoco._enums.mjtSensor, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtSensor, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtSensor) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtSensor) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtSensor, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtSensor) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtSensor, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtSensor, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtSensor, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtSensor, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtSensor, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtSensor, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtSensor, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtSensor, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtSensor, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtSensor, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtSolver:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjSOL_CG: ClassVar[mjtSolver] = ...
    mjSOL_NEWTON: ClassVar[mjtSolver] = ...
    mjSOL_PGS: ClassVar[mjtSolver] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtSolver, value: int) -> None

        2. __init__(self: mujoco._enums.mjtSolver, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtSolver, value: int) -> None

        2. __init__(self: mujoco._enums.mjtSolver, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtSolver, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtSolver) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtSolver) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtSolver, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtSolver) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtSolver, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtSolver, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtSolver, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtSolver, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtSolver, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtSolver, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtSolver, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtSolver, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtSolver, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtSolver, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtStage:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjSTAGE_ACC: ClassVar[mjtStage] = ...
    mjSTAGE_NONE: ClassVar[mjtStage] = ...
    mjSTAGE_POS: ClassVar[mjtStage] = ...
    mjSTAGE_VEL: ClassVar[mjtStage] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtStage, value: int) -> None

        2. __init__(self: mujoco._enums.mjtStage, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtStage, value: int) -> None

        2. __init__(self: mujoco._enums.mjtStage, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtStage, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtStage) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtStage) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtStage, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtStage) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtStage, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtStage, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtStage, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtStage, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtStage, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtStage, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtStage, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtStage, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtStage, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtStage, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtState:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjNSTATE: ClassVar[mjtState] = ...
    mjSTATE_ACT: ClassVar[mjtState] = ...
    mjSTATE_CTRL: ClassVar[mjtState] = ...
    mjSTATE_EQ_ACTIVE: ClassVar[mjtState] = ...
    mjSTATE_FULLPHYSICS: ClassVar[mjtState] = ...
    mjSTATE_INTEGRATION: ClassVar[mjtState] = ...
    mjSTATE_MOCAP_POS: ClassVar[mjtState] = ...
    mjSTATE_MOCAP_QUAT: ClassVar[mjtState] = ...
    mjSTATE_PHYSICS: ClassVar[mjtState] = ...
    mjSTATE_PLUGIN: ClassVar[mjtState] = ...
    mjSTATE_QFRC_APPLIED: ClassVar[mjtState] = ...
    mjSTATE_QPOS: ClassVar[mjtState] = ...
    mjSTATE_QVEL: ClassVar[mjtState] = ...
    mjSTATE_TIME: ClassVar[mjtState] = ...
    mjSTATE_USER: ClassVar[mjtState] = ...
    mjSTATE_USERDATA: ClassVar[mjtState] = ...
    mjSTATE_WARMSTART: ClassVar[mjtState] = ...
    mjSTATE_XFRC_APPLIED: ClassVar[mjtState] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtState, value: int) -> None

        2. __init__(self: mujoco._enums.mjtState, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtState, value: int) -> None

        2. __init__(self: mujoco._enums.mjtState, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtState, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtState) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtState) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtState, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtState) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtState, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtState, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtState, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtState, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtState, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtState, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtState, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtState, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtState, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtState, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtStereo:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjSTEREO_NONE: ClassVar[mjtStereo] = ...
    mjSTEREO_QUADBUFFERED: ClassVar[mjtStereo] = ...
    mjSTEREO_SIDEBYSIDE: ClassVar[mjtStereo] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtStereo, value: int) -> None

        2. __init__(self: mujoco._enums.mjtStereo, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtStereo, value: int) -> None

        2. __init__(self: mujoco._enums.mjtStereo, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtStereo, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtStereo) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtStereo) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtStereo, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtStereo) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtStereo, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtStereo, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtStereo, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtStereo, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtStereo, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtStereo, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtStereo, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtStereo, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtStereo, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtStereo, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtTaskStatus:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjTASK_COMPLETED: ClassVar[mjtTaskStatus] = ...
    mjTASK_NEW: ClassVar[mjtTaskStatus] = ...
    mjTASK_QUEUED: ClassVar[mjtTaskStatus] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTaskStatus, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTaskStatus, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTaskStatus, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTaskStatus, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtTaskStatus) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtTaskStatus) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtTaskStatus) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtTaskStatus, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtTaskStatus, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtTexture:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjTEXTURE_2D: ClassVar[mjtTexture] = ...
    mjTEXTURE_CUBE: ClassVar[mjtTexture] = ...
    mjTEXTURE_SKYBOX: ClassVar[mjtTexture] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTexture, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTexture, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTexture, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTexture, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtTexture, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtTexture) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtTexture) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtTexture, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtTexture) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtTexture, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtTexture, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtTexture, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtTexture, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtTexture, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtTexture, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTexture, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTexture, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtTexture, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtTexture, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtTextureRole:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjNTEXROLE: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_EMISSIVE: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_METALLIC: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_NORMAL: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_OCCLUSION: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_OPACITY: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_ORM: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_RGB: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_RGBA: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_ROUGHNESS: ClassVar[mjtTextureRole] = ...
    mjTEXROLE_USER: ClassVar[mjtTextureRole] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTextureRole, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTextureRole, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTextureRole, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTextureRole, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtTextureRole) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtTextureRole) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtTextureRole) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtTextureRole, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtTextureRole, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtTimer:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjNTIMER: ClassVar[mjtTimer] = ...
    mjTIMER_ACTUATION: ClassVar[mjtTimer] = ...
    mjTIMER_ADVANCE: ClassVar[mjtTimer] = ...
    mjTIMER_COL_BROAD: ClassVar[mjtTimer] = ...
    mjTIMER_COL_NARROW: ClassVar[mjtTimer] = ...
    mjTIMER_CONSTRAINT: ClassVar[mjtTimer] = ...
    mjTIMER_FORWARD: ClassVar[mjtTimer] = ...
    mjTIMER_INVERSE: ClassVar[mjtTimer] = ...
    mjTIMER_POSITION: ClassVar[mjtTimer] = ...
    mjTIMER_POS_COLLISION: ClassVar[mjtTimer] = ...
    mjTIMER_POS_INERTIA: ClassVar[mjtTimer] = ...
    mjTIMER_POS_KINEMATICS: ClassVar[mjtTimer] = ...
    mjTIMER_POS_MAKE: ClassVar[mjtTimer] = ...
    mjTIMER_POS_PROJECT: ClassVar[mjtTimer] = ...
    mjTIMER_STEP: ClassVar[mjtTimer] = ...
    mjTIMER_VELOCITY: ClassVar[mjtTimer] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTimer, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTimer, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTimer, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTimer, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtTimer, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtTimer) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtTimer) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtTimer, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtTimer) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtTimer, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtTimer, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtTimer, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtTimer, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtTimer, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtTimer, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTimer, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTimer, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtTimer, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtTimer, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtTrn:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjTRN_BODY: ClassVar[mjtTrn] = ...
    mjTRN_JOINT: ClassVar[mjtTrn] = ...
    mjTRN_JOINTINPARENT: ClassVar[mjtTrn] = ...
    mjTRN_SITE: ClassVar[mjtTrn] = ...
    mjTRN_SLIDERCRANK: ClassVar[mjtTrn] = ...
    mjTRN_TENDON: ClassVar[mjtTrn] = ...
    mjTRN_UNDEFINED: ClassVar[mjtTrn] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTrn, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTrn, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtTrn, value: int) -> None

        2. __init__(self: mujoco._enums.mjtTrn, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtTrn, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtTrn) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtTrn) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtTrn, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtTrn) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtTrn, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtTrn, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtTrn, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtTrn, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtTrn, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtTrn, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtTrn, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtTrn, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtTrn, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtTrn, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtVisFlag:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjNVISFLAG: ClassVar[mjtVisFlag] = ...
    mjVIS_ACTIVATION: ClassVar[mjtVisFlag] = ...
    mjVIS_ACTUATOR: ClassVar[mjtVisFlag] = ...
    mjVIS_AUTOCONNECT: ClassVar[mjtVisFlag] = ...
    mjVIS_BODYBVH: ClassVar[mjtVisFlag] = ...
    mjVIS_CAMERA: ClassVar[mjtVisFlag] = ...
    mjVIS_COM: ClassVar[mjtVisFlag] = ...
    mjVIS_CONSTRAINT: ClassVar[mjtVisFlag] = ...
    mjVIS_CONTACTFORCE: ClassVar[mjtVisFlag] = ...
    mjVIS_CONTACTPOINT: ClassVar[mjtVisFlag] = ...
    mjVIS_CONTACTSPLIT: ClassVar[mjtVisFlag] = ...
    mjVIS_CONVEXHULL: ClassVar[mjtVisFlag] = ...
    mjVIS_FLEXBVH: ClassVar[mjtVisFlag] = ...
    mjVIS_FLEXEDGE: ClassVar[mjtVisFlag] = ...
    mjVIS_FLEXFACE: ClassVar[mjtVisFlag] = ...
    mjVIS_FLEXSKIN: ClassVar[mjtVisFlag] = ...
    mjVIS_FLEXVERT: ClassVar[mjtVisFlag] = ...
    mjVIS_INERTIA: ClassVar[mjtVisFlag] = ...
    mjVIS_ISLAND: ClassVar[mjtVisFlag] = ...
    mjVIS_JOINT: ClassVar[mjtVisFlag] = ...
    mjVIS_LIGHT: ClassVar[mjtVisFlag] = ...
    mjVIS_MESHBVH: ClassVar[mjtVisFlag] = ...
    mjVIS_PERTFORCE: ClassVar[mjtVisFlag] = ...
    mjVIS_PERTOBJ: ClassVar[mjtVisFlag] = ...
    mjVIS_RANGEFINDER: ClassVar[mjtVisFlag] = ...
    mjVIS_SCLINERTIA: ClassVar[mjtVisFlag] = ...
    mjVIS_SDFITER: ClassVar[mjtVisFlag] = ...
    mjVIS_SELECT: ClassVar[mjtVisFlag] = ...
    mjVIS_SKIN: ClassVar[mjtVisFlag] = ...
    mjVIS_STATIC: ClassVar[mjtVisFlag] = ...
    mjVIS_TENDON: ClassVar[mjtVisFlag] = ...
    mjVIS_TEXTURE: ClassVar[mjtVisFlag] = ...
    mjVIS_TRANSPARENT: ClassVar[mjtVisFlag] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtVisFlag, value: int) -> None

        2. __init__(self: mujoco._enums.mjtVisFlag, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtVisFlag, value: int) -> None

        2. __init__(self: mujoco._enums.mjtVisFlag, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtVisFlag) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtVisFlag) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtVisFlag) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtVisFlag, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtVisFlag, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtWarning:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjNWARNING: ClassVar[mjtWarning] = ...
    mjWARN_BADCTRL: ClassVar[mjtWarning] = ...
    mjWARN_BADQACC: ClassVar[mjtWarning] = ...
    mjWARN_BADQPOS: ClassVar[mjtWarning] = ...
    mjWARN_BADQVEL: ClassVar[mjtWarning] = ...
    mjWARN_CNSTRFULL: ClassVar[mjtWarning] = ...
    mjWARN_CONTACTFULL: ClassVar[mjtWarning] = ...
    mjWARN_INERTIA: ClassVar[mjtWarning] = ...
    mjWARN_VGEOMFULL: ClassVar[mjtWarning] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtWarning, value: int) -> None

        2. __init__(self: mujoco._enums.mjtWarning, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtWarning, value: int) -> None

        2. __init__(self: mujoco._enums.mjtWarning, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtWarning, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtWarning) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtWarning) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtWarning, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtWarning) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtWarning, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtWarning, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtWarning, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtWarning, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtWarning, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtWarning, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtWarning, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtWarning, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtWarning, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtWarning, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class mjtWrap:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    mjWRAP_CYLINDER: ClassVar[mjtWrap] = ...
    mjWRAP_JOINT: ClassVar[mjtWrap] = ...
    mjWRAP_NONE: ClassVar[mjtWrap] = ...
    mjWRAP_PULLEY: ClassVar[mjtWrap] = ...
    mjWRAP_SITE: ClassVar[mjtWrap] = ...
    mjWRAP_SPHERE: ClassVar[mjtWrap] = ...
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtWrap, value: int) -> None

        2. __init__(self: mujoco._enums.mjtWrap, value: int) -> None
        """
    @overload
    def __init__(self, value: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._enums.mjtWrap, value: int) -> None

        2. __init__(self: mujoco._enums.mjtWrap, value: int) -> None
        """
    @overload
    def __add__(self, arg0: int) -> int:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __add__(self, arg0: float) -> float:
        """__add__(*args, **kwargs)
        Overloaded function.

        1. __add__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __add__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    def __and__(self, arg0: int) -> int:
        """__and__(self: mujoco._enums.mjtWrap, arg0: int) -> int"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    @overload
    def __floordiv__(self, arg0: int) -> int:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __floordiv__(self, arg0: float) -> float:
        """__floordiv__(*args, **kwargs)
        Overloaded function.

        1. __floordiv__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __floordiv__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: mujoco._enums.mjtWrap) -> int"""
    def __int__(self) -> int:
        """__int__(self: mujoco._enums.mjtWrap) -> int"""
    def __lshift__(self, arg0: int) -> int:
        """__lshift__(self: mujoco._enums.mjtWrap, arg0: int) -> int"""
    @overload
    def __mod__(self, arg0: int) -> int:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __mod__(self, arg0: float) -> float:
        """__mod__(*args, **kwargs)
        Overloaded function.

        1. __mod__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __mod__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: int) -> int:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __mul__(self, arg0: float) -> float:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __mul__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __neg__(self) -> int:
        """__neg__(self: mujoco._enums.mjtWrap) -> int"""
    def __or__(self, arg0: int) -> int:
        """__or__(self: mujoco._enums.mjtWrap, arg0: int) -> int"""
    @overload
    def __radd__(self, arg0: int) -> int:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __radd__(self, arg0: float) -> float:
        """__radd__(*args, **kwargs)
        Overloaded function.

        1. __radd__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __radd__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    def __rand__(self, arg0: int) -> int:
        """__rand__(self: mujoco._enums.mjtWrap, arg0: int) -> int"""
    @overload
    def __rfloordiv__(self, arg0: int) -> int:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __rfloordiv__(self, arg0: float) -> float:
        """__rfloordiv__(*args, **kwargs)
        Overloaded function.

        1. __rfloordiv__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __rfloordiv__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: int) -> int:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __rmod__(self, arg0: float) -> float:
        """__rmod__(*args, **kwargs)
        Overloaded function.

        1. __rmod__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __rmod__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: int) -> int:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __rmul__(self, arg0: float) -> float:
        """__rmul__(*args, **kwargs)
        Overloaded function.

        1. __rmul__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __rmul__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    def __ror__(self, arg0: int) -> int:
        """__ror__(self: mujoco._enums.mjtWrap, arg0: int) -> int"""
    def __rshift__(self, arg0: int) -> int:
        """__rshift__(self: mujoco._enums.mjtWrap, arg0: int) -> int"""
    @overload
    def __rsub__(self, arg0: int) -> int:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __rsub__(self, arg0: float) -> float:
        """__rsub__(*args, **kwargs)
        Overloaded function.

        1. __rsub__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __rsub__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    def __rtruediv__(self, arg0: float) -> float:
        """__rtruediv__(self: mujoco._enums.mjtWrap, arg0: float) -> float"""
    def __rxor__(self, arg0: int) -> int:
        """__rxor__(self: mujoco._enums.mjtWrap, arg0: int) -> int"""
    @overload
    def __sub__(self, arg0: int) -> int:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    @overload
    def __sub__(self, arg0: float) -> float:
        """__sub__(*args, **kwargs)
        Overloaded function.

        1. __sub__(self: mujoco._enums.mjtWrap, arg0: int) -> int

        2. __sub__(self: mujoco._enums.mjtWrap, arg0: float) -> float
        """
    def __truediv__(self, arg0: float) -> float:
        """__truediv__(self: mujoco._enums.mjtWrap, arg0: float) -> float"""
    def __xor__(self, arg0: int) -> int:
        """__xor__(self: mujoco._enums.mjtWrap, arg0: int) -> int"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

# --- mujoco._errors ---
from mujoco import FatalError as FatalError, UnexpectedError as UnexpectedError

# --- mujoco._functions ---
import flags
import mujoco._structs
import numpy

def mj_Euler(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_Euler(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Euler integrator, semi-implicit in velocity.
    """
def mj_RungeKutta(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, N: int) -> None:
    """mj_RungeKutta(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, N: int) -> None

    Runge-Kutta explicit order-N integrator.
    """
def mj_addContact(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, con: mujoco._structs.MjContact) -> int:
    """mj_addContact(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, con: mujoco._structs.MjContact) -> int

    Add contact to d->contact list; return 0 if success; 1 if buffer full.
    """
def mj_addM(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, dst: numpy.ndarray[numpy.float64[m, 1], flags.writeable], rownnz: numpy.ndarray[numpy.int32[m, 1], flags.writeable], rowadr: numpy.ndarray[numpy.int32[m, 1], flags.writeable], colind: numpy.ndarray[numpy.int32[m, 1], flags.writeable]) -> None:
    """mj_addM(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, dst: numpy.ndarray[numpy.float64[m, 1], flags.writeable], rownnz: numpy.ndarray[numpy.int32[m, 1], flags.writeable], rowadr: numpy.ndarray[numpy.int32[m, 1], flags.writeable], colind: numpy.ndarray[numpy.int32[m, 1], flags.writeable]) -> None

    Add inertia matrix to destination matrix. Destination can be sparse uncompressed, or dense when all int* are NULL
    """
def mj_angmomMat(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, mat: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], body: int) -> None:
    """mj_angmomMat(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, mat: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], body: int) -> None

    Compute subtree angular momentum matrix.
    """
def mj_applyFT(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, force: numpy.ndarray[numpy.float64[3, 1]], torque: numpy.ndarray[numpy.float64[3, 1]], point: numpy.ndarray[numpy.float64[3, 1]], body: int, qfrc_target: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None:
    """mj_applyFT(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, force: numpy.ndarray[numpy.float64[3, 1]], torque: numpy.ndarray[numpy.float64[3, 1]], point: numpy.ndarray[numpy.float64[3, 1]], body: int, qfrc_target: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None

    Apply Cartesian force and torque (outside xfrc_applied mechanism).
    """
def mj_camlight(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_camlight(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute camera and light positions and orientations.
    """
def mj_checkAcc(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_checkAcc(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Check qacc, reset if any element is too big or nan.
    """
def mj_checkPos(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_checkPos(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Check qpos, reset if any element is too big or nan.
    """
def mj_checkVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_checkVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Check qvel, reset if any element is too big or nan.
    """
def mj_collision(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_collision(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Run collision detection.
    """
def mj_comPos(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_comPos(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Map inertias and motion dofs to global frame centered at CoM.
    """
def mj_comVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_comVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute cvel, cdof_dot.
    """
def mj_compareFwdInv(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_compareFwdInv(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compare forward and inverse dynamics, save results in fwdinv.
    """
def mj_constraintUpdate(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jar: numpy.ndarray[numpy.float64[m, 1]], cost: numpy.ndarray[numpy.float64[1, 1], flags.writeable] | None, flg_coneHessian: int) -> None:
    """mj_constraintUpdate(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jar: numpy.ndarray[numpy.float64[m, 1]], cost: Optional[numpy.ndarray[numpy.float64[1, 1], flags.writeable]], flg_coneHessian: int) -> None

    Compute efc_state, efc_force, qfrc_constraint, and (optionally) cone Hessians. If cost is not NULL, set *cost = s(jar) where jar = Jac*qacc-aref.
    """
def mj_contactForce(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, id: int, result: numpy.ndarray[numpy.float64[6, 1], flags.writeable]) -> None:
    """mj_contactForce(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, id: int, result: numpy.ndarray[numpy.float64[6, 1], flags.writeable]) -> None

    Extract 6D force:torque given contact id, in the contact frame.
    """
def mj_crb(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_crb(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Run composite rigid body inertia algorithm (CRB).
    """
def mj_defaultLROpt(opt: mujoco._structs.MjLROpt) -> None:
    """mj_defaultLROpt(opt: mujoco._structs.MjLROpt) -> None

    Set default options for length range computation.
    """
def mj_defaultOption(opt: mujoco._structs.MjOption) -> None:
    """mj_defaultOption(opt: mujoco._structs.MjOption) -> None

    Set physics options to default values.
    """
def mj_defaultSolRefImp(solref: float, solimp: float) -> None:
    """mj_defaultSolRefImp(solref: float, solimp: float) -> None

    Set solver parameters to default values.
    """
def mj_defaultVisual(vis: mujoco._structs.MjVisual) -> None:
    """mj_defaultVisual(vis: mujoco._structs.MjVisual) -> None

    Set visual options to default values.
    """
def mj_differentiatePos(m: mujoco._structs.MjModel, qvel: numpy.ndarray[numpy.float64[m, 1], flags.writeable], dt: float, qpos1: numpy.ndarray[numpy.float64[m, 1]], qpos2: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mj_differentiatePos(m: mujoco._structs.MjModel, qvel: numpy.ndarray[numpy.float64[m, 1], flags.writeable], dt: float, qpos1: numpy.ndarray[numpy.float64[m, 1]], qpos2: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Compute velocity by finite-differencing two positions.
    """
def mj_energyPos(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_energyPos(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Evaluate position-dependent energy (potential).
    """
def mj_energyVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_energyVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Evaluate velocity-dependent energy (kinetic).
    """
def mj_factorM(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_factorM(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute sparse L'*D*L factorizaton of inertia matrix.
    """
def mj_flex(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_flex(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute flex-related quantities.
    """
def mj_forward(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_forward(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Forward dynamics: same as mj_step but do not integrate in time.
    """
def mj_forwardSkip(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, skipstage: int, skipsensor: int) -> None:
    """mj_forwardSkip(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, skipstage: int, skipsensor: int) -> None

    Forward dynamics with skip; skipstage is mjtStage.
    """
def mj_fullM(m: mujoco._structs.MjModel, dst: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], M: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mj_fullM(m: mujoco._structs.MjModel, dst: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], M: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Convert sparse inertia matrix M into full (i.e. dense) matrix.
    """
def mj_fwdAcceleration(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_fwdAcceleration(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Add up all non-constraint forces, compute qacc_smooth.
    """
def mj_fwdActuation(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_fwdActuation(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute actuator force qfrc_actuator.
    """
def mj_fwdConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_fwdConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Run selected constraint solver.
    """
def mj_fwdPosition(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_fwdPosition(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Run position-dependent computations.
    """
def mj_fwdVelocity(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_fwdVelocity(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Run velocity-dependent computations.
    """
def mj_geomDistance(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, geom1: int, geom2: int, distmax: float, fromto: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None) -> float:
    """mj_geomDistance(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, geom1: int, geom2: int, distmax: float, fromto: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]]) -> float

    Returns smallest signed distance between two geoms and optionally segment from geom1 to geom2.
    """
def mj_getState(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, state: numpy.ndarray[numpy.float64[m, 1], flags.writeable], spec: int) -> None:
    """mj_getState(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, state: numpy.ndarray[numpy.float64[m, 1], flags.writeable], spec: int) -> None

    Get state.
    """
def mj_getTotalmass(m: mujoco._structs.MjModel) -> float:
    """mj_getTotalmass(m: mujoco._structs.MjModel) -> float

    Sum all body masses.
    """
def mj_id2name(m: mujoco._structs.MjModel, type: int, id: int) -> str:
    """mj_id2name(m: mujoco._structs.MjModel, type: int, id: int) -> str

    Get name of object with the specified mjtObj type and id, returns NULL if name not found.
    """
def mj_implicit(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_implicit(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Implicit-in-velocity integrators.
    """
def mj_integratePos(m: mujoco._structs.MjModel, qpos: numpy.ndarray[numpy.float64[m, 1], flags.writeable], qvel: numpy.ndarray[numpy.float64[m, 1]], dt: float) -> None:
    """mj_integratePos(m: mujoco._structs.MjModel, qpos: numpy.ndarray[numpy.float64[m, 1], flags.writeable], qvel: numpy.ndarray[numpy.float64[m, 1]], dt: float) -> None

    Integrate position with given velocity.
    """
def mj_invConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_invConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Apply the analytical formula for inverse constraint dynamics.
    """
def mj_invPosition(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_invPosition(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Run position-dependent computations in inverse dynamics.
    """
def mj_invVelocity(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_invVelocity(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Run velocity-dependent computations in inverse dynamics.
    """
def mj_inverse(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_inverse(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Inverse dynamics: qacc must be set before calling.
    """
def mj_inverseSkip(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, skipstage: int, skipsensor: int) -> None:
    """mj_inverseSkip(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, skipstage: int, skipsensor: int) -> None

    Inverse dynamics with skip; skipstage is mjtStage.
    """
def mj_isDual(m: mujoco._structs.MjModel) -> int:
    """mj_isDual(m: mujoco._structs.MjModel) -> int

    Determine type of solver (PGS is dual, CG and Newton are primal).
    """
def mj_isPyramidal(m: mujoco._structs.MjModel) -> int:
    """mj_isPyramidal(m: mujoco._structs.MjModel) -> int

    Determine type of friction cone.
    """
def mj_isSparse(m: mujoco._structs.MjModel) -> int:
    """mj_isSparse(m: mujoco._structs.MjModel) -> int

    Determine type of constraint Jacobian.
    """
def mj_island(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_island(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Find constraint islands.
    """
def mj_jac(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, jacr: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, point: numpy.ndarray[numpy.float64[3, 1]], body: int) -> None:
    """mj_jac(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], jacr: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], point: numpy.ndarray[numpy.float64[3, 1]], body: int) -> None

    Compute 3/6-by-nv end-effector Jacobian of global point attached to given body.
    """
def mj_jacBody(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, jacr: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, body: int) -> None:
    """mj_jacBody(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], jacr: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], body: int) -> None

    Compute body frame end-effector Jacobian.
    """
def mj_jacBodyCom(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, jacr: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, body: int) -> None:
    """mj_jacBodyCom(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], jacr: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], body: int) -> None

    Compute body center-of-mass end-effector Jacobian.
    """
def mj_jacDot(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, jacr: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, point: numpy.ndarray[numpy.float64[3, 1]], body: int) -> None:
    """mj_jacDot(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], jacr: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], point: numpy.ndarray[numpy.float64[3, 1]], body: int) -> None

    Compute 3/6-by-nv Jacobian time derivative of global point attached to given body.
    """
def mj_jacGeom(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, jacr: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, geom: int) -> None:
    """mj_jacGeom(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], jacr: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], geom: int) -> None

    Compute geom end-effector Jacobian.
    """
def mj_jacPointAxis(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacPoint: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, jacAxis: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, point: numpy.ndarray[numpy.float64[3, 1]], axis: numpy.ndarray[numpy.float64[3, 1]], body: int) -> None:
    """mj_jacPointAxis(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacPoint: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], jacAxis: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], point: numpy.ndarray[numpy.float64[3, 1]], axis: numpy.ndarray[numpy.float64[3, 1]], body: int) -> None

    Compute translation end-effector Jacobian of point, and rotation Jacobian of axis.
    """
def mj_jacSite(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, jacr: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, site: int) -> None:
    """mj_jacSite(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], jacr: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], site: int) -> None

    Compute site end-effector Jacobian.
    """
def mj_jacSubtreeCom(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, body: int) -> None:
    """mj_jacSubtreeCom(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, jacp: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], body: int) -> None

    Compute subtree center-of-mass end-effector Jacobian.
    """
def mj_kinematics(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_kinematics(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Run forward kinematics.
    """
def mj_loadAllPluginLibraries(directory: str) -> None:
    """mj_loadAllPluginLibraries(directory: str) -> None

    Scan a directory and load all dynamic libraries. Dynamic libraries in the specified directory are assumed to register one or more plugins. Optionally, if a callback is specified, it is called for each dynamic library encountered that registers plugins.
    """
def mj_loadPluginLibrary(path: str) -> None:
    """mj_loadPluginLibrary(path: str) -> None

    Load a dynamic library. The dynamic library is assumed to register one or more plugins.
    """
def mj_local2Global(d: mujoco._structs.MjData, xpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], xmat: numpy.ndarray[numpy.float64[9, 1], flags.writeable], pos: numpy.ndarray[numpy.float64[3, 1]], quat: numpy.ndarray[numpy.float64[4, 1]], body: int, sameframe: int) -> None:
    """mj_local2Global(d: mujoco._structs.MjData, xpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], xmat: numpy.ndarray[numpy.float64[9, 1], flags.writeable], pos: numpy.ndarray[numpy.float64[3, 1]], quat: numpy.ndarray[numpy.float64[4, 1]], body: int, sameframe: int) -> None

    Map from body local to global Cartesian coordinates, sameframe takes values from mjtSameFrame.
    """
def mj_makeConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_makeConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Construct constraints.
    """
def mj_mulJacTVec(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mj_mulJacTVec(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Multiply dense or sparse constraint Jacobian transpose by vector.
    """
def mj_mulJacVec(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mj_mulJacVec(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Multiply dense or sparse constraint Jacobian by vector.
    """
def mj_mulM(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mj_mulM(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Multiply vector by inertia matrix.
    """
def mj_mulM2(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mj_mulM2(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Multiply vector by (inertia matrix)^(1/2).
    """
def mj_multiRay(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[m, 1]], geomgroup: numpy.ndarray[numpy.uint8[6, 1]] | None, flg_static: int, bodyexclude: int, geomid: numpy.ndarray[numpy.int32[m, 1], flags.writeable], dist: numpy.ndarray[numpy.float64[m, 1], flags.writeable], nray: int, cutoff: float) -> None:
    """mj_multiRay(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[m, 1]], geomgroup: Optional[numpy.ndarray[numpy.uint8[6, 1]]], flg_static: int, bodyexclude: int, geomid: numpy.ndarray[numpy.int32[m, 1], flags.writeable], dist: numpy.ndarray[numpy.float64[m, 1], flags.writeable], nray: int, cutoff: float) -> None

    Intersect multiple rays emanating from a single point. Similar semantics to mj_ray, but vec is an array of (nray x 3) directions.
    """
def mj_name2id(m: mujoco._structs.MjModel, type: int, name: str) -> int:
    """mj_name2id(m: mujoco._structs.MjModel, type: int, name: str) -> int

    Get id of object with the specified mjtObj type and name, returns -1 if id not found.
    """
def mj_normalizeQuat(m: mujoco._structs.MjModel, qpos: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None:
    """mj_normalizeQuat(m: mujoco._structs.MjModel, qpos: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None

    Normalize all quaternions in qpos-type vector.
    """
def mj_objectAcceleration(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, objtype: int, objid: int, res: numpy.ndarray[numpy.float64[6, 1], flags.writeable], flg_local: int) -> None:
    """mj_objectAcceleration(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, objtype: int, objid: int, res: numpy.ndarray[numpy.float64[6, 1], flags.writeable], flg_local: int) -> None

    Compute object 6D acceleration (rot:lin) in object-centered frame, world/local orientation.
    """
def mj_objectVelocity(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, objtype: int, objid: int, res: numpy.ndarray[numpy.float64[6, 1], flags.writeable], flg_local: int) -> None:
    """mj_objectVelocity(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, objtype: int, objid: int, res: numpy.ndarray[numpy.float64[6, 1], flags.writeable], flg_local: int) -> None

    Compute object 6D velocity (rot:lin) in object-centered frame, world/local orientation.
    """
def mj_passive(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_passive(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute qfrc_passive from spring-dampers, gravity compensation and fluid forces.
    """
def mj_printData(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, filename: str) -> None:
    """mj_printData(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, filename: str) -> None

    Print data to text file.
    """
def mj_printFormattedData(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, filename: str, float_format: str) -> None:
    """mj_printFormattedData(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, filename: str, float_format: str) -> None

    Print mjData to text file, specifying format. float_format must be a valid printf-style format string for a single float value
    """
def mj_printFormattedModel(m: mujoco._structs.MjModel, filename: str, float_format: str) -> None:
    """mj_printFormattedModel(m: mujoco._structs.MjModel, filename: str, float_format: str) -> None

    Print mjModel to text file, specifying format. float_format must be a valid printf-style format string for a single float value.
    """
def mj_printModel(m: mujoco._structs.MjModel, filename: str) -> None:
    """mj_printModel(m: mujoco._structs.MjModel, filename: str) -> None

    Print model to text file.
    """
def mj_printSchema(flg_html: bool, flg_pad: bool) -> str:
    """mj_printSchema(flg_html: bool, flg_pad: bool) -> str

    Print internal XML schema as plain text or HTML, with style-padding or &nbsp;.
    """
def mj_projectConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_projectConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute inverse constraint inertia efc_AR.
    """
def mj_ray(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]], geomgroup: numpy.ndarray[numpy.uint8[6, 1]] | None, flg_static: int, bodyexclude: int, geomid: numpy.ndarray[numpy.int32[1, 1], flags.writeable]) -> float:
    """mj_ray(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]], geomgroup: Optional[numpy.ndarray[numpy.uint8[6, 1]]], flg_static: int, bodyexclude: int, geomid: numpy.ndarray[numpy.int32[1, 1], flags.writeable]) -> float

    Intersect ray (pnt+x*vec, x>=0) with visible geoms, except geoms in bodyexclude. Return distance (x) to nearest surface, or -1 if no intersection and output geomid. geomgroup, flg_static are as in mjvOption; geomgroup==NULL skips group exclusion.
    """
def mj_rayHfield(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, geomid: int, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> float:
    """mj_rayHfield(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, geomid: int, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> float

    Intersect ray with hfield, return nearest distance or -1 if no intersection.
    """
def mj_rayMesh(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, geomid: int, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> float:
    """mj_rayMesh(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, geomid: int, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> float

    Intersect ray with mesh, return nearest distance or -1 if no intersection.
    """
def mj_referenceConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_referenceConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute efc_vel, efc_aref.
    """
def mj_resetCallbacks() -> None:
    """mj_resetCallbacks() -> None

    Reset all callbacks to NULL pointers (NULL is the default).
    """
def mj_resetData(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_resetData(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Reset data to defaults.
    """
def mj_resetDataDebug(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, debug_value: int) -> None:
    """mj_resetDataDebug(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, debug_value: int) -> None

    Reset data to defaults, fill everything else with debug_value.
    """
def mj_resetDataKeyframe(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, key: int) -> None:
    """mj_resetDataKeyframe(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, key: int) -> None

    Reset data. If 0 <= key < nkey, set fields from specified keyframe.
    """
def mj_rne(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, flg_acc: int, result: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None:
    """mj_rne(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, flg_acc: int, result: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None

    RNE: compute M(qpos)*qacc + C(qpos,qvel); flg_acc=0 removes inertial term.
    """
def mj_rnePostConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_rnePostConstraint(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    RNE with complete data: compute cacc, cfrc_ext, cfrc_int.
    """
def mj_saveLastXML(filename: str, m: mujoco._structs.MjModel) -> None:
    """mj_saveLastXML(filename: str, m: mujoco._structs.MjModel) -> None

    Update XML data structures with info from low-level model, save as MJCF. If error is not NULL, it must have size error_sz.
    """
def mj_saveModel(m: mujoco._structs.MjModel, filename: str | None = ..., buffer: numpy.ndarray[numpy.uint8[m, 1], flags.writeable] | None = ...) -> None:
    """mj_saveModel(m: mujoco._structs.MjModel, filename: Optional[str] = None, buffer: Optional[numpy.ndarray[numpy.uint8[m, 1], flags.writeable]] = None) -> None

    Save model to binary MJB file or memory buffer; buffer has precedence when given.
    """
def mj_sensorAcc(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_sensorAcc(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Evaluate acceleration and force-dependent sensors.
    """
def mj_sensorPos(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_sensorPos(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Evaluate position-dependent sensors.
    """
def mj_sensorVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_sensorVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Evaluate velocity-dependent sensors.
    """
def mj_setConst(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_setConst(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Set constant fields of mjModel, corresponding to qpos0 configuration.
    """
def mj_setKeyframe(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, k: int) -> None:
    """mj_setKeyframe(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, k: int) -> None

    Copy current state to the k-th model keyframe.
    """
def mj_setLengthRange(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, index: int, opt: mujoco._structs.MjLROpt) -> None:
    """mj_setLengthRange(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, index: int, opt: mujoco._structs.MjLROpt) -> None

    Set actuator_lengthrange for specified actuator; return 1 if ok, 0 if error.
    """
def mj_setState(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, state: numpy.ndarray[numpy.float64[m, 1], flags.writeable], spec: int) -> None:
    """mj_setState(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, state: numpy.ndarray[numpy.float64[m, 1], flags.writeable], spec: int) -> None

    Set state.
    """
def mj_setTotalmass(m: mujoco._structs.MjModel, newmass: float) -> None:
    """mj_setTotalmass(m: mujoco._structs.MjModel, newmass: float) -> None

    Scale body masses and inertias to achieve specified total mass.
    """
def mj_sizeModel(m: mujoco._structs.MjModel) -> int:
    """mj_sizeModel(m: mujoco._structs.MjModel) -> int

    Return size of buffer needed to hold model.
    """
def mj_solveM(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, x: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], y: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None:
    """mj_solveM(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, x: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], y: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None

    Solve linear system M * x = y using factorization:  x = inv(L'*D*L)*y
    """
def mj_solveM2(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, x: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], y: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], sqrtInvD: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None:
    """mj_solveM2(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, x: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], y: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], sqrtInvD: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None

    Half of linear solve:  x = sqrt(inv(D))*inv(L')*y
    """
def mj_stateSize(m: mujoco._structs.MjModel, spec: int) -> int:
    """mj_stateSize(m: mujoco._structs.MjModel, spec: int) -> int

    Return size of state specification.
    """
def mj_step(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, nstep: int = ...) -> None:
    """mj_step(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, nstep: int = 1) -> None

    Advance simulation, use control callback to obtain external force and control. Optionally, repeat nstep times.
    """
def mj_step1(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_step1(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Advance simulation in two steps: before external force and control is set by user.
    """
def mj_step2(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_step2(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Advance simulation in two steps: after external force and control is set by user.
    """
def mj_subtreeVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_subtreeVel(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Sub-tree linear velocity and angular momentum: compute subtree_linvel, subtree_angmom.
    """
def mj_tendon(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_tendon(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute tendon lengths, velocities and moment arms.
    """
def mj_transmission(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None:
    """mj_transmission(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None

    Compute actuator transmission lengths and moments.
    """
def mj_version() -> int:
    """mj_version() -> int

    Return version number: 1.0.2 is encoded as 102.
    """
def mj_versionString() -> str:
    """mj_versionString() -> str

    Return the current version of MuJoCo as a null-terminated string.
    """
def mjd_inverseFD(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, eps: float, flg_actuation: int, DfDq: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, DfDv: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, DfDa: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, DsDq: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, DsDv: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, DsDa: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, DmDq: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None) -> None:
    """mjd_inverseFD(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, eps: float, flg_actuation: int, DfDq: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], DfDv: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], DfDa: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], DsDq: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], DsDv: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], DsDa: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], DmDq: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]]) -> None

    Finite differenced Jacobians of (force, sensors) = mj_inverse(state, acceleration)   All outputs are optional. Output dimensions (transposed w.r.t Control Theory convention):     DfDq: (nv x nv)     DfDv: (nv x nv)     DfDa: (nv x nv)     DsDq: (nv x nsensordata)     DsDv: (nv x nsensordata)     DsDa: (nv x nsensordata)     DmDq: (nv x nM)   single-letter shortcuts:     inputs: q=qpos, v=qvel, a=qacc     outputs: f=qfrc_inverse, s=sensordata, m=qM   notes:     optionally computes mass matrix Jacobian DmDq     flg_actuation specifies whether to subtract qfrc_actuator from qfrc_inverse
    """
def mjd_quatIntegrate(vel: numpy.ndarray[numpy.float64[3, 1]], scale: float, Dquat: numpy.ndarray[numpy.float64[9, 1], flags.writeable], Dvel: numpy.ndarray[numpy.float64[9, 1], flags.writeable], Dscale: numpy.ndarray[numpy.float64[3, 1], flags.writeable]) -> None:
    """mjd_quatIntegrate(vel: numpy.ndarray[numpy.float64[3, 1]], scale: float, Dquat: numpy.ndarray[numpy.float64[9, 1], flags.writeable], Dvel: numpy.ndarray[numpy.float64[9, 1], flags.writeable], Dscale: numpy.ndarray[numpy.float64[3, 1], flags.writeable]) -> None

    Derivatives of mju_quatIntegrate.
    """
def mjd_subQuat(qa: numpy.ndarray[numpy.float64[m, 1]], qb: numpy.ndarray[numpy.float64[m, 1]], Da: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, Db: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None) -> None:
    """mjd_subQuat(qa: numpy.ndarray[numpy.float64[m, 1]], qb: numpy.ndarray[numpy.float64[m, 1]], Da: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], Db: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]]) -> None

    Derivatives of mju_subQuat.
    """
def mjd_transitionFD(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, eps: float, flg_centered: int, A: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, B: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, C: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None, D: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous] | None) -> None:
    """mjd_transitionFD(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, eps: float, flg_centered: int, A: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], B: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], C: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]], D: Optional[numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]]) -> None

    Finite differenced transition matrices (control theory notation)   d(x_next) = A*dx + B*du   d(sensor) = C*dx + D*du   required output matrix dimensions:      A: (2*nv+na x 2*nv+na)      B: (2*nv+na x nu)      D: (nsensordata x 2*nv+na)      C: (nsensordata x nu)
    """
def mju_Halton(index: int, base: int) -> float:
    """mju_Halton(index: int, base: int) -> float

    Generate Halton sequence.
    """
def mju_L1(vec: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> float:
    """mju_L1(vec: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> float

    Return L1 norm: sum(abs(vec)).
    """
def mju_add(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[m, 1]], vec2: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_add(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[m, 1]], vec2: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Set res = vec1 + vec2.
    """
def mju_add3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[3, 1]], vec2: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_add3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[3, 1]], vec2: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Set res = vec1 + vec2.
    """
def mju_addScl(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[m, 1]], vec2: numpy.ndarray[numpy.float64[m, 1]], scl: float) -> None:
    """mju_addScl(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[m, 1]], vec2: numpy.ndarray[numpy.float64[m, 1]], scl: float) -> None

    Set res = vec1 + vec2*scl.
    """
def mju_addScl3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[3, 1]], vec2: numpy.ndarray[numpy.float64[3, 1]], scl: float) -> None:
    """mju_addScl3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[3, 1]], vec2: numpy.ndarray[numpy.float64[3, 1]], scl: float) -> None

    Set res = vec1 + vec2*scl.
    """
def mju_addTo(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_addTo(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Set res = res + vec.
    """
def mju_addTo3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_addTo3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Set res = res + vec.
    """
def mju_addToScl(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]], scl: float) -> None:
    """mju_addToScl(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]], scl: float) -> None

    Set res = res + vec*scl.
    """
def mju_addToScl3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]], scl: float) -> None:
    """mju_addToScl3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]], scl: float) -> None

    Set res = res + vec*scl.
    """
def mju_axisAngle2Quat(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], axis: numpy.ndarray[numpy.float64[3, 1]], angle: float) -> None:
    """mju_axisAngle2Quat(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], axis: numpy.ndarray[numpy.float64[3, 1]], angle: float) -> None

    Convert axisAngle to quaternion.
    """
def mju_band2Dense(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, 1]], ntotal: int, nband: int, ndense: int, flg_sym: int) -> None:
    """mju_band2Dense(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, 1]], ntotal: int, nband: int, ndense: int, flg_sym: int) -> None

    Convert banded matrix to dense matrix, fill upper triangle if flg_sym>0.
    """
def mju_bandDiag(i: int, ntotal: int, nband: int, ndense: int) -> int:
    """mju_bandDiag(i: int, ntotal: int, nband: int, ndense: int) -> int

    Address of diagonal element i in band-dense matrix representation.
    """
def mju_bandMulMatVec(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], ntotal: int, nband: int, ndense: int, nvec: int, flg_sym: int) -> None:
    """mju_bandMulMatVec(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], ntotal: int, nband: int, ndense: int, nvec: int, flg_sym: int) -> None

    Multiply band-diagonal matrix with nvec vectors, include upper triangle if flg_sym>0.
    """
def mju_boxQP(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], R: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], index: numpy.ndarray[numpy.int32[m, 1], flags.writeable] | None, H: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], g: numpy.ndarray[numpy.float64[m, 1]], lower: numpy.ndarray[numpy.float64[m, 1]] | None, upper: numpy.ndarray[numpy.float64[m, 1]] | None) -> int:
    """mju_boxQP(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], R: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], index: Optional[numpy.ndarray[numpy.int32[m, 1], flags.writeable]], H: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], g: numpy.ndarray[numpy.float64[m, 1]], lower: Optional[numpy.ndarray[numpy.float64[m, 1]]], upper: Optional[numpy.ndarray[numpy.float64[m, 1]]]) -> int

    minimize 0.5*x'*H*x + x'*g  s.t. lower <= x <= upper, return rank or -1 if failed   inputs:     n           - problem dimension     H           - SPD matrix                n*n     g           - bias vector               n     lower       - lower bounds              n     upper       - upper bounds              n     res         - solution warmstart        n   return value:     nfree <= n  - rank of unconstrained subspace, -1 if failure   outputs (required):     res         - solution                  n     R           - subspace Cholesky factor  nfree*nfree    allocated: n*(n+7)   outputs (optional):     index       - set of free dimensions    nfree          allocated: n   notes:     the initial value of res is used to warmstart the solver     R must have allocatd size n*(n+7), but only nfree*nfree values are used in output     index (if given) must have allocated size n, but only nfree values are used in output     only the lower triangles of H and R and are read from and written to, respectively     the convenience function mju_boxQPmalloc allocates the required data structures
    """
def mju_cholFactor(mat: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mindiag: float) -> int:
    """mju_cholFactor(mat: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mindiag: float) -> int

    Cholesky decomposition: mat = L*L'; return rank, decomposition performed in-place into mat.
    """
def mju_cholFactorBand(mat: numpy.ndarray[numpy.float64[m, 1], flags.writeable], ntotal: int, nband: int, ndense: int, diagadd: float, diagmul: float) -> float:
    """mju_cholFactorBand(mat: numpy.ndarray[numpy.float64[m, 1], flags.writeable], ntotal: int, nband: int, ndense: int, diagadd: float, diagmul: float) -> float

    Band-dense Cholesky decomposition.  Returns minimum value in the factorized diagonal, or 0 if rank-deficient.  mat has (ntotal-ndense) x nband + ndense x ntotal elements.  The first (ntotal-ndense) x nband store the band part, left of diagonal, inclusive.  The second ndense x ntotal store the band part as entire dense rows.  Add diagadd+diagmul*mat_ii to diagonal before factorization.
    """
def mju_cholSolve(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_cholSolve(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Solve (mat*mat') * res = vec, where mat is a Cholesky factor.
    """
def mju_cholSolveBand(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, 1]], vec: numpy.ndarray[numpy.float64[m, 1]], ntotal: int, nband: int, ndense: int) -> None:
    """mju_cholSolveBand(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, 1]], vec: numpy.ndarray[numpy.float64[m, 1]], ntotal: int, nband: int, ndense: int) -> None

    Solve (mat*mat')*res = vec where mat is a band-dense Cholesky factor.
    """
def mju_cholUpdate(mat: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], x: numpy.ndarray[numpy.float64[m, 1], flags.writeable], flg_plus: int) -> int:
    """mju_cholUpdate(mat: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], x: numpy.ndarray[numpy.float64[m, 1], flags.writeable], flg_plus: int) -> int

    Cholesky rank-one update: L*L' +/- x*x'; return rank.
    """
def mju_clip(x: float, min: float, max: float) -> float:
    """mju_clip(x: float, min: float, max: float) -> float

    Clip x to the range [min, max].
    """
def mju_copy(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_copy(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Set res = vec.
    """
def mju_copy3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], data: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_copy3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], data: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Set res = vec.
    """
def mju_copy4(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], data: numpy.ndarray[numpy.float64[4, 1]]) -> None:
    """mju_copy4(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], data: numpy.ndarray[numpy.float64[4, 1]]) -> None

    Set res = vec.
    """
def mju_cross(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], a: numpy.ndarray[numpy.float64[3, 1]], b: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_cross(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], a: numpy.ndarray[numpy.float64[3, 1]], b: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Compute cross-product: res = cross(a, b).
    """
def mju_d2n(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_d2n(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Convert from double to mjtNum.
    """
def mju_decodePyramid(force: numpy.ndarray[numpy.float64[m, 1], flags.writeable], pyramid: numpy.ndarray[numpy.float64[m, 1]], mu: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_decodePyramid(force: numpy.ndarray[numpy.float64[m, 1], flags.writeable], pyramid: numpy.ndarray[numpy.float64[m, 1]], mu: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Convert pyramid representation to contact force.
    """
def mju_dense2Band(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], ntotal: int, nband: int, ndense: int) -> None:
    """mju_dense2Band(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], ntotal: int, nband: int, ndense: int) -> None

    Convert dense matrix to banded matrix.
    """
def mju_dense2sparse(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], rownnz: numpy.ndarray[numpy.int32[m, 1], flags.writeable], rowadr: numpy.ndarray[numpy.int32[m, 1], flags.writeable], colind: numpy.ndarray[numpy.int32[m, 1], flags.writeable]) -> int:
    """mju_dense2sparse(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], rownnz: numpy.ndarray[numpy.int32[m, 1], flags.writeable], rowadr: numpy.ndarray[numpy.int32[m, 1], flags.writeable], colind: numpy.ndarray[numpy.int32[m, 1], flags.writeable]) -> int

    Convert matrix from dense to sparse.  nnz is size of res and colind, return 1 if too small, 0 otherwise.
    """
def mju_derivQuat(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]], vel: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_derivQuat(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]], vel: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Compute time-derivative of quaternion, given 3D rotational velocity.
    """
def mju_dist3(pos1: numpy.ndarray[numpy.float64[3, 1]], pos2: numpy.ndarray[numpy.float64[3, 1]]) -> float:
    """mju_dist3(pos1: numpy.ndarray[numpy.float64[3, 1]], pos2: numpy.ndarray[numpy.float64[3, 1]]) -> float

    Return Cartesian distance between 3D vectors pos1 and pos2.
    """
def mju_dot(vec1: numpy.ndarray[numpy.float64[m, 1]], vec2: numpy.ndarray[numpy.float64[m, 1]]) -> float:
    """mju_dot(vec1: numpy.ndarray[numpy.float64[m, 1]], vec2: numpy.ndarray[numpy.float64[m, 1]]) -> float

    Return dot-product of vec1 and vec2.
    """
def mju_dot3(vec1: numpy.ndarray[numpy.float64[3, 1]], vec2: numpy.ndarray[numpy.float64[3, 1]]) -> float:
    """mju_dot3(vec1: numpy.ndarray[numpy.float64[3, 1]], vec2: numpy.ndarray[numpy.float64[3, 1]]) -> float

    Return dot-product of vec1 and vec2.
    """
def mju_eig3(eigval: numpy.ndarray[numpy.float64[3, 1], flags.writeable], eigvec: numpy.ndarray[numpy.float64[9, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]]) -> int:
    """mju_eig3(eigval: numpy.ndarray[numpy.float64[3, 1], flags.writeable], eigvec: numpy.ndarray[numpy.float64[9, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]]) -> int

    Eigenvalue decomposition of symmetric 3x3 matrix, mat = eigvec * diag(eigval) * eigvec'.
    """
def mju_encodePyramid(pyramid: numpy.ndarray[numpy.float64[m, 1], flags.writeable], force: numpy.ndarray[numpy.float64[m, 1]], mu: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_encodePyramid(pyramid: numpy.ndarray[numpy.float64[m, 1], flags.writeable], force: numpy.ndarray[numpy.float64[m, 1]], mu: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Convert contact force to pyramid representation.
    """
def mju_euler2Quat(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], euler: numpy.ndarray[numpy.float64[3, 1]], seq: str) -> None:
    """mju_euler2Quat(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], euler: numpy.ndarray[numpy.float64[3, 1]], seq: str) -> None

    Convert sequence of Euler angles (radians) to quaternion. seq[0,1,2] must be in 'xyzXYZ', lower/upper-case mean intrinsic/extrinsic rotations.
    """
def mju_eye(mat: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]) -> None:
    """mju_eye(mat: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous]) -> None

    Set mat to the identity matrix.
    """
def mju_f2n(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float32[m, 1]]) -> None:
    """mju_f2n(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float32[m, 1]]) -> None

    Convert from float to mjtNum.
    """
def mju_fill(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], val: float) -> None:
    """mju_fill(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], val: float) -> None

    Set res = val.
    """
def mju_insertionSort(list: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None:
    """mju_insertionSort(list: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None

    Insertion sort, resulting list is in increasing order.
    """
def mju_insertionSortInt(list: numpy.ndarray[numpy.int32[m, 1], flags.writeable]) -> None:
    """mju_insertionSortInt(list: numpy.ndarray[numpy.int32[m, 1], flags.writeable]) -> None

    Integer insertion sort, resulting list is in increasing order.
    """
def mju_isBad(x: float) -> int:
    """mju_isBad(x: float) -> int

    Return 1 if nan or abs(x)>mjMAXVAL, 0 otherwise. Used by check functions.
    """
def mju_isZero(vec: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> int:
    """mju_isZero(vec: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> int

    Return 1 if all elements are 0.
    """
def mju_mat2Quat(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]]) -> None:
    """mju_mat2Quat(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]]) -> None

    Convert 3D rotation matrix to quaternion.
    """
def mju_mat2Rot(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]]) -> int:
    """mju_mat2Rot(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]]) -> int

    Extract 3D rotation from an arbitrary 3x3 matrix by refining the input quaternion. Returns the number of iterations required to converge
    """
def mju_max(a: float, b: float) -> float:
    """mju_max(a: float, b: float) -> float

    Return max(a,b) with single evaluation of a and b.
    """
def mju_min(a: float, b: float) -> float:
    """mju_min(a: float, b: float) -> float

    Return min(a,b) with single evaluation of a and b.
    """
def mju_mulMatMat(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat1: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], mat2: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None:
    """mju_mulMatMat(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat1: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], mat2: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None

    Multiply matrices: res = mat1 * mat2.
    """
def mju_mulMatMatT(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat1: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], mat2: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None:
    """mju_mulMatMatT(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat1: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], mat2: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None

    Multiply matrices, second argument transposed: res = mat1 * mat2'.
    """
def mju_mulMatTMat(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat1: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], mat2: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None:
    """mju_mulMatTMat(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat1: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], mat2: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None

    Multiply matrices, first argument transposed: res = mat1' * mat2.
    """
def mju_mulMatTVec(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_mulMatTVec(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Multiply transposed matrix and vector: res = mat' * vec.
    """
def mju_mulMatTVec3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_mulMatTVec3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Multiply transposed 3-by-3 matrix by vector: res = mat' * vec.
    """
def mju_mulMatVec(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_mulMatVec(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Multiply matrix and vector: res = mat * vec.
    """
def mju_mulMatVec3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_mulMatVec3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], mat: numpy.ndarray[numpy.float64[9, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Multiply 3-by-3 matrix by vector: res = mat * vec.
    """
def mju_mulPose(posres: numpy.ndarray[numpy.float64[3, 1], flags.writeable], quatres: numpy.ndarray[numpy.float64[4, 1], flags.writeable], pos1: numpy.ndarray[numpy.float64[3, 1]], quat1: numpy.ndarray[numpy.float64[4, 1]], pos2: numpy.ndarray[numpy.float64[3, 1]], quat2: numpy.ndarray[numpy.float64[4, 1]]) -> None:
    """mju_mulPose(posres: numpy.ndarray[numpy.float64[3, 1], flags.writeable], quatres: numpy.ndarray[numpy.float64[4, 1], flags.writeable], pos1: numpy.ndarray[numpy.float64[3, 1]], quat1: numpy.ndarray[numpy.float64[4, 1]], pos2: numpy.ndarray[numpy.float64[3, 1]], quat2: numpy.ndarray[numpy.float64[4, 1]]) -> None

    Multiply two poses.
    """
def mju_mulQuat(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], quat1: numpy.ndarray[numpy.float64[4, 1]], quat2: numpy.ndarray[numpy.float64[4, 1]]) -> None:
    """mju_mulQuat(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], quat1: numpy.ndarray[numpy.float64[4, 1]], quat2: numpy.ndarray[numpy.float64[4, 1]]) -> None

    Multiply quaternions.
    """
def mju_mulQuatAxis(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]], axis: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_mulQuatAxis(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]], axis: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Multiply quaternion and axis.
    """
def mju_mulVecMatVec(vec1: numpy.ndarray[numpy.float64[m, 1]], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec2: numpy.ndarray[numpy.float64[m, 1]]) -> float:
    """mju_mulVecMatVec(vec1: numpy.ndarray[numpy.float64[m, 1]], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], vec2: numpy.ndarray[numpy.float64[m, 1]]) -> float

    Multiply square matrix with vectors on both sides: returns vec1' * mat * vec2.
    """
def mju_muscleBias(len: float, lengthrange: numpy.ndarray[numpy.float64[2, 1]], acc0: float, prm: numpy.ndarray[numpy.float64[9, 1]]) -> float:
    """mju_muscleBias(len: float, lengthrange: numpy.ndarray[numpy.float64[2, 1]], acc0: float, prm: numpy.ndarray[numpy.float64[9, 1]]) -> float

    Muscle passive force, prm = (range[2], force, scale, lmin, lmax, vmax, fpmax, fvmax).
    """
def mju_muscleDynamics(ctrl: float, act: float, prm: numpy.ndarray[numpy.float64[3, 1]]) -> float:
    """mju_muscleDynamics(ctrl: float, act: float, prm: numpy.ndarray[numpy.float64[3, 1]]) -> float

    Muscle activation dynamics, prm = (tau_act, tau_deact, smoothing_width).
    """
def mju_muscleGain(len: float, vel: float, lengthrange: numpy.ndarray[numpy.float64[2, 1]], acc0: float, prm: numpy.ndarray[numpy.float64[9, 1]]) -> float:
    """mju_muscleGain(len: float, vel: float, lengthrange: numpy.ndarray[numpy.float64[2, 1]], acc0: float, prm: numpy.ndarray[numpy.float64[9, 1]]) -> float

    Muscle active force, prm = (range[2], force, scale, lmin, lmax, vmax, fpmax, fvmax).
    """
def mju_n2d(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_n2d(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Convert from mjtNum to double.
    """
def mju_n2f(res: numpy.ndarray[numpy.float32[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_n2f(res: numpy.ndarray[numpy.float32[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Convert from mjtNum to float.
    """
def mju_negPose(posres: numpy.ndarray[numpy.float64[3, 1], flags.writeable], quatres: numpy.ndarray[numpy.float64[4, 1], flags.writeable], pos: numpy.ndarray[numpy.float64[3, 1]], quat: numpy.ndarray[numpy.float64[4, 1]]) -> None:
    """mju_negPose(posres: numpy.ndarray[numpy.float64[3, 1], flags.writeable], quatres: numpy.ndarray[numpy.float64[4, 1], flags.writeable], pos: numpy.ndarray[numpy.float64[3, 1]], quat: numpy.ndarray[numpy.float64[4, 1]]) -> None

    Conjugate pose, corresponding to the opposite spatial transformation.
    """
def mju_negQuat(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]]) -> None:
    """mju_negQuat(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]]) -> None

    Conjugate quaternion, corresponding to opposite rotation.
    """
def mju_norm(res: numpy.ndarray[numpy.float64[m, 1]]) -> float:
    """mju_norm(res: numpy.ndarray[numpy.float64[m, 1]]) -> float

    Return vector length (without normalizing vector).
    """
def mju_norm3(vec: numpy.ndarray[numpy.float64[3, 1]]) -> float:
    """mju_norm3(vec: numpy.ndarray[numpy.float64[3, 1]]) -> float

    Return vector length (without normalizing the vector).
    """
def mju_normalize(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> float:
    """mju_normalize(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> float

    Normalize vector, return length before normalization.
    """
def mju_normalize3(vec: numpy.ndarray[numpy.float64[3, 1], flags.writeable]) -> float:
    """mju_normalize3(vec: numpy.ndarray[numpy.float64[3, 1], flags.writeable]) -> float

    Normalize vector, return length before normalization.
    """
def mju_normalize4(vec: numpy.ndarray[numpy.float64[4, 1], flags.writeable]) -> float:
    """mju_normalize4(vec: numpy.ndarray[numpy.float64[4, 1], flags.writeable]) -> float

    Normalize vector, return length before normalization.
    """
def mju_printMat(mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None:
    """mju_printMat(mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None

    Print matrix to screen.
    """
def mju_printMatSparse(mat: numpy.ndarray[numpy.float64[m, 1]], rownnz: numpy.ndarray[numpy.int32[m, 1]], rowadr: numpy.ndarray[numpy.int32[m, 1]], colind: numpy.ndarray[numpy.int32[m, 1]]) -> None:
    """mju_printMatSparse(mat: numpy.ndarray[numpy.float64[m, 1]], rownnz: numpy.ndarray[numpy.int32[m, 1]], rowadr: numpy.ndarray[numpy.int32[m, 1]], colind: numpy.ndarray[numpy.int32[m, 1]]) -> None

    Print sparse matrix to screen.
    """
def mju_quat2Mat(res: numpy.ndarray[numpy.float64[9, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]]) -> None:
    """mju_quat2Mat(res: numpy.ndarray[numpy.float64[9, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]]) -> None

    Convert quaternion to 3D rotation matrix.
    """
def mju_quat2Vel(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]], dt: float) -> None:
    """mju_quat2Vel(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], quat: numpy.ndarray[numpy.float64[4, 1]], dt: float) -> None

    Convert quaternion (corresponding to orientation difference) to 3D velocity.
    """
def mju_quatIntegrate(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], vel: numpy.ndarray[numpy.float64[3, 1]], scale: float) -> None:
    """mju_quatIntegrate(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], vel: numpy.ndarray[numpy.float64[3, 1]], scale: float) -> None

    Integrate quaternion given 3D angular velocity.
    """
def mju_quatZ2Vec(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_quatZ2Vec(quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Construct quaternion performing rotation from z-axis to given vector.
    """
def mju_rayFlex(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, flex_layer: int, flg_vert: int, flg_edge: int, flg_face: int, flg_skin: int, flexid: int, pnt: float, vec: float, vertid: numpy.ndarray[numpy.int32[1, 1], flags.writeable]) -> float:
    """mju_rayFlex(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, flex_layer: int, flg_vert: int, flg_edge: int, flg_face: int, flg_skin: int, flexid: int, pnt: float, vec: float, vertid: numpy.ndarray[numpy.int32[1, 1], flags.writeable]) -> float

    Intersect ray with flex, return nearest distance or -1 if no intersection, and also output nearest vertex id.
    """
def mju_rayGeom(pos: numpy.ndarray[numpy.float64[3, 1]], mat: numpy.ndarray[numpy.float64[9, 1]], size: numpy.ndarray[numpy.float64[3, 1]], pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]], geomtype: int) -> float:
    """mju_rayGeom(pos: numpy.ndarray[numpy.float64[3, 1]], mat: numpy.ndarray[numpy.float64[9, 1]], size: numpy.ndarray[numpy.float64[3, 1]], pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]], geomtype: int) -> float

    Intersect ray with pure geom, return nearest distance or -1 if no intersection.
    """
def mju_raySkin(nface: int, nvert: int, face: int, vert: float, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]], vertid: numpy.ndarray[numpy.int32[1, 1], flags.writeable]) -> float:
    """mju_raySkin(nface: int, nvert: int, face: int, vert: float, pnt: numpy.ndarray[numpy.float64[3, 1]], vec: numpy.ndarray[numpy.float64[3, 1]], vertid: numpy.ndarray[numpy.int32[1, 1], flags.writeable]) -> float

    Intersect ray with skin, return nearest distance or -1 if no intersection, and also output nearest vertex id.
    """
def mju_rotVecQuat(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]], quat: numpy.ndarray[numpy.float64[4, 1]]) -> None:
    """mju_rotVecQuat(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]], quat: numpy.ndarray[numpy.float64[4, 1]]) -> None

    Rotate vector by quaternion.
    """
def mju_round(x: float) -> int:
    """mju_round(x: float) -> int

    Round x to nearest integer.
    """
def mju_scl(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]], scl: float) -> None:
    """mju_scl(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]], scl: float) -> None

    Set res = vec*scl.
    """
def mju_scl3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]], scl: float) -> None:
    """mju_scl3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]], scl: float) -> None

    Set res = vec*scl.
    """
def mju_sigmoid(x: float) -> float:
    """mju_sigmoid(x: float) -> float

    Sigmoid function over 0<=x<=1 using quintic polynomial.
    """
def mju_sign(x: float) -> float:
    """mju_sign(x: float) -> float

    Return sign of x: +1, -1 or 0.
    """
def mju_sparse2dense(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, 1]], rownnz: numpy.ndarray[numpy.int32[m, 1]], rowadr: numpy.ndarray[numpy.int32[m, 1]], colind: numpy.ndarray[numpy.int32[m, 1]]) -> None:
    """mju_sparse2dense(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, 1]], rownnz: numpy.ndarray[numpy.int32[m, 1]], rowadr: numpy.ndarray[numpy.int32[m, 1]], colind: numpy.ndarray[numpy.int32[m, 1]]) -> None

    Convert matrix from sparse to dense.
    """
def mju_springDamper(pos0: float, vel0: float, Kp: float, Kv: float, dt: float) -> float:
    """mju_springDamper(pos0: float, vel0: float, Kp: float, Kv: float, dt: float) -> float

    Integrate spring-damper analytically, return pos(dt).
    """
def mju_sqrMatTD(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], diag: numpy.ndarray[numpy.float64[m, 1], flags.writeable] | None) -> None:
    """mju_sqrMatTD(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous], diag: Optional[numpy.ndarray[numpy.float64[m, 1], flags.writeable]]) -> None

    Set res = mat' * diag * mat if diag is not NULL, and res = mat' * mat otherwise.
    """
def mju_standardNormal(num2: float | None) -> float:
    """mju_standardNormal(num2: Optional[float]) -> float

    Standard normal random number generator (optional second number).
    """
def mju_str2Type(str: str) -> int:
    """mju_str2Type(str: str) -> int

    Convert type name to type id (mjtObj).
    """
def mju_sub(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[m, 1]], vec2: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_sub(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[m, 1]], vec2: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Set res = vec1 - vec2.
    """
def mju_sub3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[3, 1]], vec2: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_sub3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec1: numpy.ndarray[numpy.float64[3, 1]], vec2: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Set res = vec1 - vec2.
    """
def mju_subFrom(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None:
    """mju_subFrom(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[m, 1]]) -> None

    Set res = res - vec.
    """
def mju_subFrom3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_subFrom3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Set res = res - vec.
    """
def mju_subQuat(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], qa: numpy.ndarray[numpy.float64[4, 1]], qb: numpy.ndarray[numpy.float64[4, 1]]) -> None:
    """mju_subQuat(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], qa: numpy.ndarray[numpy.float64[4, 1]], qb: numpy.ndarray[numpy.float64[4, 1]]) -> None

    Subtract quaternions, express as 3D velocity: qb*quat(res) = qa.
    """
def mju_sum(vec: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> float:
    """mju_sum(vec: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> float

    Return sum(vec).
    """
def mju_symmetrize(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None:
    """mju_symmetrize(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None

    Symmetrize square matrix res = (mat + mat')/2.
    """
def mju_transformSpatial(res: numpy.ndarray[numpy.float64[6, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[6, 1]], flg_force: int, newpos: numpy.ndarray[numpy.float64[3, 1]], oldpos: numpy.ndarray[numpy.float64[3, 1]], rotnew2old: numpy.ndarray[numpy.float64[9, 1]]) -> None:
    """mju_transformSpatial(res: numpy.ndarray[numpy.float64[6, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[6, 1]], flg_force: int, newpos: numpy.ndarray[numpy.float64[3, 1]], oldpos: numpy.ndarray[numpy.float64[3, 1]], rotnew2old: numpy.ndarray[numpy.float64[9, 1]]) -> None

    Coordinate transform of 6D motion or force vector in rotation:translation format. rotnew2old is 3-by-3, NULL means no rotation; flg_force specifies force or motion type.
    """
def mju_transpose(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None:
    """mju_transpose(res: numpy.ndarray[numpy.float64[m, n], flags.writeable, flags.c_contiguous], mat: numpy.ndarray[numpy.float64[m, n], flags.c_contiguous]) -> None

    Transpose matrix: res = mat'.
    """
def mju_trnVecPose(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], pos: numpy.ndarray[numpy.float64[3, 1]], quat: numpy.ndarray[numpy.float64[4, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mju_trnVecPose(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], pos: numpy.ndarray[numpy.float64[3, 1]], quat: numpy.ndarray[numpy.float64[4, 1]], vec: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Transform vector by pose.
    """
def mju_type2Str(type: int) -> str:
    """mju_type2Str(type: int) -> str

    Convert type id (mjtObj) to type name.
    """
def mju_unit4(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable]) -> None:
    """mju_unit4(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable]) -> None

    Set res = (1,0,0,0).
    """
def mju_warningText(warning: int, info: int) -> str:
    """mju_warningText(warning: int, info: int) -> str

    Construct a warning message given the warning type and info.
    """
def mju_writeLog(type: str, msg: str) -> None:
    """mju_writeLog(type: str, msg: str) -> None

    Write [datetime, type: message] to MUJOCO_LOG.TXT.
    """
def mju_writeNumBytes(nbytes: int) -> str:
    """mju_writeNumBytes(nbytes: int) -> str

    Return human readable number of bytes using standard letter suffix.
    """
def mju_zero(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None:
    """mju_zero(res: numpy.ndarray[numpy.float64[m, 1], flags.writeable]) -> None

    Set res = 0.
    """
def mju_zero3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable]) -> None:
    """mju_zero3(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable]) -> None

    Set res = 0.
    """
def mju_zero4(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable]) -> None:
    """mju_zero4(res: numpy.ndarray[numpy.float64[4, 1], flags.writeable]) -> None

    Set res = 0.
    """
def mjv_addGeoms(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, opt: mujoco._structs.MjvOption, pert: mujoco._structs.MjvPerturb, catmask: int, scn: mujoco._structs.MjvScene) -> None:
    """mjv_addGeoms(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, opt: mujoco._structs.MjvOption, pert: mujoco._structs.MjvPerturb, catmask: int, scn: mujoco._structs.MjvScene) -> None

    Add geoms from selected categories.
    """
def mjv_alignToCamera(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]], forward: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mjv_alignToCamera(res: numpy.ndarray[numpy.float64[3, 1], flags.writeable], vec: numpy.ndarray[numpy.float64[3, 1]], forward: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Rotate 3D vec in horizontal plane by angle between (0,1) and (forward_x,forward_y).
    """
def mjv_applyPerturbForce(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, pert: mujoco._structs.MjvPerturb) -> None:
    """mjv_applyPerturbForce(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, pert: mujoco._structs.MjvPerturb) -> None

    Set perturb force,torque in d->xfrc_applied, if selected body is dynamic.
    """
def mjv_applyPerturbPose(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, pert: mujoco._structs.MjvPerturb, flg_paused: int) -> None:
    """mjv_applyPerturbPose(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, pert: mujoco._structs.MjvPerturb, flg_paused: int) -> None

    Set perturb pos,quat in d->mocap when selected body is mocap, and in d->qpos otherwise. Write d->qpos only if flg_paused and subtree root for selected body has free joint.
    """
def mjv_cameraInModel(headpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], forward: numpy.ndarray[numpy.float64[3, 1], flags.writeable], up: numpy.ndarray[numpy.float64[3, 1], flags.writeable], scn: mujoco._structs.MjvScene) -> None:
    """mjv_cameraInModel(headpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], forward: numpy.ndarray[numpy.float64[3, 1], flags.writeable], up: numpy.ndarray[numpy.float64[3, 1], flags.writeable], scn: mujoco._structs.MjvScene) -> None

    Get camera info in model space; average left and right OpenGL cameras.
    """
def mjv_cameraInRoom(headpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], forward: numpy.ndarray[numpy.float64[3, 1], flags.writeable], up: numpy.ndarray[numpy.float64[3, 1], flags.writeable], scn: mujoco._structs.MjvScene) -> None:
    """mjv_cameraInRoom(headpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], forward: numpy.ndarray[numpy.float64[3, 1], flags.writeable], up: numpy.ndarray[numpy.float64[3, 1], flags.writeable], scn: mujoco._structs.MjvScene) -> None

    Get camera info in room space; average left and right OpenGL cameras.
    """
def mjv_connector(geom: mujoco._structs.MjvGeom, type: int, width: float, from_: numpy.ndarray[numpy.float64[3, 1]], to: numpy.ndarray[numpy.float64[3, 1]]) -> None:
    """mjv_connector(geom: mujoco._structs.MjvGeom, type: int, width: float, from_: numpy.ndarray[numpy.float64[3, 1]], to: numpy.ndarray[numpy.float64[3, 1]]) -> None

    Set (type, size, pos, mat) for connector-type geom between given points. Assume that mjv_initGeom was already called to set all other properties. Width of mjGEOM_LINE is denominated in pixels.
    """
def mjv_defaultCamera(cam: mujoco._structs.MjvCamera) -> None:
    """mjv_defaultCamera(cam: mujoco._structs.MjvCamera) -> None

    Set default camera.
    """
def mjv_defaultFigure(fig: mujoco._structs.MjvFigure) -> None:
    """mjv_defaultFigure(fig: mujoco._structs.MjvFigure) -> None

    Set default figure.
    """
def mjv_defaultFreeCamera(m: mujoco._structs.MjModel, cam: mujoco._structs.MjvCamera) -> None:
    """mjv_defaultFreeCamera(m: mujoco._structs.MjModel, cam: mujoco._structs.MjvCamera) -> None

    Set default free camera.
    """
def mjv_defaultOption(opt: mujoco._structs.MjvOption) -> None:
    """mjv_defaultOption(opt: mujoco._structs.MjvOption) -> None

    Set default visualization options.
    """
def mjv_defaultPerturb(pert: mujoco._structs.MjvPerturb) -> None:
    """mjv_defaultPerturb(pert: mujoco._structs.MjvPerturb) -> None

    Set default perturbation.
    """
def mjv_frustumHeight(scn: mujoco._structs.MjvScene) -> float:
    """mjv_frustumHeight(scn: mujoco._structs.MjvScene) -> float

    Get frustum height at unit distance from camera; average left and right OpenGL cameras.
    """
def mjv_initGeom(geom: mujoco._structs.MjvGeom, type: int, size: numpy.ndarray[numpy.float64[3, 1]], pos: numpy.ndarray[numpy.float64[3, 1]], mat: numpy.ndarray[numpy.float64[9, 1]], rgba: numpy.ndarray[numpy.float32[4, 1]]) -> None:
    """mjv_initGeom(geom: mujoco._structs.MjvGeom, type: int, size: numpy.ndarray[numpy.float64[3, 1]], pos: numpy.ndarray[numpy.float64[3, 1]], mat: numpy.ndarray[numpy.float64[9, 1]], rgba: numpy.ndarray[numpy.float32[4, 1]]) -> None

    Initialize given geom fields when not NULL, set the rest to their default values.
    """
def mjv_initPerturb(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, scn: mujoco._structs.MjvScene, pert: mujoco._structs.MjvPerturb) -> None:
    """mjv_initPerturb(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, scn: mujoco._structs.MjvScene, pert: mujoco._structs.MjvPerturb) -> None

    Copy perturb pos,quat from selected body; set scale for perturbation.
    """
def mjv_makeLights(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, scn: mujoco._structs.MjvScene) -> None:
    """mjv_makeLights(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, scn: mujoco._structs.MjvScene) -> None

    Make list of lights.
    """
def mjv_model2room(roompos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], roomquat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], modelpos: numpy.ndarray[numpy.float64[3, 1]], modelquat: numpy.ndarray[numpy.float64[4, 1]], scn: mujoco._structs.MjvScene) -> None:
    """mjv_model2room(roompos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], roomquat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], modelpos: numpy.ndarray[numpy.float64[3, 1]], modelquat: numpy.ndarray[numpy.float64[4, 1]], scn: mujoco._structs.MjvScene) -> None

    Transform pose from model to room space.
    """
def mjv_moveCamera(m: mujoco._structs.MjModel, action: int, reldx: float, reldy: float, scn: mujoco._structs.MjvScene, cam: mujoco._structs.MjvCamera) -> None:
    """mjv_moveCamera(m: mujoco._structs.MjModel, action: int, reldx: float, reldy: float, scn: mujoco._structs.MjvScene, cam: mujoco._structs.MjvCamera) -> None

    Move camera with mouse; action is mjtMouse.
    """
def mjv_moveModel(m: mujoco._structs.MjModel, action: int, reldx: float, reldy: float, roomup: numpy.ndarray[numpy.float64[3, 1]], scn: mujoco._structs.MjvScene) -> None:
    """mjv_moveModel(m: mujoco._structs.MjModel, action: int, reldx: float, reldy: float, roomup: numpy.ndarray[numpy.float64[3, 1]], scn: mujoco._structs.MjvScene) -> None

    Move model with mouse; action is mjtMouse.
    """
def mjv_movePerturb(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, action: int, reldx: float, reldy: float, scn: mujoco._structs.MjvScene, pert: mujoco._structs.MjvPerturb) -> None:
    """mjv_movePerturb(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, action: int, reldx: float, reldy: float, scn: mujoco._structs.MjvScene, pert: mujoco._structs.MjvPerturb) -> None

    Move perturb object with mouse; action is mjtMouse.
    """
def mjv_room2model(modelpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], modelquat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], roompos: numpy.ndarray[numpy.float64[3, 1]], roomquat: numpy.ndarray[numpy.float64[4, 1]], scn: mujoco._structs.MjvScene) -> None:
    """mjv_room2model(modelpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable], modelquat: numpy.ndarray[numpy.float64[4, 1], flags.writeable], roompos: numpy.ndarray[numpy.float64[3, 1]], roomquat: numpy.ndarray[numpy.float64[4, 1]], scn: mujoco._structs.MjvScene) -> None

    Transform pose from room to model space.
    """
def mjv_select(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, vopt: mujoco._structs.MjvOption, aspectratio: float, relx: float, rely: float, scn: mujoco._structs.MjvScene, selpnt: numpy.ndarray[numpy.float64[3, 1], flags.writeable], geomid: numpy.ndarray[numpy.int32[1, 1], flags.writeable], flexid: numpy.ndarray[numpy.int32[1, 1], flags.writeable], skinid: numpy.ndarray[numpy.int32[1, 1], flags.writeable]) -> int:
    """mjv_select(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, vopt: mujoco._structs.MjvOption, aspectratio: float, relx: float, rely: float, scn: mujoco._structs.MjvScene, selpnt: numpy.ndarray[numpy.float64[3, 1], flags.writeable], geomid: numpy.ndarray[numpy.int32[1, 1], flags.writeable], flexid: numpy.ndarray[numpy.int32[1, 1], flags.writeable], skinid: numpy.ndarray[numpy.int32[1, 1], flags.writeable]) -> int

    Select geom, flex or skin with mouse, return bodyid; -1: none selected.
    """
def mjv_updateCamera(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, cam: mujoco._structs.MjvCamera, scn: mujoco._structs.MjvScene) -> None:
    """mjv_updateCamera(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, cam: mujoco._structs.MjvCamera, scn: mujoco._structs.MjvScene) -> None

    Update camera.
    """
def mjv_updateScene(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, opt: mujoco._structs.MjvOption, pert: mujoco._structs.MjvPerturb | None, cam: mujoco._structs.MjvCamera, catmask: int, scn: mujoco._structs.MjvScene) -> None:
    """mjv_updateScene(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, opt: mujoco._structs.MjvOption, pert: Optional[mujoco._structs.MjvPerturb], cam: mujoco._structs.MjvCamera, catmask: int, scn: mujoco._structs.MjvScene) -> None

    Update entire scene given model state.
    """
def mjv_updateSkin(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, scn: mujoco._structs.MjvScene) -> None:
    """mjv_updateSkin(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, scn: mujoco._structs.MjvScene) -> None

    Update skins.
    """

# --- mujoco._render ---
import mujoco._structs
import numpy
from typing import overload

class MjrContext:
    auxColor: numpy.ndarray[numpy.uint32]
    auxColor_r: numpy.ndarray[numpy.uint32]
    auxFBO: numpy.ndarray[numpy.uint32]
    auxFBO_r: numpy.ndarray[numpy.uint32]
    auxHeight: numpy.ndarray[numpy.int32]
    auxSamples: numpy.ndarray[numpy.int32]
    auxWidth: numpy.ndarray[numpy.int32]
    baseBuiltin: int
    baseFontBig: int
    baseFontNormal: int
    baseFontShadow: int
    baseHField: int
    baseMesh: int
    basePlane: int
    charHeight: int
    charHeightBig: int
    charWidth: numpy.ndarray[numpy.int32]
    charWidthBig: numpy.ndarray[numpy.int32]
    currentBuffer: int
    fogEnd: float
    fogRGBA: numpy.ndarray[numpy.float32]
    fogStart: float
    fontScale: int
    glInitialized: int
    lineWidth: float
    mat_texid: numpy.ndarray[numpy.int32]
    mat_texrepeat: numpy.ndarray[numpy.float32]
    mat_texuniform: numpy.ndarray[numpy.int32]
    ntexture: int
    offColor: int
    offColor_r: int
    offDepthStencil: int
    offDepthStencil_r: int
    offFBO: int
    offFBO_r: int
    offHeight: int
    offSamples: int
    offWidth: int
    rangeBuiltin: int
    rangeFont: int
    rangeHField: int
    rangeMesh: int
    rangePlane: int
    readDepthMap: int
    readPixelFormat: int
    shadowClip: float
    shadowFBO: int
    shadowScale: float
    shadowSize: int
    shadowTex: int
    texture: numpy.ndarray[numpy.uint32]
    textureType: numpy.ndarray[numpy.int32]
    windowAvailable: int
    windowDoublebuffer: int
    windowSamples: int
    windowStereo: int
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._render.MjrContext) -> None

        2. __init__(self: mujoco._render.MjrContext, arg0: mujoco._structs.MjModel, arg1: int) -> None
        """
    @overload
    def __init__(self, arg0: mujoco._structs.MjModel, arg1: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._render.MjrContext) -> None

        2. __init__(self: mujoco._render.MjrContext, arg0: mujoco._structs.MjModel, arg1: int) -> None
        """
    def free(self) -> None:
        """free(self: mujoco._render.MjrContext) -> None

        Frees resources in current active OpenGL context, sets struct to default.
        """
    @property
    def nskin(self) -> int: ...
    @property
    def skinfaceVBO(self) -> tuple: ...
    @property
    def skinnormalVBO(self) -> tuple: ...
    @property
    def skintexcoordVBO(self) -> tuple: ...
    @property
    def skinvertVBO(self) -> tuple: ...

class MjrRect:
    bottom: int
    height: int
    left: int
    width: int
    def __init__(self, left: int, bottom: int, width: int, height: int) -> None:
        """__init__(self: mujoco._render.MjrRect, left: int, bottom: int, width: int, height: int) -> None"""
    def __copy__(self) -> MjrRect:
        """__copy__(self: mujoco._render.MjrRect) -> mujoco._render.MjrRect"""
    def __deepcopy__(self, arg0: dict) -> MjrRect:
        """__deepcopy__(self: mujoco._render.MjrRect, arg0: dict) -> mujoco._render.MjrRect"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

def mjr_addAux(index: int, width: int, height: int, samples: int, con: MjrContext) -> None:
    """mjr_addAux(index: int, width: int, height: int, samples: int, con: mujoco._render.MjrContext) -> None

    Add Aux buffer with given index to context; free previous Aux buffer.
    """
def mjr_blitAux(index: int, src: MjrRect, left: int, bottom: int, con: MjrContext) -> None:
    """mjr_blitAux(index: int, src: mujoco._render.MjrRect, left: int, bottom: int, con: mujoco._render.MjrContext) -> None

    Blit from Aux buffer to con->currentBuffer.
    """
def mjr_blitBuffer(src: MjrRect, dst: MjrRect, flg_color: int, flg_depth: int, con: MjrContext) -> None:
    """mjr_blitBuffer(src: mujoco._render.MjrRect, dst: mujoco._render.MjrRect, flg_color: int, flg_depth: int, con: mujoco._render.MjrContext) -> None

    Blit from src viewpoint in current framebuffer to dst viewport in other framebuffer. If src, dst have different size and flg_depth==0, color is interpolated with GL_LINEAR.
    """
def mjr_changeFont(fontscale: int, con: MjrContext) -> None:
    """mjr_changeFont(fontscale: int, con: mujoco._render.MjrContext) -> None

    Change font of existing context.
    """
def mjr_drawPixels(rgb: numpy.ndarray[numpy.uint8[m, 1]] | None, depth: numpy.ndarray[numpy.float32[m, 1]] | None, viewport: MjrRect, con: MjrContext) -> None:
    """mjr_drawPixels(rgb: Optional[numpy.ndarray[numpy.uint8[m, 1]]], depth: Optional[numpy.ndarray[numpy.float32[m, 1]]], viewport: mujoco._render.MjrRect, con: mujoco._render.MjrContext) -> None

    Draw pixels from client buffer to current OpenGL framebuffer. Viewport is in OpenGL framebuffer; client buffer starts at (0,0).
    """
def mjr_figure(viewport: MjrRect, fig: mujoco._structs.MjvFigure, con: MjrContext) -> None:
    """mjr_figure(viewport: mujoco._render.MjrRect, fig: mujoco._structs.MjvFigure, con: mujoco._render.MjrContext) -> None

    Draw 2D figure.
    """
def mjr_findRect(x: int, y: int, nrect: int, rect: MjrRect) -> int:
    """mjr_findRect(x: int, y: int, nrect: int, rect: mujoco._render.MjrRect) -> int

    Find first rectangle containing mouse, -1: not found.
    """
def mjr_finish() -> None:
    """mjr_finish() -> None

    Call glFinish.
    """
def mjr_getError() -> int:
    """mjr_getError() -> int

    Call glGetError and return result.
    """
def mjr_label(viewport: MjrRect, font: int, txt: str, r: float, g: float, b: float, a: float, rt: float, gt: float, bt: float, con: MjrContext) -> None:
    """mjr_label(viewport: mujoco._render.MjrRect, font: int, txt: str, r: float, g: float, b: float, a: float, rt: float, gt: float, bt: float, con: mujoco._render.MjrContext) -> None

    Draw rectangle with centered text.
    """
def mjr_maxViewport(con: MjrContext) -> MjrRect:
    """mjr_maxViewport(con: mujoco._render.MjrContext) -> mujoco._render.MjrRect

    Get maximum viewport for active buffer.
    """
def mjr_overlay(font: int, gridpos: int, viewport: MjrRect, overlay: str, overlay2: str, con: MjrContext) -> None:
    """mjr_overlay(font: int, gridpos: int, viewport: mujoco._render.MjrRect, overlay: str, overlay2: str, con: mujoco._render.MjrContext) -> None

    Draw text overlay; font is mjtFont; gridpos is mjtGridPos.
    """
def mjr_readPixels(rgb: numpy.ndarray[numpy.uint8] | None, depth: numpy.ndarray[numpy.float32] | None, viewport: MjrRect, con: MjrContext) -> None:
    """mjr_readPixels(rgb: Optional[numpy.ndarray[numpy.uint8]], depth: Optional[numpy.ndarray[numpy.float32]], viewport: mujoco._render.MjrRect, con: mujoco._render.MjrContext) -> None

    Read pixels from current OpenGL framebuffer to client buffer. Viewport is in OpenGL framebuffer; client buffer starts at (0,0).
    """
def mjr_rectangle(viewport: MjrRect, r: float, g: float, b: float, a: float) -> None:
    """mjr_rectangle(viewport: mujoco._render.MjrRect, r: float, g: float, b: float, a: float) -> None

    Draw rectangle.
    """
def mjr_render(viewport: MjrRect, scn: mujoco._structs.MjvScene, con: MjrContext) -> None:
    """mjr_render(viewport: mujoco._render.MjrRect, scn: mujoco._structs.MjvScene, con: mujoco._render.MjrContext) -> None

    Render 3D scene.
    """
def mjr_resizeOffscreen(width: int, height: int, con: MjrContext) -> None:
    """mjr_resizeOffscreen(width: int, height: int, con: mujoco._render.MjrContext) -> None

    Resize offscreen buffers.
    """
def mjr_restoreBuffer(con: MjrContext) -> None:
    """mjr_restoreBuffer(con: mujoco._render.MjrContext) -> None

    Make con->currentBuffer current again.
    """
def mjr_setAux(index: int, con: MjrContext) -> None:
    """mjr_setAux(index: int, con: mujoco._render.MjrContext) -> None

    Set Aux buffer for custom OpenGL rendering (call restoreBuffer when done).
    """
def mjr_setBuffer(framebuffer: int, con: MjrContext) -> None:
    """mjr_setBuffer(framebuffer: int, con: mujoco._render.MjrContext) -> None

    Set OpenGL framebuffer for rendering: mjFB_WINDOW or mjFB_OFFSCREEN. If only one buffer is available, set that buffer and ignore framebuffer argument.
    """
def mjr_text(font: int, txt: str, con: MjrContext, x: float, y: float, r: float, g: float, b: float) -> None:
    """mjr_text(font: int, txt: str, con: mujoco._render.MjrContext, x: float, y: float, r: float, g: float, b: float) -> None

    Draw text at (x,y) in relative coordinates; font is mjtFont.
    """
def mjr_uploadHField(m: mujoco._structs.MjModel, con: MjrContext, hfieldid: int) -> None:
    """mjr_uploadHField(m: mujoco._structs.MjModel, con: mujoco._render.MjrContext, hfieldid: int) -> None

    Upload height field to GPU, overwriting previous upload if any.
    """
def mjr_uploadMesh(m: mujoco._structs.MjModel, con: MjrContext, meshid: int) -> None:
    """mjr_uploadMesh(m: mujoco._structs.MjModel, con: mujoco._render.MjrContext, meshid: int) -> None

    Upload mesh to GPU, overwriting previous upload if any.
    """
def mjr_uploadTexture(m: mujoco._structs.MjModel, con: MjrContext, texid: int) -> None:
    """mjr_uploadTexture(m: mujoco._structs.MjModel, con: mujoco._render.MjrContext, texid: int) -> None

    Upload texture to GPU, overwriting previous upload if any.
    """

# --- mujoco._specs ---
import flags
import mujoco._enums
import mujoco._structs
import mujoco._structs.MjVisual
import numpy
from typing import Callable, ClassVar, Iterator, overload

class MjByteVec:
    def __init__(self, arg0, arg1: int) -> None:
        """__init__(self: mujoco._specs.MjByteVec, arg0: std::byte, arg1: int) -> None"""
    def __getitem__(self, index):
        """__getitem__(self: mujoco._specs.MjByteVec, arg0: int) -> std::byte"""
    def __iter__(self):
        """__iter__(self: mujoco._specs.MjByteVec) -> Iterator[std::byte]"""
    def __len__(self) -> int:
        """__len__(self: mujoco._specs.MjByteVec) -> int"""
    def __setitem__(self, arg0: int, arg1) -> None:
        """__setitem__(self: mujoco._specs.MjByteVec, arg0: int, arg1: std::byte) -> None"""

class MjCharVec:
    def __init__(self, arg0: str, arg1: int) -> None:
        """__init__(self: mujoco._specs.MjCharVec, arg0: str, arg1: int) -> None"""
    def __getitem__(self, arg0: int) -> str:
        """__getitem__(self: mujoco._specs.MjCharVec, arg0: int) -> str"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: mujoco._specs.MjCharVec) -> Iterator[str]"""
    def __len__(self) -> int:
        """__len__(self: mujoco._specs.MjCharVec) -> int"""
    def __setitem__(self, arg0: int, arg1: str) -> None:
        """__setitem__(self: mujoco._specs.MjCharVec, arg0: int, arg1: str) -> None"""

class MjOption:
    apirate: float
    ccd_iterations: int
    ccd_tolerance: float
    cone: int
    density: float
    disableactuator: int
    disableflags: int
    enableflags: int
    gravity: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    impratio: float
    integrator: int
    iterations: int
    jacobian: int
    ls_iterations: int
    ls_tolerance: float
    magnetic: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    noslip_iterations: int
    noslip_tolerance: float
    o_friction: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    o_margin: float
    o_solimp: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    o_solref: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    sdf_initpoints: int
    sdf_iterations: int
    solver: int
    timestep: float
    tolerance: float
    viscosity: float
    wind: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjSpec:
    to_zip: ClassVar[Callable] = ...
    assets: dict
    comment: str
    compiler: MjsCompiler
    copy_during_attach: None
    hasImplicitPluginElem: int
    memory: int
    meshdir: str
    modelfiledir: str
    modelname: str
    nconmax: int
    nemax: int
    njmax: int
    nkey: int
    nstack: int
    nuser_actuator: int
    nuser_body: int
    nuser_cam: int
    nuser_geom: int
    nuser_jnt: int
    nuser_sensor: int
    nuser_site: int
    nuser_tendon: int
    nuserdata: int
    option: MjOption
    override_assets: bool
    stat: MjStatistic
    strippath: int
    texturedir: str
    visual: MjVisual
    def __init__(self) -> None:
        """__init__(self: mujoco._specs.MjSpec) -> None"""
    def actuator(self, arg0: str) -> MjsActuator:
        """actuator(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsActuator"""
    def add_actuator(self, default: MjsDefault = ..., **kwargs) -> MjsActuator:
        """add_actuator(self: mujoco._specs.MjSpec, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsActuator"""
    def add_default(self, arg0: str, arg1: MjsDefault) -> MjsDefault:
        """add_default(self: mujoco._specs.MjSpec, arg0: str, arg1: mujoco._specs.MjsDefault) -> mujoco._specs.MjsDefault"""
    def add_equality(self, default: MjsDefault = ..., **kwargs) -> MjsEquality:
        """add_equality(self: mujoco._specs.MjSpec, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsEquality"""
    def add_exclude(self, **kwargs) -> MjsExclude:
        """add_exclude(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsExclude"""
    def add_flex(self, **kwargs) -> MjsFlex:
        """add_flex(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsFlex"""
    def add_hfield(self, **kwargs) -> MjsHField:
        """add_hfield(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsHField"""
    def add_key(self, **kwargs) -> MjsKey:
        """add_key(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsKey"""
    def add_material(self, default: MjsDefault = ..., **kwargs) -> MjsMaterial:
        """add_material(self: mujoco._specs.MjSpec, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsMaterial"""
    def add_mesh(self, default: MjsDefault = ..., **kwargs) -> MjsMesh:
        """add_mesh(self: mujoco._specs.MjSpec, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsMesh"""
    def add_numeric(self, **kwargs) -> MjsNumeric:
        """add_numeric(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsNumeric"""
    def add_pair(self, default: MjsDefault = ..., **kwargs) -> MjsPair:
        """add_pair(self: mujoco._specs.MjSpec, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsPair"""
    def add_plugin(self, **kwargs) -> MjsPlugin:
        """add_plugin(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsPlugin"""
    def add_sensor(self, **kwargs) -> MjsSensor:
        """add_sensor(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsSensor"""
    def add_skin(self, **kwargs) -> MjsSkin:
        """add_skin(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsSkin"""
    def add_tendon(self, default: MjsDefault = ..., **kwargs) -> MjsTendon:
        """add_tendon(self: mujoco._specs.MjSpec, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsTendon"""
    def add_text(self, **kwargs) -> MjsText:
        """add_text(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsText"""
    def add_texture(self, **kwargs) -> MjsTexture:
        """add_texture(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsTexture"""
    def add_tuple(self, **kwargs) -> MjsTuple:
        """add_tuple(self: mujoco._specs.MjSpec, **kwargs) -> mujoco._specs.MjsTuple"""
    def attach(self, child: MjSpec, prefix: str | None = ..., suffix: str | None = ..., site: object | None = ..., frame: object | None = ...) -> MjsFrame:
        """attach(self: mujoco._specs.MjSpec, child: mujoco._specs.MjSpec, prefix: Optional[str] = None, suffix: Optional[str] = None, site: Optional[object] = None, frame: Optional[object] = None) -> mujoco._specs.MjsFrame"""
    def body(self, arg0: str) -> MjsBody:
        """body(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsBody"""
    def camera(self, arg0: str) -> MjsCamera:
        """camera(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsCamera"""
    def compile(self) -> object:
        """compile(self: mujoco._specs.MjSpec) -> object"""
    def copy(self) -> MjSpec:
        """copy(self: mujoco._specs.MjSpec) -> mujoco._specs.MjSpec"""
    def detach_body(self, arg0: MjsBody) -> None:
        """detach_body(self: mujoco._specs.MjSpec, arg0: mujoco._specs.MjsBody) -> None"""
    def equality(self, arg0: str) -> MjsEquality:
        """equality(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsEquality"""
    def exclude(self, arg0: str) -> MjsExclude:
        """exclude(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsExclude"""
    def find_default(self, arg0: str) -> MjsDefault:
        """find_default(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsDefault"""
    def flex(self, arg0: str) -> MjsFlex:
        """flex(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsFlex"""
    def frame(self, arg0: str) -> MjsFrame:
        """frame(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsFrame"""
    @staticmethod
    def from_file(filename: str, include: dict[str, bytes] | None = ..., assets: dict | None = ...) -> MjSpec:
        """from_file(filename: str, include: Optional[dict[str, bytes]] = None, assets: Optional[dict] = None) -> mujoco._specs.MjSpec


            Creates a spec from an XML file.

            Parameters
            ----------
            filename : str
                Path to the XML file.
            include : dict, optional
                A dictionary of xml files included by the model. The keys are file names
                and the values are file contents.
            assets : dict, optional
                A dictionary of assets to be used by the spec. The keys are asset names
                and the values are asset contents.
  
        """
    @staticmethod
    def from_string(xml: str, include: dict[str, bytes] | None = ..., assets: dict | None = ...) -> MjSpec:
        """from_string(xml: str, include: Optional[dict[str, bytes]] = None, assets: Optional[dict] = None) -> mujoco._specs.MjSpec


            Creates a spec from an XML string.

            Parameters
            ----------
            xml : str
                XML string.
            include : dict, optional
                A dictionary of xml files included by the model. The keys are file names
                and the values are file contents.
            assets : dict, optional
                A dictionary of assets to be used by the spec. The keys are asset names
                and the values are asset contents.
  
        """
    def geom(self, arg0: str) -> MjsGeom:
        """geom(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsGeom"""
    def hfield(self, arg0: str) -> MjsHField:
        """hfield(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsHField"""
    def joint(self, arg0: str) -> MjsJoint:
        """joint(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsJoint"""
    def key(self, arg0: str) -> MjsKey:
        """key(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsKey"""
    def light(self, arg0: str) -> MjsLight:
        """light(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsLight"""
    def material(self, arg0: str) -> MjsMaterial:
        """material(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsMaterial"""
    def mesh(self, arg0: str) -> MjsMesh:
        """mesh(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsMesh"""
    def numeric(self, arg0: str) -> MjsNumeric:
        """numeric(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsNumeric"""
    def pair(self, arg0: str) -> MjsPair:
        """pair(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsPair"""
    def plugin(self, arg0: str) -> MjsPlugin:
        """plugin(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsPlugin"""
    def recompile(self, arg0: object, arg1: object) -> object:
        """recompile(self: mujoco._specs.MjSpec, arg0: object, arg1: object) -> object"""
    def sensor(self, arg0: str) -> MjsSensor:
        """sensor(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsSensor"""
    def site(self, arg0: str) -> MjsSite:
        """site(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsSite"""
    def skin(self, arg0: str) -> MjsSkin:
        """skin(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsSkin"""
    def tendon(self, arg0: str) -> MjsTendon:
        """tendon(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsTendon"""
    def text(self, arg0: str) -> MjsText:
        """text(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsText"""
    def texture(self, arg0: str) -> MjsTexture:
        """texture(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsTexture"""
    def to_file(self, arg0: str) -> None:
        """to_file(self: mujoco._specs.MjSpec, arg0: str) -> None"""
    def to_xml(self) -> str:
        """to_xml(self: mujoco._specs.MjSpec) -> str"""
    def tuple(self, arg0: str) -> MjsTuple:
        """tuple(self: mujoco._specs.MjSpec, arg0: str) -> mujoco._specs.MjsTuple"""
    @property
    def actuators(self) -> list: ...
    @property
    def bodies(self) -> list: ...
    @property
    def cameras(self) -> list: ...
    @property
    def default(self) -> MjsDefault: ...
    @property
    def equalities(self) -> list: ...
    @property
    def excludes(self) -> list: ...
    @property
    def flexes(self) -> list: ...
    @property
    def frames(self) -> list: ...
    @property
    def geoms(self) -> list: ...
    @property
    def hfields(self) -> list: ...
    @property
    def joints(self) -> list: ...
    @property
    def keys(self) -> list: ...
    @property
    def lights(self) -> list: ...
    @property
    def materials(self) -> list: ...
    @property
    def meshes(self) -> list: ...
    @property
    def numerics(self) -> list: ...
    @property
    def pairs(self) -> list: ...
    @property
    def parent(self) -> MjSpec: ...
    @property
    def plugins(self) -> list: ...
    @property
    def sensors(self) -> list: ...
    @property
    def sites(self) -> list: ...
    @property
    def skins(self) -> list: ...
    @property
    def tendons(self) -> list: ...
    @property
    def texts(self) -> list: ...
    @property
    def textures(self) -> list: ...
    @property
    def tuples(self) -> list: ...
    @property
    def worldbody(self) -> MjsBody: ...

class MjStatistic:
    center: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    extent: float
    meaninertia: float
    meanmass: float
    meansize: float
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjStringVec:
    def __init__(self, arg0: str, arg1: int) -> None:
        """__init__(self: mujoco._specs.MjStringVec, arg0: str, arg1: int) -> None"""
    def __getitem__(self, arg0: int) -> str:
        """__getitem__(self: mujoco._specs.MjStringVec, arg0: int) -> str"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: mujoco._specs.MjStringVec) -> Iterator[str]"""
    def __len__(self) -> int:
        """__len__(self: mujoco._specs.MjStringVec) -> int"""
    def __setitem__(self, arg0: int, arg1: str) -> None:
        """__setitem__(self: mujoco._specs.MjStringVec, arg0: int, arg1: str) -> None"""

class MjVisual:
    global_: mujoco._structs.MjVisual.Global
    headlight: MjVisualHeadlight
    map: mujoco._structs.MjVisual.Map
    quality: mujoco._structs.MjVisual.Quality
    rgba: MjVisualRgba
    scale: mujoco._structs.MjVisual.Scale
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjVisualHeadlight:
    active: int
    ambient: numpy.ndarray[numpy.float32[3, 1], flags.writeable]
    diffuse: numpy.ndarray[numpy.float32[3, 1], flags.writeable]
    specular: numpy.ndarray[numpy.float32[3, 1], flags.writeable]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjVisualRgba:
    actuator: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    actuatornegative: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    actuatorpositive: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    bv: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    bvactive: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    camera: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    com: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    connect: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    constraint: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    contactforce: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    contactfriction: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    contactgap: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    contactpoint: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    contacttorque: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    crankbroken: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    fog: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    force: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    frustum: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    haze: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    inertia: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    joint: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    light: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    rangefinder: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    selectpoint: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    slidercrank: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjsActuator:
    actdim: int
    actearly: int
    actlimited: int
    actrange: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    biasprm: numpy.ndarray[numpy.float64[10, 1], flags.writeable]
    biastype: mujoco._enums.mjtBias
    classname: MjsDefault
    cranklength: float
    ctrllimited: int
    ctrlrange: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    dynprm: numpy.ndarray[numpy.float64[10, 1], flags.writeable]
    dyntype: mujoco._enums.mjtDyn
    forcelimited: int
    forcerange: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    gainprm: numpy.ndarray[numpy.float64[10, 1], flags.writeable]
    gaintype: mujoco._enums.mjtGain
    gear: numpy.ndarray[numpy.float64[6, 1], flags.writeable]
    group: int
    info: str
    inheritrange: float
    lengthrange: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    name: str
    plugin: MjsPlugin
    refsite: str
    slidersite: str
    target: str
    trntype: mujoco._enums.mjtTrn
    userdata: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsActuator) -> None"""

class MjsBody:
    alt: MjsOrientation
    childclass: str
    classname: MjsDefault
    explicitinertial: int
    fullinertia: numpy.ndarray[numpy.float64[6, 1], flags.writeable]
    gravcomp: float
    ialt: MjsOrientation
    inertia: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    info: str
    ipos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    iquat: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    mass: float
    mocap: int
    name: str
    plugin: MjsPlugin
    pos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    userdata: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def add_body(self, default: MjsDefault = ..., **kwargs) -> MjsBody:
        """add_body(self: mujoco._specs.MjsBody, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsBody"""
    def add_camera(self, default: MjsDefault = ..., **kwargs) -> MjsCamera:
        """add_camera(self: mujoco._specs.MjsBody, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsCamera"""
    def add_frame(self, default: MjsFrame = ..., **kwargs) -> MjsFrame:
        """add_frame(self: mujoco._specs.MjsBody, default: mujoco._specs.MjsFrame = None, **kwargs) -> mujoco._specs.MjsFrame"""
    def add_freejoint(self, **kwargs) -> MjsJoint:
        """add_freejoint(self: mujoco._specs.MjsBody, **kwargs) -> mujoco._specs.MjsJoint"""
    def add_geom(self, default: MjsDefault = ..., **kwargs) -> MjsGeom:
        """add_geom(self: mujoco._specs.MjsBody, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsGeom"""
    def add_joint(self, default: MjsDefault = ..., **kwargs) -> MjsJoint:
        """add_joint(self: mujoco._specs.MjsBody, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsJoint"""
    def add_light(self, default: MjsDefault = ..., **kwargs) -> MjsLight:
        """add_light(self: mujoco._specs.MjsBody, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsLight"""
    def add_site(self, default: MjsDefault = ..., **kwargs) -> MjsSite:
        """add_site(self: mujoco._specs.MjsBody, default: mujoco._specs.MjsDefault = None, **kwargs) -> mujoco._specs.MjsSite"""
    def attach_frame(self, frame: MjsFrame, prefix: str | None = ..., suffix: str | None = ...) -> MjsFrame:
        """attach_frame(self: mujoco._specs.MjsBody, frame: mujoco._specs.MjsFrame, prefix: Optional[str] = None, suffix: Optional[str] = None) -> mujoco._specs.MjsFrame"""
    @overload
    def find_all(self, arg0: mujoco._enums.mjtObj) -> list:
        """find_all(*args, **kwargs)
        Overloaded function.

        1. find_all(self: mujoco._specs.MjsBody, arg0: mujoco._enums.mjtObj) -> list

        2. find_all(self: mujoco._specs.MjsBody, arg0: str) -> list
        """
    @overload
    def find_all(self, arg0: str) -> list:
        """find_all(*args, **kwargs)
        Overloaded function.

        1. find_all(self: mujoco._specs.MjsBody, arg0: mujoco._enums.mjtObj) -> list

        2. find_all(self: mujoco._specs.MjsBody, arg0: str) -> list
        """
    def find_child(self, arg0: str) -> MjsBody:
        """find_child(self: mujoco._specs.MjsBody, arg0: str) -> mujoco._specs.MjsBody"""
    def first_body(self) -> MjsBody:
        """first_body(self: mujoco._specs.MjsBody) -> mujoco._specs.MjsBody"""
    def first_camera(self) -> MjsCamera:
        """first_camera(self: mujoco._specs.MjsBody) -> mujoco._specs.MjsCamera"""
    def first_frame(self) -> MjsFrame:
        """first_frame(self: mujoco._specs.MjsBody) -> mujoco._specs.MjsFrame"""
    def first_geom(self) -> MjsGeom:
        """first_geom(self: mujoco._specs.MjsBody) -> mujoco._specs.MjsGeom"""
    def first_joint(self) -> MjsJoint:
        """first_joint(self: mujoco._specs.MjsBody) -> mujoco._specs.MjsJoint"""
    def first_light(self) -> MjsLight:
        """first_light(self: mujoco._specs.MjsBody) -> mujoco._specs.MjsLight"""
    def first_site(self) -> MjsSite:
        """first_site(self: mujoco._specs.MjsBody) -> mujoco._specs.MjsSite"""
    def next_body(self, arg0: MjsBody) -> MjsBody:
        """next_body(self: mujoco._specs.MjsBody, arg0: mujoco._specs.MjsBody) -> mujoco._specs.MjsBody"""
    def next_camera(self, arg0: MjsCamera) -> MjsCamera:
        """next_camera(self: mujoco._specs.MjsBody, arg0: mujoco._specs.MjsCamera) -> mujoco._specs.MjsCamera"""
    def next_frame(self, arg0: MjsFrame) -> MjsFrame:
        """next_frame(self: mujoco._specs.MjsBody, arg0: mujoco._specs.MjsFrame) -> mujoco._specs.MjsFrame"""
    def next_geom(self, arg0: MjsGeom) -> MjsGeom:
        """next_geom(self: mujoco._specs.MjsBody, arg0: mujoco._specs.MjsGeom) -> mujoco._specs.MjsGeom"""
    def next_joint(self, arg0: MjsJoint) -> MjsJoint:
        """next_joint(self: mujoco._specs.MjsBody, arg0: mujoco._specs.MjsJoint) -> mujoco._specs.MjsJoint"""
    def next_light(self, arg0: MjsLight) -> MjsLight:
        """next_light(self: mujoco._specs.MjsBody, arg0: mujoco._specs.MjsLight) -> mujoco._specs.MjsLight"""
    def next_site(self, arg0: MjsSite) -> MjsSite:
        """next_site(self: mujoco._specs.MjsBody, arg0: mujoco._specs.MjsSite) -> mujoco._specs.MjsSite"""
    def set_frame(self, arg0: MjsFrame) -> None:
        """set_frame(self: mujoco._specs.MjsBody, arg0: mujoco._specs.MjsFrame) -> None"""
    def to_frame(self) -> MjsFrame:
        """to_frame(self: mujoco._specs.MjsBody) -> mujoco._specs.MjsFrame"""
    @property
    def bodies(self) -> list: ...
    @property
    def cameras(self) -> list: ...
    @property
    def frames(self) -> list: ...
    @property
    def geoms(self) -> list: ...
    @property
    def joints(self) -> list: ...
    @property
    def lights(self) -> list: ...
    @property
    def parent(self) -> MjsBody: ...
    @property
    def sites(self) -> list: ...

class MjsCamera:
    alt: MjsOrientation
    classname: MjsDefault
    focal_length: numpy.ndarray[numpy.float32[2, 1], flags.writeable]
    focal_pixel: numpy.ndarray[numpy.float32[2, 1], flags.writeable]
    fovy: float
    info: str
    intrinsic: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    ipd: float
    mode: mujoco._enums.mjtCamLight
    name: str
    orthographic: int
    pos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    principal_length: numpy.ndarray[numpy.float32[2, 1], flags.writeable]
    principal_pixel: numpy.ndarray[numpy.float32[2, 1], flags.writeable]
    quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    resolution: numpy.ndarray[numpy.float32[2, 1], flags.writeable]
    sensor_size: numpy.ndarray[numpy.float32[2, 1], flags.writeable]
    targetbody: str
    userdata: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsCamera) -> None"""
    def set_frame(self, arg0: MjsFrame) -> None:
        """set_frame(self: mujoco._specs.MjsCamera, arg0: mujoco._specs.MjsFrame) -> None"""
    @property
    def parent(self) -> MjsBody: ...

class MjsCompiler:
    LRopt: mujoco._structs.MjLROpt
    alignfree: int
    autolimits: int
    balanceinertia: int
    boundinertia: float
    boundmass: float
    degree: int
    discardvisual: int
    eulerseq: MjCharVec
    fitaabb: int
    fusestatic: int
    inertiafromgeom: int
    inertiagrouprange: numpy.ndarray[numpy.int32[2, 1], flags.writeable]
    settotalmass: float
    usethread: int
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjsDefault:
    actuator: MjsActuator
    camera: MjsCamera
    equality: MjsEquality
    flex: MjsFlex
    geom: MjsGeom
    joint: MjsJoint
    light: MjsLight
    material: MjsMaterial
    mesh: MjsMesh
    name: str
    pair: MjsPair
    site: MjsSite
    tendon: MjsTendon
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjsElement:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjsEquality:
    active: int
    classname: MjsDefault
    data: numpy.ndarray[numpy.float64[11, 1], flags.writeable]
    info: str
    name: str
    name1: str
    name2: str
    objtype: mujoco._enums.mjtObj
    solimp: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    solref: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    type: mujoco._enums.mjtEq
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsEquality) -> None"""

class MjsExclude:
    bodyname1: str
    bodyname2: str
    info: str
    name: str
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsExclude) -> None"""

class MjsFlex:
    activelayers: int
    conaffinity: int
    condim: int
    contype: int
    damping: float
    dim: int
    edgedamping: float
    edgestiffness: float
    elem: numpy.ndarray[numpy.int32]
    flatskin: int
    friction: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    gap: float
    group: int
    info: str
    internal: int
    margin: float
    material: str
    name: str
    node: numpy.ndarray[numpy.float64]
    nodebody: MjStringVec
    poisson: float
    priority: int
    radius: float
    rgba: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    selfcollide: int
    solimp: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    solmix: float
    solref: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    texcoord: numpy.ndarray[numpy.float32]
    thickness: float
    vert: numpy.ndarray[numpy.float64]
    vertbody: MjStringVec
    young: float
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsFlex) -> None"""

class MjsFrame:
    alt: MjsOrientation
    childclass: str
    info: str
    name: str
    pos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def attach_body(self, body: MjsBody, prefix: str | None = ..., suffix: str | None = ...) -> MjsBody:
        """attach_body(self: mujoco._specs.MjsFrame, body: mujoco._specs.MjsBody, prefix: Optional[str] = None, suffix: Optional[str] = None) -> mujoco._specs.MjsBody"""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsFrame) -> None"""
    def set_frame(self, arg0: MjsFrame) -> None:
        """set_frame(self: mujoco._specs.MjsFrame, arg0: mujoco._specs.MjsFrame) -> None"""
    @property
    def parent(self) -> MjsBody: ...

class MjsGeom:
    alt: MjsOrientation
    classname: MjsDefault
    conaffinity: int
    condim: int
    contype: int
    density: float
    fitscale: float
    fluid_coefs: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    fluid_ellipsoid: float
    friction: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    fromto: numpy.ndarray[numpy.float64[6, 1], flags.writeable]
    gap: float
    group: int
    hfieldname: str
    info: str
    margin: float
    mass: float
    material: str
    meshname: str
    name: str
    plugin: MjsPlugin
    pos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    priority: int
    quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    rgba: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    size: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    solimp: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    solmix: float
    solref: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    type: mujoco._enums.mjtGeom
    typeinertia: mujoco._enums.mjtGeomInertia
    userdata: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsGeom) -> None"""
    def set_frame(self, arg0: MjsFrame) -> None:
        """set_frame(self: mujoco._specs.MjsGeom, arg0: mujoco._specs.MjsFrame) -> None"""
    @property
    def parent(self) -> MjsBody: ...

class MjsHField:
    content_type: str
    file: str
    info: str
    name: str
    ncol: int
    nrow: int
    size: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    userdata: numpy.ndarray[numpy.float32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsHField) -> None"""

class MjsJoint:
    actfrclimited: int
    actfrcrange: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    actgravcomp: int
    align: int
    armature: float
    axis: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    classname: MjsDefault
    damping: float
    frictionloss: float
    group: int
    info: str
    limited: int
    margin: float
    name: str
    pos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    range: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    ref: float
    solimp_friction: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    solimp_limit: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    solref_friction: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    solref_limit: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    springdamper: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    springref: float
    stiffness: float
    type: mujoco._enums.mjtJoint
    userdata: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsJoint) -> None"""
    def set_frame(self, arg0: MjsFrame) -> None:
        """set_frame(self: mujoco._specs.MjsJoint, arg0: mujoco._specs.MjsFrame) -> None"""
    @property
    def parent(self) -> MjsBody: ...

class MjsKey:
    act: numpy.ndarray[numpy.float64]
    ctrl: numpy.ndarray[numpy.float64]
    info: str
    mpos: numpy.ndarray[numpy.float64]
    mquat: numpy.ndarray[numpy.float64]
    name: str
    qpos: numpy.ndarray[numpy.float64]
    qvel: numpy.ndarray[numpy.float64]
    time: float
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsKey) -> None"""

class MjsLight:
    active: int
    ambient: numpy.ndarray[numpy.float32[3, 1], flags.writeable]
    attenuation: numpy.ndarray[numpy.float32[3, 1], flags.writeable]
    bulbradius: float
    castshadow: int
    classname: MjsDefault
    cutoff: float
    diffuse: numpy.ndarray[numpy.float32[3, 1], flags.writeable]
    dir: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    directional: int
    exponent: float
    info: str
    mode: mujoco._enums.mjtCamLight
    name: str
    pos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    specular: numpy.ndarray[numpy.float32[3, 1], flags.writeable]
    targetbody: str
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsLight) -> None"""
    def set_frame(self, arg0: MjsFrame) -> None:
        """set_frame(self: mujoco._specs.MjsLight, arg0: mujoco._specs.MjsFrame) -> None"""
    @property
    def parent(self) -> MjsBody: ...

class MjsMaterial:
    classname: MjsDefault
    emission: float
    info: str
    metallic: float
    name: str
    reflectance: float
    rgba: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    roughness: float
    shininess: float
    specular: float
    texrepeat: numpy.ndarray[numpy.float32[2, 1], flags.writeable]
    textures: MjStringVec
    texuniform: int
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsMaterial) -> None"""

class MjsMesh:
    classname: MjsDefault
    content_type: str
    file: str
    inertia: mujoco._enums.mjtMeshInertia
    info: str
    maxhullvert: int
    name: str
    plugin: MjsPlugin
    refpos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    refquat: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    scale: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    smoothnormal: int
    userface: numpy.ndarray[numpy.int32]
    userfacetexcoord: numpy.ndarray[numpy.int32]
    usernormal: numpy.ndarray[numpy.float32]
    usertexcoord: numpy.ndarray[numpy.float32]
    uservert: numpy.ndarray[numpy.float32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsMesh) -> None"""

class MjsNumeric:
    data: numpy.ndarray[numpy.float64]
    info: str
    name: str
    size: int
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsNumeric) -> None"""

class MjsOrientation:
    axisangle: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    euler: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    type: mujoco._enums.mjtOrientation
    xyaxes: numpy.ndarray[numpy.float64[6, 1], flags.writeable]
    zaxis: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MjsPair:
    classname: MjsDefault
    condim: int
    friction: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    gap: float
    geomname1: str
    geomname2: str
    info: str
    margin: float
    name: str
    solimp: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    solref: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    solreffriction: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsPair) -> None"""

class MjsPlugin:
    active: int
    id: int
    info: str
    name: str
    plugin_name: str
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsPlugin) -> None"""

class MjsSensor:
    cutoff: float
    datatype: mujoco._enums.mjtDataType
    dim: int
    info: str
    name: str
    needstage: mujoco._enums.mjtStage
    noise: float
    objname: str
    objtype: mujoco._enums.mjtObj
    plugin: MjsPlugin
    refname: str
    reftype: mujoco._enums.mjtObj
    type: mujoco._enums.mjtSensor
    userdata: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsSensor) -> None"""

class MjsSite:
    alt: MjsOrientation
    classname: MjsDefault
    fromto: numpy.ndarray[numpy.float64[6, 1], flags.writeable]
    group: int
    info: str
    material: str
    name: str
    pos: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    quat: numpy.ndarray[numpy.float64[4, 1], flags.writeable]
    rgba: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    size: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    type: mujoco._enums.mjtGeom
    userdata: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def attach_body(self, body: MjsBody, prefix: str | None = ..., suffix: str | None = ...) -> MjsBody:
        """attach_body(self: mujoco._specs.MjsSite, body: mujoco._specs.MjsBody, prefix: Optional[str] = None, suffix: Optional[str] = None) -> mujoco._specs.MjsBody"""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsSite) -> None"""
    def set_frame(self, arg0: MjsFrame) -> None:
        """set_frame(self: mujoco._specs.MjsSite, arg0: mujoco._specs.MjsFrame) -> None"""
    @property
    def parent(self) -> MjsBody: ...

class MjsSkin:
    bindpos: numpy.ndarray[numpy.float32]
    bindquat: numpy.ndarray[numpy.float32]
    bodyname: MjStringVec
    face: numpy.ndarray[numpy.int32]
    file: str
    group: int
    inflate: float
    info: str
    material: str
    name: str
    rgba: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    texcoord: numpy.ndarray[numpy.float32]
    vert: numpy.ndarray[numpy.float32]
    vertid: list
    vertweight: list
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsSkin) -> None"""

class MjsTendon:
    damping: float
    frictionloss: float
    group: int
    info: str
    limited: int
    margin: float
    material: str
    name: str
    range: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    rgba: numpy.ndarray[numpy.float32[4, 1], flags.writeable]
    solimp_friction: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    solimp_limit: numpy.ndarray[numpy.float64[5, 1], flags.writeable]
    solref_friction: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    solref_limit: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    springlength: numpy.ndarray[numpy.float64[2, 1], flags.writeable]
    stiffness: float
    userdata: numpy.ndarray[numpy.float64]
    width: float
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def default(self) -> MjsDefault:
        """default(self: mujoco._specs.MjsTendon) -> mujoco._specs.MjsDefault"""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsTendon) -> None"""
    def wrap_geom(self, arg0: str, arg1: str) -> MjsWrap:
        """wrap_geom(self: mujoco._specs.MjsTendon, arg0: str, arg1: str) -> mujoco._specs.MjsWrap"""
    def wrap_joint(self, arg0: str, arg1: float) -> MjsWrap:
        """wrap_joint(self: mujoco._specs.MjsTendon, arg0: str, arg1: float) -> mujoco._specs.MjsWrap"""
    def wrap_pulley(self, arg0: float) -> MjsWrap:
        """wrap_pulley(self: mujoco._specs.MjsTendon, arg0: float) -> mujoco._specs.MjsWrap"""
    def wrap_site(self, arg0: str) -> MjsWrap:
        """wrap_site(self: mujoco._specs.MjsTendon, arg0: str) -> mujoco._specs.MjsWrap"""

class MjsText:
    data: str
    info: str
    name: str
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsText) -> None"""

class MjsTexture:
    builtin: int
    content_type: str
    cubefiles: MjStringVec
    data: MjByteVec
    file: str
    gridlayout: MjCharVec
    gridsize: numpy.ndarray[numpy.int32[2, 1], flags.writeable]
    height: int
    hflip: int
    info: str
    mark: int
    markrgb: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    name: str
    nchannel: int
    random: float
    rgb1: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    rgb2: numpy.ndarray[numpy.float64[3, 1], flags.writeable]
    type: mujoco._enums.mjtTexture
    vflip: int
    width: int
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsTexture) -> None"""

class MjsTuple:
    info: str
    name: str
    objname: MjStringVec
    objprm: numpy.ndarray[numpy.float64]
    objtype: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def delete(self) -> None:
        """delete(self: mujoco._specs.MjsTuple) -> None"""

class MjsWrap:
    info: str
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

# --- mujoco._structs ---
import mujoco._enums
import numpy
import typing
from typing import Callable, ClassVar, overload

class MjContact:
    H: numpy.ndarray[numpy.float64]
    dim: int
    dist: float
    efc_address: int
    elem: numpy.ndarray[numpy.int32]
    exclude: int
    flex: numpy.ndarray[numpy.int32]
    frame: numpy.ndarray[numpy.float64]
    friction: numpy.ndarray[numpy.float64]
    geom: numpy.ndarray[numpy.int32]
    geom1: int
    geom2: int
    includemargin: float
    mu: float
    pos: numpy.ndarray[numpy.float64]
    solimp: numpy.ndarray[numpy.float64]
    solref: numpy.ndarray[numpy.float64]
    solreffriction: numpy.ndarray[numpy.float64]
    vert: numpy.ndarray[numpy.int32]
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjContact) -> None"""
    def __copy__(self) -> MjContact:
        """__copy__(self: mujoco._structs.MjContact) -> mujoco._structs.MjContact"""
    def __deepcopy__(self, arg0: dict) -> MjContact:
        """__deepcopy__(self: mujoco._structs.MjContact, arg0: dict) -> mujoco._structs.MjContact"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjData:
    bind: ClassVar[Callable] = ...
    B_colind: numpy.ndarray[numpy.int32]
    B_rowadr: numpy.ndarray[numpy.int32]
    B_rownnz: numpy.ndarray[numpy.int32]
    C_colind: numpy.ndarray[numpy.int32]
    C_rowadr: numpy.ndarray[numpy.int32]
    C_rownnz: numpy.ndarray[numpy.int32]
    D_colind: numpy.ndarray[numpy.int32]
    D_diag: numpy.ndarray[numpy.int32]
    D_rowadr: numpy.ndarray[numpy.int32]
    D_rownnz: numpy.ndarray[numpy.int32]
    act: numpy.ndarray[numpy.float64]
    act_dot: numpy.ndarray[numpy.float64]
    actuator_force: numpy.ndarray[numpy.float64]
    actuator_length: numpy.ndarray[numpy.float64]
    actuator_moment: numpy.ndarray[numpy.float64]
    actuator_velocity: numpy.ndarray[numpy.float64]
    bvh_aabb_dyn: numpy.ndarray[numpy.float64]
    bvh_active: numpy.ndarray[numpy.uint8]
    cacc: numpy.ndarray[numpy.float64]
    cam_xmat: numpy.ndarray[numpy.float64]
    cam_xpos: numpy.ndarray[numpy.float64]
    cdof: numpy.ndarray[numpy.float64]
    cdof_dot: numpy.ndarray[numpy.float64]
    cfrc_ext: numpy.ndarray[numpy.float64]
    cfrc_int: numpy.ndarray[numpy.float64]
    cinert: numpy.ndarray[numpy.float64]
    crb: numpy.ndarray[numpy.float64]
    ctrl: numpy.ndarray[numpy.float64]
    cvel: numpy.ndarray[numpy.float64]
    energy: numpy.ndarray[numpy.float64]
    eq_active: numpy.ndarray[numpy.uint8]
    flexedge_J: numpy.ndarray[numpy.float64]
    flexedge_J_colind: numpy.ndarray[numpy.int32]
    flexedge_J_rowadr: numpy.ndarray[numpy.int32]
    flexedge_J_rownnz: numpy.ndarray[numpy.int32]
    flexedge_length: numpy.ndarray[numpy.float64]
    flexedge_velocity: numpy.ndarray[numpy.float64]
    flexelem_aabb: numpy.ndarray[numpy.float64]
    flexvert_xpos: numpy.ndarray[numpy.float64]
    geom_xmat: numpy.ndarray[numpy.float64]
    geom_xpos: numpy.ndarray[numpy.float64]
    light_xdir: numpy.ndarray[numpy.float64]
    light_xpos: numpy.ndarray[numpy.float64]
    mapD2M: numpy.ndarray[numpy.int32]
    mapM2C: numpy.ndarray[numpy.int32]
    mapM2D: numpy.ndarray[numpy.int32]
    maxuse_arena: int
    maxuse_con: int
    maxuse_efc: int
    maxuse_stack: int
    maxuse_threadstack: numpy.ndarray[numpy.uint64]
    mocap_pos: numpy.ndarray[numpy.float64]
    mocap_quat: numpy.ndarray[numpy.float64]
    moment_colind: numpy.ndarray[numpy.int32]
    moment_rowadr: numpy.ndarray[numpy.int32]
    moment_rownnz: numpy.ndarray[numpy.int32]
    nA: int
    nJ: int
    narena: int
    nbuffer: int
    ncon: int
    ne: int
    nefc: int
    nf: int
    nisland: int
    nl: int
    nplugin: int
    parena: int
    pbase: int
    plugin: numpy.ndarray[numpy.int32]
    plugin_data: numpy.ndarray[numpy.uint64]
    plugin_state: numpy.ndarray[numpy.float64]
    pstack: int
    qDeriv: numpy.ndarray[numpy.float64]
    qH: numpy.ndarray[numpy.float64]
    qHDiagInv: numpy.ndarray[numpy.float64]
    qLD: numpy.ndarray[numpy.float64]
    qLDiagInv: numpy.ndarray[numpy.float64]
    qLU: numpy.ndarray[numpy.float64]
    qM: numpy.ndarray[numpy.float64]
    qacc: numpy.ndarray[numpy.float64]
    qacc_smooth: numpy.ndarray[numpy.float64]
    qacc_warmstart: numpy.ndarray[numpy.float64]
    qfrc_actuator: numpy.ndarray[numpy.float64]
    qfrc_applied: numpy.ndarray[numpy.float64]
    qfrc_bias: numpy.ndarray[numpy.float64]
    qfrc_constraint: numpy.ndarray[numpy.float64]
    qfrc_damper: numpy.ndarray[numpy.float64]
    qfrc_fluid: numpy.ndarray[numpy.float64]
    qfrc_gravcomp: numpy.ndarray[numpy.float64]
    qfrc_inverse: numpy.ndarray[numpy.float64]
    qfrc_passive: numpy.ndarray[numpy.float64]
    qfrc_smooth: numpy.ndarray[numpy.float64]
    qfrc_spring: numpy.ndarray[numpy.float64]
    qpos: numpy.ndarray[numpy.float64]
    qvel: numpy.ndarray[numpy.float64]
    sensordata: numpy.ndarray[numpy.float64]
    site_xmat: numpy.ndarray[numpy.float64]
    site_xpos: numpy.ndarray[numpy.float64]
    solver_fwdinv: numpy.ndarray[numpy.float64]
    solver_nisland: int
    solver_niter: numpy.ndarray[numpy.int32]
    solver_nnz: numpy.ndarray[numpy.int32]
    subtree_angmom: numpy.ndarray[numpy.float64]
    subtree_com: numpy.ndarray[numpy.float64]
    subtree_linvel: numpy.ndarray[numpy.float64]
    ten_J: numpy.ndarray[numpy.float64]
    ten_J_colind: numpy.ndarray[numpy.int32]
    ten_J_rowadr: numpy.ndarray[numpy.int32]
    ten_J_rownnz: numpy.ndarray[numpy.int32]
    ten_length: numpy.ndarray[numpy.float64]
    ten_velocity: numpy.ndarray[numpy.float64]
    ten_wrapadr: numpy.ndarray[numpy.int32]
    ten_wrapnum: numpy.ndarray[numpy.int32]
    threadpool: int
    time: float
    userdata: numpy.ndarray[numpy.float64]
    wrap_obj: numpy.ndarray[numpy.int32]
    wrap_xpos: numpy.ndarray[numpy.float64]
    xanchor: numpy.ndarray[numpy.float64]
    xaxis: numpy.ndarray[numpy.float64]
    xfrc_applied: numpy.ndarray[numpy.float64]
    ximat: numpy.ndarray[numpy.float64]
    xipos: numpy.ndarray[numpy.float64]
    xmat: numpy.ndarray[numpy.float64]
    xpos: numpy.ndarray[numpy.float64]
    xquat: numpy.ndarray[numpy.float64]
    def __init__(self, arg0: MjModel) -> None:
        """__init__(self: mujoco._structs.MjData, arg0: mujoco._structs.MjModel) -> None"""
    def actuator(self, *args, **kwargs):
        """actuator(*args, **kwargs)
        Overloaded function.

        1. actuator(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataActuatorViews

        2. actuator(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataActuatorViews
        """
    def bind_scalar(self, *args, **kwargs):
        """bind_scalar(*args, **kwargs)
        Overloaded function.

        1. bind_scalar(self: mujoco._structs.MjData, spec: mjsActuator_ = None) -> mujoco::python::MjDataActuatorViews

        2. bind_scalar(self: mujoco._structs.MjData, spec: mjsBody_ = None) -> mujoco::python::MjDataBodyViews

        3. bind_scalar(self: mujoco._structs.MjData, spec: mjsCamera_ = None) -> mujoco::python::MjDataCameraViews

        4. bind_scalar(self: mujoco._structs.MjData, spec: mjsGeom_ = None) -> mujoco::python::MjDataGeomViews

        5. bind_scalar(self: mujoco._structs.MjData, spec: mjsJoint_ = None) -> mujoco::python::MjDataJointViews

        6. bind_scalar(self: mujoco._structs.MjData, spec: mjsLight_ = None) -> mujoco::python::MjDataLightViews

        7. bind_scalar(self: mujoco._structs.MjData, spec: mjsSensor_ = None) -> mujoco::python::MjDataSensorViews

        8. bind_scalar(self: mujoco._structs.MjData, spec: mjsSite_ = None) -> mujoco::python::MjDataSiteViews

        9. bind_scalar(self: mujoco._structs.MjData, spec: mjsTendon_ = None) -> mujoco::python::MjDataTendonViews
        """
    def body(self, *args, **kwargs):
        """body(*args, **kwargs)
        Overloaded function.

        1. body(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataBodyViews

        2. body(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataBodyViews
        """
    def cam(self, *args, **kwargs):
        """cam(*args, **kwargs)
        Overloaded function.

        1. cam(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataCameraViews

        2. cam(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataCameraViews
        """
    def camera(self, *args, **kwargs):
        """camera(*args, **kwargs)
        Overloaded function.

        1. camera(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataCameraViews

        2. camera(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataCameraViews
        """
    def geom(self, *args, **kwargs):
        """geom(*args, **kwargs)
        Overloaded function.

        1. geom(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataGeomViews

        2. geom(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataGeomViews
        """
    def jnt(self, *args, **kwargs):
        """jnt(*args, **kwargs)
        Overloaded function.

        1. jnt(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataJointViews

        2. jnt(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataJointViews
        """
    def joint(self, *args, **kwargs):
        """joint(*args, **kwargs)
        Overloaded function.

        1. joint(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataJointViews

        2. joint(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataJointViews
        """
    def light(self, *args, **kwargs):
        """light(*args, **kwargs)
        Overloaded function.

        1. light(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataLightViews

        2. light(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataLightViews
        """
    def sensor(self, *args, **kwargs):
        """sensor(*args, **kwargs)
        Overloaded function.

        1. sensor(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataSensorViews

        2. sensor(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataSensorViews
        """
    def site(self, *args, **kwargs):
        """site(*args, **kwargs)
        Overloaded function.

        1. site(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataSiteViews

        2. site(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataSiteViews
        """
    def ten(self, *args, **kwargs):
        """ten(*args, **kwargs)
        Overloaded function.

        1. ten(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataTendonViews

        2. ten(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataTendonViews
        """
    def tendon(self, *args, **kwargs):
        """tendon(*args, **kwargs)
        Overloaded function.

        1. tendon(self: mujoco._structs.MjData, arg0: int) -> mujoco::python::MjDataTendonViews

        2. tendon(self: mujoco._structs.MjData, name: str = '') -> mujoco::python::MjDataTendonViews
        """
    def __copy__(self) -> MjData:
        """__copy__(self: mujoco._structs.MjData) -> mujoco._structs.MjData"""
    def __deepcopy__(self, arg0: dict) -> MjData:
        """__deepcopy__(self: mujoco._structs.MjData, arg0: dict) -> mujoco._structs.MjData"""
    @property
    def contact(self) -> _MjContactList: ...
    @property
    def dof_island(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def dof_islandind(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_AR(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_AR_colind(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_AR_rowadr(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_AR_rownnz(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_D(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_J(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_JT(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_JT_colind(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_JT_rowadr(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_JT_rownnz(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_JT_rowsuper(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_J_colind(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_J_rowadr(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_J_rownnz(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_J_rowsuper(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_KBIP(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_R(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_aref(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_b(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_diagApprox(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_force(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_frictionloss(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_id(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_island(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_margin(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_pos(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_state(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_type(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def efc_vel(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def island_dofadr(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def island_dofind(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def island_dofnum(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def island_efcadr(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def island_efcind(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def island_efcnum(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def model(self) -> MjModel: ...
    @property
    def solver(self) -> _MjSolverStatList: ...
    @property
    def tendon_efcadr(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def timer(self) -> _MjTimerStatList: ...
    @property
    def warning(self) -> _MjWarningStatList: ...

class MjLROpt:
    accel: float
    interval: float
    inttotal: float
    maxforce: float
    mode: int
    timeconst: float
    timestep: float
    tolrange: float
    useexisting: int
    uselimit: int
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjLROpt) -> None"""
    def __copy__(self) -> MjLROpt:
        """__copy__(self: mujoco._structs.MjLROpt) -> mujoco._structs.MjLROpt"""
    def __deepcopy__(self, arg0: dict) -> MjLROpt:
        """__deepcopy__(self: mujoco._structs.MjLROpt, arg0: dict) -> mujoco._structs.MjLROpt"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjModel:
    bind: ClassVar[Callable] = ...
    actuator_acc0: numpy.ndarray[numpy.float64]
    actuator_actadr: numpy.ndarray[numpy.int32]
    actuator_actearly: numpy.ndarray[numpy.uint8]
    actuator_actlimited: numpy.ndarray[numpy.uint8]
    actuator_actnum: numpy.ndarray[numpy.int32]
    actuator_actrange: numpy.ndarray[numpy.float64]
    actuator_biasprm: numpy.ndarray[numpy.float64]
    actuator_biastype: numpy.ndarray[numpy.int32]
    actuator_cranklength: numpy.ndarray[numpy.float64]
    actuator_ctrllimited: numpy.ndarray[numpy.uint8]
    actuator_ctrlrange: numpy.ndarray[numpy.float64]
    actuator_dynprm: numpy.ndarray[numpy.float64]
    actuator_dyntype: numpy.ndarray[numpy.int32]
    actuator_forcelimited: numpy.ndarray[numpy.uint8]
    actuator_forcerange: numpy.ndarray[numpy.float64]
    actuator_gainprm: numpy.ndarray[numpy.float64]
    actuator_gaintype: numpy.ndarray[numpy.int32]
    actuator_gear: numpy.ndarray[numpy.float64]
    actuator_group: numpy.ndarray[numpy.int32]
    actuator_length0: numpy.ndarray[numpy.float64]
    actuator_lengthrange: numpy.ndarray[numpy.float64]
    actuator_plugin: numpy.ndarray[numpy.int32]
    actuator_trnid: numpy.ndarray[numpy.int32]
    actuator_trntype: numpy.ndarray[numpy.int32]
    actuator_user: numpy.ndarray[numpy.float64]
    body_bvhadr: numpy.ndarray[numpy.int32]
    body_bvhnum: numpy.ndarray[numpy.int32]
    body_conaffinity: numpy.ndarray[numpy.int32]
    body_contype: numpy.ndarray[numpy.int32]
    body_dofadr: numpy.ndarray[numpy.int32]
    body_dofnum: numpy.ndarray[numpy.int32]
    body_geomadr: numpy.ndarray[numpy.int32]
    body_geomnum: numpy.ndarray[numpy.int32]
    body_gravcomp: numpy.ndarray[numpy.float64]
    body_inertia: numpy.ndarray[numpy.float64]
    body_invweight0: numpy.ndarray[numpy.float64]
    body_ipos: numpy.ndarray[numpy.float64]
    body_iquat: numpy.ndarray[numpy.float64]
    body_jntadr: numpy.ndarray[numpy.int32]
    body_jntnum: numpy.ndarray[numpy.int32]
    body_margin: numpy.ndarray[numpy.float64]
    body_mass: numpy.ndarray[numpy.float64]
    body_mocapid: numpy.ndarray[numpy.int32]
    body_parentid: numpy.ndarray[numpy.int32]
    body_plugin: numpy.ndarray[numpy.int32]
    body_pos: numpy.ndarray[numpy.float64]
    body_quat: numpy.ndarray[numpy.float64]
    body_rootid: numpy.ndarray[numpy.int32]
    body_sameframe: numpy.ndarray[numpy.uint8]
    body_simple: numpy.ndarray[numpy.uint8]
    body_subtreemass: numpy.ndarray[numpy.float64]
    body_treeid: numpy.ndarray[numpy.int32]
    body_user: numpy.ndarray[numpy.float64]
    body_weldid: numpy.ndarray[numpy.int32]
    bvh_aabb: numpy.ndarray[numpy.float64]
    bvh_child: numpy.ndarray[numpy.int32]
    bvh_depth: numpy.ndarray[numpy.int32]
    bvh_nodeid: numpy.ndarray[numpy.int32]
    cam_bodyid: numpy.ndarray[numpy.int32]
    cam_fovy: numpy.ndarray[numpy.float64]
    cam_intrinsic: numpy.ndarray[numpy.float32]
    cam_ipd: numpy.ndarray[numpy.float64]
    cam_mat0: numpy.ndarray[numpy.float64]
    cam_mode: numpy.ndarray[numpy.int32]
    cam_orthographic: numpy.ndarray[numpy.int32]
    cam_pos: numpy.ndarray[numpy.float64]
    cam_pos0: numpy.ndarray[numpy.float64]
    cam_poscom0: numpy.ndarray[numpy.float64]
    cam_quat: numpy.ndarray[numpy.float64]
    cam_resolution: numpy.ndarray[numpy.int32]
    cam_sensorsize: numpy.ndarray[numpy.float32]
    cam_targetbodyid: numpy.ndarray[numpy.int32]
    cam_user: numpy.ndarray[numpy.float64]
    dof_M0: numpy.ndarray[numpy.float64]
    dof_Madr: numpy.ndarray[numpy.int32]
    dof_armature: numpy.ndarray[numpy.float64]
    dof_bodyid: numpy.ndarray[numpy.int32]
    dof_damping: numpy.ndarray[numpy.float64]
    dof_frictionloss: numpy.ndarray[numpy.float64]
    dof_invweight0: numpy.ndarray[numpy.float64]
    dof_jntid: numpy.ndarray[numpy.int32]
    dof_parentid: numpy.ndarray[numpy.int32]
    dof_simplenum: numpy.ndarray[numpy.int32]
    dof_solimp: numpy.ndarray[numpy.float64]
    dof_solref: numpy.ndarray[numpy.float64]
    dof_treeid: numpy.ndarray[numpy.int32]
    eq_active0: numpy.ndarray[numpy.uint8]
    eq_data: numpy.ndarray[numpy.float64]
    eq_obj1id: numpy.ndarray[numpy.int32]
    eq_obj2id: numpy.ndarray[numpy.int32]
    eq_objtype: numpy.ndarray[numpy.int32]
    eq_solimp: numpy.ndarray[numpy.float64]
    eq_solref: numpy.ndarray[numpy.float64]
    eq_type: numpy.ndarray[numpy.int32]
    exclude_signature: numpy.ndarray[numpy.int32]
    flex_activelayers: numpy.ndarray[numpy.int32]
    flex_bvhadr: numpy.ndarray[numpy.int32]
    flex_bvhnum: numpy.ndarray[numpy.int32]
    flex_centered: numpy.ndarray[numpy.uint8]
    flex_conaffinity: numpy.ndarray[numpy.int32]
    flex_condim: numpy.ndarray[numpy.int32]
    flex_contype: numpy.ndarray[numpy.int32]
    flex_damping: numpy.ndarray[numpy.float64]
    flex_dim: numpy.ndarray[numpy.int32]
    flex_edge: numpy.ndarray[numpy.int32]
    flex_edgeadr: numpy.ndarray[numpy.int32]
    flex_edgedamping: numpy.ndarray[numpy.float64]
    flex_edgeequality: numpy.ndarray[numpy.uint8]
    flex_edgenum: numpy.ndarray[numpy.int32]
    flex_edgestiffness: numpy.ndarray[numpy.float64]
    flex_elem: numpy.ndarray[numpy.int32]
    flex_elemadr: numpy.ndarray[numpy.int32]
    flex_elemdataadr: numpy.ndarray[numpy.int32]
    flex_elemedge: numpy.ndarray[numpy.int32]
    flex_elemedgeadr: numpy.ndarray[numpy.int32]
    flex_elemlayer: numpy.ndarray[numpy.int32]
    flex_elemnum: numpy.ndarray[numpy.int32]
    flex_evpair: numpy.ndarray[numpy.int32]
    flex_evpairadr: numpy.ndarray[numpy.int32]
    flex_evpairnum: numpy.ndarray[numpy.int32]
    flex_flatskin: numpy.ndarray[numpy.uint8]
    flex_friction: numpy.ndarray[numpy.float64]
    flex_gap: numpy.ndarray[numpy.float64]
    flex_group: numpy.ndarray[numpy.int32]
    flex_internal: numpy.ndarray[numpy.uint8]
    flex_interp: numpy.ndarray[numpy.int32]
    flex_margin: numpy.ndarray[numpy.float64]
    flex_matid: numpy.ndarray[numpy.int32]
    flex_node: numpy.ndarray[numpy.float64]
    flex_node0: numpy.ndarray[numpy.float64]
    flex_nodeadr: numpy.ndarray[numpy.int32]
    flex_nodebodyid: numpy.ndarray[numpy.int32]
    flex_nodenum: numpy.ndarray[numpy.int32]
    flex_priority: numpy.ndarray[numpy.int32]
    flex_radius: numpy.ndarray[numpy.float64]
    flex_rgba: numpy.ndarray[numpy.float32]
    flex_rigid: numpy.ndarray[numpy.uint8]
    flex_selfcollide: numpy.ndarray[numpy.int32]
    flex_shell: numpy.ndarray[numpy.int32]
    flex_shelldataadr: numpy.ndarray[numpy.int32]
    flex_shellnum: numpy.ndarray[numpy.int32]
    flex_solimp: numpy.ndarray[numpy.float64]
    flex_solmix: numpy.ndarray[numpy.float64]
    flex_solref: numpy.ndarray[numpy.float64]
    flex_stiffness: numpy.ndarray[numpy.float64]
    flex_texcoord: numpy.ndarray[numpy.float32]
    flex_texcoordadr: numpy.ndarray[numpy.int32]
    flex_vert: numpy.ndarray[numpy.float64]
    flex_vert0: numpy.ndarray[numpy.float64]
    flex_vertadr: numpy.ndarray[numpy.int32]
    flex_vertbodyid: numpy.ndarray[numpy.int32]
    flex_vertnum: numpy.ndarray[numpy.int32]
    flexedge_invweight0: numpy.ndarray[numpy.float64]
    flexedge_length0: numpy.ndarray[numpy.float64]
    flexedge_rigid: numpy.ndarray[numpy.uint8]
    geom_aabb: numpy.ndarray[numpy.float64]
    geom_bodyid: numpy.ndarray[numpy.int32]
    geom_conaffinity: numpy.ndarray[numpy.int32]
    geom_condim: numpy.ndarray[numpy.int32]
    geom_contype: numpy.ndarray[numpy.int32]
    geom_dataid: numpy.ndarray[numpy.int32]
    geom_fluid: numpy.ndarray[numpy.float64]
    geom_friction: numpy.ndarray[numpy.float64]
    geom_gap: numpy.ndarray[numpy.float64]
    geom_group: numpy.ndarray[numpy.int32]
    geom_margin: numpy.ndarray[numpy.float64]
    geom_matid: numpy.ndarray[numpy.int32]
    geom_plugin: numpy.ndarray[numpy.int32]
    geom_pos: numpy.ndarray[numpy.float64]
    geom_priority: numpy.ndarray[numpy.int32]
    geom_quat: numpy.ndarray[numpy.float64]
    geom_rbound: numpy.ndarray[numpy.float64]
    geom_rgba: numpy.ndarray[numpy.float32]
    geom_sameframe: numpy.ndarray[numpy.uint8]
    geom_size: numpy.ndarray[numpy.float64]
    geom_solimp: numpy.ndarray[numpy.float64]
    geom_solmix: numpy.ndarray[numpy.float64]
    geom_solref: numpy.ndarray[numpy.float64]
    geom_type: numpy.ndarray[numpy.int32]
    geom_user: numpy.ndarray[numpy.float64]
    hfield_adr: numpy.ndarray[numpy.int32]
    hfield_data: numpy.ndarray[numpy.float32]
    hfield_ncol: numpy.ndarray[numpy.int32]
    hfield_nrow: numpy.ndarray[numpy.int32]
    hfield_pathadr: numpy.ndarray[numpy.int32]
    hfield_size: numpy.ndarray[numpy.float64]
    jnt_actfrclimited: numpy.ndarray[numpy.uint8]
    jnt_actfrcrange: numpy.ndarray[numpy.float64]
    jnt_actgravcomp: numpy.ndarray[numpy.uint8]
    jnt_axis: numpy.ndarray[numpy.float64]
    jnt_bodyid: numpy.ndarray[numpy.int32]
    jnt_dofadr: numpy.ndarray[numpy.int32]
    jnt_group: numpy.ndarray[numpy.int32]
    jnt_limited: numpy.ndarray[numpy.uint8]
    jnt_margin: numpy.ndarray[numpy.float64]
    jnt_pos: numpy.ndarray[numpy.float64]
    jnt_qposadr: numpy.ndarray[numpy.int32]
    jnt_range: numpy.ndarray[numpy.float64]
    jnt_solimp: numpy.ndarray[numpy.float64]
    jnt_solref: numpy.ndarray[numpy.float64]
    jnt_stiffness: numpy.ndarray[numpy.float64]
    jnt_type: numpy.ndarray[numpy.int32]
    jnt_user: numpy.ndarray[numpy.float64]
    key_act: numpy.ndarray[numpy.float64]
    key_ctrl: numpy.ndarray[numpy.float64]
    key_mpos: numpy.ndarray[numpy.float64]
    key_mquat: numpy.ndarray[numpy.float64]
    key_qpos: numpy.ndarray[numpy.float64]
    key_qvel: numpy.ndarray[numpy.float64]
    key_time: numpy.ndarray[numpy.float64]
    light_active: numpy.ndarray[numpy.uint8]
    light_ambient: numpy.ndarray[numpy.float32]
    light_attenuation: numpy.ndarray[numpy.float32]
    light_bodyid: numpy.ndarray[numpy.int32]
    light_bulbradius: numpy.ndarray[numpy.float32]
    light_castshadow: numpy.ndarray[numpy.uint8]
    light_cutoff: numpy.ndarray[numpy.float32]
    light_diffuse: numpy.ndarray[numpy.float32]
    light_dir: numpy.ndarray[numpy.float64]
    light_dir0: numpy.ndarray[numpy.float64]
    light_directional: numpy.ndarray[numpy.uint8]
    light_exponent: numpy.ndarray[numpy.float32]
    light_mode: numpy.ndarray[numpy.int32]
    light_pos: numpy.ndarray[numpy.float64]
    light_pos0: numpy.ndarray[numpy.float64]
    light_poscom0: numpy.ndarray[numpy.float64]
    light_specular: numpy.ndarray[numpy.float32]
    light_targetbodyid: numpy.ndarray[numpy.int32]
    mat_emission: numpy.ndarray[numpy.float32]
    mat_metallic: numpy.ndarray[numpy.float32]
    mat_reflectance: numpy.ndarray[numpy.float32]
    mat_rgba: numpy.ndarray[numpy.float32]
    mat_roughness: numpy.ndarray[numpy.float32]
    mat_shininess: numpy.ndarray[numpy.float32]
    mat_specular: numpy.ndarray[numpy.float32]
    mat_texid: numpy.ndarray[numpy.int32]
    mat_texrepeat: numpy.ndarray[numpy.float32]
    mat_texuniform: numpy.ndarray[numpy.uint8]
    mesh_bvhadr: numpy.ndarray[numpy.int32]
    mesh_bvhnum: numpy.ndarray[numpy.int32]
    mesh_face: numpy.ndarray[numpy.int32]
    mesh_faceadr: numpy.ndarray[numpy.int32]
    mesh_facenormal: numpy.ndarray[numpy.int32]
    mesh_facenum: numpy.ndarray[numpy.int32]
    mesh_facetexcoord: numpy.ndarray[numpy.int32]
    mesh_graph: numpy.ndarray[numpy.int32]
    mesh_graphadr: numpy.ndarray[numpy.int32]
    mesh_normal: numpy.ndarray[numpy.float32]
    mesh_normaladr: numpy.ndarray[numpy.int32]
    mesh_normalnum: numpy.ndarray[numpy.int32]
    mesh_pathadr: numpy.ndarray[numpy.int32]
    mesh_polyadr: numpy.ndarray[numpy.int32]
    mesh_polymap: numpy.ndarray[numpy.int32]
    mesh_polymapadr: numpy.ndarray[numpy.int32]
    mesh_polymapnum: numpy.ndarray[numpy.int32]
    mesh_polynormal: numpy.ndarray[numpy.float64]
    mesh_polynum: numpy.ndarray[numpy.int32]
    mesh_polyvert: numpy.ndarray[numpy.int32]
    mesh_polyvertadr: numpy.ndarray[numpy.int32]
    mesh_polyvertnum: numpy.ndarray[numpy.int32]
    mesh_pos: numpy.ndarray[numpy.float64]
    mesh_quat: numpy.ndarray[numpy.float64]
    mesh_scale: numpy.ndarray[numpy.float64]
    mesh_texcoord: numpy.ndarray[numpy.float32]
    mesh_texcoordadr: numpy.ndarray[numpy.int32]
    mesh_texcoordnum: numpy.ndarray[numpy.int32]
    mesh_vert: numpy.ndarray[numpy.float32]
    mesh_vertadr: numpy.ndarray[numpy.int32]
    mesh_vertnum: numpy.ndarray[numpy.int32]
    name_actuatoradr: numpy.ndarray[numpy.int32]
    name_bodyadr: numpy.ndarray[numpy.int32]
    name_camadr: numpy.ndarray[numpy.int32]
    name_eqadr: numpy.ndarray[numpy.int32]
    name_excludeadr: numpy.ndarray[numpy.int32]
    name_flexadr: numpy.ndarray[numpy.int32]
    name_geomadr: numpy.ndarray[numpy.int32]
    name_hfieldadr: numpy.ndarray[numpy.int32]
    name_jntadr: numpy.ndarray[numpy.int32]
    name_keyadr: numpy.ndarray[numpy.int32]
    name_lightadr: numpy.ndarray[numpy.int32]
    name_matadr: numpy.ndarray[numpy.int32]
    name_meshadr: numpy.ndarray[numpy.int32]
    name_numericadr: numpy.ndarray[numpy.int32]
    name_pairadr: numpy.ndarray[numpy.int32]
    name_pluginadr: numpy.ndarray[numpy.int32]
    name_sensoradr: numpy.ndarray[numpy.int32]
    name_siteadr: numpy.ndarray[numpy.int32]
    name_skinadr: numpy.ndarray[numpy.int32]
    name_tendonadr: numpy.ndarray[numpy.int32]
    name_texadr: numpy.ndarray[numpy.int32]
    name_textadr: numpy.ndarray[numpy.int32]
    name_tupleadr: numpy.ndarray[numpy.int32]
    names_map: numpy.ndarray[numpy.int32]
    numeric_adr: numpy.ndarray[numpy.int32]
    numeric_data: numpy.ndarray[numpy.float64]
    numeric_size: numpy.ndarray[numpy.int32]
    pair_dim: numpy.ndarray[numpy.int32]
    pair_friction: numpy.ndarray[numpy.float64]
    pair_gap: numpy.ndarray[numpy.float64]
    pair_geom1: numpy.ndarray[numpy.int32]
    pair_geom2: numpy.ndarray[numpy.int32]
    pair_margin: numpy.ndarray[numpy.float64]
    pair_signature: numpy.ndarray[numpy.int32]
    pair_solimp: numpy.ndarray[numpy.float64]
    pair_solref: numpy.ndarray[numpy.float64]
    pair_solreffriction: numpy.ndarray[numpy.float64]
    plugin: numpy.ndarray[numpy.int32]
    plugin_attr: numpy.ndarray[numpy.int8]
    plugin_attradr: numpy.ndarray[numpy.int32]
    plugin_stateadr: numpy.ndarray[numpy.int32]
    plugin_statenum: numpy.ndarray[numpy.int32]
    qpos0: numpy.ndarray[numpy.float64]
    qpos_spring: numpy.ndarray[numpy.float64]
    sensor_adr: numpy.ndarray[numpy.int32]
    sensor_cutoff: numpy.ndarray[numpy.float64]
    sensor_datatype: numpy.ndarray[numpy.int32]
    sensor_dim: numpy.ndarray[numpy.int32]
    sensor_needstage: numpy.ndarray[numpy.int32]
    sensor_noise: numpy.ndarray[numpy.float64]
    sensor_objid: numpy.ndarray[numpy.int32]
    sensor_objtype: numpy.ndarray[numpy.int32]
    sensor_plugin: numpy.ndarray[numpy.int32]
    sensor_refid: numpy.ndarray[numpy.int32]
    sensor_reftype: numpy.ndarray[numpy.int32]
    sensor_type: numpy.ndarray[numpy.int32]
    sensor_user: numpy.ndarray[numpy.float64]
    site_bodyid: numpy.ndarray[numpy.int32]
    site_group: numpy.ndarray[numpy.int32]
    site_matid: numpy.ndarray[numpy.int32]
    site_pos: numpy.ndarray[numpy.float64]
    site_quat: numpy.ndarray[numpy.float64]
    site_rgba: numpy.ndarray[numpy.float32]
    site_sameframe: numpy.ndarray[numpy.uint8]
    site_size: numpy.ndarray[numpy.float64]
    site_type: numpy.ndarray[numpy.int32]
    site_user: numpy.ndarray[numpy.float64]
    skin_boneadr: numpy.ndarray[numpy.int32]
    skin_bonebindpos: numpy.ndarray[numpy.float32]
    skin_bonebindquat: numpy.ndarray[numpy.float32]
    skin_bonebodyid: numpy.ndarray[numpy.int32]
    skin_bonenum: numpy.ndarray[numpy.int32]
    skin_bonevertadr: numpy.ndarray[numpy.int32]
    skin_bonevertid: numpy.ndarray[numpy.int32]
    skin_bonevertnum: numpy.ndarray[numpy.int32]
    skin_bonevertweight: numpy.ndarray[numpy.float32]
    skin_face: numpy.ndarray[numpy.int32]
    skin_faceadr: numpy.ndarray[numpy.int32]
    skin_facenum: numpy.ndarray[numpy.int32]
    skin_group: numpy.ndarray[numpy.int32]
    skin_inflate: numpy.ndarray[numpy.float32]
    skin_matid: numpy.ndarray[numpy.int32]
    skin_pathadr: numpy.ndarray[numpy.int32]
    skin_rgba: numpy.ndarray[numpy.float32]
    skin_texcoord: numpy.ndarray[numpy.float32]
    skin_texcoordadr: numpy.ndarray[numpy.int32]
    skin_vert: numpy.ndarray[numpy.float32]
    skin_vertadr: numpy.ndarray[numpy.int32]
    skin_vertnum: numpy.ndarray[numpy.int32]
    tendon_adr: numpy.ndarray[numpy.int32]
    tendon_damping: numpy.ndarray[numpy.float64]
    tendon_frictionloss: numpy.ndarray[numpy.float64]
    tendon_group: numpy.ndarray[numpy.int32]
    tendon_invweight0: numpy.ndarray[numpy.float64]
    tendon_length0: numpy.ndarray[numpy.float64]
    tendon_lengthspring: numpy.ndarray[numpy.float64]
    tendon_limited: numpy.ndarray[numpy.uint8]
    tendon_margin: numpy.ndarray[numpy.float64]
    tendon_matid: numpy.ndarray[numpy.int32]
    tendon_num: numpy.ndarray[numpy.int32]
    tendon_range: numpy.ndarray[numpy.float64]
    tendon_rgba: numpy.ndarray[numpy.float32]
    tendon_solimp_fri: numpy.ndarray[numpy.float64]
    tendon_solimp_lim: numpy.ndarray[numpy.float64]
    tendon_solref_fri: numpy.ndarray[numpy.float64]
    tendon_solref_lim: numpy.ndarray[numpy.float64]
    tendon_stiffness: numpy.ndarray[numpy.float64]
    tendon_user: numpy.ndarray[numpy.float64]
    tendon_width: numpy.ndarray[numpy.float64]
    tex_adr: numpy.ndarray[numpy.int32]
    tex_data: numpy.ndarray[numpy.uint8]
    tex_height: numpy.ndarray[numpy.int32]
    tex_nchannel: numpy.ndarray[numpy.int32]
    tex_pathadr: numpy.ndarray[numpy.int32]
    tex_type: numpy.ndarray[numpy.int32]
    tex_width: numpy.ndarray[numpy.int32]
    text_adr: numpy.ndarray[numpy.int32]
    text_size: numpy.ndarray[numpy.int32]
    tuple_adr: numpy.ndarray[numpy.int32]
    tuple_objid: numpy.ndarray[numpy.int32]
    tuple_objprm: numpy.ndarray[numpy.float64]
    tuple_objtype: numpy.ndarray[numpy.int32]
    tuple_size: numpy.ndarray[numpy.int32]
    wrap_objid: numpy.ndarray[numpy.int32]
    wrap_prm: numpy.ndarray[numpy.float64]
    wrap_type: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def actuator(self, *args, **kwargs):
        """actuator(*args, **kwargs)
        Overloaded function.

        1. actuator(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelActuatorViews

        2. actuator(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelActuatorViews
        """
    def bind_scalar(self, *args, **kwargs):
        """bind_scalar(*args, **kwargs)
        Overloaded function.

        1. bind_scalar(self: mujoco._structs.MjModel, spec: mjsActuator_ = None) -> mujoco::python::MjModelActuatorViews

        2. bind_scalar(self: mujoco._structs.MjModel, spec: mjsBody_ = None) -> mujoco::python::MjModelBodyViews

        3. bind_scalar(self: mujoco._structs.MjModel, spec: mjsCamera_ = None) -> mujoco::python::MjModelCameraViews

        4. bind_scalar(self: mujoco._structs.MjModel, spec: mjsEquality_ = None) -> mujoco::python::MjModelEqualityViews

        5. bind_scalar(self: mujoco._structs.MjModel, spec: mjsExclude_ = None) -> mujoco::python::MjModelExcludeViews

        6. bind_scalar(self: mujoco._structs.MjModel, spec: mjsGeom_ = None) -> mujoco::python::MjModelGeomViews

        7. bind_scalar(self: mujoco._structs.MjModel, spec: mjsHField_ = None) -> mujoco::python::MjModelHfieldViews

        8. bind_scalar(self: mujoco._structs.MjModel, spec: mjsJoint_ = None) -> mujoco::python::MjModelJointViews

        9. bind_scalar(self: mujoco._structs.MjModel, spec: mjsLight_ = None) -> mujoco::python::MjModelLightViews

        10. bind_scalar(self: mujoco._structs.MjModel, spec: mjsMaterial_ = None) -> mujoco::python::MjModelMaterialViews

        11. bind_scalar(self: mujoco._structs.MjModel, spec: mjsMesh_ = None) -> mujoco::python::MjModelMeshViews

        12. bind_scalar(self: mujoco._structs.MjModel, spec: mjsNumeric_ = None) -> mujoco::python::MjModelNumericViews

        13. bind_scalar(self: mujoco._structs.MjModel, spec: mjsPair_ = None) -> mujoco::python::MjModelPairViews

        14. bind_scalar(self: mujoco._structs.MjModel, spec: mjsSensor_ = None) -> mujoco::python::MjModelSensorViews

        15. bind_scalar(self: mujoco._structs.MjModel, spec: mjsSite_ = None) -> mujoco::python::MjModelSiteViews

        16. bind_scalar(self: mujoco._structs.MjModel, spec: mjsSkin_ = None) -> mujoco::python::MjModelSkinViews

        17. bind_scalar(self: mujoco._structs.MjModel, spec: mjsTendon_ = None) -> mujoco::python::MjModelTendonViews

        18. bind_scalar(self: mujoco._structs.MjModel, spec: mjsTexture_ = None) -> mujoco::python::MjModelTextureViews

        19. bind_scalar(self: mujoco._structs.MjModel, spec: mjsTuple_ = None) -> mujoco::python::MjModelTupleViews

        20. bind_scalar(self: mujoco._structs.MjModel, spec: mjsKey_ = None) -> mujoco::python::MjModelKeyframeViews
        """
    def body(self, *args, **kwargs):
        """body(*args, **kwargs)
        Overloaded function.

        1. body(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelBodyViews

        2. body(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelBodyViews
        """
    def cam(self, *args, **kwargs):
        """cam(*args, **kwargs)
        Overloaded function.

        1. cam(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelCameraViews

        2. cam(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelCameraViews
        """
    def camera(self, *args, **kwargs):
        """camera(*args, **kwargs)
        Overloaded function.

        1. camera(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelCameraViews

        2. camera(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelCameraViews
        """
    def eq(self, *args, **kwargs):
        """eq(*args, **kwargs)
        Overloaded function.

        1. eq(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelEqualityViews

        2. eq(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelEqualityViews
        """
    def equality(self, *args, **kwargs):
        """equality(*args, **kwargs)
        Overloaded function.

        1. equality(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelEqualityViews

        2. equality(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelEqualityViews
        """
    def exclude(self, *args, **kwargs):
        """exclude(*args, **kwargs)
        Overloaded function.

        1. exclude(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelExcludeViews

        2. exclude(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelExcludeViews
        """
    @staticmethod
    def from_binary_path(filename: str, assets: dict[str, bytes] | None = ...) -> MjModel:
        """from_binary_path(filename: str, assets: Optional[dict[str, bytes]] = None) -> mujoco._structs.MjModel

        Loads an MjModel from an MJB file and an optional assets dictionary.

        The filename for the MJB can also refer to a key in the assets dictionary.
        This is useful for example when the MJB is not available as a file on disk.
        """
    @staticmethod
    def from_xml_path(filename: str, assets: dict[str, bytes] | None = ...) -> MjModel:
        """from_xml_path(filename: str, assets: Optional[dict[str, bytes]] = None) -> mujoco._structs.MjModel

        Loads an MjModel from an XML file and an optional assets dictionary.

        The filename for the XML can also refer to a key in the assets dictionary.
        This is useful for example when the XML is not available as a file on disk.
        """
    @staticmethod
    def from_xml_string(xml: str, assets: dict[str, bytes] | None = ...) -> MjModel:
        """from_xml_string(xml: str, assets: Optional[dict[str, bytes]] = None) -> mujoco._structs.MjModel

        Loads an MjModel from an XML string and an optional assets dictionary.
        """
    def geom(self, *args, **kwargs):
        """geom(*args, **kwargs)
        Overloaded function.

        1. geom(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelGeomViews

        2. geom(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelGeomViews
        """
    def hfield(self, *args, **kwargs):
        """hfield(*args, **kwargs)
        Overloaded function.

        1. hfield(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelHfieldViews

        2. hfield(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelHfieldViews
        """
    def jnt(self, *args, **kwargs):
        """jnt(*args, **kwargs)
        Overloaded function.

        1. jnt(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelJointViews

        2. jnt(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelJointViews
        """
    def joint(self, *args, **kwargs):
        """joint(*args, **kwargs)
        Overloaded function.

        1. joint(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelJointViews

        2. joint(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelJointViews
        """
    def key(self, *args, **kwargs):
        """key(*args, **kwargs)
        Overloaded function.

        1. key(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelKeyframeViews

        2. key(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelKeyframeViews
        """
    def keyframe(self, *args, **kwargs):
        """keyframe(*args, **kwargs)
        Overloaded function.

        1. keyframe(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelKeyframeViews

        2. keyframe(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelKeyframeViews
        """
    def light(self, *args, **kwargs):
        """light(*args, **kwargs)
        Overloaded function.

        1. light(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelLightViews

        2. light(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelLightViews
        """
    def mat(self, *args, **kwargs):
        """mat(*args, **kwargs)
        Overloaded function.

        1. mat(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelMaterialViews

        2. mat(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelMaterialViews
        """
    def material(self, *args, **kwargs):
        """material(*args, **kwargs)
        Overloaded function.

        1. material(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelMaterialViews

        2. material(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelMaterialViews
        """
    def mesh(self, *args, **kwargs):
        """mesh(*args, **kwargs)
        Overloaded function.

        1. mesh(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelMeshViews

        2. mesh(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelMeshViews
        """
    def numeric(self, *args, **kwargs):
        """numeric(*args, **kwargs)
        Overloaded function.

        1. numeric(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelNumericViews

        2. numeric(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelNumericViews
        """
    def pair(self, *args, **kwargs):
        """pair(*args, **kwargs)
        Overloaded function.

        1. pair(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelPairViews

        2. pair(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelPairViews
        """
    def sensor(self, *args, **kwargs):
        """sensor(*args, **kwargs)
        Overloaded function.

        1. sensor(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelSensorViews

        2. sensor(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelSensorViews
        """
    def site(self, *args, **kwargs):
        """site(*args, **kwargs)
        Overloaded function.

        1. site(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelSiteViews

        2. site(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelSiteViews
        """
    def skin(self, *args, **kwargs):
        """skin(*args, **kwargs)
        Overloaded function.

        1. skin(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelSkinViews

        2. skin(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelSkinViews
        """
    def tendon(self, *args, **kwargs):
        """tendon(*args, **kwargs)
        Overloaded function.

        1. tendon(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelTendonViews

        2. tendon(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelTendonViews
        """
    def tex(self, *args, **kwargs):
        """tex(*args, **kwargs)
        Overloaded function.

        1. tex(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelTextureViews

        2. tex(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelTextureViews
        """
    def texture(self, *args, **kwargs):
        """texture(*args, **kwargs)
        Overloaded function.

        1. texture(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelTextureViews

        2. texture(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelTextureViews
        """
    def tuple(self, *args, **kwargs):
        """tuple(*args, **kwargs)
        Overloaded function.

        1. tuple(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelTupleViews

        2. tuple(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelTupleViews
        """
    def __copy__(self) -> MjModel:
        """__copy__(self: mujoco._structs.MjModel) -> mujoco._structs.MjModel"""
    def __deepcopy__(self, arg0: dict) -> MjModel:
        """__deepcopy__(self: mujoco._structs.MjModel, arg0: dict) -> mujoco._structs.MjModel"""
    @property
    def nB(self) -> int: ...
    @property
    def nC(self) -> int: ...
    @property
    def nD(self) -> int: ...
    @property
    def nJmom(self) -> int: ...
    @property
    def nM(self) -> int: ...
    @property
    def na(self) -> int: ...
    @property
    def names(self) -> bytes: ...
    @property
    def narena(self) -> int: ...
    @property
    def nbody(self) -> int: ...
    @property
    def nbuffer(self) -> int: ...
    @property
    def nbvh(self) -> int: ...
    @property
    def nbvhdynamic(self) -> int: ...
    @property
    def nbvhstatic(self) -> int: ...
    @property
    def ncam(self) -> int: ...
    @property
    def nconmax(self) -> int: ...
    @property
    def nemax(self) -> int: ...
    @property
    def neq(self) -> int: ...
    @property
    def nexclude(self) -> int: ...
    @property
    def nflex(self) -> int: ...
    @property
    def nflexedge(self) -> int: ...
    @property
    def nflexelem(self) -> int: ...
    @property
    def nflexelemdata(self) -> int: ...
    @property
    def nflexelemedge(self) -> int: ...
    @property
    def nflexevpair(self) -> int: ...
    @property
    def nflexnode(self) -> int: ...
    @property
    def nflexshelldata(self) -> int: ...
    @property
    def nflextexcoord(self) -> int: ...
    @property
    def nflexvert(self) -> int: ...
    @property
    def ngeom(self) -> int: ...
    @property
    def ngravcomp(self) -> int: ...
    @property
    def nhfield(self) -> int: ...
    @property
    def nhfielddata(self) -> int: ...
    @property
    def njmax(self) -> int: ...
    @property
    def njnt(self) -> int: ...
    @property
    def nkey(self) -> int: ...
    @property
    def nlight(self) -> int: ...
    @property
    def nmat(self) -> int: ...
    @property
    def nmesh(self) -> int: ...
    @property
    def nmeshface(self) -> int: ...
    @property
    def nmeshgraph(self) -> int: ...
    @property
    def nmeshnormal(self) -> int: ...
    @property
    def nmeshpoly(self) -> int: ...
    @property
    def nmeshpolymap(self) -> int: ...
    @property
    def nmeshpolyvert(self) -> int: ...
    @property
    def nmeshtexcoord(self) -> int: ...
    @property
    def nmeshvert(self) -> int: ...
    @property
    def nmocap(self) -> int: ...
    @property
    def nnames(self) -> int: ...
    @property
    def nnames_map(self) -> int: ...
    @property
    def nnumeric(self) -> int: ...
    @property
    def nnumericdata(self) -> int: ...
    @property
    def npair(self) -> int: ...
    @property
    def npaths(self) -> int: ...
    @property
    def nplugin(self) -> int: ...
    @property
    def npluginattr(self) -> int: ...
    @property
    def npluginstate(self) -> int: ...
    @property
    def nq(self) -> int: ...
    @property
    def nsensor(self) -> int: ...
    @property
    def nsensordata(self) -> int: ...
    @property
    def nsite(self) -> int: ...
    @property
    def nskin(self) -> int: ...
    @property
    def nskinbone(self) -> int: ...
    @property
    def nskinbonevert(self) -> int: ...
    @property
    def nskinface(self) -> int: ...
    @property
    def nskintexvert(self) -> int: ...
    @property
    def nskinvert(self) -> int: ...
    @property
    def ntendon(self) -> int: ...
    @property
    def ntex(self) -> int: ...
    @property
    def ntexdata(self) -> int: ...
    @property
    def ntext(self) -> int: ...
    @property
    def ntextdata(self) -> int: ...
    @property
    def ntree(self) -> int: ...
    @property
    def ntuple(self) -> int: ...
    @property
    def ntupledata(self) -> int: ...
    @property
    def nu(self) -> int: ...
    @property
    def nuser_actuator(self) -> int: ...
    @property
    def nuser_body(self) -> int: ...
    @property
    def nuser_cam(self) -> int: ...
    @property
    def nuser_geom(self) -> int: ...
    @property
    def nuser_jnt(self) -> int: ...
    @property
    def nuser_sensor(self) -> int: ...
    @property
    def nuser_site(self) -> int: ...
    @property
    def nuser_tendon(self) -> int: ...
    @property
    def nuserdata(self) -> int: ...
    @property
    def nv(self) -> int: ...
    @property
    def nwrap(self) -> int: ...
    @property
    def opt(self) -> MjOption: ...
    @property
    def paths(self) -> bytes: ...
    @property
    def stat(self): ...
    @property
    def text_data(self) -> bytes: ...
    @property
    def vis(self) -> MjVisual: ...

class MjOption:
    apirate: float
    ccd_iterations: int
    ccd_tolerance: float
    cone: int
    density: float
    disableactuator: int
    disableflags: int
    enableflags: int
    gravity: numpy.ndarray[numpy.float64]
    impratio: float
    integrator: int
    iterations: int
    jacobian: int
    ls_iterations: int
    ls_tolerance: float
    magnetic: numpy.ndarray[numpy.float64]
    noslip_iterations: int
    noslip_tolerance: float
    o_friction: numpy.ndarray[numpy.float64]
    o_margin: float
    o_solimp: numpy.ndarray[numpy.float64]
    o_solref: numpy.ndarray[numpy.float64]
    sdf_initpoints: int
    sdf_iterations: int
    solver: int
    timestep: float
    tolerance: float
    viscosity: float
    wind: numpy.ndarray[numpy.float64]
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjOption) -> None"""
    def __copy__(self) -> MjOption:
        """__copy__(self: mujoco._structs.MjOption) -> mujoco._structs.MjOption"""
    def __deepcopy__(self, arg0: dict) -> MjOption:
        """__deepcopy__(self: mujoco._structs.MjOption, arg0: dict) -> mujoco._structs.MjOption"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjSolverStat:
    gradient: float
    improvement: float
    lineslope: float
    nactive: int
    nchange: int
    neval: int
    nupdate: int
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjSolverStat) -> None"""
    def __copy__(self) -> MjSolverStat:
        """__copy__(self: mujoco._structs.MjSolverStat) -> mujoco._structs.MjSolverStat"""
    def __deepcopy__(self, arg0: dict) -> MjSolverStat:
        """__deepcopy__(self: mujoco._structs.MjSolverStat, arg0: dict) -> mujoco._structs.MjSolverStat"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjStatistic:
    center: numpy.ndarray[numpy.float64]
    extent: float
    meaninertia: float
    meanmass: float
    meansize: float
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjStatistic) -> None"""
    def __copy__(self) -> MjStatistic:
        """__copy__(self: mujoco._structs.MjStatistic) -> mujoco._structs.MjStatistic"""
    def __deepcopy__(self, arg0: dict) -> MjStatistic:
        """__deepcopy__(self: mujoco._structs.MjStatistic, arg0: dict) -> mujoco._structs.MjStatistic"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjTimerStat:
    duration: float
    number: int
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjTimerStat) -> None"""
    def __copy__(self) -> MjTimerStat:
        """__copy__(self: mujoco._structs.MjTimerStat) -> mujoco._structs.MjTimerStat"""
    def __deepcopy__(self, arg0: dict) -> MjTimerStat:
        """__deepcopy__(self: mujoco._structs.MjTimerStat, arg0: dict) -> mujoco._structs.MjTimerStat"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjVisual:
    class Global:
        azimuth: float
        bvactive: int
        elevation: float
        ellipsoidinertia: int
        fovy: float
        glow: float
        ipd: float
        linewidth: float
        offheight: int
        offwidth: int
        orthographic: int
        realtime: float
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""
        def __copy__(self) -> MjVisual.Global:
            """__copy__(self: mujoco._structs.MjVisual.Global) -> mujoco._structs.MjVisual.Global"""
        def __deepcopy__(self, arg0: dict) -> MjVisual.Global:
            """__deepcopy__(self: mujoco._structs.MjVisual.Global, arg0: dict) -> mujoco._structs.MjVisual.Global"""
        def __eq__(self, arg0: object) -> bool:
            """__eq__(self: object, arg0: object) -> bool"""

    class Headlight:
        active: int
        ambient: numpy.ndarray[numpy.float32]
        diffuse: numpy.ndarray[numpy.float32]
        specular: numpy.ndarray[numpy.float32]
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""
        def __copy__(self) -> MjVisual.Headlight:
            """__copy__(self: mujoco._structs.MjVisual.Headlight) -> mujoco._structs.MjVisual.Headlight"""
        def __deepcopy__(self, arg0: dict) -> MjVisual.Headlight:
            """__deepcopy__(self: mujoco._structs.MjVisual.Headlight, arg0: dict) -> mujoco._structs.MjVisual.Headlight"""
        def __eq__(self, arg0: object) -> bool:
            """__eq__(self: object, arg0: object) -> bool"""

    class Map:
        actuatortendon: float
        alpha: float
        fogend: float
        fogstart: float
        force: float
        haze: float
        shadowclip: float
        shadowscale: float
        stiffness: float
        stiffnessrot: float
        torque: float
        zfar: float
        znear: float
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""
        def __copy__(self) -> MjVisual.Map:
            """__copy__(self: mujoco._structs.MjVisual.Map) -> mujoco._structs.MjVisual.Map"""
        def __deepcopy__(self, arg0: dict) -> MjVisual.Map:
            """__deepcopy__(self: mujoco._structs.MjVisual.Map, arg0: dict) -> mujoco._structs.MjVisual.Map"""
        def __eq__(self, arg0: object) -> bool:
            """__eq__(self: object, arg0: object) -> bool"""

    class Quality:
        numquads: int
        numslices: int
        numstacks: int
        offsamples: int
        shadowsize: int
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""
        def __copy__(self) -> MjVisual.Quality:
            """__copy__(self: mujoco._structs.MjVisual.Quality) -> mujoco._structs.MjVisual.Quality"""
        def __deepcopy__(self, arg0: dict) -> MjVisual.Quality:
            """__deepcopy__(self: mujoco._structs.MjVisual.Quality, arg0: dict) -> mujoco._structs.MjVisual.Quality"""
        def __eq__(self, arg0: object) -> bool:
            """__eq__(self: object, arg0: object) -> bool"""

    class Rgba:
        actuator: numpy.ndarray[numpy.float32]
        actuatornegative: numpy.ndarray[numpy.float32]
        actuatorpositive: numpy.ndarray[numpy.float32]
        bv: numpy.ndarray[numpy.float32]
        bvactive: numpy.ndarray[numpy.float32]
        camera: numpy.ndarray[numpy.float32]
        com: numpy.ndarray[numpy.float32]
        connect: numpy.ndarray[numpy.float32]
        constraint: numpy.ndarray[numpy.float32]
        contactforce: numpy.ndarray[numpy.float32]
        contactfriction: numpy.ndarray[numpy.float32]
        contactgap: numpy.ndarray[numpy.float32]
        contactpoint: numpy.ndarray[numpy.float32]
        contacttorque: numpy.ndarray[numpy.float32]
        crankbroken: numpy.ndarray[numpy.float32]
        fog: numpy.ndarray[numpy.float32]
        force: numpy.ndarray[numpy.float32]
        frustum: numpy.ndarray[numpy.float32]
        haze: numpy.ndarray[numpy.float32]
        inertia: numpy.ndarray[numpy.float32]
        joint: numpy.ndarray[numpy.float32]
        light: numpy.ndarray[numpy.float32]
        rangefinder: numpy.ndarray[numpy.float32]
        selectpoint: numpy.ndarray[numpy.float32]
        slidercrank: numpy.ndarray[numpy.float32]
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""
        def __copy__(self) -> MjVisual.Rgba:
            """__copy__(self: mujoco._structs.MjVisual.Rgba) -> mujoco._structs.MjVisual.Rgba"""
        def __deepcopy__(self, arg0: dict) -> MjVisual.Rgba:
            """__deepcopy__(self: mujoco._structs.MjVisual.Rgba, arg0: dict) -> mujoco._structs.MjVisual.Rgba"""
        def __eq__(self, arg0: object) -> bool:
            """__eq__(self: object, arg0: object) -> bool"""

    class Scale:
        actuatorlength: float
        actuatorwidth: float
        camera: float
        com: float
        connect: float
        constraint: float
        contactheight: float
        contactwidth: float
        forcewidth: float
        framelength: float
        framewidth: float
        frustum: float
        jointlength: float
        jointwidth: float
        light: float
        selectpoint: float
        slidercrank: float
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""
        def __copy__(self) -> MjVisual.Scale:
            """__copy__(self: mujoco._structs.MjVisual.Scale) -> mujoco._structs.MjVisual.Scale"""
        def __deepcopy__(self, arg0: dict) -> MjVisual.Scale:
            """__deepcopy__(self: mujoco._structs.MjVisual.Scale, arg0: dict) -> mujoco._structs.MjVisual.Scale"""
        def __eq__(self, arg0: object) -> bool:
            """__eq__(self: object, arg0: object) -> bool"""
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __copy__(self) -> MjVisual:
        """__copy__(self: mujoco._structs.MjVisual) -> mujoco._structs.MjVisual"""
    def __deepcopy__(self, arg0: dict) -> MjVisual:
        """__deepcopy__(self: mujoco._structs.MjVisual, arg0: dict) -> mujoco._structs.MjVisual"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""
    @property
    def global_(self) -> MjVisual.Global: ...
    @property
    def headlight(self) -> MjVisual.Headlight: ...
    @property
    def map(self) -> MjVisual.Map: ...
    @property
    def quality(self) -> MjVisual.Quality: ...
    @property
    def rgba(self) -> MjVisual.Rgba: ...
    @property
    def scale(self) -> MjVisual.Scale: ...

class MjWarningStat:
    lastinfo: int
    number: int
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjWarningStat) -> None"""
    def __copy__(self) -> MjWarningStat:
        """__copy__(self: mujoco._structs.MjWarningStat) -> mujoco._structs.MjWarningStat"""
    def __deepcopy__(self, arg0: dict) -> MjWarningStat:
        """__deepcopy__(self: mujoco._structs.MjWarningStat, arg0: dict) -> mujoco._structs.MjWarningStat"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjvCamera:
    azimuth: float
    distance: float
    elevation: float
    fixedcamid: int
    lookat: numpy.ndarray[numpy.float64]
    orthographic: int
    trackbodyid: int
    type: int
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjvCamera) -> None"""
    def __copy__(self) -> MjvCamera:
        """__copy__(self: mujoco._structs.MjvCamera) -> mujoco._structs.MjvCamera"""
    def __deepcopy__(self, arg0: dict) -> MjvCamera:
        """__deepcopy__(self: mujoco._structs.MjvCamera, arg0: dict) -> mujoco._structs.MjvCamera"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjvFigure:
    figurergba: numpy.ndarray[numpy.float32]
    flg_barplot: int
    flg_extend: int
    flg_legend: int
    flg_selection: int
    flg_symmetric: int
    flg_ticklabel: numpy.ndarray[numpy.int32]
    gridrgb: numpy.ndarray[numpy.float32]
    gridsize: numpy.ndarray[numpy.int32]
    gridwidth: float
    highlight: numpy.ndarray[numpy.int32]
    highlightid: int
    legendoffset: int
    legendrgba: numpy.ndarray[numpy.float32]
    linedata: numpy.ndarray[numpy.float32]
    linepnt: numpy.ndarray[numpy.int32]
    linergb: numpy.ndarray[numpy.float32]
    linewidth: float
    minwidth: str
    panergba: numpy.ndarray[numpy.float32]
    range: numpy.ndarray[numpy.float32]
    selection: float
    subplot: int
    textrgb: numpy.ndarray[numpy.float32]
    title: str
    xaxisdata: numpy.ndarray[numpy.float32]
    xaxispixel: numpy.ndarray[numpy.int32]
    xformat: str
    xlabel: str
    yaxisdata: numpy.ndarray[numpy.float32]
    yaxispixel: numpy.ndarray[numpy.int32]
    yformat: str
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjvFigure) -> None"""
    def __copy__(self) -> MjvFigure:
        """__copy__(self: mujoco._structs.MjvFigure) -> mujoco._structs.MjvFigure"""
    def __deepcopy__(self, arg0: dict) -> MjvFigure:
        """__deepcopy__(self: mujoco._structs.MjvFigure, arg0: dict) -> mujoco._structs.MjvFigure"""
    @property
    def linename(self) -> numpy.ndarray: ...

class MjvGLCamera:
    forward: numpy.ndarray[numpy.float32]
    frustum_bottom: float
    frustum_center: float
    frustum_far: float
    frustum_near: float
    frustum_top: float
    frustum_width: float
    orthographic: int
    pos: numpy.ndarray[numpy.float32]
    up: numpy.ndarray[numpy.float32]
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjvGLCamera) -> None"""
    def __copy__(self) -> MjvGLCamera:
        """__copy__(self: mujoco._structs.MjvGLCamera) -> mujoco._structs.MjvGLCamera"""
    def __deepcopy__(self, arg0: dict) -> MjvGLCamera:
        """__deepcopy__(self: mujoco._structs.MjvGLCamera, arg0: dict) -> mujoco._structs.MjvGLCamera"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjvGeom:
    camdist: float
    category: int
    dataid: int
    emission: float
    label: str
    mat: numpy.ndarray[numpy.float32]
    matid: int
    modelrbound: float
    objid: int
    objtype: int
    pos: numpy.ndarray[numpy.float32]
    reflectance: float
    rgba: numpy.ndarray[numpy.float32]
    segid: int
    shininess: float
    size: numpy.ndarray[numpy.float32]
    specular: float
    texcoord: int
    transparent: int
    type: int
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjvGeom) -> None"""
    def __copy__(self) -> MjvGeom:
        """__copy__(self: mujoco._structs.MjvGeom) -> mujoco._structs.MjvGeom"""
    def __deepcopy__(self, arg0: dict) -> MjvGeom:
        """__deepcopy__(self: mujoco._structs.MjvGeom, arg0: dict) -> mujoco._structs.MjvGeom"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjvLight:
    ambient: numpy.ndarray[numpy.float32]
    attenuation: numpy.ndarray[numpy.float32]
    bulbradius: float
    castshadow: int
    cutoff: float
    diffuse: numpy.ndarray[numpy.float32]
    dir: numpy.ndarray[numpy.float32]
    directional: int
    exponent: float
    headlight: int
    pos: numpy.ndarray[numpy.float32]
    specular: numpy.ndarray[numpy.float32]
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjvLight) -> None"""
    def __copy__(self) -> MjvLight:
        """__copy__(self: mujoco._structs.MjvLight) -> mujoco._structs.MjvLight"""
    def __deepcopy__(self, arg0: dict) -> MjvLight:
        """__deepcopy__(self: mujoco._structs.MjvLight, arg0: dict) -> mujoco._structs.MjvLight"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjvOption:
    actuatorgroup: numpy.ndarray[numpy.uint8]
    bvh_depth: int
    flags: numpy.ndarray[numpy.uint8]
    flex_layer: int
    flexgroup: numpy.ndarray[numpy.uint8]
    frame: int
    geomgroup: numpy.ndarray[numpy.uint8]
    jointgroup: numpy.ndarray[numpy.uint8]
    label: int
    sitegroup: numpy.ndarray[numpy.uint8]
    skingroup: numpy.ndarray[numpy.uint8]
    tendongroup: numpy.ndarray[numpy.uint8]
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjvOption) -> None"""
    def __copy__(self) -> MjvOption:
        """__copy__(self: mujoco._structs.MjvOption) -> mujoco._structs.MjvOption"""
    def __deepcopy__(self, arg0: dict) -> MjvOption:
        """__deepcopy__(self: mujoco._structs.MjvOption, arg0: dict) -> mujoco._structs.MjvOption"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjvPerturb:
    active: int
    active2: int
    flexselect: int
    localmass: float
    localpos: numpy.ndarray[numpy.float64]
    refpos: numpy.ndarray[numpy.float64]
    refquat: numpy.ndarray[numpy.float64]
    refselpos: numpy.ndarray[numpy.float64]
    scale: float
    select: int
    skinselect: int
    def __init__(self) -> None:
        """__init__(self: mujoco._structs.MjvPerturb) -> None"""
    def __copy__(self) -> MjvPerturb:
        """__copy__(self: mujoco._structs.MjvPerturb) -> mujoco._structs.MjvPerturb"""
    def __deepcopy__(self, arg0: dict) -> MjvPerturb:
        """__deepcopy__(self: mujoco._structs.MjvPerturb, arg0: dict) -> mujoco._structs.MjvPerturb"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""

class MjvScene:
    enabletransform: int
    flags: numpy.ndarray[numpy.uint8]
    flexedge: numpy.ndarray[numpy.int32]
    flexedgeadr: numpy.ndarray[numpy.int32]
    flexedgenum: numpy.ndarray[numpy.int32]
    flexedgeopt: int
    flexface: numpy.ndarray[numpy.float32]
    flexfaceadr: numpy.ndarray[numpy.int32]
    flexfacenum: numpy.ndarray[numpy.int32]
    flexfaceopt: int
    flexfaceused: numpy.ndarray[numpy.int32]
    flexnormal: numpy.ndarray[numpy.float32]
    flexskinopt: int
    flextexcoord: numpy.ndarray[numpy.float32]
    flexvert: numpy.ndarray[numpy.float32]
    flexvertadr: numpy.ndarray[numpy.int32]
    flexvertnum: numpy.ndarray[numpy.int32]
    flexvertopt: int
    framergb: numpy.ndarray[numpy.float32]
    framewidth: int
    geomorder: numpy.ndarray[numpy.int32]
    maxgeom: int
    nflex: int
    ngeom: int
    nlight: int
    nskin: int
    rotate: numpy.ndarray[numpy.float32]
    scale: float
    skinfacenum: numpy.ndarray[numpy.int32]
    skinnormal: numpy.ndarray[numpy.float32]
    skinvert: numpy.ndarray[numpy.float32]
    skinvertadr: numpy.ndarray[numpy.int32]
    skinvertnum: numpy.ndarray[numpy.int32]
    stereo: int
    translate: numpy.ndarray[numpy.float32]
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._structs.MjvScene) -> None

        2. __init__(self: mujoco._structs.MjvScene, model: mujoco._structs.MjModel, maxgeom: int) -> None
        """
    @overload
    def __init__(self, model: MjModel, maxgeom: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: mujoco._structs.MjvScene) -> None

        2. __init__(self: mujoco._structs.MjvScene, model: mujoco._structs.MjModel, maxgeom: int) -> None
        """
    def __copy__(self) -> MjvScene:
        """__copy__(self: mujoco._structs.MjvScene) -> mujoco._structs.MjvScene"""
    def __deepcopy__(self, arg0: dict) -> MjvScene:
        """__deepcopy__(self: mujoco._structs.MjvScene, arg0: dict) -> mujoco._structs.MjvScene"""
    @property
    def camera(self) -> tuple: ...
    @property
    def geoms(self) -> tuple: ...
    @property
    def lights(self) -> tuple: ...

class _MjContactList:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""
    @overload
    def __getitem__(self, arg0: int) -> MjContact:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjContactList, arg0: int) -> mujoco._structs.MjContact

        2. __getitem__(self: mujoco._structs._MjContactList, arg0: slice) -> mujoco._structs._MjContactList
        """
    @overload
    def __getitem__(self, arg0: slice) -> _MjContactList:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjContactList, arg0: int) -> mujoco._structs.MjContact

        2. __getitem__(self: mujoco._structs._MjContactList, arg0: slice) -> mujoco._structs._MjContactList
        """
    def __iter__(self) -> typing.Iterator[MjContact]:
        """def __iter__(self) -> typing.Iterator[MjContact]"""
    def __len__(self) -> int:
        """__len__(self: mujoco._structs._MjContactList) -> int"""
    @property
    def H(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def dim(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def dist(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def efc_address(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def elem(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def exclude(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def flex(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def frame(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def friction(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def geom(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def geom1(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def geom2(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def includemargin(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def mu(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def pos(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def solimp(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def solref(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def solreffriction(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def vert(self) -> numpy.ndarray[numpy.int32]: ...

class _MjDataActuatorViews:
    ctrl: numpy.ndarray[numpy.float64]
    force: numpy.ndarray[numpy.float64]
    length: numpy.ndarray[numpy.float64]
    moment: numpy.ndarray[numpy.float64]
    velocity: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjDataBodyViews:
    cacc: numpy.ndarray[numpy.float64]
    cfrc_ext: numpy.ndarray[numpy.float64]
    cfrc_int: numpy.ndarray[numpy.float64]
    cinert: numpy.ndarray[numpy.float64]
    crb: numpy.ndarray[numpy.float64]
    cvel: numpy.ndarray[numpy.float64]
    subtree_angmom: numpy.ndarray[numpy.float64]
    subtree_com: numpy.ndarray[numpy.float64]
    subtree_linvel: numpy.ndarray[numpy.float64]
    xfrc_applied: numpy.ndarray[numpy.float64]
    ximat: numpy.ndarray[numpy.float64]
    xipos: numpy.ndarray[numpy.float64]
    xmat: numpy.ndarray[numpy.float64]
    xpos: numpy.ndarray[numpy.float64]
    xquat: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjDataCameraViews:
    xmat: numpy.ndarray[numpy.float64]
    xpos: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjDataGeomViews:
    xmat: numpy.ndarray[numpy.float64]
    xpos: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjDataJointViews:
    cdof: numpy.ndarray[numpy.float64]
    cdof_dot: numpy.ndarray[numpy.float64]
    qLDiagInv: numpy.ndarray[numpy.float64]
    qacc: numpy.ndarray[numpy.float64]
    qacc_smooth: numpy.ndarray[numpy.float64]
    qacc_warmstart: numpy.ndarray[numpy.float64]
    qfrc_actuator: numpy.ndarray[numpy.float64]
    qfrc_applied: numpy.ndarray[numpy.float64]
    qfrc_bias: numpy.ndarray[numpy.float64]
    qfrc_constraint: numpy.ndarray[numpy.float64]
    qfrc_inverse: numpy.ndarray[numpy.float64]
    qfrc_passive: numpy.ndarray[numpy.float64]
    qfrc_smooth: numpy.ndarray[numpy.float64]
    qpos: numpy.ndarray[numpy.float64]
    qvel: numpy.ndarray[numpy.float64]
    xanchor: numpy.ndarray[numpy.float64]
    xaxis: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjDataLightViews:
    xdir: numpy.ndarray[numpy.float64]
    xpos: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjDataSensorViews:
    data: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjDataSiteViews:
    xmat: numpy.ndarray[numpy.float64]
    xpos: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjDataTendonViews:
    J: numpy.ndarray[numpy.float64]
    J_colind: numpy.ndarray[numpy.int32]
    J_rowadr: numpy.ndarray[numpy.int32]
    J_rownnz: numpy.ndarray[numpy.int32]
    length: numpy.ndarray[numpy.float64]
    velocity: numpy.ndarray[numpy.float64]
    wrapadr: numpy.ndarray[numpy.int32]
    wrapnum: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelActuatorViews:
    acc0: numpy.ndarray[numpy.float64]
    actadr: numpy.ndarray[numpy.int32]
    actlimited: numpy.ndarray[numpy.uint8]
    actnum: numpy.ndarray[numpy.int32]
    actrange: numpy.ndarray[numpy.float64]
    biasprm: numpy.ndarray[numpy.float64]
    biastype: numpy.ndarray[numpy.int32]
    cranklength: numpy.ndarray[numpy.float64]
    ctrllimited: numpy.ndarray[numpy.uint8]
    ctrlrange: numpy.ndarray[numpy.float64]
    dynprm: numpy.ndarray[numpy.float64]
    dyntype: numpy.ndarray[numpy.int32]
    forcelimited: numpy.ndarray[numpy.uint8]
    forcerange: numpy.ndarray[numpy.float64]
    gainprm: numpy.ndarray[numpy.float64]
    gaintype: numpy.ndarray[numpy.int32]
    gear: numpy.ndarray[numpy.float64]
    group: numpy.ndarray[numpy.int32]
    length0: numpy.ndarray[numpy.float64]
    lengthrange: numpy.ndarray[numpy.float64]
    trnid: numpy.ndarray[numpy.int32]
    trntype: numpy.ndarray[numpy.int32]
    user: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelBodyViews:
    dofadr: numpy.ndarray[numpy.int32]
    dofnum: numpy.ndarray[numpy.int32]
    geomadr: numpy.ndarray[numpy.int32]
    geomnum: numpy.ndarray[numpy.int32]
    inertia: numpy.ndarray[numpy.float64]
    invweight0: numpy.ndarray[numpy.float64]
    ipos: numpy.ndarray[numpy.float64]
    iquat: numpy.ndarray[numpy.float64]
    jntadr: numpy.ndarray[numpy.int32]
    jntnum: numpy.ndarray[numpy.int32]
    mass: numpy.ndarray[numpy.float64]
    mocapid: numpy.ndarray[numpy.int32]
    parentid: numpy.ndarray[numpy.int32]
    pos: numpy.ndarray[numpy.float64]
    quat: numpy.ndarray[numpy.float64]
    rootid: numpy.ndarray[numpy.int32]
    sameframe: numpy.ndarray[numpy.uint8]
    simple: numpy.ndarray[numpy.uint8]
    subtreemass: numpy.ndarray[numpy.float64]
    user: numpy.ndarray[numpy.float64]
    weldid: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelCameraViews:
    bodyid: numpy.ndarray[numpy.int32]
    fovy: numpy.ndarray[numpy.float64]
    ipd: numpy.ndarray[numpy.float64]
    mat0: numpy.ndarray[numpy.float64]
    mode: numpy.ndarray[numpy.int32]
    pos: numpy.ndarray[numpy.float64]
    pos0: numpy.ndarray[numpy.float64]
    poscom0: numpy.ndarray[numpy.float64]
    quat: numpy.ndarray[numpy.float64]
    targetbodyid: numpy.ndarray[numpy.int32]
    user: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelEqualityViews:
    active0: numpy.ndarray[numpy.uint8]
    data: numpy.ndarray[numpy.float64]
    obj1id: numpy.ndarray[numpy.int32]
    obj2id: numpy.ndarray[numpy.int32]
    solimp: numpy.ndarray[numpy.float64]
    solref: numpy.ndarray[numpy.float64]
    type: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelExcludeViews:
    signature: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelGeomViews:
    bodyid: numpy.ndarray[numpy.int32]
    conaffinity: numpy.ndarray[numpy.int32]
    condim: numpy.ndarray[numpy.int32]
    contype: numpy.ndarray[numpy.int32]
    dataid: numpy.ndarray[numpy.int32]
    friction: numpy.ndarray[numpy.float64]
    gap: numpy.ndarray[numpy.float64]
    group: numpy.ndarray[numpy.int32]
    margin: numpy.ndarray[numpy.float64]
    matid: numpy.ndarray[numpy.int32]
    pos: numpy.ndarray[numpy.float64]
    priority: numpy.ndarray[numpy.int32]
    quat: numpy.ndarray[numpy.float64]
    rbound: numpy.ndarray[numpy.float64]
    rgba: numpy.ndarray[numpy.float32]
    sameframe: numpy.ndarray[numpy.uint8]
    size: numpy.ndarray[numpy.float64]
    solimp: numpy.ndarray[numpy.float64]
    solmix: numpy.ndarray[numpy.float64]
    solref: numpy.ndarray[numpy.float64]
    type: numpy.ndarray[numpy.int32]
    user: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelHfieldViews:
    adr: numpy.ndarray[numpy.int32]
    data: numpy.ndarray[numpy.float32]
    ncol: numpy.ndarray[numpy.int32]
    nrow: numpy.ndarray[numpy.int32]
    size: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelJointViews:
    M0: numpy.ndarray[numpy.float64]
    Madr: numpy.ndarray[numpy.int32]
    armature: numpy.ndarray[numpy.float64]
    axis: numpy.ndarray[numpy.float64]
    bodyid: numpy.ndarray[numpy.int32]
    damping: numpy.ndarray[numpy.float64]
    dofadr: numpy.ndarray[numpy.int32]
    frictionloss: numpy.ndarray[numpy.float64]
    group: numpy.ndarray[numpy.int32]
    invweight0: numpy.ndarray[numpy.float64]
    jntid: numpy.ndarray[numpy.int32]
    limited: numpy.ndarray[numpy.uint8]
    margin: numpy.ndarray[numpy.float64]
    parentid: numpy.ndarray[numpy.int32]
    pos: numpy.ndarray[numpy.float64]
    qpos0: numpy.ndarray[numpy.float64]
    qpos_spring: numpy.ndarray[numpy.float64]
    qposadr: numpy.ndarray[numpy.int32]
    range: numpy.ndarray[numpy.float64]
    simplenum: numpy.ndarray[numpy.int32]
    solimp: numpy.ndarray[numpy.float64]
    solref: numpy.ndarray[numpy.float64]
    stiffness: numpy.ndarray[numpy.float64]
    type: numpy.ndarray[numpy.int32]
    user: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelKeyframeViews:
    act: numpy.ndarray[numpy.float64]
    ctrl: numpy.ndarray[numpy.float64]
    mpos: numpy.ndarray[numpy.float64]
    mquat: numpy.ndarray[numpy.float64]
    qpos: numpy.ndarray[numpy.float64]
    qvel: numpy.ndarray[numpy.float64]
    time: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelLightViews:
    active: numpy.ndarray[numpy.uint8]
    ambient: numpy.ndarray[numpy.float32]
    attenuation: numpy.ndarray[numpy.float32]
    bodyid: numpy.ndarray[numpy.int32]
    castshadow: numpy.ndarray[numpy.uint8]
    cutoff: numpy.ndarray[numpy.float32]
    diffuse: numpy.ndarray[numpy.float32]
    dir: numpy.ndarray[numpy.float64]
    dir0: numpy.ndarray[numpy.float64]
    directional: numpy.ndarray[numpy.uint8]
    exponent: numpy.ndarray[numpy.float32]
    mode: numpy.ndarray[numpy.int32]
    pos: numpy.ndarray[numpy.float64]
    pos0: numpy.ndarray[numpy.float64]
    poscom0: numpy.ndarray[numpy.float64]
    specular: numpy.ndarray[numpy.float32]
    targetbodyid: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelMaterialViews:
    emission: numpy.ndarray[numpy.float32]
    reflectance: numpy.ndarray[numpy.float32]
    rgba: numpy.ndarray[numpy.float32]
    shininess: numpy.ndarray[numpy.float32]
    specular: numpy.ndarray[numpy.float32]
    texid: numpy.ndarray[numpy.int32]
    texrepeat: numpy.ndarray[numpy.float32]
    texuniform: numpy.ndarray[numpy.uint8]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelMeshViews:
    faceadr: numpy.ndarray[numpy.int32]
    facenum: numpy.ndarray[numpy.int32]
    graphadr: numpy.ndarray[numpy.int32]
    texcoordadr: numpy.ndarray[numpy.int32]
    vertadr: numpy.ndarray[numpy.int32]
    vertnum: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelNumericViews:
    adr: numpy.ndarray[numpy.int32]
    data: numpy.ndarray[numpy.float64]
    size: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelPairViews:
    dim: numpy.ndarray[numpy.int32]
    friction: numpy.ndarray[numpy.float64]
    gap: numpy.ndarray[numpy.float64]
    geom1: numpy.ndarray[numpy.int32]
    geom2: numpy.ndarray[numpy.int32]
    margin: numpy.ndarray[numpy.float64]
    signature: numpy.ndarray[numpy.int32]
    solimp: numpy.ndarray[numpy.float64]
    solref: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelSensorViews:
    adr: numpy.ndarray[numpy.int32]
    cutoff: numpy.ndarray[numpy.float64]
    datatype: numpy.ndarray[numpy.int32]
    dim: numpy.ndarray[numpy.int32]
    needstage: numpy.ndarray[numpy.int32]
    noise: numpy.ndarray[numpy.float64]
    objid: numpy.ndarray[numpy.int32]
    objtype: numpy.ndarray[numpy.int32]
    refid: numpy.ndarray[numpy.int32]
    reftype: numpy.ndarray[numpy.int32]
    type: numpy.ndarray[numpy.int32]
    user: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelSiteViews:
    bodyid: numpy.ndarray[numpy.int32]
    group: numpy.ndarray[numpy.int32]
    matid: numpy.ndarray[numpy.int32]
    pos: numpy.ndarray[numpy.float64]
    quat: numpy.ndarray[numpy.float64]
    rgba: numpy.ndarray[numpy.float32]
    sameframe: numpy.ndarray[numpy.uint8]
    size: numpy.ndarray[numpy.float64]
    type: numpy.ndarray[numpy.int32]
    user: numpy.ndarray[numpy.float64]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelSkinViews:
    boneadr: numpy.ndarray[numpy.int32]
    bonenum: numpy.ndarray[numpy.int32]
    faceadr: numpy.ndarray[numpy.int32]
    facenum: numpy.ndarray[numpy.int32]
    inflate: numpy.ndarray[numpy.float32]
    matid: numpy.ndarray[numpy.int32]
    rgba: numpy.ndarray[numpy.float32]
    texcoordadr: numpy.ndarray[numpy.int32]
    vertadr: numpy.ndarray[numpy.int32]
    vertnum: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelTendonViews:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelTextureViews:
    adr: numpy.ndarray[numpy.int32]
    data: numpy.ndarray[numpy.uint8]
    height: numpy.ndarray[numpy.int32]
    nchannel: numpy.ndarray[numpy.int32]
    type: numpy.ndarray[numpy.int32]
    width: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjModelTupleViews:
    adr: numpy.ndarray[numpy.int32]
    objid: numpy.ndarray[numpy.int32]
    objprm: numpy.ndarray[numpy.float64]
    objtype: numpy.ndarray[numpy.int32]
    size: numpy.ndarray[numpy.int32]
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...

class _MjSolverStatList:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""
    @overload
    def __getitem__(self, arg0: int) -> MjSolverStat:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjSolverStatList, arg0: int) -> mujoco._structs.MjSolverStat

        2. __getitem__(self: mujoco._structs._MjSolverStatList, arg0: slice) -> mujoco._structs._MjSolverStatList
        """
    @overload
    def __getitem__(self, arg0: slice) -> _MjSolverStatList:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjSolverStatList, arg0: int) -> mujoco._structs.MjSolverStat

        2. __getitem__(self: mujoco._structs._MjSolverStatList, arg0: slice) -> mujoco._structs._MjSolverStatList
        """
    def __iter__(self) -> typing.Iterator[MjSolverStat]:
        """def __iter__(self) -> typing.Iterator[MjSolverStat]"""
    def __len__(self) -> int:
        """__len__(self: mujoco._structs._MjSolverStatList) -> int"""
    @property
    def gradient(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def improvement(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def lineslope(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def nactive(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def nchange(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def neval(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def nupdate(self) -> numpy.ndarray[numpy.int32]: ...

class _MjTimerStatList:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""
    @overload
    def __getitem__(self, arg0: int) -> MjTimerStat:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: int) -> mujoco._structs.MjTimerStat

        2. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: mujoco._enums.mjtTimer) -> mujoco._structs.MjTimerStat

        3. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: slice) -> mujoco._structs._MjTimerStatList
        """
    @overload
    def __getitem__(self, arg0: mujoco._enums.mjtTimer) -> MjTimerStat:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: int) -> mujoco._structs.MjTimerStat

        2. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: mujoco._enums.mjtTimer) -> mujoco._structs.MjTimerStat

        3. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: slice) -> mujoco._structs._MjTimerStatList
        """
    @overload
    def __getitem__(self, arg0: slice) -> _MjTimerStatList:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: int) -> mujoco._structs.MjTimerStat

        2. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: mujoco._enums.mjtTimer) -> mujoco._structs.MjTimerStat

        3. __getitem__(self: mujoco._structs._MjTimerStatList, arg0: slice) -> mujoco._structs._MjTimerStatList
        """
    def __iter__(self) -> typing.Iterator[MjTimerStat]:
        """def __iter__(self) -> typing.Iterator[MjTimerStat]"""
    def __len__(self) -> int:
        """__len__(self: mujoco._structs._MjTimerStatList) -> int"""
    @property
    def duration(self) -> numpy.ndarray[numpy.float64]: ...
    @property
    def number(self) -> numpy.ndarray[numpy.int32]: ...

class _MjWarningStatList:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: object, arg0: object) -> bool"""
    @overload
    def __getitem__(self, arg0: int) -> MjWarningStat:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: int) -> mujoco._structs.MjWarningStat

        2. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: mujoco._enums.mjtWarning) -> mujoco._structs.MjWarningStat

        3. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: slice) -> mujoco._structs._MjWarningStatList
        """
    @overload
    def __getitem__(self, arg0: mujoco._enums.mjtWarning) -> MjWarningStat:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: int) -> mujoco._structs.MjWarningStat

        2. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: mujoco._enums.mjtWarning) -> mujoco._structs.MjWarningStat

        3. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: slice) -> mujoco._structs._MjWarningStatList
        """
    @overload
    def __getitem__(self, arg0: slice) -> _MjWarningStatList:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: int) -> mujoco._structs.MjWarningStat

        2. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: mujoco._enums.mjtWarning) -> mujoco._structs.MjWarningStat

        3. __getitem__(self: mujoco._structs._MjWarningStatList, arg0: slice) -> mujoco._structs._MjWarningStatList
        """
    def __iter__(self) -> typing.Iterator[MjWarningStat]:
        """def __iter__(self) -> typing.Iterator[MjWarningStat]"""
    def __len__(self) -> int:
        """__len__(self: mujoco._structs._MjWarningStatList) -> int"""
    @property
    def lastinfo(self) -> numpy.ndarray[numpy.int32]: ...
    @property
    def number(self) -> numpy.ndarray[numpy.int32]: ...

def mjv_averageCamera(cam1: MjvGLCamera, cam2: MjvGLCamera) -> MjvGLCamera:
    """mjv_averageCamera(cam1: mujoco._structs.MjvGLCamera, cam2: mujoco._structs.MjvGLCamera) -> mujoco._structs.MjvGLCamera

    Return the average of two OpenGL cameras.
    """

# --- mujoco.gl_context ---
from _typeshed import Incomplete

GLContext: Incomplete

# --- mujoco.renderer ---
import numpy as np
from mujoco import _structs, gl_context as gl_context

class Renderer:
    """Renders MuJoCo scenes."""
    def __init__(self, model: _structs.MjModel, height: int = 240, width: int = 320, max_geom: int = 10000) -> None:
        """Initializes a new `Renderer`.

    Args:
      model: an MjModel instance.
      height: image height in pixels.
      width: image width in pixels.
      max_geom: Optional integer specifying the maximum number of geoms that can
        be rendered in the same scene. If None this will be chosen automatically
        based on the estimated maximum number of renderable geoms in the model.

    Raises:
      ValueError: If `camera_id` is outside the valid range, or if `width` or
        `height` exceed the dimensions of MuJoCo's offscreen framebuffer.
    """
    @property
    def model(self): ...
    @property
    def scene(self) -> _structs.MjvScene: ...
    @property
    def height(self): ...
    @property
    def width(self): ...
    def enable_depth_rendering(self) -> None: ...
    def disable_depth_rendering(self) -> None: ...
    def enable_segmentation_rendering(self) -> None: ...
    def disable_segmentation_rendering(self) -> None: ...
    def render(self, *, out: np.ndarray | None = None) -> np.ndarray:
        """Renders the scene as a numpy array of pixel values.

    Args:
      out: Alternative output array in which to place the resulting pixels. It
        must have the same shape as the expected output but the type will be
        cast if necessary. The expted shape depends on the value of
        `self._depth_rendering`: when `True`, we expect `out.shape == (width,
        height)`, and `out.shape == (width, height, 3)` when `False`.

    Returns:
      A new numpy array holding the pixels with shape `(H, W)` or `(H, W, 3)`,
      depending on the value of `self._depth_rendering` unless
      `out is None`, in which case a reference to `out` is returned.

    Raises:
      RuntimeError: if this method is called after the close method.
    """
    def update_scene(self, data: _structs.MjData, camera: int | str | _structs.MjvCamera = -1, scene_option: _structs.MjvOption | None = None):
        """Updates geometry used for rendering.

    Args:
      data: An instance of `MjData`.
      camera: An instance of `MjvCamera`, a string or an integer
      scene_option: A custom `MjvOption` instance to use to render the scene
        instead of the default.

    Raises:
      ValueError: If `camera_id` is outside the valid range, or if camera does
        not exist.
    """
    def close(self) -> None:
        """Frees the resources used by the renderer.

    This method can be used directly:

    ```python
    renderer = Renderer(...)
    # Use renderer.
    renderer.close()
    ```

    or via a context manager:

    ```python
    with Renderer(...) as renderer:
      # Use renderer.
    ```
    """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __del__(self) -> None: ...
