from . import AndroidTVConfigEntry as AndroidTVConfigEntry
from .const import CONF_APPS as CONF_APPS, CONF_EXCLUDE_UNNAMED_APPS as CONF_EXCLUDE_UNNAMED_APPS, CONF_GET_SOURCES as CONF_GET_SOURCES, CONF_SCREENCAP_INTERVAL as CONF_SCREENCAP_INTERVAL, CONF_TURN_OFF_COMMAND as CONF_TURN_OFF_COMMAND, CONF_TURN_ON_COMMAND as CONF_TURN_ON_COMMAND, DEFAULT_EXCLUDE_UNNAMED_APPS as DEFAULT_EXCLUDE_UNNAMED_APPS, DEFAULT_GET_SOURCES as DEFAULT_GET_SOURCES, DEFAULT_SCREENCAP_INTERVAL as DEFAULT_SCREENCAP_INTERVAL, DEVICE_ANDROIDTV as DEVICE_ANDROIDTV, SIGNAL_CONFIG_ENTITY as SIGNAL_CONFIG_ENTITY
from .entity import AndroidTVEntity as AndroidTVEntity, adb_decorator as adb_decorator
from _typeshed import Incomplete
from androidtv.setup_async import AndroidTVAsync as AndroidTVAsync, FireTVAsync as FireTVAsync
from datetime import datetime, timedelta
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow

_LOGGER: Incomplete
ATTR_ADB_RESPONSE: str
ATTR_DEVICE_PATH: str
ATTR_HDMI_INPUT: str
ATTR_LOCAL_PATH: str
SERVICE_ADB_COMMAND: str
SERVICE_DOWNLOAD: str
SERVICE_LEARN_SENDEVENT: str
SERVICE_UPLOAD: str
ANDROIDTV_STATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AndroidTVConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ADBDevice(AndroidTVEntity, MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _entry_id: Incomplete
    _media_image: tuple[bytes | None, str | None]
    _attr_media_image_hash: Incomplete
    _app_id_to_name: dict[str, str]
    _app_name_to_id: dict[str, str]
    _get_sources: Incomplete
    _exclude_unnamed_apps: Incomplete
    _screencap_delta: timedelta | None
    _last_screencap: datetime | None
    turn_on_command: str | None
    turn_off_command: str | None
    _attr_extra_state_attributes: Incomplete
    _failed_connect_count: int
    def __init__(self, entry: AndroidTVConfigEntry) -> None: ...
    def _process_config(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @adb_decorator()
    async def _adb_screencap(self) -> bytes | None: ...
    async def _async_get_screencap(self, prev_app_id: str | None = None) -> None: ...
    async def _adb_get_screencap(self, force: bool = False) -> None: ...
    async def async_get_media_image(self) -> tuple[bytes | None, str | None]: ...
    @adb_decorator()
    async def async_media_play(self) -> None: ...
    @adb_decorator()
    async def async_media_pause(self) -> None: ...
    @adb_decorator()
    async def async_media_play_pause(self) -> None: ...
    @adb_decorator()
    async def async_turn_on(self) -> None: ...
    @adb_decorator()
    async def async_turn_off(self) -> None: ...
    @adb_decorator()
    async def async_media_previous_track(self) -> None: ...
    @adb_decorator()
    async def async_media_next_track(self) -> None: ...
    @adb_decorator()
    async def async_select_source(self, source: str) -> None: ...
    @adb_decorator()
    async def adb_command(self, command: str) -> None: ...
    @adb_decorator()
    async def learn_sendevent(self) -> None: ...
    @adb_decorator()
    async def service_download(self, device_path: str, local_path: str) -> None: ...
    @adb_decorator()
    async def service_upload(self, device_path: str, local_path: str) -> None: ...

class AndroidTVDevice(ADBDevice):
    _attr_supported_features: Incomplete
    aftv: AndroidTVAsync
    _failed_connect_count: int
    _attr_available: bool
    _attr_state: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    @adb_decorator(override_available=True)
    async def async_update(self) -> None: ...
    @adb_decorator()
    async def async_media_stop(self) -> None: ...
    @adb_decorator()
    async def async_mute_volume(self, mute: bool) -> None: ...
    @adb_decorator()
    async def async_set_volume_level(self, volume: float) -> None: ...
    _attr_volume_level: Incomplete
    @adb_decorator()
    async def async_volume_down(self) -> None: ...
    @adb_decorator()
    async def async_volume_up(self) -> None: ...

class FireTVDevice(ADBDevice):
    _attr_supported_features: Incomplete
    aftv: FireTVAsync
    _failed_connect_count: int
    _attr_available: bool
    _attr_state: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    @adb_decorator(override_available=True)
    async def async_update(self) -> None: ...
    @adb_decorator()
    async def async_media_stop(self) -> None: ...
