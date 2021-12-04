from . import VelbusEntity as VelbusEntity
from .const import DOMAIN as DOMAIN
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_FLASH as ATTR_FLASH, ATTR_TRANSITION as ATTR_TRANSITION, FLASH_LONG as FLASH_LONG, FLASH_SHORT as FLASH_SHORT, LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_FLASH as SUPPORT_FLASH, SUPPORT_TRANSITION as SUPPORT_TRANSITION
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from velbusaio.channels import Button as VelbusButton, Channel as VelbusChannel, Dimmer as VelbusDimmer

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusLight(VelbusEntity, LightEntity):
    _channel: VelbusDimmer
    _attr_supported_feature: Any
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class VelbusButtonLight(VelbusEntity, LightEntity):
    _channel: VelbusButton
    _attr_entity_registry_enabled_default: bool
    _attr_supported_feature: Any
    _attr_name: Any
    def __init__(self, channel: VelbusChannel) -> None: ...
    @property
    def is_on(self) -> Any: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...