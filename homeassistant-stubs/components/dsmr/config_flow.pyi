from .const import CONF_DSMR_VERSION as CONF_DSMR_VERSION, CONF_SERIAL_ID as CONF_SERIAL_ID, CONF_SERIAL_ID_GAS as CONF_SERIAL_ID_GAS, CONF_TIME_BETWEEN_UPDATE as CONF_TIME_BETWEEN_UPDATE, DEFAULT_TIME_BETWEEN_UPDATE as DEFAULT_TIME_BETWEEN_UPDATE, DOMAIN as DOMAIN, DSMR_VERSIONS as DSMR_VERSIONS, LOGGER as LOGGER
from dsmr_parser.objects import DSMRObject as DSMRObject
from homeassistant import config_entries as config_entries, core as core, exceptions as exceptions
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONF_MANUAL_PATH: str

class DSMRConnection:
    _host: Any
    _port: Any
    _dsmr_version: Any
    _telegram: Any
    _equipment_identifier: Any
    def __init__(self, host: Union[str, None], port: int, dsmr_version: str) -> None: ...
    def equipment_identifier(self) -> Union[str, None]: ...
    def equipment_identifier_gas(self) -> Union[str, None]: ...
    async def validate_connect(self, hass: core.HomeAssistant) -> bool: ...

async def _validate_dsmr_connection(hass: core.HomeAssistant, data: dict[str, Any]) -> dict[str, Union[str, None]]: ...

class DSMRFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _dsmr_version: Union[str, None]
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> DSMROptionFlowHandler: ...
    def _abort_if_host_port_configured(self, port: str, host: Union[str, None] = ..., updates: Union[dict[Any, Any], None] = ..., reload_on_update: bool = ...) -> Union[FlowResult, None]: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_setup_network(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_setup_serial(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_setup_serial_manual_path(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_validate_dsmr(self, input_data: dict[str, Any], errors: dict[str, str]) -> dict[str, Any]: ...
    async def async_step_import(self, import_config: ConfigType) -> FlowResult: ...

class DSMROptionFlowHandler(config_entries.OptionsFlow):
    entry: Any
    def __init__(self, entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

def get_serial_by_id(dev_path: str) -> str: ...

class CannotConnect(exceptions.HomeAssistantError): ...
class CannotCommunicate(exceptions.HomeAssistantError): ...