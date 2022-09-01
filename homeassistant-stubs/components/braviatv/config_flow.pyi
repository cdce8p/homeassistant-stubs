from . import BraviaTVCoordinator as BraviaTVCoordinator
from .const import ATTR_CID as ATTR_CID, ATTR_MAC as ATTR_MAC, ATTR_MODEL as ATTR_MODEL, CLIENTID_PREFIX as CLIENTID_PREFIX, CONF_IGNORED_SOURCES as CONF_IGNORED_SOURCES, DOMAIN as DOMAIN, NICKNAME as NICKNAME
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PIN as CONF_PIN
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from pybravia import BraviaTV
from typing import Any

def host_valid(host: str) -> bool: ...

class BraviaTVConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    client: BraviaTV
    device_config: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> BraviaTVOptionsFlowHandler: ...
    async def async_init_device(self) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_authorize(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class BraviaTVOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    ignored_sources: Incomplete
    source_list: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
