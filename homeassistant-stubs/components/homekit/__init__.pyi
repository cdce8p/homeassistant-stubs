from . import type_cameras as type_cameras, type_covers as type_covers, type_fans as type_fans, type_humidifiers as type_humidifiers, type_lights as type_lights, type_locks as type_locks, type_media_players as type_media_players, type_remotes as type_remotes, type_security_systems as type_security_systems, type_sensors as type_sensors, type_switches as type_switches, type_thermostats as type_thermostats
from .accessories import HomeAccessory as HomeAccessory, HomeBridge as HomeBridge, HomeDriver as HomeDriver, get_accessory as get_accessory
from .aidmanager import AccessoryAidStorage as AccessoryAidStorage
from .const import ATTR_INTEGRATION as ATTR_INTEGRATION, BRIDGE_NAME as BRIDGE_NAME, BRIDGE_SERIAL_NUMBER as BRIDGE_SERIAL_NUMBER, CONFIG_OPTIONS as CONFIG_OPTIONS, CONF_ADVERTISE_IP as CONF_ADVERTISE_IP, CONF_ENTITY_CONFIG as CONF_ENTITY_CONFIG, CONF_ENTRY_INDEX as CONF_ENTRY_INDEX, CONF_EXCLUDE_ACCESSORY_MODE as CONF_EXCLUDE_ACCESSORY_MODE, CONF_FILTER as CONF_FILTER, CONF_HOMEKIT_MODE as CONF_HOMEKIT_MODE, CONF_LINKED_BATTERY_CHARGING_SENSOR as CONF_LINKED_BATTERY_CHARGING_SENSOR, CONF_LINKED_BATTERY_SENSOR as CONF_LINKED_BATTERY_SENSOR, CONF_LINKED_DOORBELL_SENSOR as CONF_LINKED_DOORBELL_SENSOR, CONF_LINKED_HUMIDITY_SENSOR as CONF_LINKED_HUMIDITY_SENSOR, CONF_LINKED_MOTION_SENSOR as CONF_LINKED_MOTION_SENSOR, DEFAULT_EXCLUDE_ACCESSORY_MODE as DEFAULT_EXCLUDE_ACCESSORY_MODE, DEFAULT_HOMEKIT_MODE as DEFAULT_HOMEKIT_MODE, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, HOMEKIT as HOMEKIT, HOMEKIT_MODES as HOMEKIT_MODES, HOMEKIT_MODE_ACCESSORY as HOMEKIT_MODE_ACCESSORY, HOMEKIT_PAIRING_QR as HOMEKIT_PAIRING_QR, HOMEKIT_PAIRING_QR_SECRET as HOMEKIT_PAIRING_QR_SECRET, MANUFACTURER as MANUFACTURER, PERSIST_LOCK as PERSIST_LOCK, SERVICE_HOMEKIT_RESET_ACCESSORY as SERVICE_HOMEKIT_RESET_ACCESSORY, SERVICE_HOMEKIT_UNPAIR as SERVICE_HOMEKIT_UNPAIR, SHUTDOWN_TIMEOUT as SHUTDOWN_TIMEOUT
from .type_triggers import DeviceTriggerAccessory as DeviceTriggerAccessory
from .util import accessory_friendly_name as accessory_friendly_name, async_dismiss_setup_message as async_dismiss_setup_message, async_port_is_available as async_port_is_available, async_show_setup_message as async_show_setup_message, get_persist_fullpath_for_entry_id as get_persist_fullpath_for_entry_id, remove_state_files_for_entry_id as remove_state_files_for_entry_id, state_needs_accessory_mode as state_needs_accessory_mode, validate_entity_config as validate_entity_config
from aiohttp import web
from collections.abc import Iterable
from homeassistant.components import device_automation as device_automation, network as network, zeroconf as zeroconf
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.network.const import MDNS_TARGET_IP as MDNS_TARGET_IP
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING, ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_DEVICES as CONF_DEVICES, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized
from homeassistant.helpers import device_registry as device_registry, entity_registry as entity_registry
from homeassistant.helpers.entityfilter import BASE_FILTER_SCHEMA as BASE_FILTER_SCHEMA, EntityFilter as EntityFilter, FILTER_SCHEMA as FILTER_SCHEMA
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.service import async_extract_referenced_entity_ids as async_extract_referenced_entity_ids
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from typing import Any
from uuid import UUID
from zeroconf.asyncio import AsyncZeroconf as AsyncZeroconf

