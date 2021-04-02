import logging
from .debounce import Debouncer as Debouncer
from datetime import datetime, timedelta
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import entity as entity, event as event
from homeassistant.util.dt import utcnow as utcnow
from typing import Any, Awaitable, Callable, TypeVar

REQUEST_REFRESH_DEFAULT_COOLDOWN: int
REQUEST_REFRESH_DEFAULT_IMMEDIATE: bool
T = TypeVar('T')

class UpdateFailed(Exception): ...

class DataUpdateCoordinator:
    hass: Any = ...
    logger: Any = ...
    name: Any = ...
    update_method: Any = ...
    update_interval: Any = ...
    data: Any = ...
    _listeners: Any = ...
    _job: Any = ...
    _unsub_refresh: Any = ...
    _request_refresh_task: Any = ...
    last_update_success: bool = ...
    last_exception: Any = ...
    _debounced_refresh: Any = ...
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, name: str, *, update_interval: Union[timedelta, None]=..., update_method: Union[Callable[[], Awaitable[T]], None]=..., request_refresh_debouncer: Union[Debouncer, None]=...) -> None: ...
    def async_add_listener(self, update_callback: CALLBACK_TYPE) -> Callable[[], None]: ...
    def async_remove_listener(self, update_callback: CALLBACK_TYPE) -> None: ...
    def _schedule_refresh(self) -> None: ...
    async def _handle_refresh_interval(self, _now: datetime) -> None: ...
    async def async_request_refresh(self) -> None: ...
    async def _async_update_data(self) -> Union[T, None]: ...
    async def async_config_entry_first_refresh(self) -> None: ...
    async def async_refresh(self) -> None: ...
    async def _async_refresh(self, log_failures: bool=...) -> None: ...
    def async_set_updated_data(self, data: T) -> None: ...
    def _async_stop_refresh(self, _: Event) -> None: ...

class CoordinatorEntity(entity.Entity):
    coordinator: Any = ...
    def __init__(self, coordinator: DataUpdateCoordinator[Any]) -> None: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_update(self) -> None: ...
