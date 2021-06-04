from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant.components.media_player import MediaPlayerEntity as MediaPlayerEntity
from homeassistant.components.media_player.const import SUPPORT_NEXT_TRACK as SUPPORT_NEXT_TRACK, SUPPORT_PAUSE as SUPPORT_PAUSE, SUPPORT_PLAY as SUPPORT_PLAY, SUPPORT_PREVIOUS_TRACK as SUPPORT_PREVIOUS_TRACK, SUPPORT_TURN_OFF as SUPPORT_TURN_OFF, SUPPORT_TURN_ON as SUPPORT_TURN_ON
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from pdunehd import DuneHDPlayer as DuneHDPlayer
from typing import Any, Final

CONF_SOURCES: Final[str]
PLATFORM_SCHEMA: Final[Any]
DUNEHD_PLAYER_SUPPORT: Final[int]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DuneHDPlayerEntity(MediaPlayerEntity):
    _player: Any = ...
    _name: Any = ...
    _media_title: Any = ...
    _state: Any = ...
    _unique_id: Any = ...
    def __init__(self, player: DuneHDPlayer, name: str, unique_id: str) -> None: ...
    def update(self) -> bool: ...
    @property
    def state(self) -> StateType: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def volume_level(self) -> float: ...
    @property
    def is_volume_muted(self) -> bool: ...
    @property
    def supported_features(self) -> int: ...
    def volume_up(self) -> None: ...
    def volume_down(self) -> None: ...
    def mute_volume(self, mute: bool) -> None: ...
    def turn_off(self) -> None: ...
    def turn_on(self) -> None: ...
    def media_play(self) -> None: ...
    def media_pause(self) -> None: ...
    @property
    def media_title(self) -> Union[str, None]: ...
    def __update_title(self) -> None: ...
    def media_previous_track(self) -> None: ...
    def media_next_track(self) -> None: ...