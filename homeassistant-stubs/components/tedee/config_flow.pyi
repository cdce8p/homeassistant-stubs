from .const import CONF_LOCAL_ACCESS_TOKEN as CONF_LOCAL_ACCESS_TOKEN, DOMAIN as DOMAIN, NAME as NAME
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class TedeeConfigFlow(ConfigFlow, domain=DOMAIN):
    reauth_entry: ConfigEntry | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
