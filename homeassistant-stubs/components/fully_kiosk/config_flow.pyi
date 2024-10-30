from .const import DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.service_info.mqtt import MqttServiceInfo as MqttServiceInfo
from typing import Any

class FullyKioskConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: str
    _discovered_device_info: Incomplete
    def __init__(self) -> None: ...
    async def _create_entry(self, host: str, user_input: dict[str, Any], errors: dict[str, str], description_placeholders: dict[str, str] | Any = None) -> ConfigFlowResult | None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_mqtt(self, discovery_info: MqttServiceInfo) -> ConfigFlowResult: ...
