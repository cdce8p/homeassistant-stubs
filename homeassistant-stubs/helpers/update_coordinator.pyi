import abc
import logging
from . import entity as entity, event as event
from .debounce import Debouncer as Debouncer
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Awaitable, Callable as Callable, Coroutine, Generator
from datetime import datetime, timedelta
from homeassistant import config_entries as config_entries
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.util.dt import utcnow as utcnow
from typing import Any, Generic, Protocol, TypeVar

REQUEST_REFRESH_DEFAULT_COOLDOWN: int
REQUEST_REFRESH_DEFAULT_IMMEDIATE: bool
_T = TypeVar('_T')
_BaseDataUpdateCoordinatorT = TypeVar('_BaseDataUpdateCoordinatorT', bound='BaseDataUpdateCoordinatorProtocol')
_DataUpdateCoordinatorT = TypeVar('_DataUpdateCoordinatorT', bound='DataUpdateCoordinator[Any]')

class UpdateFailed(Exception): ...

class BaseDataUpdateCoordinatorProtocol(Protocol):
    def async_add_listener(self, update_callback: CALLBACK_TYPE, context: Any = ...) -> Callable[[], None]: ...

class DataUpdateCoordinator(BaseDataUpdateCoordinatorProtocol, Generic[_T]):
    hass: Incomplete
    logger: Incomplete
    name: Incomplete
    update_method: Incomplete
    update_interval: Incomplete
    _shutdown_requested: bool
    config_entry: Incomplete
    data: Incomplete
    _microsecond: Incomplete
    _listeners: Incomplete
    _job: Incomplete
    _unsub_refresh: Incomplete
    _unsub_shutdown: Incomplete
    _request_refresh_task: Incomplete
    last_update_success: bool
    last_exception: Incomplete
    _debounced_refresh: Incomplete
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, *, name: str, update_interval: timedelta | None = ..., update_method: Callable[[], Awaitable[_T]] | None = ..., request_refresh_debouncer: Debouncer[Coroutine[Any, Any, None]] | None = ...) -> None: ...
    async def async_register_shutdown(self) -> None: ...
    def async_add_listener(self, update_callback: CALLBACK_TYPE, context: Any = ...) -> Callable[[], None]: ...
    def async_update_listeners(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    def _unschedule_refresh(self) -> None: ...
    def async_contexts(self) -> Generator[Any, None, None]: ...
    def _async_unsub_refresh(self) -> None: ...
    def _async_unsub_shutdown(self) -> None: ...
    def _schedule_refresh(self) -> None: ...
    async def _handle_refresh_interval(self, _now: datetime) -> None: ...
    async def async_request_refresh(self) -> None: ...
    async def _async_update_data(self) -> _T: ...
    async def async_config_entry_first_refresh(self) -> None: ...
    async def async_refresh(self) -> None: ...
    async def _async_refresh(self, log_failures: bool = ..., raise_on_auth_failed: bool = ..., scheduled: bool = ..., raise_on_entry_error: bool = ...) -> None: ...
    def async_set_update_error(self, err: Exception) -> None: ...
    def async_set_updated_data(self, data: _T) -> None: ...

class BaseCoordinatorEntity(entity.Entity, Generic[_BaseDataUpdateCoordinatorT], metaclass=abc.ABCMeta):
    coordinator: Incomplete
    coordinator_context: Incomplete
    def __init__(self, coordinator: _BaseDataUpdateCoordinatorT, context: Any = ...) -> None: ...
    @property
    def should_poll(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    async def async_update(self) -> None: ...

class CoordinatorEntity(BaseCoordinatorEntity[_DataUpdateCoordinatorT]):
    def __init__(self, coordinator: _DataUpdateCoordinatorT, context: Any = ...) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
