from .frame import MissingIntegrationFrame as MissingIntegrationFrame, get_integration_frame as get_integration_frame
from collections.abc import Callable as Callable
from enum import Enum
from homeassistant.core import HomeAssistant as HomeAssistant, async_get_hass as async_get_hass
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from typing import Any, NamedTuple, ParamSpec, TypeVar

_ObjectT = TypeVar('_ObjectT', bound=object)
_R = TypeVar('_R')
_P = ParamSpec('_P')

def deprecated_substitute(substitute_name: str) -> Callable[[Callable[[_ObjectT], Any]], Callable[[_ObjectT], Any]]: ...
def get_deprecated(config: dict[str, Any], new_name: str, old_name: str, default: Any | None = None) -> Any | None: ...
def deprecated_class(replacement: str, *, breaks_in_ha_version: str | None = None) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...
def deprecated_function(replacement: str, *, breaks_in_ha_version: str | None = None) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...
def _print_deprecation_warning(obj: Any, replacement: str, description: str, verb: str, breaks_in_ha_version: str | None) -> None: ...
def _print_deprecation_warning_internal(obj_name: str, module_name: str, replacement: str, description: str, verb: str, breaks_in_ha_version: str | None, *, log_when_no_integration_is_found: bool) -> None: ...

class DeprecatedConstant(NamedTuple):
    value: Any
    replacement: str
    breaks_in_ha_version: str | None

class DeprecatedConstantEnum(NamedTuple):
    enum: Enum
    breaks_in_ha_version: str | None

_PREFIX_DEPRECATED: str

def check_if_deprecated_constant(name: str, module_globals: dict[str, Any]) -> Any: ...
def dir_with_deprecated_constants(module_globals: dict[str, Any]) -> list[str]: ...
