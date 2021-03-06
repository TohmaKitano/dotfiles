import sys
from typing import Any, Tuple

DEBUG_COLLECTABLE: int
DEBUG_LEAK: int
DEBUG_SAVEALL: int
DEBUG_STATS: int
DEBUG_UNCOLLECTABLE: int
callbacks: list[Any]
garbage: list[Any]

def collect(generation: int = ...) -> int: ...
def disable() -> None: ...
def enable() -> None: ...
def get_count() -> Tuple[int, int, int]: ...
def get_debug() -> int: ...

if sys.version_info >= (3, 8):
    def get_objects(generation: int | None = ...) -> list[Any]: ...

else:
    def get_objects() -> list[Any]: ...

if sys.version_info >= (3, 7):
    def freeze() -> None: ...
    def unfreeze() -> None: ...
    def get_freeze_count() -> int: ...

def get_referents(*objs: Any) -> list[Any]: ...
def get_referrers(*objs: Any) -> list[Any]: ...
def get_stats() -> list[dict[str, Any]]: ...
def get_threshold() -> Tuple[int, int, int]: ...
def is_tracked(__obj: Any) -> bool: ...

if sys.version_info >= (3, 9):
    def is_finalized(__obj: Any) -> bool: ...

def isenabled() -> bool: ...
def set_debug(__flags: int) -> None: ...
def set_threshold(threshold0: int, threshold1: int = ..., threshold2: int = ...) -> None: ...
