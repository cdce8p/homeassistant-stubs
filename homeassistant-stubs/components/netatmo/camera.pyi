from .const import ATTR_CAMERA_LIGHT_MODE as ATTR_CAMERA_LIGHT_MODE, ATTR_PERSON as ATTR_PERSON, ATTR_PERSONS as ATTR_PERSONS, CAMERA_LIGHT_MODES as CAMERA_LIGHT_MODES, CONF_URL_SECURITY as CONF_URL_SECURITY, DATA_CAMERAS as DATA_CAMERAS, DATA_EVENTS as DATA_EVENTS, DOMAIN as DOMAIN, EVENT_TYPE_LIGHT_MODE as EVENT_TYPE_LIGHT_MODE, EVENT_TYPE_OFF as EVENT_TYPE_OFF, EVENT_TYPE_ON as EVENT_TYPE_ON, MANUFACTURER as MANUFACTURER, NETATMO_CREATE_CAMERA as NETATMO_CREATE_CAMERA, SERVICE_SET_CAMERA_LIGHT as SERVICE_SET_CAMERA_LIGHT, SERVICE_SET_PERSONS_HOME as SERVICE_SET_PERSONS_HOME, SERVICE_SET_PERSON_AWAY as SERVICE_SET_PERSON_AWAY, WEBHOOK_LIGHT_MODE as WEBHOOK_LIGHT_MODE, WEBHOOK_NACAMERA_CONNECTION as WEBHOOK_NACAMERA_CONNECTION, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from .data_handler import EVENT as EVENT, HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .entity import NetatmoBaseEntity as NetatmoBaseEntity
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyatmo.event import Event as NaEvent
from typing import Any

_LOGGER: Incomplete
DEFAULT_QUALITY: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoCamera(NetatmoBaseEntity, Camera):
    _attr_brand = MANUFACTURER
    _attr_has_entity_name: bool
    _attr_supported_features: Incomplete
    _camera: Incomplete
    _id: Incomplete
    _home_id: Incomplete
    _device_name: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _attr_unique_id: Incomplete
    _quality: Incomplete
    _monitoring: Incomplete
    _light_state: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_streaming: bool
    def handle_event(self, event: dict) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    @property
    def supported_features(self) -> CameraEntityFeature: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def stream_source(self) -> str: ...
    _attr_is_on: Incomplete
    _attr_available: Incomplete
    _attr_motion_detection_enabled: Incomplete
    def async_update_callback(self) -> None: ...
    def process_events(self, event_list: list[NaEvent]) -> dict: ...
    def get_video_url(self, video_id: str) -> str: ...
    def fetch_person_ids(self, persons: list[str | None]) -> list[str]: ...
    async def _service_set_persons_home(self, **kwargs: Any) -> None: ...
    async def _service_set_person_away(self, **kwargs: Any) -> None: ...
    async def _service_set_camera_light(self, **kwargs: Any) -> None: ...
