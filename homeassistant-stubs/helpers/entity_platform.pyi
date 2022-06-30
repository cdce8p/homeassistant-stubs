import asyncio
import voluptuous as vol
from . import service as service
from .device_registry import DeviceRegistry as DeviceRegistry
from .entity import Entity as Entity
from .entity_registry import EntityRegistry as EntityRegistry, RegistryEntryDisabler as RegistryEntryDisabler, RegistryEntryHider as RegistryEntryHider
from .event import async_call_later as async_call_later, async_track_time_interval as async_track_time_interval
from .typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Iterable
from contextvars import ContextVar
from datetime import datetime, timedelta
from homeassistant import config_entries as config_entries
from homeassistant.const import ATTR_RESTORED as ATTR_RESTORED, DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, CoreState as CoreState, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, PlatformNotReady as PlatformNotReady, RequiredParameterMissing as RequiredParameterMissing
from homeassistant.setup import async_start_setup as async_start_setup
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from logging import Logger
from types import ModuleType
from typing import Any, Protocol

SLOW_SETUP_WARNING: int
SLOW_SETUP_MAX_WAIT: int
SLOW_ADD_ENTITY_MAX_WAIT: int
SLOW_ADD_MIN_TIMEOUT: int
PLATFORM_NOT_READY_RETRIES: int
DATA_ENTITY_PLATFORM: str
PLATFORM_NOT_READY_BASE_WAIT_TIME: int
_LOGGER: Incomplete

class AddEntitiesCallback(Protocol):
    def __call__(self, new_entities: Iterable[Entity], update_before_add: bool = ...) -> None: ...

class EntityPlatform:
    hass: Incomplete
    logger: Incomplete
    domain: Incomplete
    platform_name: Incomplete
    platform: Incomplete
    scan_interval: Incomplete
    entity_namespace: Incomplete
    config_entry: Incomplete
    entities: Incomplete
    _tasks: Incomplete
    _setup_complete: bool
    _async_unsub_polling: Incomplete
    _async_cancel_retry_setup: Incomplete
    _process_updates: Incomplete
    parallel_updates: Incomplete
    parallel_updates_created: Incomplete
    def __init__(self, *, hass: HomeAssistant, logger: Logger, domain: str, platform_name: str, platform: Union[ModuleType, None], scan_interval: timedelta, entity_namespace: Union[str, None]) -> None: ...
    def __repr__(self) -> str: ...
    def _get_parallel_updates_semaphore(self, entity_has_sync_update: bool) -> Union[asyncio.Semaphore, None]: ...
    async def async_setup(self, platform_config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
    async def async_shutdown(self) -> None: ...
    def async_cancel_retry_setup(self) -> None: ...
    async def async_setup_entry(self, config_entry: config_entries.ConfigEntry) -> bool: ...
    async def _async_setup_platform(self, async_create_setup_task: Callable[[], Coroutine], tries: int = ...) -> bool: ...
    def _schedule_add_entities(self, new_entities: Iterable[Entity], update_before_add: bool = ...) -> None: ...
    def _async_schedule_add_entities(self, new_entities: Iterable[Entity], update_before_add: bool = ...) -> None: ...
    def _async_schedule_add_entities_for_entry(self, new_entities: Iterable[Entity], update_before_add: bool = ...) -> None: ...
    def add_entities(self, new_entities: Iterable[Entity], update_before_add: bool = ...) -> None: ...
    async def async_add_entities(self, new_entities: Iterable[Entity], update_before_add: bool = ...) -> None: ...
    async def _async_add_entity(self, entity: Entity, update_before_add: bool, entity_registry: EntityRegistry, device_registry: DeviceRegistry) -> None: ...
    async def async_reset(self) -> None: ...
    def async_unsub_polling(self) -> None: ...
    async def async_destroy(self) -> None: ...
    async def async_remove_entity(self, entity_id: str) -> None: ...
    async def async_extract_from_service(self, service_call: ServiceCall, expand_group: bool = ...) -> list[Entity]: ...
    def async_register_entity_service(self, name: str, schema: Union[dict, vol.Schema], func: Union[str, Callable[..., Any]], required_features: Union[Iterable[int], None] = ...) -> None: ...
    async def _update_entity_states(self, now: datetime) -> None: ...

current_platform: ContextVar[Union[EntityPlatform, None]]

def async_get_current_platform() -> EntityPlatform: ...
def async_get_platforms(hass: HomeAssistant, integration_name: str) -> list[EntityPlatform]: ...
