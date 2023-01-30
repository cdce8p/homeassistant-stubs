from . import Recorder as Recorder
from .const import DOMAIN as DOMAIN, EVENT_RECORDER_5MIN_STATISTICS_GENERATED as EVENT_RECORDER_5MIN_STATISTICS_GENERATED, EVENT_RECORDER_HOURLY_STATISTICS_GENERATED as EVENT_RECORDER_HOURLY_STATISTICS_GENERATED, MAX_ROWS_TO_PURGE as MAX_ROWS_TO_PURGE, SupportedDialect as SupportedDialect
from .db_schema import Statistics as Statistics, StatisticsBase as StatisticsBase, StatisticsMeta as StatisticsMeta, StatisticsRuns as StatisticsRuns, StatisticsShortTerm as StatisticsShortTerm
from .models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData, StatisticResult as StatisticResult, process_timestamp as process_timestamp
from .util import execute as execute, execute_stmt_lambda_element as execute_stmt_lambda_element, get_instance as get_instance, retryable_database_job as retryable_database_job, session_scope as session_scope
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from datetime import datetime, timedelta
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback, valid_entity_id as valid_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from homeassistant.helpers.start import async_at_start as async_at_start
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.util.unit_conversion import BaseUnitConverter as BaseUnitConverter, DistanceConverter as DistanceConverter, EnergyConverter as EnergyConverter, MassConverter as MassConverter, PowerConverter as PowerConverter, PressureConverter as PressureConverter, SpeedConverter as SpeedConverter, TemperatureConverter as TemperatureConverter, UnitlessRatioConverter as UnitlessRatioConverter, VolumeConverter as VolumeConverter
from sqlalchemy.engine import Engine as Engine
from sqlalchemy.engine.row import Row as Row
from sqlalchemy.orm.session import Session as Session
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlalchemy.sql.selectable import Subquery as Subquery
from statistics import mean
from typing import Any, Literal

QUERY_STATISTICS: Incomplete
QUERY_STATISTICS_SHORT_TERM: Incomplete
QUERY_STATISTICS_SUMMARY_MEAN: Incomplete
QUERY_STATISTICS_SUMMARY_SUM: Incomplete
QUERY_STATISTIC_META: Incomplete
STATISTIC_UNIT_TO_UNIT_CONVERTER: dict[Union[str, None], type[BaseUnitConverter]]
_LOGGER: Incomplete

def _get_unit_class(unit: Union[str, None]) -> Union[str, None]: ...
def get_display_unit(hass: HomeAssistant, statistic_id: str, statistic_unit: Union[str, None]) -> Union[str, None]: ...
def _get_statistic_to_display_unit_converter(statistic_unit: Union[str, None], state_unit: Union[str, None], requested_units: Union[dict[str, str], None]) -> Callable[[Union[float, None]], Union[float, None]]: ...
def _get_display_to_statistic_unit_converter(display_unit: Union[str, None], statistic_unit: Union[str, None]) -> Callable[[float], float]: ...
def _get_unit_converter(from_unit: str, to_unit: str) -> Callable[[Union[float, None]], Union[float, None]]: ...
def can_convert_units(from_unit: Union[str, None], to_unit: Union[str, None]) -> bool: ...

class PlatformCompiledStatistics:
    platform_stats: list[StatisticResult]
    current_metadata: dict[str, tuple[int, StatisticMetaData]]
    def __init__(self, platform_stats, current_metadata) -> None: ...

def split_statistic_id(entity_id: str) -> list[str]: ...

VALID_STATISTIC_ID: Incomplete

def valid_statistic_id(statistic_id: str) -> bool: ...
def validate_statistic_id(value: str) -> str: ...

class ValidationIssue:
    type: str
    data: Union[dict[str, Union[str, None]], None]
    def as_dict(self) -> dict: ...
    def __init__(self, type, data) -> None: ...

