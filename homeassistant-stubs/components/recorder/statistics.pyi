from . import Recorder as Recorder
from .const import DATA_INSTANCE as DATA_INSTANCE, DOMAIN as DOMAIN, MAX_ROWS_TO_PURGE as MAX_ROWS_TO_PURGE
from .models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData, StatisticResult as StatisticResult, Statistics as Statistics, StatisticsMeta as StatisticsMeta, StatisticsRuns as StatisticsRuns, StatisticsShortTerm as StatisticsShortTerm, process_timestamp as process_timestamp, process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from .util import execute as execute, retryable_database_job as retryable_database_job, session_scope as session_scope
from collections.abc import Callable as Callable, Iterable
from datetime import datetime, timedelta
from homeassistant.const import PRESSURE_PA as PRESSURE_PA, TEMP_CELSIUS as TEMP_CELSIUS, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.util.unit_system import UnitSystem as UnitSystem
from sqlalchemy.orm.scoping import scoped_session as scoped_session
from statistics import mean
from typing import Any, Literal, overload

QUERY_STATISTICS: Any
QUERY_STATISTICS_SHORT_TERM: Any
QUERY_STATISTICS_SUMMARY_MEAN: Any
QUERY_STATISTICS_SUMMARY_SUM: Any
QUERY_STATISTICS_SUMMARY_SUM_LEGACY: Any
QUERY_STATISTIC_META: Any
QUERY_STATISTIC_META_ID: Any
STATISTICS_BAKERY: str
STATISTICS_META_BAKERY: str
STATISTICS_SHORT_TERM_BAKERY: str
STATISTIC_UNIT_TO_DISPLAY_UNIT_CONVERSIONS: Any
DISPLAY_UNIT_TO_STATISTIC_UNIT_CONVERSIONS: dict[str, Callable[[float, UnitSystem], float]]
_LOGGER: Any

def split_statistic_id(entity_id: str) -> list[str]: ...

VALID_STATISTIC_ID: Any

def valid_statistic_id(statistic_id: str) -> bool: ...
def validate_statistic_id(value: str) -> str: ...

class ValidationIssue:
    type: str
    data: Union[dict[str, Union[str, None]], None]
    def as_dict(self) -> dict: ...
    def __init__(self, type, data) -> None: ...

