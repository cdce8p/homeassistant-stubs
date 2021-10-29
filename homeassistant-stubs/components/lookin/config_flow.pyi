from .const import DOMAIN as DOMAIN
from aiolookin import Device as Device
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

LOGGER: Any

class LookinFlowHandler(config_entries.ConfigFlow):
    _host: Any
    _name: Any
    def __init__(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _validate_device(self, host: str) -> Device: ...
    async def async_step_discovery_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...