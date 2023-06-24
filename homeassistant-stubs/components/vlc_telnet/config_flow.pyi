import voluptuous as vol
from .const import DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiovlc.client import Client
from collections.abc import Mapping
from homeassistant import core as core, exceptions as exceptions
from homeassistant.components.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

_LOGGER: Incomplete

def user_form_schema(user_input: dict[str, Any] | None) -> vol.Schema: ...

STEP_REAUTH_DATA_SCHEMA: Incomplete

async def vlc_connect(vlc: Client) -> None: ...
async def validate_input(hass: core.HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class VLCTelnetConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    entry: ConfigEntry | None
    hassio_discovery: dict[str, Any] | None
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> FlowResult: ...
    async def async_step_hassio_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class CannotConnect(exceptions.HomeAssistantError): ...
class InvalidAuth(exceptions.HomeAssistantError): ...
