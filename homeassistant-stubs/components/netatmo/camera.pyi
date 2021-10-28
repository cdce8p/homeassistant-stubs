import pyatmo
from .const import ATTR_CAMERA_LIGHT_MODE as ATTR_CAMERA_LIGHT_MODE, ATTR_PERSON as ATTR_PERSON, ATTR_PERSONS as ATTR_PERSONS, ATTR_PSEUDO as ATTR_PSEUDO, CAMERA_LIGHT_MODES as CAMERA_LIGHT_MODES, DATA_CAMERAS as DATA_CAMERAS, DATA_EVENTS as DATA_EVENTS, DATA_HANDLER as DATA_HANDLER, DATA_PERSONS as DATA_PERSONS, DOMAIN as DOMAIN, EVENT_TYPE_LIGHT_MODE as EVENT_TYPE_LIGHT_MODE, EVENT_TYPE_OFF as EVENT_TYPE_OFF, EVENT_TYPE_ON as EVENT_TYPE_ON, MANUFACTURER as MANUFACTURER, MODELS as MODELS, SERVICE_SET_CAMERA_LIGHT as SERVICE_SET_CAMERA_LIGHT, SERVICE_SET_PERSONS_HOME as SERVICE_SET_PERSONS_HOME, SERVICE_SET_PERSON_AWAY as SERVICE_SET_PERSON_AWAY, SIGNAL_NAME as SIGNAL_NAME, TYPE_SECURITY as TYPE_SECURITY, WEBHOOK_LIGHT_MODE as WEBHOOK_LIGHT_MODE, WEBHOOK_NACAMERA_CONNECTION as WEBHOOK_NACAMERA_CONNECTION, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from .data_handler import CAMERA_DATA_CLASS_NAME as CAMERA_DATA_CLASS_NAME, NetatmoDataHandler as NetatmoDataHandler
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from homeassistant.components.camera import Camera as Camera, SUPPORT_STREAM as SUPPORT_STREAM
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, PlatformNotReady as PlatformNotReady
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any
DEFAULT_QUALITY: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoCamera(NetatmoBase, Camera):
    _id: Any
    _home_id: Any
    _device_name: Any
    _attr_name: Any
    _model: Any
    _netatmo_type: Any
    _attr_unique_id: Any
    _quality: Any
    _vpnurl: Any
    _localurl: Any
    _status: Any
    _sd_status: Any
    _alim_status: Any
    _is_local: Any
    _light_state: Any
    def __init__(self, data_handler: NetatmoDataHandler, camera_id: str, camera_type: str, home_id: str, quality: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    is_streaming: bool
    def handle_event(self, event: dict) -> None: ...
    @property
    def _data(self) -> pyatmo.AsyncCameraData: ...
    async def async_camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def brand(self) -> str: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def stream_source(self) -> str: ...
    @property
    def model(self) -> str: ...
    def async_update_callback(self) -> None: ...
    def process_events(self, events: dict) -> dict: ...
    def fetch_person_ids(self, persons: list[Union[str, None]]) -> list[str]: ...
    async def _service_set_persons_home(self, **kwargs: Any) -> None: ...
    async def _service_set_person_away(self, **kwargs: Any) -> None: ...
    async def _service_set_camera_light(self, **kwargs: Any) -> None: ...
