import datetime
from .const import DATA_SONOS as DATA_SONOS, MEDIA_TYPES_TO_SONOS as MEDIA_TYPES_TO_SONOS, PLAYABLE_MEDIA_TYPES as PLAYABLE_MEDIA_TYPES, SONOS_CREATE_MEDIA_PLAYER as SONOS_CREATE_MEDIA_PLAYER, SONOS_STATE_PLAYING as SONOS_STATE_PLAYING, SONOS_STATE_TRANSITIONING as SONOS_STATE_TRANSITIONING, SOURCE_LINEIN as SOURCE_LINEIN, SOURCE_TV as SOURCE_TV
from .entity import SonosEntity as SonosEntity
from .helpers import soco_error as soco_error
from .media_browser import build_item_response as build_item_response, get_media as get_media, library_payload as library_payload
from .speaker import SonosMedia as SonosMedia, SonosSpeaker as SonosSpeaker
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity
from homeassistant.components.media_player.const import ATTR_MEDIA_ENQUEUE as ATTR_MEDIA_ENQUEUE, MEDIA_TYPE_ALBUM as MEDIA_TYPE_ALBUM, MEDIA_TYPE_ARTIST as MEDIA_TYPE_ARTIST, MEDIA_TYPE_MUSIC as MEDIA_TYPE_MUSIC, MEDIA_TYPE_PLAYLIST as MEDIA_TYPE_PLAYLIST, MEDIA_TYPE_TRACK as MEDIA_TYPE_TRACK, REPEAT_MODE_ALL as REPEAT_MODE_ALL, REPEAT_MODE_OFF as REPEAT_MODE_OFF, REPEAT_MODE_ONE as REPEAT_MODE_ONE, SUPPORT_BROWSE_MEDIA as SUPPORT_BROWSE_MEDIA, SUPPORT_CLEAR_PLAYLIST as SUPPORT_CLEAR_PLAYLIST, SUPPORT_NEXT_TRACK as SUPPORT_NEXT_TRACK, SUPPORT_PAUSE as SUPPORT_PAUSE, SUPPORT_PLAY as SUPPORT_PLAY, SUPPORT_PLAY_MEDIA as SUPPORT_PLAY_MEDIA, SUPPORT_PREVIOUS_TRACK as SUPPORT_PREVIOUS_TRACK, SUPPORT_REPEAT_SET as SUPPORT_REPEAT_SET, SUPPORT_SEEK as SUPPORT_SEEK, SUPPORT_SELECT_SOURCE as SUPPORT_SELECT_SOURCE, SUPPORT_SHUFFLE_SET as SUPPORT_SHUFFLE_SET, SUPPORT_STOP as SUPPORT_STOP, SUPPORT_VOLUME_MUTE as SUPPORT_VOLUME_MUTE, SUPPORT_VOLUME_SET as SUPPORT_VOLUME_SET
from homeassistant.components.media_player.errors import BrowseError as BrowseError
from homeassistant.components.plex.const import PLEX_URI_SCHEME as PLEX_URI_SCHEME
from homeassistant.components.plex.services import play_on_sonos as play_on_sonos
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TIME as ATTR_TIME, STATE_IDLE as STATE_IDLE, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import entity_platform as entity_platform, service as service
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.network import is_internal_request as is_internal_request
from typing import Any

_LOGGER: Any
SUPPORT_SONOS: Any
VOLUME_INCREMENT: int
REPEAT_TO_SONOS: Any
SONOS_TO_REPEAT: Any
ATTR_SONOS_GROUP: str
UPNP_ERRORS_TO_IGNORE: Any
SERVICE_JOIN: str
SERVICE_UNJOIN: str
SERVICE_SNAPSHOT: str
SERVICE_RESTORE: str
SERVICE_SET_TIMER: str
SERVICE_CLEAR_TIMER: str
SERVICE_UPDATE_ALARM: str
SERVICE_SET_OPTION: str
SERVICE_PLAY_QUEUE: str
SERVICE_REMOVE_FROM_QUEUE: str
ATTR_SLEEP_TIME: str
ATTR_ALARM_ID: str
ATTR_VOLUME: str
ATTR_ENABLED: str
ATTR_INCLUDE_LINKED_ZONES: str
ATTR_MASTER: str
ATTR_WITH_GROUP: str
ATTR_QUEUE_POSITION: str
ATTR_EQ_BASS: str
ATTR_EQ_TREBLE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SonosMediaPlayerEntity(SonosEntity, MediaPlayerEntity):
    @property
    def coordinator(self) -> SonosSpeaker: ...
    @property
    def unique_id(self) -> str: ...
    def __hash__(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> str: ...
    async def _async_poll(self) -> None: ...
    def _update(self) -> None: ...
    @property
    def volume_level(self) -> Union[float, None]: ...
    @property
    def is_volume_muted(self) -> Union[bool, None]: ...
    @property
    def shuffle(self) -> Union[str, None]: ...
    @property
    def repeat(self) -> Union[str, None]: ...
    @property
    def media(self) -> SonosMedia: ...
    @property
    def media_content_id(self) -> Union[str, None]: ...
    @property
    def media_content_type(self) -> str: ...
    @property
    def media_duration(self) -> Union[float, None]: ...
    @property
    def media_position(self) -> Union[float, None]: ...
    @property
    def media_position_updated_at(self) -> Union[datetime.datetime, None]: ...
    @property
    def media_image_url(self) -> Union[str, None]: ...
    @property
    def media_channel(self) -> Union[str, None]: ...
    @property
    def media_playlist(self) -> Union[str, None]: ...
    @property
    def media_artist(self) -> Union[str, None]: ...
    @property
    def media_album_name(self) -> Union[str, None]: ...
    @property
    def media_title(self) -> Union[str, None]: ...
    @property
    def source(self) -> Union[str, None]: ...
    @property
    def supported_features(self) -> int: ...
    def volume_up(self) -> None: ...
    def volume_down(self) -> None: ...
    def set_volume_level(self, volume: str) -> None: ...
    def set_shuffle(self, shuffle: str) -> None: ...
    def set_repeat(self, repeat: str) -> None: ...
    def mute_volume(self, mute: bool) -> None: ...
    def select_source(self, source: str) -> None: ...
    @property
    def source_list(self) -> list[str]: ...
    def media_play(self) -> None: ...
    def media_stop(self) -> None: ...
    def media_pause(self) -> None: ...
    def media_next_track(self) -> None: ...
    def media_previous_track(self) -> None: ...
    def media_seek(self, position: str) -> None: ...
    def clear_playlist(self) -> None: ...
    def play_media(self, media_type: str, media_id: str, **kwargs: Any) -> None: ...
    def set_sleep_timer(self, sleep_time: int) -> None: ...
    def clear_sleep_timer(self) -> None: ...
    def set_alarm(self, alarm_id: int, time: Union[datetime.datetime, None] = ..., volume: Union[float, None] = ..., enabled: Union[bool, None] = ..., include_linked_zones: Union[bool, None] = ...) -> None: ...
    def set_option(self, bass_level: Union[int, None] = ..., treble_level: Union[int, None] = ...) -> None: ...
    def play_queue(self, queue_position: int = ...) -> None: ...
    def remove_from_queue(self, queue_position: int = ...) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_get_browse_image(self, media_content_type: Union[str, None], media_content_id: Union[str, None], media_image_id: Union[str, None] = ...) -> tuple[Union[None, str], Union[None, str]]: ...
    async def async_browse_media(self, media_content_type: Union[str, None] = ..., media_content_id: Union[str, None] = ...) -> Any: ...
