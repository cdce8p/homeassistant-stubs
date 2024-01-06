import abc
import voluptuous as vol
from .core import HomeAssistant as HomeAssistant, callback as callback
from .exceptions import HomeAssistantError as HomeAssistantError
from .helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from .helpers.frame import report as report
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable, Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Required, TypedDict

_LOGGER: Incomplete

class FlowResultType(StrEnum):
    FORM: str
    CREATE_ENTRY: str
    ABORT: str
    EXTERNAL_STEP: str
    EXTERNAL_STEP_DONE: str
    SHOW_PROGRESS: str
    SHOW_PROGRESS_DONE: str
    MENU: str

_DEPRECATED_RESULT_TYPE_FORM: Incomplete
_DEPRECATED_RESULT_TYPE_CREATE_ENTRY: Incomplete
_DEPRECATED_RESULT_TYPE_ABORT: Incomplete
_DEPRECATED_RESULT_TYPE_EXTERNAL_STEP: Incomplete
_DEPRECATED_RESULT_TYPE_EXTERNAL_STEP_DONE: Incomplete
_DEPRECATED_RESULT_TYPE_SHOW_PROGRESS: Incomplete
_DEPRECATED_RESULT_TYPE_SHOW_PROGRESS_DONE: Incomplete
_DEPRECATED_RESULT_TYPE_MENU: Incomplete
EVENT_DATA_ENTRY_FLOW_PROGRESSED: str
FLOW_NOT_COMPLETE_STEPS: Incomplete

@dataclass(slots=True)
class BaseServiceInfo: ...
class FlowError(HomeAssistantError): ...
class UnknownHandler(FlowError): ...
class UnknownFlow(FlowError): ...
class UnknownStep(FlowError): ...

class AbortFlow(FlowError):
    reason: Incomplete
    description_placeholders: Incomplete
    def __init__(self, reason: str, description_placeholders: Mapping[str, str] | None = None) -> None: ...

class FlowResult(TypedDict, total=False):
    context: dict[str, Any]
    data_schema: vol.Schema | None
    data: Mapping[str, Any]
    description_placeholders: Mapping[str, str | None] | None
    description: str | None
    errors: dict[str, str] | None
    extra: str
    flow_id: Required[str]
    handler: Required[str]
    last_step: bool | None
    menu_options: list[str] | dict[str, str]
    minor_version: int
    options: Mapping[str, Any]
    preview: str | None
    progress_action: str
    reason: str
    required: bool
    result: Any
    step_id: str
    title: str
    type: FlowResultType
    url: str
    version: int

def _async_flow_handler_to_flow_result(flows: Iterable[FlowHandler], include_uninitialized: bool) -> list[FlowResult]: ...

class FlowManager(abc.ABC, metaclass=abc.ABCMeta):
    hass: Incomplete
    _preview: Incomplete
    _progress: Incomplete
    _handler_progress_index: Incomplete
    _init_data_process_index: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @abc.abstractmethod
    async def async_create_flow(self, handler_key: str, *, context: dict[str, Any] | None = None, data: dict[str, Any] | None = None) -> FlowHandler: ...
    @abc.abstractmethod
    async def async_finish_flow(self, flow: FlowHandler, result: FlowResult) -> FlowResult: ...
    async def async_post_init(self, flow: FlowHandler, result: FlowResult) -> None: ...
    def async_has_matching_flow(self, handler: str, match_context: dict[str, Any], data: Any) -> bool: ...
    def async_get(self, flow_id: str) -> FlowResult: ...
    def async_progress(self, include_uninitialized: bool = False) -> list[FlowResult]: ...
    def async_progress_by_handler(self, handler: str, include_uninitialized: bool = False, match_context: dict[str, Any] | None = None) -> list[FlowResult]: ...
    def async_progress_by_init_data_type(self, init_data_type: type, matcher: Callable[[Any], bool], include_uninitialized: bool = False) -> list[FlowResult]: ...
    def _async_progress_by_handler(self, handler: str, match_context: dict[str, Any] | None) -> list[FlowHandler]: ...
    async def async_init(self, handler: str, *, context: dict[str, Any] | None = None, data: Any = None) -> FlowResult: ...
    async def async_configure(self, flow_id: str, user_input: dict | None = None) -> FlowResult: ...
    def async_abort(self, flow_id: str) -> None: ...
    def _async_add_flow_progress(self, flow: FlowHandler) -> None: ...
    def _async_remove_flow_from_index(self, flow: FlowHandler) -> None: ...
    def _async_remove_flow_progress(self, flow_id: str) -> None: ...
    async def _async_handle_step(self, flow: FlowHandler, step_id: str, user_input: dict | BaseServiceInfo | None) -> FlowResult: ...
    def _raise_if_step_does_not_exist(self, flow: FlowHandler, step_id: str) -> None: ...
    async def _async_setup_preview(self, flow: FlowHandler) -> None: ...

class FlowHandler:
    cur_step: FlowResult | None
    flow_id: str
    hass: HomeAssistant
    handler: str
    context: dict[str, Any]
    init_step: str
    init_data: Any
    VERSION: int
    MINOR_VERSION: int
    @property
    def source(self) -> str | None: ...
    @property
    def show_advanced_options(self) -> bool: ...
    def add_suggested_values_to_schema(self, data_schema: vol.Schema, suggested_values: Mapping[str, Any] | None) -> vol.Schema: ...
    def async_show_form(self, *, step_id: str, data_schema: vol.Schema | None = None, errors: dict[str, str] | None = None, description_placeholders: Mapping[str, str | None] | None = None, last_step: bool | None = None, preview: str | None = None) -> FlowResult: ...
    def async_create_entry(self, *, title: str | None = None, data: Mapping[str, Any], description: str | None = None, description_placeholders: Mapping[str, str] | None = None) -> FlowResult: ...
    def async_abort(self, *, reason: str, description_placeholders: Mapping[str, str] | None = None) -> FlowResult: ...
    def async_external_step(self, *, step_id: str, url: str, description_placeholders: Mapping[str, str] | None = None) -> FlowResult: ...
    def async_external_step_done(self, *, next_step_id: str) -> FlowResult: ...
    def async_show_progress(self, *, step_id: str, progress_action: str, description_placeholders: Mapping[str, str] | None = None) -> FlowResult: ...
    def async_show_progress_done(self, *, next_step_id: str) -> FlowResult: ...
    def async_show_menu(self, *, step_id: str, menu_options: list[str] | dict[str, str], description_placeholders: Mapping[str, str] | None = None) -> FlowResult: ...
    def async_remove(self) -> None: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...

def _create_abort_data(flow_id: str, handler: str, reason: str, description_placeholders: Mapping[str, str] | None = None) -> FlowResult: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
