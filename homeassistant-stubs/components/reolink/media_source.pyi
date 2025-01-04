from .const import DOMAIN as DOMAIN
from .util import get_host as get_host
from .views import async_generate_playback_proxy_url as async_generate_playback_proxy_url
from _typeshed import Incomplete
from homeassistant.components.camera import DynamicStreamSettings as DynamicStreamSettings
from homeassistant.components.media_player import MediaClass as MediaClass, MediaType as MediaType
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.components.stream import create_stream as create_stream
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete

async def async_get_media_source(hass: HomeAssistant) -> ReolinkVODMediaSource: ...
def res_name(stream: str) -> str: ...

class ReolinkVODMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    async def _async_generate_root(self) -> BrowseMediaSource: ...
    async def _async_generate_resolution_select(self, config_entry_id: str, channel: int) -> BrowseMediaSource: ...
    async def _async_generate_camera_days(self, config_entry_id: str, channel: int, stream: str) -> BrowseMediaSource: ...
    async def _async_generate_camera_files(self, config_entry_id: str, channel: int, stream: str, year: int, month: int, day: int) -> BrowseMediaSource: ...
