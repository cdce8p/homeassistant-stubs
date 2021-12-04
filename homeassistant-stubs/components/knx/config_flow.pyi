from .const import CONF_KNX_AUTOMATIC as CONF_KNX_AUTOMATIC, CONF_KNX_CONNECTION_TYPE as CONF_KNX_CONNECTION_TYPE, CONF_KNX_INDIVIDUAL_ADDRESS as CONF_KNX_INDIVIDUAL_ADDRESS, CONF_KNX_INITIAL_CONNECTION_TYPES as CONF_KNX_INITIAL_CONNECTION_TYPES, CONF_KNX_ROUTING as CONF_KNX_ROUTING, CONF_KNX_TUNNELING as CONF_KNX_TUNNELING, DOMAIN as DOMAIN
from .schema import ConnectionSchema as ConnectionSchema
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any, Final
from xknx.io.gateway_scanner import GatewayDescriptor as GatewayDescriptor

CONF_KNX_GATEWAY: Final[str]
CONF_MAX_RATE_LIMIT: Final[int]
DEFAULT_ENTRY_DATA: Final[Any]

class FlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _tunnels: list
    _gateway_ip: str
    _gateway_port: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> KNXOptionsFlowHandler: ...
    async def async_step_user(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_type(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_manual_tunnel(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_tunnel(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_routing(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_import(self, config: Union[dict, None] = ...) -> FlowResult: ...

class KNXOptionsFlowHandler(OptionsFlow):
    general_settings: dict
    current_config: dict
    config_entry: Any
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_tunnel(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

async def scan_for_gateways(stop_on_found: int = ...) -> list: ...