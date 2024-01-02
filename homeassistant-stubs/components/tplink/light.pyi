from . import legacy_device_id as legacy_device_id
from .const import DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkEntity as CoordinatedTPLinkEntity, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from collections.abc import Sequence
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import SmartBulb, SmartLightStrip
from typing import Any, Final

_LOGGER: Incomplete
SERVICE_RANDOM_EFFECT: str
SERVICE_SEQUENCE_EFFECT: str
HUE: Incomplete
SAT: Incomplete
VAL: Incomplete
TRANSITION: Incomplete
HSV_SEQUENCE: Incomplete
BASE_EFFECT_DICT: Final[Incomplete]
SEQUENCE_EFFECT_DICT: Final[Incomplete]
RANDOM_EFFECT_DICT: Final[Incomplete]

def _async_build_base_effect(brightness: int, duration: int, transition: int, segments: list[int]) -> dict[str, Any]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkSmartBulb(CoordinatedTPLinkEntity, LightEntity):
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    device: SmartBulb
    _attr_unique_id: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, device: SmartBulb, coordinator: TPLinkDataUpdateCoordinator) -> None: ...
    def _async_extract_brightness_transition(self, **kwargs: Any) -> tuple[int | None, int | None]: ...
    async def _async_set_hsv(self, hs_color: tuple[int, int], brightness: int | None, transition: int | None) -> None: ...
    async def _async_turn_on_with_brightness(self, brightness: int | None, transition: int | None) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def min_color_temp_kelvin(self) -> int: ...
    @property
    def max_color_temp_kelvin(self) -> int: ...
    @property
    def color_temp_kelvin(self) -> int: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def hs_color(self) -> tuple[int, int] | None: ...
    @property
    def color_mode(self) -> ColorMode: ...

class TPLinkSmartLightStrip(TPLinkSmartBulb):
    device: SmartLightStrip
    _attr_supported_features: Incomplete
    @property
    def effect_list(self) -> list[str] | None: ...
    @property
    def effect(self) -> str | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_set_random_effect(self, brightness: int, duration: int, transition: int, segments: list[int], fadeoff: int, init_states: tuple[int, int, int], random_seed: int, backgrounds: Sequence[tuple[int, int, int]] | None = None, hue_range: tuple[int, int] | None = None, saturation_range: tuple[int, int] | None = None, brightness_range: tuple[int, int] | None = None, transition_range: tuple[int, int] | None = None) -> None: ...
    async def async_set_sequence_effect(self, brightness: int, duration: int, transition: int, segments: list[int], sequence: Sequence[tuple[int, int, int]], repeat_times: int, spread: int, direction: int) -> None: ...
