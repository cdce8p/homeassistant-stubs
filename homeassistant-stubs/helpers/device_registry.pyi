from . import entity_registry as entity_registry
from .debounce import Debouncer as Debouncer
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

DATA_REGISTRY: str
EVENT_DEVICE_REGISTRY_UPDATED: str
STORAGE_KEY: str
STORAGE_VERSION: int
SAVE_DELAY: int
CLEANUP_DELAY: int
CONNECTION_NETWORK_MAC: str
CONNECTION_UPNP: str
CONNECTION_ZIGBEE: str
IDX_CONNECTIONS: str
IDX_IDENTIFIERS: str
REGISTERED_DEVICE: str
DELETED_DEVICE: str
DISABLED_CONFIG_ENTRY: str
DISABLED_INTEGRATION: str
DISABLED_USER: str
ORPHANED_DEVICE_KEEP_SECONDS: Any

class DeviceEntry:
    config_entries: set[str] = ...
    connections: set[tuple[str, str]] = ...
    identifiers: set[tuple[str, str]] = ...
    manufacturer: Union[str, None] = ...
    model: Union[str, None] = ...
    name: Union[str, None] = ...
    sw_version: Union[str, None] = ...
    via_device_id: Union[str, None] = ...
    area_id: Union[str, None] = ...
    name_by_user: Union[str, None] = ...
    entry_type: Union[str, None] = ...
    id: str = ...
    is_new: bool = ...
    disabled_by: Union[str, None] = ...
    suggested_area: Union[str, None] = ...
    @property
    def disabled(self) -> bool: ...
    def __init__(self, config_entries: Any, connections: Any, identifiers: Any, manufacturer: Any, model: Any, name: Any, sw_version: Any, via_device_id: Any, area_id: Any, name_by_user: Any, entry_type: Any, id: Any, is_new: Any, disabled_by: Any, suggested_area: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class DeletedDeviceEntry:
    config_entries: set[str] = ...
    connections: set[tuple[str, str]] = ...
    identifiers: set[tuple[str, str]] = ...
    id: str = ...
    orphaned_timestamp: Union[float, None] = ...
    def to_device_entry(self, config_entry_id: str, connections: set[tuple[str, str]], identifiers: set[tuple[str, str]]) -> DeviceEntry: ...
    def __init__(self, config_entries: Any, connections: Any, identifiers: Any, id: Any, orphaned_timestamp: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def format_mac(mac: str) -> str: ...

class DeviceRegistry:
    devices: dict[str, DeviceEntry]
    deleted_devices: dict[str, DeletedDeviceEntry]
    hass: Any = ...
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get(self, device_id: str) -> Union[DeviceEntry, None]: ...
    def async_get_device(self, identifiers: set[tuple[str, str]], connections: Union[set[tuple[str, str]], None]=...) -> Union[DeviceEntry, None]: ...
    def async_get_or_create(self, config_entry_id: str, *, connections: Union[set[tuple[str, str]], None]=..., identifiers: Union[set[tuple[str, str]], None]=..., manufacturer: Union[str, None, UndefinedType]=..., model: Union[str, None, UndefinedType]=..., name: Union[str, None, UndefinedType]=..., default_manufacturer: Union[str, None, UndefinedType]=..., default_model: Union[str, None, UndefinedType]=..., default_name: Union[str, None, UndefinedType]=..., sw_version: Union[str, None, UndefinedType]=..., entry_type: Union[str, None, UndefinedType]=..., via_device: Union[tuple[str, str], None]=..., disabled_by: Union[str, None, UndefinedType]=..., suggested_area: Union[str, None, UndefinedType]=...) -> Union[DeviceEntry, None]: ...
    def async_update_device(self, device_id: str, *, area_id: Union[str, None, UndefinedType]=..., manufacturer: Union[str, None, UndefinedType]=..., model: Union[str, None, UndefinedType]=..., name: Union[str, None, UndefinedType]=..., name_by_user: Union[str, None, UndefinedType]=..., new_identifiers: Union[set[tuple[str, str]], UndefinedType]=..., sw_version: Union[str, None, UndefinedType]=..., via_device_id: Union[str, None, UndefinedType]=..., remove_config_entry_id: Union[str, UndefinedType]=..., disabled_by: Union[str, None, UndefinedType]=..., suggested_area: Union[str, None, UndefinedType]=...) -> Union[DeviceEntry, None]: ...
    def async_remove_device(self, device_id: str) -> None: ...
    async def async_load(self) -> None: ...
    def async_schedule_save(self) -> None: ...
    def async_clear_config_entry(self, config_entry_id: str) -> None: ...
    def async_purge_expired_orphaned_devices(self) -> None: ...
    def async_clear_area_id(self, area_id: str) -> None: ...

def async_get(hass: HomeAssistant) -> DeviceRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
async def async_get_registry(hass: HomeAssistant) -> DeviceRegistry: ...
def async_entries_for_area(registry: DeviceRegistry, area_id: str) -> list[DeviceEntry]: ...
def async_entries_for_config_entry(registry: DeviceRegistry, config_entry_id: str) -> list[DeviceEntry]: ...
def async_config_entry_disabled_by_changed(registry: DeviceRegistry, config_entry: ConfigEntry) -> None: ...
def async_cleanup(hass: HomeAssistant, dev_reg: DeviceRegistry, ent_reg: entity_registry.EntityRegistry) -> None: ...
def async_setup_cleanup(hass: HomeAssistant, dev_reg: DeviceRegistry) -> None: ...