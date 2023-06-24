import asyncio
from . import entity_registry as er
from .device_registry import DeviceEntryType as DeviceEntryType
from .entity_platform import EntityPlatform as EntityPlatform
from .event import async_track_device_registry_updated_event as async_track_device_registry_updated_event, async_track_entity_registry_updated_event as async_track_entity_registry_updated_event
from .typing import StateType as StateType
from _typeshed import Incomplete
from abc import ABC
from collections.abc import Coroutine, Iterable, Mapping, MutableMapping
from datetime import datetime, timedelta
from enum import Enum
from homeassistant.config import DATA_CUSTOMIZE as DATA_CUSTOMIZE
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME, EntityCategory as EntityCategory, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, NoEntitySpecifiedError as NoEntitySpecifiedError
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import ensure_unique_string as ensure_unique_string, slugify as slugify
from typing import Any, Final, Literal, TypedDict

_LOGGER: Incomplete
SLOW_UPDATE_WARNING: int
DATA_ENTITY_SOURCE: str
SOURCE_CONFIG_ENTRY: str
SOURCE_PLATFORM_CONFIG: str
FLOAT_PRECISION: Incomplete

def async_setup(hass: HomeAssistant) -> None: ...
def entity_sources(hass: HomeAssistant) -> dict[str, dict[str, str]]: ...
def generate_entity_id(entity_id_format: str, name: str | None, current_ids: list[str] | None = ..., hass: HomeAssistant | None = ...) -> str: ...
def async_generate_entity_id(entity_id_format: str, name: str | None, current_ids: Iterable[str] | None = ..., hass: HomeAssistant | None = ...) -> str: ...
def get_capability(hass: HomeAssistant, entity_id: str, capability: str) -> Any | None: ...
def get_device_class(hass: HomeAssistant, entity_id: str) -> str | None: ...
def get_supported_features(hass: HomeAssistant, entity_id: str) -> int: ...
def get_unit_of_measurement(hass: HomeAssistant, entity_id: str) -> str | None: ...

class DeviceInfo(TypedDict, total=False):
    configuration_url: str | None
    connections: set[tuple[str, str]]
    default_manufacturer: str
    default_model: str
    default_name: str
    entry_type: DeviceEntryType | None
    identifiers: set[tuple[str, str]]
    manufacturer: str | None
    model: str | None
    name: str | None
    suggested_area: str | None
    sw_version: str | None
    hw_version: str | None
    via_device: tuple[str, str]

ENTITY_CATEGORIES_SCHEMA: Final[Incomplete]

class EntityPlatformState(Enum):
    NOT_ADDED: Incomplete
    ADDED: Incomplete
    REMOVED: Incomplete

class EntityDescription:
    key: str
    device_class: str | None
    entity_category: EntityCategory | None
    entity_registry_enabled_default: bool
    entity_registry_visible_default: bool
    force_update: bool
    icon: str | None
    has_entity_name: bool
    name: str | None
    translation_key: str | None
    unit_of_measurement: str | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class Entity(ABC):
    entity_id: str
    hass: HomeAssistant
    platform: EntityPlatform | None
    entity_description: EntityDescription
    _slow_reported: bool
    _disabled_reported: bool
    _async_update_ha_state_reported: bool
    _update_staged: bool
    parallel_updates: asyncio.Semaphore | None
    registry_entry: er.RegistryEntry | None
    _on_remove: list[CALLBACK_TYPE] | None
    _unsub_device_updates: CALLBACK_TYPE | None
    _context: Context | None
    _context_set: datetime | None
    _platform_state: Incomplete
    _attr_assumed_state: bool
    _attr_attribution: str | None
    _attr_available: bool
    _attr_capability_attributes: Mapping[str, Any] | None
    _attr_context_recent_time: timedelta
    _attr_device_class: str | None
    _attr_device_info: DeviceInfo | None
    _attr_entity_category: EntityCategory | None
    _attr_has_entity_name: bool
    _attr_entity_picture: str | None
    _attr_entity_registry_enabled_default: bool
    _attr_entity_registry_visible_default: bool
    _attr_extra_state_attributes: MutableMapping[str, Any]
    _attr_force_update: bool
    _attr_icon: str | None
    _attr_name: str | None
    _attr_should_poll: bool
    _attr_state: StateType
    _attr_supported_features: int | None
    _attr_translation_key: str | None
    _attr_unique_id: str | None
    _attr_unit_of_measurement: str | None
    @property
    def should_poll(self) -> bool: ...
    @property
    def unique_id(self) -> str | None: ...
    @property
    def has_entity_name(self) -> bool: ...
    @property
    def name(self) -> str | None: ...
    @property
    def state(self) -> StateType: ...
    @property
    def capability_attributes(self) -> Mapping[str, Any] | None: ...
    def get_initial_entity_options(self) -> er.EntityOptionsType | None: ...
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def device_state_attributes(self) -> Mapping[str, Any] | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    @property
    def device_info(self) -> DeviceInfo | None: ...
    @property
    def device_class(self) -> str | None: ...
    @property
    def unit_of_measurement(self) -> str | None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def force_update(self) -> bool: ...
    @property
    def supported_features(self) -> int | None: ...
    @property
    def context_recent_time(self) -> timedelta: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def entity_registry_visible_default(self) -> bool: ...
    @property
    def attribution(self) -> str | None: ...
    @property
    def entity_category(self) -> EntityCategory | None: ...
    @property
    def translation_key(self) -> str | None: ...
    @property
    def enabled(self) -> bool: ...
    def async_set_context(self, context: Context) -> None: ...
    async def async_update_ha_state(self, force_refresh: bool = ...) -> None: ...
    def async_write_ha_state(self) -> None: ...
    def _stringify_state(self, available: bool) -> str: ...
    def _friendly_name_internal(self) -> str | None: ...
    def _async_write_ha_state(self) -> None: ...
    def schedule_update_ha_state(self, force_refresh: bool = ...) -> None: ...
    def async_schedule_update_ha_state(self, force_refresh: bool = ...) -> None: ...
    def _async_slow_update_warning(self) -> None: ...
    async def async_device_update(self, warning: bool = ...) -> None: ...
    def async_on_remove(self, func: CALLBACK_TYPE) -> None: ...
    async def async_removed_from_registry(self) -> None: ...
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: asyncio.Semaphore | None) -> None: ...
    def _call_on_remove_callbacks(self) -> None: ...
    def add_to_platform_abort(self) -> None: ...
    async def add_to_platform_finish(self) -> None: ...
    async def async_remove(self, *, force_remove: bool = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def async_registry_entry_updated(self) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    async def async_internal_will_remove_from_hass(self) -> None: ...
    async def _async_registry_updated(self, event: Event) -> None: ...
    def _async_unsubscribe_device_updates(self) -> None: ...
    def _async_subscribe_device_updates(self) -> None: ...
    def __repr__(self) -> str: ...
    async def async_request_call(self, coro: Coroutine[Any, Any, Any]) -> None: ...
    def _suggest_report_issue(self) -> str: ...

class ToggleEntityDescription(EntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class ToggleEntity(Entity):
    entity_description: ToggleEntityDescription
    _attr_is_on: bool | None
    _attr_state: None
    @property
    def state(self) -> Literal['on', 'off'] | None: ...
    @property
    def is_on(self) -> bool | None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def toggle(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...
