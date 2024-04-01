import voluptuous as vol
from .const import CONF_DEVICE_TOKEN as CONF_DEVICE_TOKEN, CONF_SNAPSHOT_QUALITY as CONF_SNAPSHOT_QUALITY, CONF_VOLUMES as CONF_VOLUMES, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_PORT_SSL as DEFAULT_PORT_SSL, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_SNAPSHOT_QUALITY as DEFAULT_SNAPSHOT_QUALITY, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DEFAULT_USE_SSL as DEFAULT_USE_SSL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import ssdp as ssdp, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_DISKS as CONF_DISKS, CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_SSL as CONF_SSL, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from synology_dsm import SynologyDSM
from typing import Any

_LOGGER: Incomplete
CONF_OTP_CODE: str
HTTP_SUFFIX: str

def _discovery_schema_with_defaults(discovery_info: DiscoveryInfoType) -> vol.Schema: ...
def _reauth_schema() -> vol.Schema: ...
def _user_schema_with_defaults(user_input: dict[str, Any]) -> vol.Schema: ...
def _ordered_shared_schema(schema_input: dict[str, Any]) -> dict[vol.Required | vol.Optional, Any]: ...
def format_synology_mac(mac: str) -> str: ...

class SynologyDSMFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> SynologyDSMOptionsFlowHandler: ...
    saved_user_input: Incomplete
    discovered_conf: Incomplete
    reauth_conf: Incomplete
    reauth_reason: Incomplete
    def __init__(self) -> None: ...
    def _show_form(self, step_id: str, user_input: dict[str, Any] | None = None, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_validate_input_create_entry(self, user_input: dict[str, Any], step_id: str) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def _async_from_discovery(self, host: str, friendly_name: str, discovered_macs: list[str]) -> ConfigFlowResult: ...
    async def async_step_link(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_2sa(self, user_input: dict[str, Any], errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    def _async_get_existing_entry(self, discovered_mac: str) -> ConfigEntry | None: ...

class SynologyDSMOptionsFlowHandler(OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

async def _login_and_fetch_syno_info(api: SynologyDSM, otp_code: str | None) -> str: ...

class InvalidData(HomeAssistantError): ...
