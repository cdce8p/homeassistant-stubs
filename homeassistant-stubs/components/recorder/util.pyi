from . import Recorder as Recorder
from .const import DEFAULT_MAX_BIND_VARS as DEFAULT_MAX_BIND_VARS, DOMAIN as DOMAIN, SQLITE_MAX_BIND_VARS as SQLITE_MAX_BIND_VARS, SQLITE_MODERN_MAX_BIND_VARS as SQLITE_MODERN_MAX_BIND_VARS, SQLITE_URL_PREFIX as SQLITE_URL_PREFIX, SupportedDialect as SupportedDialect
from .db_schema import RecorderRuns as RecorderRuns, TABLES_TO_CHECK as TABLES_TO_CHECK, TABLE_RECORDER_RUNS as TABLE_RECORDER_RUNS, TABLE_SCHEMA_CHANGES as TABLE_SCHEMA_CHANGES
from .models import DatabaseEngine as DatabaseEngine, DatabaseOptimizer as DatabaseOptimizer, StatisticPeriod as StatisticPeriod, UnsupportedDialect as UnsupportedDialect, process_timestamp as process_timestamp
from _typeshed import Incomplete
from awesomeversion import AwesomeVersion
from collections.abc import Callable, Generator, Sequence
from datetime import date, datetime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.recorder import DATA_INSTANCE as DATA_INSTANCE, get_instance as get_instance, session_scope as session_scope
from sqlalchemy.engine import Result as Result, Row as Row
from sqlalchemy.engine.interfaces import DBAPIConnection as DBAPIConnection
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.query import Query as Query
from sqlalchemy.orm.session import Session as Session
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlite3.dbapi2 import Cursor as SQLiteCursor
from typing import Any, Concatenate, NoReturn

_LOGGER: Incomplete
RETRIES: int
QUERY_RETRY_WAIT: float
SQLITE3_POSTFIXES: Incomplete
DEFAULT_YIELD_STATES_ROWS: int

def _simple_version(version: str) -> AwesomeVersion: ...

MIN_VERSION_MARIA_DB: Incomplete
RECOMMENDED_MIN_VERSION_MARIA_DB: Incomplete
MARIADB_WITH_FIXED_IN_QUERIES_105: Incomplete
MARIA_DB_106: Incomplete
MARIADB_WITH_FIXED_IN_QUERIES_106: Incomplete
RECOMMENDED_MIN_VERSION_MARIA_DB_106: Incomplete
MARIA_DB_107: Incomplete
RECOMMENDED_MIN_VERSION_MARIA_DB_107: Incomplete
MARIADB_WITH_FIXED_IN_QUERIES_107: Incomplete
MARIA_DB_108: Incomplete
RECOMMENDED_MIN_VERSION_MARIA_DB_108: Incomplete
MARIADB_WITH_FIXED_IN_QUERIES_108: Incomplete
MIN_VERSION_MYSQL: Incomplete
MIN_VERSION_PGSQL: Incomplete
MIN_VERSION_SQLITE: Incomplete
UPCOMING_MIN_VERSION_SQLITE: Incomplete
MIN_VERSION_SQLITE_MODERN_BIND_VARS: Incomplete
MAX_RESTART_TIME: Incomplete
RETRYABLE_MYSQL_ERRORS: Incomplete
FIRST_POSSIBLE_SUNDAY: int
SUNDAY_WEEKDAY: int
DAYS_IN_WEEK: int