def async_setup(hass: HomeAssistant) -> None: ...
def get_start_time() -> datetime: ...
def _update_or_add_metadata(hass: HomeAssistant, session: scoped_session, new_metadata: StatisticMetaData) -> int: ...
def _find_duplicates(session: scoped_session, table: type[Union[Statistics, StatisticsShortTerm]]) -> tuple[list[int], list[dict]]: ...
def _delete_duplicates_from_table(session: scoped_session, table: type[Union[Statistics, StatisticsShortTerm]]) -> tuple[int, list[dict]]: ...
def delete_duplicates(instance: Recorder, session: scoped_session) -> None: ...
def compile_hourly_statistics(instance: Recorder, session: scoped_session, start: datetime) -> None: ...
def compile_statistics(instance: Recorder, start: datetime) -> bool: ...
def _adjust_sum_statistics(session: scoped_session, table: type[Union[Statistics, StatisticsShortTerm]], metadata_id: int, start_time: datetime, adj: float) -> None: ...
def _insert_statistics(session: scoped_session, table: type[Union[Statistics, StatisticsShortTerm]], metadata_id: int, statistic: StatisticData) -> None: ...
def _update_statistics(session: scoped_session, table: type[Union[Statistics, StatisticsShortTerm]], stat_id: int, statistic: StatisticData) -> None: ...
def get_metadata_with_session(hass: HomeAssistant, session: scoped_session, *, statistic_ids: Union[list[str], tuple[str], None] = ..., statistic_type: Union[Literal['mean'], Literal['sum'], None] = ..., statistic_source: Union[str, None] = ...) -> dict[str, tuple[int, StatisticMetaData]]: ...
def get_metadata(hass: HomeAssistant, *, statistic_ids: Union[list[str], tuple[str], None] = ..., statistic_type: Union[Literal['mean'], Literal['sum'], None] = ..., statistic_source: Union[str, None] = ...) -> dict[str, tuple[int, StatisticMetaData]]: ...
@overload
def _configured_unit(unit: None, units: UnitSystem) -> None: ...
@overload
def _configured_unit(unit: str, units: UnitSystem) -> str: ...
def clear_statistics(instance: Recorder, statistic_ids: list[str]) -> None: ...
def update_statistics_metadata(instance: Recorder, statistic_id: str, unit_of_measurement: Union[str, None]) -> None: ...
def list_statistic_ids(hass: HomeAssistant, statistic_ids: Union[list[str], tuple[str], None] = ..., statistic_type: Union[Literal['mean'], Literal['sum'], None] = ...) -> list[dict]: ...
def _statistics_during_period_query(hass: HomeAssistant, end_time: Union[datetime, None], statistic_ids: Union[list[str], None], bakery: Any, base_query: Iterable, table: type[Union[Statistics, StatisticsShortTerm]]) -> Callable: ...
def _reduce_statistics(stats: dict[str, list[dict[str, Any]]], same_period: Callable[[datetime, datetime], bool], period_start_end: Callable[[datetime], tuple[datetime, datetime]], period: timedelta) -> dict[str, list[dict[str, Any]]]: ...
def same_day(time1: datetime, time2: datetime) -> bool: ...
def day_start_end(time: datetime) -> tuple[datetime, datetime]: ...
def _reduce_statistics_per_day(stats: dict[str, list[dict[str, Any]]]) -> dict[str, list[dict[str, Any]]]: ...
def same_month(time1: datetime, time2: datetime) -> bool: ...
def month_start_end(time: datetime) -> tuple[datetime, datetime]: ...
def _reduce_statistics_per_month(stats: dict[str, list[dict[str, Any]]]) -> dict[str, list[dict[str, Any]]]: ...
def statistics_during_period(hass: HomeAssistant, start_time: datetime, end_time: Union[datetime, None] = ..., statistic_ids: Union[list[str], None] = ..., period: Literal['5minute', 'day', 'hour', 'month'] = ..., start_time_as_datetime: bool = ...) -> dict[str, list[dict[str, Any]]]: ...
def _get_last_statistics(hass: HomeAssistant, number_of_stats: int, statistic_id: str, convert_units: bool, table: type[Union[Statistics, StatisticsShortTerm]]) -> dict[str, list[dict]]: ...
def get_last_statistics(hass: HomeAssistant, number_of_stats: int, statistic_id: str, convert_units: bool) -> dict[str, list[dict]]: ...
def get_last_short_term_statistics(hass: HomeAssistant, number_of_stats: int, statistic_id: str, convert_units: bool) -> dict[str, list[dict]]: ...
def _statistics_at_time(session: scoped_session, metadata_ids: set[int], table: type[Union[Statistics, StatisticsShortTerm]], start_time: datetime) -> Union[list, None]: ...
def _sorted_statistics_to_dict(hass: HomeAssistant, session: scoped_session, stats: list, statistic_ids: Union[list[str], None], _metadata: dict[str, tuple[int, StatisticMetaData]], convert_units: bool, table: type[Union[Statistics, StatisticsShortTerm]], start_time: Union[datetime, None], start_time_as_datetime: bool = ...) -> dict[str, list[dict]]: ...
def validate_statistics(hass: HomeAssistant) -> dict[str, list[ValidationIssue]]: ...
def _statistics_exists(session: scoped_session, table: type[Union[Statistics, StatisticsShortTerm]], metadata_id: int, start: datetime) -> Union[int, None]: ...
def async_add_external_statistics(hass: HomeAssistant, metadata: StatisticMetaData, statistics: Iterable[StatisticData]) -> None: ...
def _filter_unique_constraint_integrity_error(instance: Recorder) -> Callable[[Exception], bool]: ...
def add_external_statistics(instance: Recorder, metadata: StatisticMetaData, statistics: Iterable[StatisticData]) -> bool: ...
def adjust_statistics(instance: Recorder, statistic_id: str, start_time: datetime, sum_adjustment: float) -> bool: ...
