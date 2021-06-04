from . import Recorder as Recorder
from .const import DOMAIN as DOMAIN
from .models import Statistics as Statistics, process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from .util import execute as execute, retryable_database_job as retryable_database_job, session_scope as session_scope
from datetime import datetime as datetime
from typing import Any, Optional

QUERY_STATISTICS: Any
STATISTICS_BAKERY: str
_LOGGER: Any

def async_setup(hass: Any) -> None: ...
def get_start_time() -> datetime.datetime: ...
def compile_statistics(instance: Recorder, start: datetime.datetime) -> bool: ...
def statistics_during_period(hass: Any, start_time: Any, end_time: Optional[Any] = ..., statistic_id: Optional[Any] = ...): ...
def get_last_statistics(hass: Any, number_of_stats: Any, statistic_id: Optional[Any] = ...): ...
def _sorted_statistics_to_dict(stats: Any, statistic_ids: Any): ...