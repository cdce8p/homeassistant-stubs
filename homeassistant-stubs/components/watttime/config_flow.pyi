import voluptuous as vol
from .const import CONF_BALANCING_AUTHORITY as CONF_BALANCING_AUTHORITY, CONF_BALANCING_AUTHORITY_ABBREV as CONF_BALANCING_AUTHORITY_ABBREV, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONF_LOCATION_TYPE: str
LOCATION_TYPE_COORDINATES: str
LOCATION_TYPE_HOME: str
STEP_COORDINATES_DATA_SCHEMA: Any
STEP_LOCATION_DATA_SCHEMA: Any
STEP_REAUTH_CONFIRM_DATA_SCHEMA: Any
STEP_USER_DATA_SCHEMA: Any

def get_unique_id(data: dict[str, Any]) -> str: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    _client: Any
    _data: Any
    def __init__(self) -> None: ...
    async def _async_validate_credentials(self, username: str, password: str, error_step_id: str, error_schema: vol.Schema) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    async def async_step_coordinates(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_location(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, config: ConfigType) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class WattTimeOptionsFlowHandler(config_entries.OptionsFlow):
    entry: Any
    def __init__(self, entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...