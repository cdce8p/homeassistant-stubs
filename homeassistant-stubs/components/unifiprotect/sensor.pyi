from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import EventThumbnailMixin as EventThumbnailMixin, ProtectDeviceEntity as ProtectDeviceEntity, ProtectNVREntity as ProtectNVREntity, async_all_device_entities as async_all_device_entities
from .models import ProtectRequiredKeysMixin as ProtectRequiredKeysMixin, T as T
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DATA_BYTES as DATA_BYTES, DATA_RATE_BYTES_PER_SECOND as DATA_RATE_BYTES_PER_SECOND, DATA_RATE_MEGABITS_PER_SECOND as DATA_RATE_MEGABITS_PER_SECOND, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, TEMP_CELSIUS as TEMP_CELSIUS, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Camera as Camera, Event as Event, NVR, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectDeviceModel, Sensor
from typing import Any

_LOGGER: Any
OBJECT_TYPE_NONE: str
DEVICE_CLASS_DETECTION: str

class ProtectSensorEntityDescription(ProtectRequiredKeysMixin, SensorEntityDescription):
    precision: Union[int, None]
    def get_ufp_value(self, obj: ProtectDeviceModel) -> Any: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, precision) -> None: ...

def _get_uptime(obj: ProtectDeviceModel) -> Union[datetime, None]: ...
def _get_nvr_recording_capacity(obj: NVR) -> int: ...
def _get_nvr_memory(obj: NVR) -> Union[float, None]: ...
def _get_alarm_sound(obj: Sensor) -> str: ...

ALL_DEVICES_SENSORS: tuple[ProtectSensorEntityDescription, ...]
CAMERA_SENSORS: tuple[ProtectSensorEntityDescription, ...]
CAMERA_DISABLED_SENSORS: tuple[ProtectSensorEntityDescription, ...]
SENSE_SENSORS: tuple[ProtectSensorEntityDescription, ...]
DOORLOCK_SENSORS: tuple[ProtectSensorEntityDescription, ...]
NVR_SENSORS: tuple[ProtectSensorEntityDescription, ...]
NVR_DISABLED_SENSORS: tuple[ProtectSensorEntityDescription, ...]
MOTION_SENSORS: tuple[ProtectSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _async_motion_entities(data: ProtectData) -> list[ProtectDeviceEntity]: ...
def _async_nvr_entities(data: ProtectData) -> list[ProtectDeviceEntity]: ...

class ProtectDeviceSensor(ProtectDeviceEntity, SensorEntity):
    entity_description: ProtectSensorEntityDescription
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel, description: ProtectSensorEntityDescription) -> None: ...
    _attr_native_value: Any
    def _async_update_device_from_protect(self) -> None: ...

class ProtectNVRSensor(ProtectNVREntity, SensorEntity):
    entity_description: ProtectSensorEntityDescription
    def __init__(self, data: ProtectData, device: NVR, description: ProtectSensorEntityDescription) -> None: ...
    _attr_native_value: Any
    def _async_update_device_from_protect(self) -> None: ...

class ProtectEventSensor(ProtectDeviceSensor, EventThumbnailMixin):
    device: Camera
    def _async_get_event(self) -> Union[Event, None]: ...
    _attr_native_value: Any
    def _async_update_device_from_protect(self) -> None: ...