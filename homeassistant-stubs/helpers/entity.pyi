import asyncio
import dataclasses
from . import device_registry as dr, entity_registry as er
from .device_registry import DeviceInfo as DeviceInfo, EventDeviceRegistryUpdatedData as EventDeviceRegistryUpdatedData
from .entity_platform import EntityPlatform as EntityPlatform
from .event import async_track_device_registry_updated_event as async_track_device_registry_updated_event, async_track_entity_registry_updated_event as async_track_entity_registry_updated_event
from .typing import EventType as EventType, StateType as StateType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from abc import ABCMeta
from collections import deque
from collections.abc import Callable as Callable, Coroutine, Iterable, Mapping, MutableMapping
from enum import Enum, IntFlag
from functools import cached_property as cached_property
from homeassistant.config import DATA_CUSTOMIZE as DATA_CUSTOMIZE
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME, EntityCategory as EntityCategory, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HomeAssistant as HomeAssistant, callback as callback, get_release_channel as get_release_channel
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, InvalidStateError as InvalidStateError, NoEntitySpecifiedError as NoEntitySpecifiedError
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue, bind_hass as bind_hass
from homeassistant.util import ensure_unique_string as ensure_unique_string, slugify as slugify
from homeassistant.util.frozen_dataclass_compat import FrozenOrThawed as FrozenOrThawed
from typing import Any, Final, Literal, NotRequired, TypeVar, TypedDict

_T = TypeVar('_T')
_LOGGER: Incomplete
SLOW_UPDATE_WARNING: int
DATA_ENTITY_SOURCE: str
FLOAT_PRECISION: Incomplete
CAPABILITIES_UPDATE_LIMIT: int
CONTEXT_RECENT_TIME_SECONDS: int

def async_setup(hass: HomeAssistant) -> None: ...
def entity_sources(hass: HomeAssistant) -> dict[str, EntityInfo]: ...
def generate_entity_id(entity_id_format: str, name: str | None, current_ids: list[str] | None = None, hass: HomeAssistant | None = None) -> str: ...
def async_generate_entity_id(entity_id_format: str, name: str | None, current_ids: Iterable[str] | None = None, hass: HomeAssistant | None = None) -> str: ...
def get_capability(hass: HomeAssistant, entity_id: str, capability: str) -> Any | None: ...
def get_device_class(hass: HomeAssistant, entity_id: str) -> str | None: ...
def get_supported_features(hass: HomeAssistant, entity_id: str) -> int: ...
def get_unit_of_measurement(hass: HomeAssistant, entity_id: str) -> str | None: ...

ENTITY_CATEGORIES_SCHEMA: Final[Incomplete]

class EntityInfo(TypedDict):
    domain: str
    custom_component: bool
    config_entry: NotRequired[str]

class StateInfo(TypedDict):
    unrecorded_attributes: frozenset[str]

class EntityPlatformState(Enum):
    NOT_ADDED: Incomplete
    ADDED: Incomplete
    REMOVED: Incomplete

_SENTINEL: Incomplete

class EntityDescription(frozen_or_thawed=True, metaclass=FrozenOrThawed):
    key: str
    device_class: str | None
    entity_category: EntityCategory | None
    entity_registry_enabled_default: bool
    entity_registry_visible_default: bool
    force_update: bool
    icon: str | None
    has_entity_name: bool
    name: str | UndefinedType | None
    translation_key: str | None
    translation_placeholders: Mapping[str, str] | None
    unit_of_measurement: str | None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

@dataclasses.dataclass(frozen=True, slots=True)
class CalculatedState:
    state: str
    attributes: dict[str, Any]
    capability_attributes: Mapping[str, Any] | None
    shadowed_attributes: Mapping[str, Any]
    def __init__(self, state, attributes, capability_attributes, shadowed_attributes) -> None: ...

class CachedProperties(type):
    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: dict[Any, Any], cached_properties: set[str] | None = None, **kwargs: Any) -> Any: ...
    def __init__(cls, name: str, bases: tuple[type, ...], namespace: dict[Any, Any], **kwargs: Any) -> None: ...