_LOGGER: Any
MAX_DEVICES: int
STATUS_READY: int
STATUS_RUNNING: int
STATUS_STOPPED: int
STATUS_WAIT: int
PORT_CLEANUP_CHECK_INTERVAL_SECS: int
_HOMEKIT_CONFIG_UPDATE_TIME: int

def _has_all_unique_names_and_ports(bridges: list[dict[str, Any]]) -> list[dict[str, Any]]: ...

BRIDGE_SCHEMA: Any
CONFIG_SCHEMA: Any
RESET_ACCESSORY_SERVICE_SCHEMA: Any
UNPAIR_SERVICE_SCHEMA: Any

def _async_all_homekit_instances(hass: HomeAssistant) -> list[HomeKit]: ...
def _async_get_entries_by_name(current_entries: list[ConfigEntry]) -> dict[str, ConfigEntry]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _async_update_config_entry_if_from_yaml(hass: HomeAssistant, entries_by_name: dict[str, ConfigEntry], conf: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def _async_import_options_from_data_if_missing(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def _async_register_events_and_services(hass: HomeAssistant) -> None: ...

class HomeKit:
    driver: HomeDriver
    hass: Any
    _name: Any
    _port: Any
    _ip_address: Any
    _filter: Any
    _config: Any
    _exclude_accessory_mode: Any
    _advertise_ip: Any
    _entry_id: Any
    _entry_title: Any
    _homekit_mode: Any
    _devices: Any
    aid_storage: Any
    status: Any
    bridge: Any
    def __init__(self, hass: HomeAssistant, name: str, port: int, ip_address: Union[str, None], entity_filter: EntityFilter, exclude_accessory_mode: bool, entity_config: dict, homekit_mode: str, advertise_ip: Union[str, None], entry_id: str, entry_title: str, devices: Union[Iterable[str], None] = ...) -> None: ...
    def setup(self, async_zeroconf_instance: AsyncZeroconf, uuid: UUID) -> None: ...
    async def async_reset_accessories(self, entity_ids: Iterable[str]) -> None: ...
    async def async_reset_accessories_in_accessory_mode(self, entity_ids: Iterable[str]) -> None: ...
    async def async_reset_accessories_in_bridge_mode(self, entity_ids: Iterable[str]) -> None: ...
    async def async_config_changed(self) -> None: ...
    def add_bridge_accessory(self, state: State) -> Union[HomeAccessory, None]: ...
    def _would_exceed_max_devices(self, name: Union[str, None]) -> bool: ...
    def add_bridge_triggers_accessory(self, device: device_registry.DeviceEntry, device_triggers: list[dict[str, Any]]) -> None: ...
    async def async_remove_bridge_accessory(self, aid: int) -> Union[HomeAccessory, None]: ...
    async def async_configure_accessories(self) -> list[State]: ...
    async def async_start(self, *args: Any) -> None: ...
    def _async_show_setup_message(self) -> None: ...
    def async_unpair(self) -> None: ...
    def _async_register_bridge(self) -> None: ...
    def _async_purge_old_bridges(self, dev_reg: device_registry.DeviceRegistry, identifier: tuple[str, str, str], connection: tuple[str, str]) -> None: ...
    def _async_create_single_accessory(self, entity_states: list[State]) -> Union[HomeAccessory, None]: ...
    async def _async_create_bridge_accessory(self, entity_states: Iterable[State]) -> HomeAccessory: ...
    async def _async_create_accessories(self) -> bool: ...
    async def async_stop(self, *args: Any) -> None: ...
    def _async_configure_linked_sensors(self, ent_reg_ent: entity_registry.RegistryEntry, device_lookup: dict[str, dict[tuple[str, Union[str, None]], str]], state: State) -> None: ...
    async def _async_set_device_info_attributes(self, ent_reg_ent: entity_registry.RegistryEntry, dev_reg: device_registry.DeviceRegistry, entity_id: str) -> None: ...
    def _fill_config_from_device_registry_entry(self, device_entry: device_registry.DeviceEntry, config: dict[str, Any]) -> None: ...

class HomeKitPairingQRView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    async def get(self, request: web.Request) -> web.Response: ...