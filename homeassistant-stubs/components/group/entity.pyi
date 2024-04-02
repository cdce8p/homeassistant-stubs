import abc
from .const import ATTR_AUTO as ATTR_AUTO, ATTR_ORDER as ATTR_ORDER, DOMAIN as DOMAIN, GROUP_ORDER as GROUP_ORDER, REG_KEY as REG_KEY
from .registry import GroupIntegrationRegistry as GroupIntegrationRegistry
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable, Collection, Mapping
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, STATE_ON as STATE_ON
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers import start as start
from homeassistant.helpers.entity import Entity as Entity, async_generate_entity_id as async_generate_entity_id
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import EventStateChangedData as EventStateChangedData, async_track_state_change_event as async_track_state_change_event
from typing import Any

ENTITY_ID_FORMAT: Incomplete
_PACKAGE_LOGGER: Incomplete
_LOGGER: Incomplete

class GroupEntity(Entity, metaclass=abc.ABCMeta):
    _unrecorded_attributes: Incomplete
    _attr_should_poll: bool
    _entity_ids: list[str]
    def async_start_preview(self, preview_callback: Callable[[str, Mapping[str, Any]], None]) -> CALLBACK_TYPE: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_at_start(self, _: HomeAssistant) -> None: ...
    def async_defer_or_update_ha_state(self) -> None: ...
    @abstractmethod
    def async_update_group_state(self) -> None: ...
    def async_update_supported_features(self, entity_id: str, new_state: State | None) -> None: ...

class Group(Entity):
    _unrecorded_attributes: Incomplete
    _attr_should_poll: bool
    tracking: tuple[str, ...]
    trackable: tuple[str, ...]
    hass: Incomplete
    _name: Incomplete
    _state: Incomplete
    _icon: Incomplete
    _on_off: Incomplete
    _assumed: Incomplete
    _on_states: Incomplete
    created_by_service: Incomplete
    mode: Incomplete
    _order: Incomplete
    _assumed_state: bool
    _async_unsub_state_changed: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, *, created_by_service: bool, entity_ids: Collection[str] | None, icon: str | None, mode: bool | None, order: int | None) -> None: ...
    @staticmethod
    def async_create_group_entity(hass: HomeAssistant, name: str, *, created_by_service: bool, entity_ids: Collection[str] | None, icon: str | None, mode: bool | None, object_id: str | None, order: int | None) -> Group: ...
    @staticmethod
    async def async_create_group(hass: HomeAssistant, name: str, *, created_by_service: bool, entity_ids: Collection[str] | None, icon: str | None, mode: bool | None, object_id: str | None, order: int | None) -> Group: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def state(self) -> str | None: ...
    @property
    def icon(self) -> str | None: ...
    @icon.setter
    def icon(self, value: str | None) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def assumed_state(self) -> bool: ...
    def update_tracked_entity_ids(self, entity_ids: Collection[str] | None) -> None: ...
    async def async_update_tracked_entity_ids(self, entity_ids: Collection[str] | None) -> None: ...
    def _set_tracked(self, entity_ids: Collection[str] | None) -> None: ...
    def _async_start(self, _: HomeAssistant | None = None) -> None: ...
    def _async_start_tracking(self) -> None: ...
    def _async_stop(self) -> None: ...
    def async_update_group_state(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def _async_state_changed_listener(self, event: Event[EventStateChangedData]) -> None: ...
    def _reset_tracked_state(self) -> None: ...
    def _see_state(self, new_state: State) -> None: ...
    def _async_update_group_state(self, tr_state: State | None = None) -> None: ...

def async_get_component(hass: HomeAssistant) -> EntityComponent[Group]: ...