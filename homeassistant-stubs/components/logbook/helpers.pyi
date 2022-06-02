from .const import ALL_EVENT_TYPES_EXCEPT_STATE_CHANGED as ALL_EVENT_TYPES_EXCEPT_STATE_CHANGED, DOMAIN as DOMAIN, ENTITY_EVENTS_WITHOUT_CONFIG_ENTRY as ENTITY_EVENTS_WITHOUT_CONFIG_ENTRY
from .models import LazyEventPartialState as LazyEventPartialState
from collections.abc import Callable as Callable
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, EVENT_LOGBOOK_ENTRY as EVENT_LOGBOOK_ENTRY, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback, is_callback as is_callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event

def async_filter_entities(hass: HomeAssistant, entity_ids: list[str]) -> list[str]: ...
def async_determine_event_types(hass: HomeAssistant, entity_ids: Union[list[str], None], device_ids: Union[list[str], None]) -> tuple[str, ...]: ...
def async_subscribe_events(hass: HomeAssistant, subscriptions: list[CALLBACK_TYPE], target: Callable[[Event], None], event_types: tuple[str, ...], entity_ids: Union[list[str], None], device_ids: Union[list[str], None]) -> None: ...
def is_sensor_continuous(ent_reg: er.EntityRegistry, entity_id: str) -> bool: ...
def _is_state_filtered(ent_reg: er.EntityRegistry, state: State) -> bool: ...
def _is_entity_id_filtered(hass: HomeAssistant, ent_reg: er.EntityRegistry, entity_id: str) -> bool: ...