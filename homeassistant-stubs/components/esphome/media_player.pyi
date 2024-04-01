from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, MediaPlayerEntityState, MediaPlayerInfo, MediaPlayerState as EspMediaPlayerState
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_STATES: EsphomeEnumMapper[EspMediaPlayerState, MediaPlayerState]

class EsphomeMediaPlayer(EsphomeEntity[MediaPlayerInfo, MediaPlayerEntityState], MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def state(self) -> MediaPlayerState | None: ...
    @property
    def is_volume_muted(self) -> bool: ...
    @property
    def volume_level(self) -> float | None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
