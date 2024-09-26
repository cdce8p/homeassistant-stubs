from . import SqueezeboxConfigEntry as SqueezeboxConfigEntry
from .browse_media import build_item_response as build_item_response, generate_playlist as generate_playlist, library_payload as library_payload, media_source_content_filter as media_source_content_filter
from .const import DISCOVERY_TASK as DISCOVERY_TASK, DOMAIN as DOMAIN, KNOWN_PLAYERS as KNOWN_PLAYERS, SQUEEZEBOX_SOURCE_STRINGS as SQUEEZEBOX_SOURCE_STRINGS
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import ATTR_MEDIA_ENQUEUE as ATTR_MEDIA_ENQUEUE, BrowseError as BrowseError, BrowseMedia as BrowseMedia, MediaPlayerEnqueue as MediaPlayerEnqueue, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, RepeatMode as RepeatMode, async_process_play_media_url as async_process_play_media_url
from homeassistant.config_entries import SOURCE_INTEGRATION_DISCOVERY as SOURCE_INTEGRATION_DISCOVERY
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import discovery_flow as discovery_flow, entity_platform as entity_platform
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.start import async_at_start as async_at_start
from homeassistant.util.dt import utcnow as utcnow
from pysqueezebox import Player as Player, Server as Server
from typing import Any

SERVICE_CALL_METHOD: str
SERVICE_CALL_QUERY: str
ATTR_QUERY_RESULT: str
SIGNAL_PLAYER_REDISCOVERED: str
_LOGGER: Incomplete
DISCOVERY_INTERVAL: int
KNOWN_SERVERS: str
ATTR_PARAMETERS: str
ATTR_OTHER_PLAYER: str
ATTR_TO_PROPERTY: Incomplete
SQUEEZEBOX_MODE: Incomplete

async def start_server_discovery(hass: HomeAssistant) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SqueezeBoxEntity(MediaPlayerEntity):
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _last_update: datetime | None
    _attr_available: bool
    _player: Incomplete
    _query_result: Incomplete
    _remove_dispatcher: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, player: Player, server: Server) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def rediscovered(self, unique_id: str, connected: bool) -> None: ...
    @property
    def state(self) -> MediaPlayerState | None: ...
    async def async_update(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def volume_level(self) -> float | None: ...
    @property
    def is_volume_muted(self) -> bool: ...
    @property
    def media_content_id(self) -> str | None: ...
    @property
    def media_content_type(self) -> MediaType | None: ...
    @property
    def media_duration(self) -> int: ...
    @property
    def media_position(self) -> int: ...
    @property
    def media_position_updated_at(self) -> datetime | None: ...
    @property
    def media_image_url(self) -> str | None: ...
    @property
    def media_title(self) -> str | None: ...
    @property
    def media_channel(self) -> str | None: ...
    @property
    def media_artist(self) -> str | None: ...
    @property
    def media_album_name(self) -> str | None: ...
    @property
    def repeat(self) -> RepeatMode: ...
    @property
    def shuffle(self) -> bool: ...
    @property
    def group_members(self) -> list[str]: ...
    @property
    def query_result(self) -> dict | bool: ...
    async def async_turn_off(self) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_seek(self, position: float) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_set_repeat(self, repeat: RepeatMode) -> None: ...
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    async def async_clear_playlist(self) -> None: ...
    async def async_call_method(self, command: str, parameters: list[str] | None = None) -> None: ...
    async def async_call_query(self, command: str, parameters: list[str] | None = None) -> None: ...
    async def async_join_players(self, group_members: list[str]) -> None: ...
    async def async_unjoin_player(self) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    async def async_get_browse_image(self, media_content_type: MediaType | str, media_content_id: str, media_image_id: str | None = None) -> tuple[bytes | None, str | None]: ...
