from _typeshed import Incomplete
from dataclasses import dataclass
from enum import IntFlag, StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_CLOSE_VALVE as SERVICE_CLOSE_VALVE, SERVICE_OPEN_VALVE as SERVICE_OPEN_VALVE, SERVICE_SET_VALVE_POSITION as SERVICE_SET_VALVE_POSITION, SERVICE_STOP_VALVE as SERVICE_STOP_VALVE, SERVICE_TOGGLE as SERVICE_TOGGLE, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete

class ValveDeviceClass(StrEnum):
    WATER: str
    GAS: str

DEVICE_CLASSES_SCHEMA: Incomplete

class ValveEntityFeature(IntFlag):
    OPEN: int
    CLOSE: int
    SET_POSITION: int
    STOP: int

ATTR_CURRENT_POSITION: str
ATTR_POSITION: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class ValveEntityDescription(EntityDescription):
    device_class: ValveDeviceClass | None = ...
    reports_position: bool = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, reports_position) -> None: ...

class ValveEntity(Entity):
    entity_description: ValveEntityDescription
    _attr_current_valve_position: int | None
    _attr_device_class: ValveDeviceClass | None
    _attr_is_closed: bool | None
    _attr_is_closing: bool | None
    _attr_is_opening: bool | None
    _attr_reports_position: bool
    _attr_supported_features: ValveEntityFeature
    __is_last_toggle_direction_open: bool
    @property
    def reports_position(self) -> bool: ...
    @property
    def current_valve_position(self) -> int | None: ...
    @property
    def device_class(self) -> ValveDeviceClass | None: ...
    @property
    def state(self) -> str | None: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @property
    def supported_features(self) -> ValveEntityFeature: ...
    @property
    def is_opening(self) -> bool | None: ...
    @property
    def is_closing(self) -> bool | None: ...
    @property
    def is_closed(self) -> bool | None: ...
    def open_valve(self) -> None: ...
    async def async_open_valve(self) -> None: ...
    async def async_handle_open_valve(self) -> None: ...
    def close_valve(self) -> None: ...
    async def async_close_valve(self) -> None: ...
    async def async_handle_close_valve(self) -> None: ...
    async def async_toggle(self) -> None: ...
    def set_valve_position(self, position: int) -> None: ...
    async def async_set_valve_position(self, position: int) -> None: ...
    def stop_valve(self) -> None: ...
    async def async_stop_valve(self) -> None: ...
