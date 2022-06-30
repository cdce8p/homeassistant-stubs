from . import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import CoverInfo, CoverState
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature, DEVICE_CLASSES as DEVICE_CLASSES
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeCover(EsphomeEntity[CoverInfo, CoverState], CoverEntity):
    @property
    def supported_features(self) -> int: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def assumed_state(self) -> bool: ...
    def is_closed(self) -> Union[bool, None]: ...
    def is_opening(self) -> bool: ...
    def is_closing(self) -> bool: ...
    def current_cover_position(self) -> Union[int, None]: ...
    def current_cover_tilt_position(self) -> Union[int, None]: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
