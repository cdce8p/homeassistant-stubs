from . import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import LightColorCapability, LightInfo, LightState
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE as ATTR_WHITE, ColorMode as ColorMode, FLASH_LONG as FLASH_LONG, FLASH_SHORT as FLASH_SHORT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

FLASH_LENGTHS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_COLOR_MODE_MAPPING: Incomplete

def _color_mode_to_ha(mode: int) -> str: ...
def _filter_color_modes(supported: list[int], features: LightColorCapability) -> list[int]: ...

class EsphomeLight(EsphomeEntity[LightInfo, LightState], LightEntity):
    @property
    def _supports_color_mode(self) -> bool: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    @property
    def color_mode(self) -> Union[str, None]: ...
    @property
    def rgb_color(self) -> Union[tuple[int, int, int], None]: ...
    @property
    def rgbw_color(self) -> Union[tuple[int, int, int, int], None]: ...
    @property
    def rgbww_color(self) -> Union[tuple[int, int, int, int, int], None]: ...
    @property
    def color_temp(self) -> int: ...
    @property
    def effect(self) -> Union[str, None]: ...
    @property
    def _native_supported_color_modes(self) -> list[int]: ...
    @property
    def supported_features(self) -> LightEntityFeature: ...
    @property
    def supported_color_modes(self) -> Union[set[str], None]: ...
    @property
    def effect_list(self) -> list[str]: ...
    @property
    def min_mireds(self) -> int: ...
    @property
    def max_mireds(self) -> int: ...
