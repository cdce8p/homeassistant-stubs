from .const import DOMAIN as DOMAIN, TYPE_TO_PLATFORM as TYPE_TO_PLATFORM
from .entity import LookinPowerPushRemoteEntity as LookinPowerPushRemoteEntity
from .models import LookinData as LookinData
from aiolookin import Remote as Remote
from homeassistant.components.light import COLOR_MODE_ONOFF as COLOR_MODE_ONOFF, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LookinLightEntity(LookinPowerPushRemoteEntity, LightEntity):
    _attr_supported_color_modes: Any
    _attr_color_mode: Any
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update_from_status(self, status: str) -> None: ...