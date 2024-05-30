from .const import BINSENSOR_PORTS as BINSENSOR_PORTS, CONF_CLIMATES as CONF_CLIMATES, CONF_CONNECTIONS as CONF_CONNECTIONS, CONF_DIM_MODE as CONF_DIM_MODE, CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, CONF_HARDWARE_SERIAL as CONF_HARDWARE_SERIAL, CONF_HARDWARE_TYPE as CONF_HARDWARE_TYPE, CONF_OUTPUT as CONF_OUTPUT, CONF_SCENES as CONF_SCENES, CONF_SK_NUM_TRIES as CONF_SK_NUM_TRIES, CONF_SOFTWARE_SERIAL as CONF_SOFTWARE_SERIAL, CONNECTION as CONNECTION, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, LED_PORTS as LED_PORTS, LOGICOP_PORTS as LOGICOP_PORTS, OUTPUT_PORTS as OUTPUT_PORTS, S0_INPUTS as S0_INPUTS, SETPOINTS as SETPOINTS, THRESHOLDS as THRESHOLDS, VARIABLES as VARIABLES
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_COVERS as CONF_COVERS, CONF_DEVICES as CONF_DEVICES, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_HOST as CONF_HOST, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_LIGHTS as CONF_LIGHTS, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_RESOURCE as CONF_RESOURCE, CONF_SENSORS as CONF_SENSORS, CONF_SOURCE as CONF_SOURCE, CONF_SWITCHES as CONF_SWITCHES, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

AddressType = tuple[int, int, bool]
DeviceConnectionType: Incomplete
InputType: Incomplete
PATTERN_ADDRESS: Incomplete
DOMAIN_LOOKUP: Incomplete

def get_device_connection(hass: HomeAssistant, address: AddressType, config_entry: ConfigEntry) -> DeviceConnectionType | None: ...
def get_resource(domain_name: str, domain_data: ConfigType) -> str: ...
def get_device_model(domain_name: str, domain_data: ConfigType) -> str: ...
def generate_unique_id(entry_id: str, address: AddressType, resource: str | None = None) -> str: ...
def import_lcn_config(lcn_config: ConfigType) -> list[ConfigType]: ...
def purge_entity_registry(hass: HomeAssistant, entry_id: str, imported_entry_data: ConfigType) -> None: ...
def purge_device_registry(hass: HomeAssistant, entry_id: str, imported_entry_data: ConfigType) -> None: ...
def register_lcn_host_device(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
def register_lcn_address_devices(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def async_update_device_config(device_connection: DeviceConnectionType, device_config: ConfigType) -> None: ...
async def async_update_config_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
def has_unique_host_names(hosts: list[ConfigType]) -> list[ConfigType]: ...
def is_address(value: str) -> tuple[AddressType, str]: ...
def is_states_string(states_string: str) -> list[str]: ...