def execute(qry: Query, to_native: bool = False, validate_entity_ids: bool = True) -> list[Row]: ...
def execute_stmt_lambda_element(session: Session, stmt: StatementLambdaElement, start_time: datetime | None = None, end_time: datetime | None = None, yield_per: int = ..., orm_rows: bool = True) -> Sequence[Row] | Result: ...
def validate_or_move_away_sqlite_database(dburl: str) -> bool: ...
def dburl_to_path(dburl: str) -> str: ...
def last_run_was_recently_clean(cursor: SQLiteCursor) -> bool: ...
def basic_sanity_check(cursor: SQLiteCursor) -> bool: ...
def validate_sqlite_database(dbpath: str) -> bool: ...
def run_checks_on_open_db(dbpath: str, cursor: SQLiteCursor) -> None: ...
def move_away_broken_database(dbfile: str) -> None: ...
def execute_on_connection(dbapi_connection: DBAPIConnection, statement: str) -> None: ...
def query_on_connection(dbapi_connection: DBAPIConnection, statement: str) -> Any: ...
def _fail_unsupported_dialect(dialect_name: str) -> NoReturn: ...
def _raise_if_version_unsupported(server_version: str, dialect_name: str, minimum_version: str) -> NoReturn: ...
def _async_delete_issue_deprecated_version(hass: HomeAssistant, dialect_name: str) -> None: ...
def _async_create_issue_deprecated_version(hass: HomeAssistant, server_version: AwesomeVersion, dialect_name: str, min_version: AwesomeVersion) -> None: ...
def _extract_version_from_server_response_or_raise(server_response: str) -> AwesomeVersion: ...
def _extract_version_from_server_response(server_response: str) -> AwesomeVersion | None: ...
def _datetime_or_none(value: str) -> datetime | None: ...
def build_mysqldb_conv() -> dict: ...
def _async_create_mariadb_range_index_regression_issue(hass: HomeAssistant, version: AwesomeVersion) -> None: ...
def async_create_backup_failure_issue(hass: HomeAssistant, local_start_time: datetime) -> None: ...
def setup_connection_for_dialect(instance: Recorder, dialect_name: str, dbapi_connection: DBAPIConnection, first_connection: bool) -> DatabaseEngine | None: ...
def end_incomplete_runs(session: Session, start_time: datetime) -> None: ...
def _is_retryable_error(instance: Recorder, err: OperationalError) -> bool: ...
type _FuncType[**P, R] = Callable[Concatenate[Recorder, P], R]
type _MethType[Self, **P, R] = Callable[Concatenate[Self, Recorder, P], R]
type _FuncOrMethType[**_P, _R] = Callable[_P, _R]
def retryable_database_job[**_P](description: str) -> Callable[[_FuncType[_P, bool]], _FuncType[_P, bool]]: ...
def retryable_database_job_method[_Self, **_P](description: str) -> Callable[[_MethType[_Self, _P, bool]], _MethType[_Self, _P, bool]]: ...
def _wrap_retryable_database_job_func_or_meth[**_P](job: _FuncOrMethType[_P, bool], description: str, method: bool) -> _FuncOrMethType[_P, bool]: ...
def database_job_retry_wrapper[**_P, _R](description: str, attempts: int) -> Callable[[_FuncType[_P, _R]], _FuncType[_P, _R]]: ...
def database_job_retry_wrapper_method[_Self, **_P, _R](description: str, attempts: int) -> Callable[[_MethType[_Self, _P, _R]], _MethType[_Self, _P, _R]]: ...
def _database_job_retry_wrapper_func_or_meth[**_P, _R](job: _FuncOrMethType[_P, _R], description: str, attempts: int, method: bool) -> _FuncOrMethType[_P, _R]: ...
def periodic_db_cleanups(instance: Recorder) -> None: ...
def write_lock_db_sqlite(instance: Recorder) -> Generator[None]: ...
def async_migration_in_progress(hass: HomeAssistant) -> bool: ...
def async_migration_is_live(hass: HomeAssistant) -> bool: ...
def second_sunday(year: int, month: int) -> date: ...
def is_second_sunday(date_time: datetime) -> bool: ...

PERIOD_SCHEMA: Incomplete

def resolve_period(period_def: StatisticPeriod) -> tuple[datetime | None, datetime | None]: ...
def get_index_by_name(session: Session, table_name: str, index_name: str) -> str | None: ...
def filter_unique_constraint_integrity_error(instance: Recorder, row_type: str) -> Callable[[Exception], bool]: ...