class ABCCachedProperties(CachedProperties, ABCMeta): ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class Entity(cached_properties=CACHED_PROPERTIES_WITH_ATTR_, metaclass=ABCCachedProperties):
    entity_id: str
    hass: HomeAssistant
    platform: EntityPlatform
    entity_description: EntityDescription
    _slow_reported: bool
    _deprecated_supported_features_reported: bool
    _disabled_reported: bool
    _async_update_ha_state_reported: bool
    _no_platform_reported: bool
    _name_translation_placeholders_reported: bool
    _update_staged: bool
    parallel_updates: asyncio.Semaphore | None
    registry_entry: er.RegistryEntry | None
    device_entry: dr.DeviceEntry | None
    _on_remove: list[CALLBACK_TYPE] | None
    _unsub_device_updates: CALLBACK_TYPE | None
    _context: Context | None
    _context_set: float | None
    _platform_state: Incomplete
    _entity_component_unrecorded_attributes: frozenset[str]
    _unrecorded_attributes: frozenset[str]
    __combined_unrecorded_attributes: frozenset[str]
    _state_info: StateInfo
    __capabilities_updated_at: deque[float]
    __capabilities_updated_at_reported: bool
    __remove_event: asyncio.Event | None
    _attr_assumed_state: bool
    _attr_attribution: str | None
    _attr_available: bool
    _attr_capability_attributes: Mapping[str, Any] | None
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
    _attr_translation_placeholders: Mapping[str, str]
    _attr_unique_id: str | None
    _attr_unit_of_measurement: str | None
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    @cached_property
    def should_poll(self) -> bool: ...
    @cached_property
    def unique_id(self) -> str | None: ...
    @property
    def use_device_name(self) -> bool: ...
    @cached_property
    def has_entity_name(self) -> bool: ...
    def _device_class_name_helper(self, component_translations: dict[str, Any]) -> str | None: ...
    @cached_property
    def _object_id_device_class_name(self) -> str | None: ...
    @cached_property
    def _device_class_name(self) -> str | None: ...
    def _default_to_device_class_name(self) -> bool: ...
    @cached_property
    def _name_translation_key(self) -> str | None: ...
    def _substitute_name_placeholders(self, name: str) -> str: ...
    def _name_internal(self, device_class_name: str | None, platform_translations: dict[str, Any]) -> str | UndefinedType | None: ...
    @property
    def suggested_object_id(self) -> str | None: ...
    @cached_property
    def name(self) -> str | UndefinedType | None: ...
    @cached_property
    def state(self) -> StateType: ...
    @cached_property
    def capability_attributes(self) -> Mapping[str, Any] | None: ...
    def get_initial_entity_options(self) -> er.EntityOptionsType | None: ...
    @cached_property
    def state_attributes(self) -> dict[str, Any] | None: ...
    @cached_property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    @cached_property
    def device_info(self) -> DeviceInfo | None: ...
    @cached_property
    def device_class(self) -> str | None: ...
    @cached_property
    def unit_of_measurement(self) -> str | None: ...
    @cached_property
    def icon(self) -> str | None: ...
    @cached_property
    def entity_picture(self) -> str | None: ...
    @cached_property
    def available(self) -> bool: ...
    @cached_property
    def assumed_state(self) -> bool: ...
    @cached_property
    def force_update(self) -> bool: ...
    @cached_property
    def supported_features(self) -> int | None: ...
    @cached_property
    def entity_registry_enabled_default(self) -> bool: ...
    @cached_property
    def entity_registry_visible_default(self) -> bool: ...
    @cached_property
    def attribution(self) -> str | None: ...
    @cached_property
    def entity_category(self) -> EntityCategory | None: ...
    @cached_property
    def translation_key(self) -> str | None: ...
    @cached_property
    def translation_placeholders(self) -> Mapping[str, str]: ...
    @property
    def enabled(self) -> bool: ...
    def async_set_context(self, context: Context) -> None: ...
    async def async_update_ha_state(self, force_refresh: bool = False) -> None: ...
    def async_write_ha_state(self) -> None: ...
    def _stringify_state(self, available: bool) -> str: ...
    def _friendly_name_internal(self) -> str | None: ...
    def _async_calculate_state(self) -> CalculatedState: ...
    def __async_calculate_state(self) -> tuple[str, dict[str, Any], Mapping[str, Any] | None, Mapping[str, Any]]: ...
    def _async_write_ha_state(self) -> None: ...
    def schedule_update_ha_state(self, force_refresh: bool = False) -> None: ...
    def async_schedule_update_ha_state(self, force_refresh: bool = False) -> None: ...
    def _async_slow_update_warning(self) -> None: ...
    async def async_device_update(self, warning: bool = True) -> None: ...
    def async_on_remove(self, func: CALLBACK_TYPE) -> None: ...
    async def async_removed_from_registry(self) -> None: ...
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: asyncio.Semaphore | None) -> None: ...
    def _call_on_remove_callbacks(self) -> None: ...
    def add_to_platform_abort(self) -> None: ...
    async def add_to_platform_finish(self) -> None: ...
    async def async_remove(self, *, force_remove: bool = False) -> None: ...
    async def __async_remove_impl(self, force_remove: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def async_registry_entry_updated(self) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    async def async_internal_will_remove_from_hass(self) -> None: ...
    async def _async_registry_updated(self, event: EventType[er.EventEntityRegistryUpdatedData]) -> None: ...
    def _async_unsubscribe_device_updates(self) -> None: ...
    def _async_device_registry_updated(self, event: EventType[EventDeviceRegistryUpdatedData]) -> None: ...
    def _async_subscribe_device_updates(self) -> None: ...
    def __repr__(self) -> str: ...
    async def async_request_call(self, coro: Coroutine[Any, Any, _T]) -> _T: ...
    def _suggest_report_issue(self) -> str: ...
    def _report_deprecated_supported_features_values(self, replacement: IntFlag) -> None: ...

class ToggleEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

TOGGLE_ENTITY_CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class ToggleEntity(Entity, cached_properties=TOGGLE_ENTITY_CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: ToggleEntityDescription
    _attr_is_on: bool | None
    _attr_state: None
    @property
    def state(self) -> Literal['on', 'off'] | None: ...
    @cached_property
    def is_on(self) -> bool | None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def toggle(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...
