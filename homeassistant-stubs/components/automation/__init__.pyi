from .config import AutomationConfig as AutomationConfig, async_validate_config_item as async_validate_config_item
from .const import CONF_ACTION as CONF_ACTION, CONF_INITIAL_STATE as CONF_INITIAL_STATE, CONF_TRACE as CONF_TRACE, CONF_TRIGGER as CONF_TRIGGER, CONF_TRIGGER_VARIABLES as CONF_TRIGGER_VARIABLES, DEFAULT_INITIAL_STATE as DEFAULT_INITIAL_STATE, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helpers import async_get_blueprints as async_get_blueprints
from .trace import trace_automation as trace_automation
from homeassistant.components import blueprint as blueprint
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODE as ATTR_MODE, ATTR_NAME as ATTR_NAME, CONF_ALIAS as CONF_ALIAS, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_ID as CONF_ID, CONF_MODE as CONF_MODE, CONF_PLATFORM as CONF_PLATFORM, CONF_VARIABLES as CONF_VARIABLES, CONF_ZONE as CONF_ZONE, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, SERVICE_RELOAD as SERVICE_RELOAD, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import Context as Context, CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import ConditionError as ConditionError, ConditionErrorContainer as ConditionErrorContainer, ConditionErrorIndex as ConditionErrorIndex, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import condition as condition, extract_domain_configs as extract_domain_configs, template as template
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.script import ATTR_CUR as ATTR_CUR, ATTR_MAX as ATTR_MAX, CONF_MAX as CONF_MAX, CONF_MAX_EXCEEDED as CONF_MAX_EXCEEDED, Script as Script
from homeassistant.helpers.script_variables import ScriptVariables as ScriptVariables
from homeassistant.helpers.service import ReloadServiceHelper as ReloadServiceHelper, async_register_admin_service as async_register_admin_service
from homeassistant.helpers.trace import TraceElement as TraceElement, script_execution_set as script_execution_set, trace_append_element as trace_append_element, trace_get as trace_get, trace_path as trace_path
from homeassistant.helpers.trigger import async_initialize_triggers as async_initialize_triggers
from homeassistant.helpers.typing import TemplateVarsType as TemplateVarsType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.dt import parse_datetime as parse_datetime
from typing import Any, Awaitable, Callable

ENTITY_ID_FORMAT: Any
CONF_SKIP_CONDITION: str
CONF_STOP_ACTIONS: str
DEFAULT_STOP_ACTIONS: bool
EVENT_AUTOMATION_RELOADED: str
EVENT_AUTOMATION_TRIGGERED: str
ATTR_LAST_TRIGGERED: str
ATTR_SOURCE: str
ATTR_VARIABLES: str
SERVICE_TRIGGER: str
_LOGGER: Any
AutomationActionType = Callable[[HomeAssistant, TemplateVarsType], Awaitable[None]]

def is_on(hass, entity_id): ...
def automations_with_entity(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def entities_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def automations_with_device(hass: HomeAssistant, device_id: str) -> list[str]: ...
def devices_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def automations_with_area(hass: HomeAssistant, area_id: str) -> list[str]: ...
def areas_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
async def async_setup(hass, config): ...

class AutomationEntity(ToggleEntity, RestoreEntity):
    _attr_should_poll: bool
    _attr_name: Any
    _trigger_config: Any
    _async_detach_triggers: Any
    _cond_func: Any
    action_script: Any
    _initial_state: Any
    _is_enabled: bool
    _referenced_entities: Any
    _referenced_devices: Any
    _logger: Any
    _variables: Any
    _trigger_variables: Any
    _raw_config: Any
    _blueprint_inputs: Any
    _trace_config: Any
    _attr_unique_id: Any
    def __init__(self, automation_id, name, trigger_config, cond_func, action_script, initial_state, variables, trigger_variables, raw_config, blueprint_inputs, trace_config) -> None: ...
    @property
    def extra_state_attributes(self): ...
    @property
    def is_on(self) -> bool: ...
    @property
    def referenced_areas(self): ...
    @property
    def referenced_devices(self): ...
    @property
    def referenced_entities(self): ...
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_trigger(self, run_variables, context: Any | None = ..., skip_condition: bool = ...) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_enable(self) -> None: ...
    async def async_disable(self, stop_actions=...) -> None: ...
    async def _async_attach_triggers(self, home_assistant_start: bool) -> Union[Callable[[], None], None]: ...

async def _async_process_config(hass: HomeAssistant, config: dict[str, Any], component: EntityComponent) -> bool: ...
async def _async_process_if(hass, name, config, p_config): ...
def _trigger_extract_device(trigger_conf: dict) -> Union[str, None]: ...
def _trigger_extract_entities(trigger_conf: dict) -> list[str]: ...
