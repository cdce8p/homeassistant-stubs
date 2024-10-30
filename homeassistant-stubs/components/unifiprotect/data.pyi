from .const import AUTH_RETRIES as AUTH_RETRIES, CONF_DISABLE_RTSP as CONF_DISABLE_RTSP, CONF_MAX_MEDIA as CONF_MAX_MEDIA, DEFAULT_MAX_MEDIA as DEFAULT_MAX_MEDIA, DEVICES_THAT_ADOPT as DEVICES_THAT_ADOPT, DISPATCH_ADD as DISPATCH_ADD, DISPATCH_ADOPT as DISPATCH_ADOPT, DISPATCH_CHANNELS as DISPATCH_CHANNELS, DOMAIN as DOMAIN
from .utils import async_get_devices_by_type as async_get_devices_by_type
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator, Iterable
from datetime import datetime, timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from typing import Any
from uiprotect import ProtectApiClient as ProtectApiClient
from uiprotect.data import Camera, ModelType, NVR, ProtectAdoptableDeviceModel, WSSubscriptionMessage as WSSubscriptionMessage
from uiprotect.websocket import WebsocketState

_LOGGER: Incomplete
type ProtectDeviceType = ProtectAdoptableDeviceModel | NVR
type UFPConfigEntry = ConfigEntry[ProtectData]

def async_last_update_was_successful(hass: HomeAssistant, entry: UFPConfigEntry) -> bool: ...
def _async_dispatch_id(entry: UFPConfigEntry, dispatch: str) -> str: ...

class ProtectData:
    _entry: Incomplete
    _hass: Incomplete
    _update_interval: Incomplete
    _subscriptions: Incomplete
    _pending_camera_ids: Incomplete
    _unsubs: Incomplete
    _auth_failures: int
    last_update_success: bool
    api: Incomplete
    adopt_signal: Incomplete
    add_signal: Incomplete
    channels_signal: Incomplete
    def __init__(self, hass: HomeAssistant, protect: ProtectApiClient, update_interval: timedelta, entry: UFPConfigEntry) -> None: ...
    @property
    def disable_stream(self) -> bool: ...
    @property
    def max_events(self) -> int: ...
    def async_subscribe_adopt(self, add_callback: Callable[[ProtectAdoptableDeviceModel], None]) -> None: ...
    def get_by_types(self, device_types: Iterable[ModelType], ignore_unadopted: bool = True) -> Generator[ProtectAdoptableDeviceModel]: ...
    def get_cameras(self, ignore_unadopted: bool = True) -> Generator[Camera]: ...
    def async_setup(self) -> None: ...
    def _async_websocket_state_changed(self, state: WebsocketState) -> None: ...
    def _async_update_change(self, success: bool, force_update: bool = False, exception: Exception | None = None) -> None: ...
    async def async_stop(self, *args: Any) -> None: ...
    async def async_refresh(self) -> None: ...
    def async_add_pending_camera_id(self, camera_id: str) -> None: ...
    def _async_add_device(self, device: ProtectAdoptableDeviceModel) -> None: ...
    def _async_remove_device(self, device: ProtectAdoptableDeviceModel) -> None: ...
    def _async_update_device(self, device: ProtectAdoptableDeviceModel | NVR, changed_data: dict[str, Any]) -> None: ...
    def _async_process_ws_message(self, message: WSSubscriptionMessage) -> None: ...
    def _async_process_updates(self) -> None: ...
    def _async_poll(self, now: datetime) -> None: ...
    def async_subscribe(self, mac: str, update_callback: Callable[[ProtectDeviceType], None]) -> CALLBACK_TYPE: ...
    def _async_unsubscribe(self, mac: str, update_callback: Callable[[ProtectDeviceType], None]) -> None: ...
    def _async_signal_device_update(self, device: ProtectDeviceType) -> None: ...

def async_ufp_instance_for_config_entry_ids(hass: HomeAssistant, config_entry_ids: set[str]) -> ProtectApiClient | None: ...
def async_get_ufp_entries(hass: HomeAssistant) -> list[UFPConfigEntry]: ...
def async_get_data_for_nvr_id(hass: HomeAssistant, nvr_id: str) -> ProtectData | None: ...
def async_get_data_for_entry_id(hass: HomeAssistant, entry_id: str) -> ProtectData | None: ...
