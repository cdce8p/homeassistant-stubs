from . import BangOlufsenData as BangOlufsenData
from .const import BANG_OLUFSEN_STATES as BANG_OLUFSEN_STATES, BangOlufsenMediaType as BangOlufsenMediaType, BangOlufsenSource as BangOlufsenSource, CONF_BEOLINK_JID as CONF_BEOLINK_JID, CONNECTION_STATUS as CONNECTION_STATUS, DOMAIN as DOMAIN, FALLBACK_SOURCES as FALLBACK_SOURCES, HIDDEN_SOURCE_IDS as HIDDEN_SOURCE_IDS, VALID_MEDIA_TYPES as VALID_MEDIA_TYPES, WebsocketNotification as WebsocketNotification
from .entity import BangOlufsenEntity as BangOlufsenEntity
from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import ATTR_MEDIA_EXTRA as ATTR_MEDIA_EXTRA, BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from mozart_api.models import PlaybackContentMetadata as PlaybackContentMetadata, PlaybackError as PlaybackError, PlaybackProgress, RenderingState as RenderingState, Source, VolumeState as VolumeState
from mozart_api.mozart_client import MozartClient as MozartClient
from typing import Any

_LOGGER: Incomplete
BANG_OLUFSEN_FEATURES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BangOlufsenMediaPlayer(BangOlufsenEntity, MediaPlayerEntity):
    _attr_icon: str
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features = BANG_OLUFSEN_FEATURES
    _beolink_jid: Incomplete
    _model: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _audio_sources: Incomplete
    _media_image: Incomplete
    _software_status: Incomplete
    _sources: Incomplete
    _state: Incomplete
    _video_sources: Incomplete
    def __init__(self, entry: ConfigEntry, client: MozartClient) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _volume: Incomplete
    _playback_metadata: Incomplete
    _playback_progress: Incomplete
    _source_change: Incomplete
    _playback_state: Incomplete
    _attr_media_position_updated_at: Incomplete
    _attr_source_list: Incomplete
    async def _initialize(self) -> None: ...
    async def _async_update_sources(self) -> None: ...
    def _async_update_playback_metadata(self, data: PlaybackContentMetadata) -> None: ...
    def _async_update_playback_error(self, data: PlaybackError) -> None: ...
    def _async_update_playback_progress(self, data: PlaybackProgress) -> None: ...
    def _async_update_playback_state(self, data: RenderingState) -> None: ...
    def _async_update_source_change(self, data: Source) -> None: ...
    def _async_update_volume(self, data: VolumeState) -> None: ...
    @property
    def state(self) -> MediaPlayerState: ...
    @property
    def volume_level(self) -> float | None: ...
    @property
    def is_volume_muted(self) -> bool | None: ...
    @property
    def media_content_type(self) -> str: ...
    @property
    def media_duration(self) -> int | None: ...
    @property
    def media_position(self) -> int | None: ...
    @property
    def media_image_url(self) -> str | None: ...
    @property
    def media_image_remotely_accessible(self) -> bool: ...
    @property
    def media_title(self) -> str | None: ...
    @property
    def media_album_name(self) -> str | None: ...
    @property
    def media_album_artist(self) -> str | None: ...
    @property
    def media_track(self) -> int | None: ...
    @property
    def media_channel(self) -> str | None: ...
    @property
    def source(self) -> str | None: ...
    async def async_turn_off(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_seek(self, position: float) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_clear_playlist(self) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, announce: bool | None = None, **kwargs: Any) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
