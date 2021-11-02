from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.components.dhcp import IP_ADDRESS as IP_ADDRESS, MAC_ADDRESS as MAC_ADDRESS
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any

class GoalZeroFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    ip_address: Any
    def __init__(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_try_connect(self, host: str) -> tuple[Union[str, None], Union[str, None]]: ...
