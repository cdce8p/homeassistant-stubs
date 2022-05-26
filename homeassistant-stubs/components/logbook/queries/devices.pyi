from .common import EVENT_DATA_JSON as EVENT_DATA_JSON, select_events_context_id_subquery as select_events_context_id_subquery, select_events_context_only as select_events_context_only, select_events_without_states as select_events_without_states, select_states_context_only as select_states_context_only
from collections.abc import Iterable
from datetime import datetime as dt
from homeassistant.components.recorder.models import Events as Events, States as States
from sqlalchemy import Column as Column
from sqlalchemy.orm import Query as Query
from sqlalchemy.sql.elements import ClauseList as ClauseList
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlalchemy.sql.selectable import CTE as CTE, CompoundSelect as CompoundSelect

DEVICE_ID_IN_EVENT: Column

def _select_device_id_context_ids_sub_query(start_day: dt, end_day: dt, event_types: tuple[str, ...], json_quotable_device_ids: list[str]) -> CompoundSelect: ...
def _apply_devices_context_union(query: Query, start_day: dt, end_day: dt, event_types: tuple[str, ...], json_quotable_device_ids: list[str]) -> CompoundSelect: ...
def devices_stmt(start_day: dt, end_day: dt, event_types: tuple[str, ...], json_quotable_device_ids: list[str]) -> StatementLambdaElement: ...
def apply_event_device_id_matchers(json_quotable_device_ids: Iterable[str]) -> ClauseList: ...
