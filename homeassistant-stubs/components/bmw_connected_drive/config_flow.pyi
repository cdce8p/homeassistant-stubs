from . import DOMAIN as DOMAIN
from .const import CONF_ALLOWED_REGIONS as CONF_ALLOWED_REGIONS, CONF_READ_ONLY as CONF_READ_ONLY, CONF_USE_LOCATION as CONF_USE_LOCATION
from homeassistant import config_entries as config_entries, core as core, exceptions as exceptions
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_REGION as CONF_REGION, CONF_SOURCE as CONF_SOURCE, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA: Any

async def validate_input(hass: core.HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class BMWConnectedDriveConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> BMWConnectedDriveOptionsFlow: ...

class BMWConnectedDriveOptionsFlow(config_entries.OptionsFlow):
    config_entry: Any
    options: Any
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_account_options(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class CannotConnect(exceptions.HomeAssistantError): ...