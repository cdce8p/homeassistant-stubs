from collections.abc import Callable
from homeassistant import core as core
from homeassistant.components.websocket_api.const import JSON_DUMP as JSON_DUMP
from homeassistant.const import EVENT_STATE_CHANGED as EVENT_STATE_CHANGED
from homeassistant.helpers.entityfilter import convert_include_exclude_filter as convert_include_exclude_filter
from homeassistant.helpers.event import async_track_state_change as async_track_state_change, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from typing import TypeVar

_CallableT = TypeVar('_CallableT', bound=Callable)
BENCHMARKS: dict[str, Callable]

def run(args) -> None: ...
async def run_benchmark(bench) -> None: ...
def benchmark(func: _CallableT) -> _CallableT: ...
async def fire_events(hass): ...
async def fire_events_with_filter(hass): ...
async def state_changed_helper(hass): ...
async def state_changed_event_helper(hass): ...
async def state_changed_event_filter_helper(hass): ...
async def filtering_entity_id(hass): ...
async def valid_entity_id(hass): ...
async def json_serialize_states(hass): ...
def _create_state_changed_event_from_old_new(entity_id, event_time_fired, old_state, new_state): ...
