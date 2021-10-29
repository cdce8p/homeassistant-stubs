from . import Trackables as Trackables
from .const import ATTR_DAILY_GOAL as ATTR_DAILY_GOAL, ATTR_MINUTES_ACTIVE as ATTR_MINUTES_ACTIVE, CLIENT as CLIENT, DOMAIN as DOMAIN, SERVER_UNAVAILABLE as SERVER_UNAVAILABLE, TRACKABLES as TRACKABLES, TRACKER_ACTIVITY_STATUS_UPDATED as TRACKER_ACTIVITY_STATUS_UPDATED, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC, PERCENTAGE as PERCENTAGE, TIME_MINUTES as TIME_MINUTES
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class TractiveRequiredKeysMixin:
    entity_class: type[TractiveSensor]

class TractiveSensorEntityDescription(SensorEntityDescription, TractiveRequiredKeysMixin): ...

class TractiveSensor(TractiveEntity, SensorEntity):
    _attr_name: Any
    _attr_unique_id: Any
    entity_description: Any
    def __init__(self, user_id: str, item: Trackables, description: TractiveSensorEntityDescription) -> None: ...
    _attr_available: bool
    def handle_server_unavailable(self) -> None: ...

class TractiveHardwareSensor(TractiveSensor):
    _attr_native_value: Any
    _attr_available: bool
    def handle_hardware_status_update(self, event: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class TractiveActivitySensor(TractiveSensor):
    _attr_native_value: Any
    _attr_available: bool
    def handle_activity_status_update(self, event: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...

SENSOR_TYPES: tuple[TractiveSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...