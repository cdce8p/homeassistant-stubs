from . import AmcrestDevice as AmcrestDevice
from .const import CAMERAS as CAMERAS, CAMERA_WEB_SESSION_TIMEOUT as CAMERA_WEB_SESSION_TIMEOUT, COMM_TIMEOUT as COMM_TIMEOUT, DATA_AMCREST as DATA_AMCREST, DEVICES as DEVICES, DOMAIN as DOMAIN, RESOLUTION_TO_STREAM as RESOLUTION_TO_STREAM, SERVICE_UPDATE as SERVICE_UPDATE, SNAPSHOT_TIMEOUT as SNAPSHOT_TIMEOUT
from .helpers import log_update_error as log_update_error, service_signal as service_signal
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Callable as Callable
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.components.ffmpeg import FFmpegManager as FFmpegManager, get_ffmpeg_manager as get_ffmpeg_manager
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_NAME as CONF_NAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream as async_aiohttp_proxy_stream, async_aiohttp_proxy_web as async_aiohttp_proxy_web, async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
STREAM_SOURCE_LIST: Incomplete
_SRV_EN_REC: str
_SRV_DS_REC: str
_SRV_EN_AUD: str
_SRV_DS_AUD: str
_SRV_EN_MOT_REC: str
_SRV_DS_MOT_REC: str
_SRV_GOTO: str
_SRV_CBW: str
_SRV_TOUR_ON: str
_SRV_TOUR_OFF: str
_SRV_PTZ_CTRL: str
_ATTR_PTZ_TT: str
_ATTR_PTZ_MOV: str
_MOV: Incomplete
_ZOOM_ACTIONS: Incomplete
_MOVE_1_ACTIONS: Incomplete
_MOVE_2_ACTIONS: Incomplete
_ACTION: Incomplete
_DEFAULT_TT: float
_ATTR_PRESET: str
_ATTR_COLOR_BW: str
_CBW_COLOR: str
_CBW_AUTO: str
_CBW_BW: str
_CBW: Incomplete
_SRV_SCHEMA: Incomplete
_SRV_GOTO_SCHEMA: Incomplete
_SRV_CBW_SCHEMA: Incomplete
_SRV_PTZ_SCHEMA: Incomplete
CAMERA_SERVICES: Incomplete
_BOOL_TO_STATE: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class CannotSnapshot(Exception): ...
class AmcrestCommandFailed(Exception): ...

class AmcrestCam(Camera):
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    _name: Incomplete
    _api: Incomplete
    _ffmpeg: Incomplete
    _ffmpeg_arguments: Incomplete
    _stream_source: Incomplete
    _resolution: Incomplete
    _channel: Incomplete
    _token: Incomplete
    _control_light: Incomplete
    _is_recording: bool
    _motion_detection_enabled: bool
    _brand: Incomplete
    _model: Incomplete
    _audio_enabled: Incomplete
    _motion_recording_enabled: Incomplete
    _color_bw: Incomplete
    _rtsp_url: Incomplete
    _snapshot_task: Incomplete
    _unsub_dispatcher: Incomplete
    def __init__(self, name: str, device: AmcrestDevice, ffmpeg: FFmpegManager) -> None: ...
    def _check_snapshot_ok(self) -> None: ...
    async def _async_get_image(self) -> Union[bytes, None]: ...
    async def async_camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> Union[web.StreamResponse, None]: ...
    @property
    def name(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_recording(self) -> bool: ...
    @property
    def brand(self) -> Union[str, None]: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    @property
    def model(self) -> Union[str, None]: ...
    async def stream_source(self) -> Union[str, None]: ...
    @property
    def is_on(self) -> bool: ...
    async def async_on_demand_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _attr_unique_id: Incomplete
    async def async_update(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_enable_motion_detection(self) -> None: ...
    async def async_disable_motion_detection(self) -> None: ...
    async def async_enable_recording(self) -> None: ...
    async def async_disable_recording(self) -> None: ...
    async def async_enable_audio(self) -> None: ...
    async def async_disable_audio(self) -> None: ...
    async def async_enable_motion_recording(self) -> None: ...
    async def async_disable_motion_recording(self) -> None: ...
    async def async_goto_preset(self, preset: int) -> None: ...
    async def async_set_color_bw(self, color_bw: str) -> None: ...
    async def async_start_tour(self) -> None: ...
    async def async_stop_tour(self) -> None: ...
    async def async_ptz_control(self, movement: str, travel_time: float) -> None: ...
    async def _async_change_setting(self, value: Union[str, bool], description: str, attr: Union[str, None] = ...) -> None: ...
    async def _async_get_video(self) -> bool: ...
    async def _async_set_video(self, enable: bool) -> None: ...
    async def _async_enable_video(self, enable: bool) -> None: ...
    async def _async_get_recording(self) -> bool: ...
    async def _async_set_recording(self, enable: bool) -> None: ...
    async def _async_enable_recording(self, enable: bool) -> None: ...
    async def _async_get_motion_detection(self) -> bool: ...
    async def _async_set_motion_detection(self, enable: bool) -> None: ...
    async def _async_enable_motion_detection(self, enable: bool) -> None: ...
    async def _async_get_audio(self) -> bool: ...
    async def _async_set_audio(self, enable: bool) -> None: ...
    async def _async_enable_audio(self, enable: bool) -> None: ...
    async def _async_get_indicator_light(self) -> bool: ...
    async def _async_set_indicator_light(self, enable: bool) -> None: ...
    async def _async_change_light(self) -> None: ...
    async def _async_get_motion_recording(self) -> bool: ...
    async def _async_set_motion_recording(self, enable: bool) -> None: ...
    async def _async_enable_motion_recording(self, enable: bool) -> None: ...
    async def _async_goto_preset(self, preset: int) -> None: ...
    async def _async_get_color_mode(self) -> str: ...
    async def _async_set_color_mode(self, cbw: str) -> None: ...
    async def _async_set_color_bw(self, cbw: str) -> None: ...
    async def _async_start_tour(self, start: bool) -> None: ...
