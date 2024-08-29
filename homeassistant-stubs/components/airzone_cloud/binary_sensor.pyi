import abc
from . import AirzoneCloudConfigEntry as AirzoneCloudConfigEntry
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneAidooEntity as AirzoneAidooEntity, AirzoneEntity as AirzoneEntity, AirzoneSystemEntity as AirzoneSystemEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

@dataclass(frozen=True)
class AirzoneBinarySensorEntityDescription(BinarySensorEntityDescription):
    attributes: dict[str, str] | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., attributes=...) -> None: ...

AIDOO_BINARY_SENSOR_TYPES: Final[tuple[AirzoneBinarySensorEntityDescription, ...]]
SYSTEM_BINARY_SENSOR_TYPES: Final[tuple[AirzoneBinarySensorEntityDescription, ...]]
ZONE_BINARY_SENSOR_TYPES: Final[tuple[AirzoneBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneCloudConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneBinarySensor(AirzoneEntity, BinarySensorEntity, metaclass=abc.ABCMeta):
    entity_description: AirzoneBinarySensorEntityDescription
    @property
    def available(self) -> bool: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _async_update_attrs(self) -> None: ...

class AirzoneAidooBinarySensor(AirzoneAidooEntity, AirzoneBinarySensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneBinarySensorEntityDescription, aidoo_id: str, aidoo_data: dict[str, Any]) -> None: ...

class AirzoneSystemBinarySensor(AirzoneSystemEntity, AirzoneBinarySensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneBinarySensorEntityDescription, system_id: str, system_data: dict[str, Any]) -> None: ...

class AirzoneZoneBinarySensor(AirzoneZoneEntity, AirzoneBinarySensor):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneBinarySensorEntityDescription, zone_id: str, zone_data: dict[str, Any]) -> None: ...
