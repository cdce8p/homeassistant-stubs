from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import SensiboDevice as SensiboDevice

PARALLEL_UPDATES: int

class DeviceBaseEntityDescriptionMixin:
    value_version: Callable[[SensiboDevice], Union[str, None]]
    value_available: Callable[[SensiboDevice], Union[str, None]]
    def __init__(self, value_version, value_available) -> None: ...

class SensiboDeviceUpdateEntityDescription(UpdateEntityDescription, DeviceBaseEntityDescriptionMixin):
    def __init__(self, value_version, value_available, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

DEVICE_SENSOR_TYPES: tuple[SensiboDeviceUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboDeviceUpdate(SensiboDeviceBaseEntity, UpdateEntity):
    entity_description: SensiboDeviceUpdateEntityDescription
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_title: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboDeviceUpdateEntityDescription) -> None: ...
    @property
    def installed_version(self) -> Union[str, None]: ...
    @property
    def latest_version(self) -> Union[str, None]: ...