def async_setup(hass: HomeAssistant) -> None: ...
def get_start_time() -> datetime: ...
def _update_or_add_metadata(session: Session, new_metadata: StatisticMetaData, old_metadata_dict: dict[str, tuple[int, StatisticMetaData]]) -> int: ...
def _find_duplicates(session: Session, table: type[Union[Statistics, StatisticsShortTerm]]) -> tuple[list[int], list[dict]]: ...
def _delete_duplicates_from_table(session: Session, table: type[Union[Statistics, StatisticsShortTerm]]) -> tuple[int, list[dict]]: ...
def delete_statistics_duplicates(hass: HomeAssistant, session: Session) -> None: ...
def _find_statistics_meta_duplicates(session: Session) -> list[int]: ...
def _delete_statistics_meta_duplicates(session: Session) -> int: ...
def delete_statistics_meta_duplicates(session: Session) -> None: ...
def _compile_hourly_statistics_summary_mean_stmt(start_time: datetime, end_time: datetime) -> StatementLambdaElement: ...
def _compile_hourly_statistics(session: Session, start: datetime) -> None: ...
def compile_statistics(instance: Recorder, start: datetime, fire_events: bool) -> bool: ...
def _adjust_sum_statistics(session: Session, table: type[Union[Statistics, StatisticsShortTerm]], metadata_id: int, start_time: datetime, adj: float) -> None: ...
def _insert_statistics(session: Session, table: type[Union[Statistics, StatisticsShortTerm]], metadata_id: int, statistic: StatisticData) -> None: ...
def _update_statistics(session: Session, table: type[Union[Statistics, StatisticsShortTerm]], stat_id: int, statistic: StatisticData) -> None: ...
def _generate_get_metadata_stmt(statistic_ids: Union[list[str], None] = ..., statistic_type: Union[Literal['mean'], Literal['sum'], None] = ..., statistic_source: Union[str, None] = ...) -> StatementLambdaElement: ...
def get_metadata_with_session(session: Session, *, statistic_ids: Union[list[str], None] = ..., statistic_type: Union[Literal['mean'], Literal['sum'], None] = ..., statistic_source: Union[str, None] = ...) -> dict[str, tuple[int, StatisticMetaData]]: ...
def get_metadata(hass: HomeAssistant, *, statistic_ids: Union[list[str], None] = ..., statistic_type: Union[Literal['mean'], Literal['sum'], None] = ..., statistic_source: Union[str, None] = ...) -> dict[str, tuple[int, StatisticMetaData]]: ...
def _clear_statistics_with_session(session: Session, statistic_ids: list[str]) -> None: ...
def clear_statistics(instance: Recorder, statistic_ids: list[str]) -> None: ...
def update_statistics_metadata(instance: Recorder, statistic_id: str, new_statistic_id: Union[str, None, UndefinedType], new_unit_of_measurement: Union[str, None, UndefinedType]) -> None: ...
def list_statistic_ids(hass: HomeAssistant, statistic_ids: Union[list[str], None] = ..., statistic_type: Union[Literal['mean'], Literal['sum'], None] = ...) -> list[dict]: ...
def _reduce_statistics(stats: dict[str, list[dict[str, Any]]], same_period: Callable[[datetime, datetime], bool], period_start_end: Callable[[datetime], tuple[datetime, datetime]], period: timedelta, types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict[str, Any]]]: ...
def same_day(time1: datetime, time2: datetime) -> bool: ...
def day_start_end(time: datetime) -> tuple[datetime, datetime]: ...
def _reduce_statistics_per_day(stats: dict[str, list[dict[str, Any]]], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict[str, Any]]]: ...
def same_week(time1: datetime, time2: datetime) -> bool: ...
def week_start_end(time: datetime) -> tuple[datetime, datetime]: ...
def _reduce_statistics_per_week(stats: dict[str, list[dict[str, Any]]], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict[str, Any]]]: ...
def same_month(time1: datetime, time2: datetime) -> bool: ...
def month_start_end(time: datetime) -> tuple[datetime, datetime]: ...
def _reduce_statistics_per_month(stats: dict[str, list[dict[str, Any]]], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict[str, Any]]]: ...
def _statistics_during_period_stmt(start_time: datetime, end_time: Union[datetime, None], metadata_ids: Union[list[int], None], table: type[Union[Statistics, StatisticsShortTerm]], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> StatementLambdaElement: ...
def _get_max_mean_min_statistic_in_sub_period(session: Session, result: dict[str, float], start_time: Union[datetime, None], end_time: Union[datetime, None], table: type[Union[Statistics, StatisticsShortTerm]], types: set[Literal['max', 'mean', 'min', 'change']], metadata_id: int) -> None: ...
def _get_max_mean_min_statistic(session: Session, head_start_time: Union[datetime, None], head_end_time: Union[datetime, None], main_start_time: Union[datetime, None], main_end_time: Union[datetime, None], tail_start_time: Union[datetime, None], tail_end_time: Union[datetime, None], tail_only: bool, metadata_id: int, types: set[Literal['max', 'mean', 'min', 'change']]) -> dict[str, Union[float, None]]: ...
def _first_statistic(session: Session, table: type[Union[Statistics, StatisticsShortTerm]], metadata_id: int) -> Union[datetime, None]: ...
def _get_oldest_sum_statistic(session: Session, head_start_time: Union[datetime, None], main_start_time: Union[datetime, None], tail_start_time: Union[datetime, None], oldest_stat: Union[datetime, None], tail_only: bool, metadata_id: int) -> Union[float, None]: ...
def _get_newest_sum_statistic(session: Session, head_start_time: Union[datetime, None], head_end_time: Union[datetime, None], main_start_time: Union[datetime, None], main_end_time: Union[datetime, None], tail_start_time: Union[datetime, None], tail_end_time: Union[datetime, None], tail_only: bool, metadata_id: int) -> Union[float, None]: ...
def statistic_during_period(hass: HomeAssistant, start_time: Union[datetime, None], end_time: Union[datetime, None], statistic_id: str, types: Union[set[Literal['max', 'mean', 'min', 'change']], None], units: Union[dict[str, str], None]) -> dict[str, Any]: ...
def _statistics_during_period_with_session(hass: HomeAssistant, session: Session, start_time: datetime, end_time: Union[datetime, None], statistic_ids: Union[list[str], None], period: Literal['5minute', 'day', 'hour', 'week', 'month'], units: Union[dict[str, str], None], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict[str, Any]]]: ...
def statistics_during_period(hass: HomeAssistant, start_time: datetime, end_time: Union[datetime, None], statistic_ids: Union[list[str], None], period: Literal['5minute', 'day', 'hour', 'week', 'month'], units: Union[dict[str, str], None], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict[str, Any]]]: ...
def _get_last_statistics_stmt(metadata_id: int, number_of_stats: int) -> StatementLambdaElement: ...
def _get_last_statistics_short_term_stmt(metadata_id: int, number_of_stats: int) -> StatementLambdaElement: ...
def _get_last_statistics(hass: HomeAssistant, number_of_stats: int, statistic_id: str, convert_units: bool, table: type[Union[Statistics, StatisticsShortTerm]], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict]]: ...
def get_last_statistics(hass: HomeAssistant, number_of_stats: int, statistic_id: str, convert_units: bool, types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict]]: ...
def get_last_short_term_statistics(hass: HomeAssistant, number_of_stats: int, statistic_id: str, convert_units: bool, types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict]]: ...
def _generate_most_recent_statistic_row(metadata_ids: list[int]) -> Subquery: ...
def _latest_short_term_statistics_stmt(metadata_ids: list[int]) -> StatementLambdaElement: ...
def get_latest_short_term_statistics(hass: HomeAssistant, statistic_ids: list[str], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']], metadata: Union[dict[str, tuple[int, StatisticMetaData]], None] = ...) -> dict[str, list[dict]]: ...
def _statistics_at_time(session: Session, metadata_ids: set[int], table: type[Union[Statistics, StatisticsShortTerm]], start_time: datetime, types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> Union[list, None]: ...
def _sorted_statistics_to_dict(hass: HomeAssistant, session: Session, stats: Iterable[Row], statistic_ids: Union[list[str], None], _metadata: dict[str, tuple[int, StatisticMetaData]], convert_units: bool, table: type[Union[Statistics, StatisticsShortTerm]], start_time: Union[datetime, None], units: Union[dict[str, str], None], types: set[Literal['last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> dict[str, list[dict]]: ...
def validate_statistics(hass: HomeAssistant) -> dict[str, list[ValidationIssue]]: ...
def _statistics_exists(session: Session, table: type[Union[Statistics, StatisticsShortTerm]], metadata_id: int, start: datetime) -> Union[int, None]: ...
def _async_import_statistics(hass: HomeAssistant, metadata: StatisticMetaData, statistics: Iterable[StatisticData]) -> None: ...
def async_import_statistics(hass: HomeAssistant, metadata: StatisticMetaData, statistics: Iterable[StatisticData]) -> None: ...
def async_add_external_statistics(hass: HomeAssistant, metadata: StatisticMetaData, statistics: Iterable[StatisticData]) -> None: ...
def _filter_unique_constraint_integrity_error(instance: Recorder) -> Callable[[Exception], bool]: ...
def _import_statistics_with_session(session: Session, metadata: StatisticMetaData, statistics: Iterable[StatisticData], table: type[Union[Statistics, StatisticsShortTerm]]) -> bool: ...
def import_statistics(instance: Recorder, metadata: StatisticMetaData, statistics: Iterable[StatisticData], table: type[Union[Statistics, StatisticsShortTerm]]) -> bool: ...
def adjust_statistics(instance: Recorder, statistic_id: str, start_time: datetime, sum_adjustment: float, adjustment_unit: str) -> bool: ...
def _change_statistics_unit_for_table(session: Session, table: type[StatisticsBase], metadata_id: int, convert: Callable[[Union[float, None]], Union[float, None]]) -> None: ...
def change_statistics_unit(instance: Recorder, statistic_id: str, new_unit: str, old_unit: str) -> None: ...
def async_change_statistics_unit(hass: HomeAssistant, statistic_id: str, *, new_unit_of_measurement: str, old_unit_of_measurement: str) -> None: ...
def _validate_db_schema_utf8(instance: Recorder, session_maker: Callable[[], Session]) -> set[str]: ...
def _validate_db_schema(hass: HomeAssistant, instance: Recorder, session_maker: Callable[[], Session]) -> set[str]: ...
def validate_db_schema(hass: HomeAssistant, instance: Recorder, session_maker: Callable[[], Session]) -> set[str]: ...
def correct_db_schema(instance: Recorder, engine: Engine, session_maker: Callable[[], Session], schema_errors: set[str]) -> None: ...
