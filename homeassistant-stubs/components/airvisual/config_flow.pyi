import voluptuous as vol
from . import async_get_geography_id as async_get_geography_id
from .const import CONF_CITY as CONF_CITY, CONF_COUNTRY as CONF_COUNTRY, CONF_INTEGRATION_TYPE as CONF_INTEGRATION_TYPE, DOMAIN as DOMAIN, INTEGRATION_TYPE_GEOGRAPHY_COORDS as INTEGRATION_TYPE_GEOGRAPHY_COORDS, INTEGRATION_TYPE_GEOGRAPHY_NAME as INTEGRATION_TYPE_GEOGRAPHY_NAME, INTEGRATION_TYPE_NODE_PRO as INTEGRATION_TYPE_NODE_PRO, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_PASSWORD as CONF_PASSWORD, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, CONF_STATE as CONF_STATE
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

API_KEY_DATA_SCHEMA: Incomplete
GEOGRAPHY_NAME_SCHEMA: Incomplete
NODE_PRO_SCHEMA: Incomplete
PICK_INTEGRATION_TYPE_SCHEMA: Incomplete

class AirVisualFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _entry_data_for_reauth: Incomplete
    _geo_id: Incomplete
    def __init__(self) -> None: ...
    @property
    def geography_coords_schema(self) -> vol.Schema: ...
    async def _async_finish_geography(self, user_input: dict[str, str], integration_type: str) -> FlowResult: ...
    async def _async_init_geography(self, user_input: dict[str, str], integration_type: str) -> FlowResult: ...
    async def _async_set_unique_id(self, unique_id: str) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    async def async_step_geography_by_coords(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_geography_by_name(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_node_pro(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...

class AirVisualOptionsFlowHandler(config_entries.OptionsFlow):
    entry: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
