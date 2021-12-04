from . import TailscaleEntity as TailscaleEntity
from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tailscale import Device as TailscaleDevice

class TailscaleBinarySensorEntityDescriptionMixin:
    is_on_fn: Callable[[TailscaleDevice], Union[bool, None]]

class TailscaleBinarySensorEntityDescription(BinarySensorEntityDescription, TailscaleBinarySensorEntityDescriptionMixin): ...

BINARY_SENSORS: tuple[TailscaleBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailscaleBinarySensorEntity(TailscaleEntity, BinarySensorEntity):
    entity_description: TailscaleBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...