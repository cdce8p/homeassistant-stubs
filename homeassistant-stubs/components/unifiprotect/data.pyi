from .const import AUTH_RETRIES as AUTH_RETRIES, CONF_DISABLE_RTSP as CONF_DISABLE_RTSP, CONF_MAX_MEDIA as CONF_MAX_MEDIA, DEFAULT_MAX_MEDIA as DEFAULT_MAX_MEDIA, DEVICES_THAT_ADOPT as DEVICES_THAT_ADOPT, DISPATCH_ADD as DISPATCH_ADD, DISPATCH_ADOPT as DISPATCH_ADOPT, DISPATCH_CHANNELS as DISPATCH_CHANNELS, DOMAIN as DOMAIN
from .utils import async_get_devices_by_type as async_get_devices_by_type
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator, Iterable
from datetime import datetime, timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from pyunifiprotect import ProtectApiClient as ProtectApiClient
from pyunifiprotect.data import Bootstrap as Bootstrap, ModelType, NVR, ProtectAdoptableDeviceModel, WSSubscriptionMessage as WSSubscriptionMessage
from typing import Any

_LOGGER: Incomplete
ProtectDeviceType: Incomplete

def async_last_update_was_successful(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class ProtectData:
    _hass: Incomplete
    _entry: Incomplete
    _update_interval: Incomplete
    _subscriptions: Incomplete
    _pending_camera_ids: Incomplete
    _unsub_interval: Incomplete
    _unsub_websocket: Incomplete
    _auth_failures: int
    last_update_success: bool
    api: Incomplete
    def __init__(self, hass: HomeAssistant, protect: ProtectApiClient, update_interval: timedelta, entry: ConfigEntry) -> None: ...
    @property
    def disable_stream(self) -> bool: ...
    @property
    def max_events(self) -> int: ...
    def get_by_types(self, device_types: Iterable[ModelType], ignore_unadopted: bool = True) -> Generator[ProtectAdoptableDeviceModel, None, None]: ...
    async def async_setup(self) -> None: ...
    async def async_stop(self, *args: Any) -> None: ...
    async def async_refresh(self, *_: Any, force: bool = False) -> None: ...
    def async_add_pending_camera_id(self, camera_id: str) -> None: ...
    def _async_add_device(self, device: ProtectAdoptableDeviceModel) -> None: ...
    def _async_remove_device(self, device: ProtectAdoptableDeviceModel) -> None: ...
    def _async_update_device(self, device: ProtectAdoptableDeviceModel | NVR, changed_data: dict[str, Any]) -> None: ...
    def _async_process_ws_message(self, message: WSSubscriptionMessage) -> None: ...
    def _async_process_updates(self, updates: Bootstrap | None) -> None: ...
    def _async_poll(self, now: datetime) -> None: ...
    def async_subscribe_device_id(self, mac: str, update_callback: Callable[[ProtectDeviceType], None]) -> CALLBACK_TYPE: ...
    def async_unsubscribe_device_id(self, mac: str, update_callback: Callable[[ProtectDeviceType], None]) -> None: ...
    def _async_signal_device_update(self, device: ProtectDeviceType) -> None: ...

def async_ufp_instance_for_config_entry_ids(hass: HomeAssistant, config_entry_ids: set[str]) -> ProtectApiClient | None: ...
