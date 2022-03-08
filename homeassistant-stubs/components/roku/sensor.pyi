from .const import DOMAIN as DOMAIN
from .coordinator import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .entity import RokuEntity as RokuEntity
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from rokuecp.models import Device as RokuDevice

class RokuSensorEntityDescriptionMixin:
    value_fn: Callable[[RokuDevice], Union[str, None]]
    def __init__(self, value_fn) -> None: ...

class RokuSensorEntityDescription(SensorEntityDescription, RokuSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSORS: tuple[RokuSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuSensorEntity(RokuEntity, SensorEntity):
    entity_description: RokuSensorEntityDescription
    @property
    def native_value(self) -> Union[str, None]: ...