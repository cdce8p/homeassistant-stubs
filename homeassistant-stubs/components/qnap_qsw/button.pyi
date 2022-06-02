from .const import DOMAIN as DOMAIN, QSW_REBOOT as QSW_REBOOT
from .coordinator import QswUpdateCoordinator as QswUpdateCoordinator
from .entity import QswEntity as QswEntity
from _typeshed import Incomplete
from aioqsw.localapi import QnapQswApi as QnapQswApi
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

class QswButtonDescriptionMixin:
    press_action: Callable[[QnapQswApi], Awaitable[bool]]
    def __init__(self, press_action) -> None: ...

class QswButtonDescription(ButtonEntityDescription, QswButtonDescriptionMixin):
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement) -> None: ...

BUTTON_TYPES: Final[tuple[QswButtonDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class QswButton(QswEntity, ButtonEntity):
    entity_description: QswButtonDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QswUpdateCoordinator, description: QswButtonDescription, entry: ConfigEntry) -> None: ...
    async def async_press(self) -> None: ...