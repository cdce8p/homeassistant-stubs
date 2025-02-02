from aiostreammagic import StreamMagicClient as StreamMagicClient
from aiostreammagic.models import Preset as Preset
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaClass as MediaClass
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_browse_media(hass: HomeAssistant, client: StreamMagicClient, media_content_id: str | None, media_content_type: str | None) -> BrowseMedia: ...
async def _root_payload(hass: HomeAssistant, client: StreamMagicClient) -> BrowseMedia: ...
async def _presets_payload(presets: list[Preset]) -> BrowseMedia: ...
