from . import TRIGGER_BASE_SCHEMA as TRIGGER_BASE_SCHEMA
from homeassistant.components.automation import AutomationActionType as AutomationActionType
from homeassistant.components.device_automation.const import CONF_IS_OFF as CONF_IS_OFF, CONF_IS_ON as CONF_IS_ON, CONF_TOGGLE as CONF_TOGGLE, CONF_TURNED_OFF as CONF_TURNED_OFF, CONF_TURNED_ON as CONF_TURNED_ON, CONF_TURN_OFF as CONF_TURN_OFF, CONF_TURN_ON as CONF_TURN_ON
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_CONDITION as CONF_CONDITION, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FOR as CONF_FOR, CONF_PLATFORM as CONF_PLATFORM, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import condition as condition
from homeassistant.helpers.entity_registry import async_entries_for_device as async_entries_for_device
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

ENTITY_ACTIONS: Any
ENTITY_CONDITIONS: Any
ENTITY_TRIGGERS: Any
DEVICE_ACTION_TYPES: Any
ACTION_SCHEMA: Any
CONDITION_SCHEMA: Any
TRIGGER_SCHEMA: Any

async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context, domain: str) -> None: ...
def async_condition_from_config(config: ConfigType) -> condition.ConditionCheckerType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: dict) -> CALLBACK_TYPE: ...
async def async_get_actions(hass: HomeAssistant, device_id: str, domain: str) -> list[dict]: ...
async def async_get_conditions(hass: HomeAssistant, device_id: str, domain: str) -> list[dict[str, str]]: ...
async def async_get_triggers(hass: HomeAssistant, device_id: str, domain: str) -> list[dict]: ...
async def async_get_condition_capabilities(hass: HomeAssistant, config: dict) -> dict: ...
async def async_get_trigger_capabilities(hass: HomeAssistant, config: dict) -> dict: ...