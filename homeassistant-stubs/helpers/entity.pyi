import asyncio
from abc import ABC
from collections.abc import Mapping
from datetime import timedelta
from homeassistant.config import DATA_CUSTOMIZE as DATA_CUSTOMIZE
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, NoEntitySpecifiedError as NoEntitySpecifiedError
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from homeassistant.helpers.event import Event as Event, async_track_entity_registry_updated_event as async_track_entity_registry_updated_event
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import ensure_unique_string as ensure_unique_string, slugify as slugify
from typing import Any, Awaitable, Iterable

SLOW_UPDATE_WARNING: int
DATA_ENTITY_SOURCE: str
SOURCE_CONFIG_ENTRY: str
SOURCE_PLATFORM_CONFIG: str

def entity_sources(hass: HomeAssistant) -> dict[str, dict[str, str]]: ...
def generate_entity_id(entity_id_format: str, name: Union[str, None], current_ids: Union[list[str], None]=..., hass: Union[HomeAssistant, None]=...) -> str: ...
def async_generate_entity_id(entity_id_format: str, name: Union[str, None], current_ids: Union[Iterable[str], None]=..., hass: Union[HomeAssistant, None]=...) -> str: ...

class Entity(ABC):
    entity_id: str = ...
    hass: HomeAssistant = ...
    platform: Union[EntityPlatform, None] = ...
    parallel_updates: Union[asyncio.Semaphore, None] = ...
    registry_entry: Union[RegistryEntry, None] = ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def name(self) -> Union[str, None]: ...
    @property
    def state(self) -> StateType: ...
    @property
    def capability_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def device_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def device_info(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def entity_picture(self) -> Union[str, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def force_update(self) -> bool: ...
    @property
    def supported_features(self) -> Union[int, None]: ...
    @property
    def context_recent_time(self) -> timedelta: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def enabled(self) -> bool: ...
    def async_set_context(self, context: Context) -> None: ...
    async def async_update_ha_state(self, force_refresh: bool=...) -> None: ...
    def async_write_ha_state(self) -> None: ...
    def schedule_update_ha_state(self, force_refresh: bool=...) -> None: ...
    def async_schedule_update_ha_state(self, force_refresh: bool=...) -> None: ...
    async def async_device_update(self, warning: bool=...) -> None: ...
    def async_on_remove(self, func: CALLBACK_TYPE) -> None: ...
    async def async_removed_from_registry(self) -> None: ...
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: Union[asyncio.Semaphore, None]) -> None: ...
    def add_to_platform_abort(self) -> None: ...
    async def add_to_platform_finish(self) -> None: ...
    async def async_remove(self, *, force_remove: bool=...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    async def async_internal_will_remove_from_hass(self) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    async def async_request_call(self, coro: Awaitable) -> None: ...

class ToggleEntity(Entity):
    @property
    def state(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def toggle(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...