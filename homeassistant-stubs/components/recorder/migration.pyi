import abc
from . import Recorder as Recorder
from .auto_repairs.statistics.duplicates import delete_statistics_duplicates as delete_statistics_duplicates, delete_statistics_meta_duplicates as delete_statistics_meta_duplicates
from .const import CONTEXT_ID_AS_BINARY_SCHEMA_VERSION as CONTEXT_ID_AS_BINARY_SCHEMA_VERSION, EVENT_TYPE_IDS_SCHEMA_VERSION as EVENT_TYPE_IDS_SCHEMA_VERSION, LEGACY_STATES_EVENT_ID_INDEX_SCHEMA_VERSION as LEGACY_STATES_EVENT_ID_INDEX_SCHEMA_VERSION, STATES_META_SCHEMA_VERSION as STATES_META_SCHEMA_VERSION, SupportedDialect as SupportedDialect
from .db_schema import BIG_INTEGER_SQL as BIG_INTEGER_SQL, Base as Base, CONTEXT_ID_BIN_MAX_LENGTH as CONTEXT_ID_BIN_MAX_LENGTH, DOUBLE_PRECISION_TYPE_SQL as DOUBLE_PRECISION_TYPE_SQL, EventTypes as EventTypes, Events as Events, LEGACY_STATES_ENTITY_ID_LAST_UPDATED_TS_INDEX as LEGACY_STATES_ENTITY_ID_LAST_UPDATED_TS_INDEX, LEGACY_STATES_EVENT_ID_INDEX as LEGACY_STATES_EVENT_ID_INDEX, LegacyBase as LegacyBase, MYSQL_COLLATE as MYSQL_COLLATE, MYSQL_DEFAULT_CHARSET as MYSQL_DEFAULT_CHARSET, MigrationChanges as MigrationChanges, SCHEMA_VERSION as SCHEMA_VERSION, STATISTICS_TABLES as STATISTICS_TABLES, SchemaChanges as SchemaChanges, States as States, StatesMeta as StatesMeta, Statistics as Statistics, StatisticsMeta as StatisticsMeta, StatisticsRuns as StatisticsRuns, StatisticsShortTerm as StatisticsShortTerm, TABLE_STATES as TABLE_STATES
from .models import process_timestamp as process_timestamp
from .models.time import datetime_to_timestamp_or_none as datetime_to_timestamp_or_none
from .queries import batch_cleanup_entity_ids as batch_cleanup_entity_ids, delete_duplicate_short_term_statistics_row as delete_duplicate_short_term_statistics_row, delete_duplicate_statistics_row as delete_duplicate_statistics_row, find_entity_ids_to_migrate as find_entity_ids_to_migrate, find_event_type_to_migrate as find_event_type_to_migrate, find_events_context_ids_to_migrate as find_events_context_ids_to_migrate, find_states_context_ids_to_migrate as find_states_context_ids_to_migrate, find_unmigrated_short_term_statistics_rows as find_unmigrated_short_term_statistics_rows, find_unmigrated_statistics_rows as find_unmigrated_statistics_rows, get_migration_changes as get_migration_changes, has_entity_ids_to_migrate as has_entity_ids_to_migrate, has_event_type_to_migrate as has_event_type_to_migrate, has_events_context_ids_to_migrate as has_events_context_ids_to_migrate, has_states_context_ids_to_migrate as has_states_context_ids_to_migrate, has_used_states_entity_ids as has_used_states_entity_ids, has_used_states_event_ids as has_used_states_event_ids, migrate_single_short_term_statistics_row_to_timestamp as migrate_single_short_term_statistics_row_to_timestamp, migrate_single_statistics_row_to_timestamp as migrate_single_statistics_row_to_timestamp
from .statistics import cleanup_statistics_timestamp_migration as cleanup_statistics_timestamp_migration, get_start_time as get_start_time
from .tasks import RecorderTask as RecorderTask
from .util import database_job_retry_wrapper as database_job_retry_wrapper, database_job_retry_wrapper_method as database_job_retry_wrapper_method, execute_stmt_lambda_element as execute_stmt_lambda_element, get_index_by_name as get_index_by_name, retryable_database_job_method as retryable_database_job_method, session_scope as session_scope
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable, Iterable
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from homeassistant.util.ulid import ulid_at_time as ulid_at_time, ulid_to_bytes as ulid_to_bytes
from sqlalchemy.engine import CursorResult as CursorResult, Engine as Engine
from sqlalchemy.orm import DeclarativeBase as DeclarativeBase
from sqlalchemy.orm.session import Session as Session
from sqlalchemy.schema import AddConstraint
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from typing import Any, final

LIVE_MIGRATION_MIN_SCHEMA_VERSION: int
MIGRATION_NOTE_OFFLINE: str
MIGRATION_NOTE_MINUTES: str
MIGRATION_NOTE_WHILE: str
_EMPTY_ENTITY_ID: str
_EMPTY_EVENT_TYPE: str
_LOGGER: Incomplete

@dataclass
class _ColumnTypesForDialect:
    big_int_type: str
    timestamp_type: str
    context_bin_type: str

_MYSQL_COLUMN_TYPES: Incomplete
_POSTGRESQL_COLUMN_TYPES: Incomplete
_SQLITE_COLUMN_TYPES: Incomplete
_COLUMN_TYPES_FOR_DIALECT: dict[SupportedDialect | None, _ColumnTypesForDialect]

def _unindexable_legacy_column(instance: Recorder, base: type[DeclarativeBase], err: Exception) -> bool: ...
def raise_if_exception_missing_str(ex: Exception, match_substrs: Iterable[str]) -> None: ...
def _get_initial_schema_version(session: Session) -> int | None: ...
def get_initial_schema_version(session_maker: Callable[[], Session]) -> int | None: ...
def _get_current_schema_version(session: Session) -> int | None: ...
def get_current_schema_version(session_maker: Callable[[], Session]) -> int | None: ...

@dataclass(frozen=True, kw_only=True)
class SchemaValidationStatus:
    current_version: int
    initial_version: int
    migration_needed: bool
    non_live_data_migration_needed: bool
    schema_errors: set[str]
    start_version: int

def _schema_is_current(current_version: int) -> bool: ...
def validate_db_schema(hass: HomeAssistant, instance: Recorder, session_maker: Callable[[], Session]) -> SchemaValidationStatus | None: ...
def _find_schema_errors(hass: HomeAssistant, instance: Recorder, session_maker: Callable[[], Session]) -> set[str]: ...
def live_migration(schema_status: SchemaValidationStatus) -> bool: ...
def pre_migrate_schema(engine: Engine) -> None: ...
def _migrate_schema(instance: Recorder, hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], schema_status: SchemaValidationStatus, end_version: int) -> SchemaValidationStatus: ...
def migrate_schema_non_live(instance: Recorder, hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], schema_status: SchemaValidationStatus) -> SchemaValidationStatus: ...
def migrate_schema_live(instance: Recorder, hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], schema_status: SchemaValidationStatus) -> SchemaValidationStatus: ...
def _get_migration_changes(session: Session) -> dict[str, int]: ...
def non_live_data_migration_needed(instance: Recorder, session_maker: Callable[[], Session], *, initial_schema_version: int, start_schema_version: int) -> bool: ...
def migrate_data_non_live(instance: Recorder, session_maker: Callable[[], Session], schema_status: SchemaValidationStatus) -> None: ...
def migrate_data_live(instance: Recorder, session_maker: Callable[[], Session], schema_status: SchemaValidationStatus) -> None: ...
def _create_index(instance: Recorder, session_maker: Callable[[], Session], table_name: str, index_name: str, *, base: type[DeclarativeBase] = ...) -> None: ...
def _execute_or_collect_error(session_maker: Callable[[], Session], query: str, errors: list[str]) -> bool: ...
def _drop_index(session_maker: Callable[[], Session], table_name: str, index_name: str, quiet: bool | None = None) -> None: ...
def _add_columns(session_maker: Callable[[], Session], table_name: str, columns_def: list[str]) -> None: ...
def _modify_columns(session_maker: Callable[[], Session], engine: Engine, table_name: str, columns_def: list[str]) -> None: ...
def _update_states_table_with_foreign_key_options(session_maker: Callable[[], Session], engine: Engine) -> None: ...
def _drop_foreign_key_constraints(session_maker: Callable[[], Session], engine: Engine, table: str, column: str) -> None: ...
def _restore_foreign_key_constraints(session_maker: Callable[[], Session], engine: Engine, foreign_columns: list[tuple[str, str, str | None, str | None]]) -> None: ...
def _add_constraint(session_maker: Callable[[], Session], add_constraint: AddConstraint, table: str, column: str) -> None: ...
def _delete_foreign_key_violations(session_maker: Callable[[], Session], engine: Engine, table: str, column: str, foreign_table: str, foreign_column: str) -> None: ...
@database_job_retry_wrapper('Apply migration update', 10)
def _apply_update(instance: Recorder, hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], new_version: int, old_version: int) -> None: ...

class _SchemaVersionMigrator(ABC, metaclass=abc.ABCMeta):
    __migrators: dict[int, type[_SchemaVersionMigrator]]
    def __init_subclass__(cls, target_version: int, **kwargs: Any) -> None: ...
    instance: Incomplete
    hass: Incomplete
    engine: Incomplete
    session_maker: Incomplete
    old_version: Incomplete
    column_types: Incomplete
    def __init__(self, instance: Recorder, hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], old_version: int) -> None: ...
    @classmethod
    def get_migrator(cls, target_version: int) -> type[_SchemaVersionMigrator]: ...
    @final
    def apply_update(self) -> None: ...
    @abstractmethod
    def _apply_update(self) -> None: ...

class _SchemaVersion1Migrator(_SchemaVersionMigrator, target_version=1):
    def _apply_update(self) -> None: ...

class _SchemaVersion2Migrator(_SchemaVersionMigrator, target_version=2):
    def _apply_update(self) -> None: ...

class _SchemaVersion3Migrator(_SchemaVersionMigrator, target_version=3):
    def _apply_update(self) -> None: ...

class _SchemaVersion4Migrator(_SchemaVersionMigrator, target_version=4):
    def _apply_update(self) -> None: ...

class _SchemaVersion5Migrator(_SchemaVersionMigrator, target_version=5):
    def _apply_update(self) -> None: ...

class _SchemaVersion6Migrator(_SchemaVersionMigrator, target_version=6):
    def _apply_update(self) -> None: ...

class _SchemaVersion7Migrator(_SchemaVersionMigrator, target_version=7):
    def _apply_update(self) -> None: ...

class _SchemaVersion8Migrator(_SchemaVersionMigrator, target_version=8):
    def _apply_update(self) -> None: ...

class _SchemaVersion9Migrator(_SchemaVersionMigrator, target_version=9):
    def _apply_update(self) -> None: ...

class _SchemaVersion10Migrator(_SchemaVersionMigrator, target_version=10):
    def _apply_update(self) -> None: ...

class _SchemaVersion11Migrator(_SchemaVersionMigrator, target_version=11):
    def _apply_update(self) -> None: ...

class _SchemaVersion12Migrator(_SchemaVersionMigrator, target_version=12):
    def _apply_update(self) -> None: ...

class _SchemaVersion13Migrator(_SchemaVersionMigrator, target_version=13):
    def _apply_update(self) -> None: ...

class _SchemaVersion14Migrator(_SchemaVersionMigrator, target_version=14):
    def _apply_update(self) -> None: ...

class _SchemaVersion15Migrator(_SchemaVersionMigrator, target_version=15):
    def _apply_update(self) -> None: ...

class _SchemaVersion16Migrator(_SchemaVersionMigrator, target_version=16):
    def _apply_update(self) -> None: ...

class _SchemaVersion17Migrator(_SchemaVersionMigrator, target_version=17):
    def _apply_update(self) -> None: ...

class _SchemaVersion18Migrator(_SchemaVersionMigrator, target_version=18):
    def _apply_update(self) -> None: ...

class _SchemaVersion19Migrator(_SchemaVersionMigrator, target_version=19):
    def _apply_update(self) -> None: ...

class _SchemaVersion20Migrator(_SchemaVersionMigrator, target_version=20):
    def _apply_update(self) -> None: ...

class _SchemaVersion21Migrator(_SchemaVersionMigrator, target_version=21):
    def _apply_update(self) -> None: ...

class _SchemaVersion22Migrator(_SchemaVersionMigrator, target_version=22):
    def _apply_update(self) -> None: ...

class _SchemaVersion23Migrator(_SchemaVersionMigrator, target_version=23):
    def _apply_update(self) -> None: ...

class _SchemaVersion24Migrator(_SchemaVersionMigrator, target_version=24):
    def _apply_update(self) -> None: ...

class _SchemaVersion25Migrator(_SchemaVersionMigrator, target_version=25):
    def _apply_update(self) -> None: ...

class _SchemaVersion26Migrator(_SchemaVersionMigrator, target_version=26):
    def _apply_update(self) -> None: ...

class _SchemaVersion27Migrator(_SchemaVersionMigrator, target_version=27):
    def _apply_update(self) -> None: ...

class _SchemaVersion28Migrator(_SchemaVersionMigrator, target_version=28):
    def _apply_update(self) -> None: ...

class _SchemaVersion29Migrator(_SchemaVersionMigrator, target_version=29):
    def _apply_update(self) -> None: ...

class _SchemaVersion30Migrator(_SchemaVersionMigrator, target_version=30):
    def _apply_update(self) -> None: ...

class _SchemaVersion31Migrator(_SchemaVersionMigrator, target_version=31):
    def _apply_update(self) -> None: ...

class _SchemaVersion32Migrator(_SchemaVersionMigrator, target_version=32):
    def _apply_update(self) -> None: ...

class _SchemaVersion33Migrator(_SchemaVersionMigrator, target_version=33):
    def _apply_update(self) -> None: ...

class _SchemaVersion34Migrator(_SchemaVersionMigrator, target_version=34):
    def _apply_update(self) -> None: ...

class _SchemaVersion35Migrator(_SchemaVersionMigrator, target_version=35):
    def _apply_update(self) -> None: ...

class _SchemaVersion36Migrator(_SchemaVersionMigrator, target_version=36):
    def _apply_update(self) -> None: ...

class _SchemaVersion37Migrator(_SchemaVersionMigrator, target_version=37):
    def _apply_update(self) -> None: ...

class _SchemaVersion38Migrator(_SchemaVersionMigrator, target_version=38):
    def _apply_update(self) -> None: ...

class _SchemaVersion39Migrator(_SchemaVersionMigrator, target_version=39):
    def _apply_update(self) -> None: ...

class _SchemaVersion40Migrator(_SchemaVersionMigrator, target_version=40):
    def _apply_update(self) -> None: ...

class _SchemaVersion41Migrator(_SchemaVersionMigrator, target_version=41):
    def _apply_update(self) -> None: ...

class _SchemaVersion42Migrator(_SchemaVersionMigrator, target_version=42):
    def _apply_update(self) -> None: ...

class _SchemaVersion43Migrator(_SchemaVersionMigrator, target_version=43):
    def _apply_update(self) -> None: ...

class _SchemaVersion44Migrator(_SchemaVersionMigrator, target_version=44):
    def _apply_update(self) -> None: ...

class _SchemaVersion45Migrator(_SchemaVersionMigrator, target_version=45):
    def _apply_update(self) -> None: ...

FOREIGN_COLUMNS: Incomplete

class _SchemaVersion46Migrator(_SchemaVersionMigrator, target_version=46):
    def _apply_update(self) -> None: ...

class _SchemaVersion47Migrator(_SchemaVersionMigrator, target_version=47):
    def _apply_update(self) -> None: ...

class _SchemaVersion48Migrator(_SchemaVersionMigrator, target_version=48):
    def _apply_update(self) -> None: ...

def _migrate_statistics_columns_to_timestamp_removing_duplicates(hass: HomeAssistant, instance: Recorder, session_maker: Callable[[], Session], engine: Engine) -> None: ...
def _correct_table_character_set_and_collation(table: str, session_maker: Callable[[], Session]) -> None: ...
@database_job_retry_wrapper('Wipe old string time columns', 3)
def _wipe_old_string_time_columns(instance: Recorder, engine: Engine, session: Session) -> None: ...
@database_job_retry_wrapper('Migrate columns to timestamp', 3)
def _migrate_columns_to_timestamp(instance: Recorder, session_maker: Callable[[], Session], engine: Engine) -> None: ...
@database_job_retry_wrapper('Migrate statistics columns to timestamp one by one', 3)
def _migrate_statistics_columns_to_timestamp_one_by_one(instance: Recorder, session_maker: Callable[[], Session]) -> None: ...
@database_job_retry_wrapper('Migrate statistics columns to timestamp', 3)
def _migrate_statistics_columns_to_timestamp(instance: Recorder, session_maker: Callable[[], Session], engine: Engine) -> None: ...
def _context_id_to_bytes(context_id: str | None) -> bytes | None: ...
def _generate_ulid_bytes_at_time(timestamp: float | None) -> bytes: ...
def post_migrate_entity_ids(instance: Recorder) -> bool: ...
def _initialize_database(session: Session) -> bool: ...
def initialize_database(session_maker: Callable[[], Session]) -> bool: ...

@dataclass(slots=True)
class MigrationTask(RecorderTask):
    migrator: BaseRunTimeMigration
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class CommitBeforeMigrationTask(MigrationTask):
    commit_before = ...

@dataclass(frozen=True, kw_only=True)
class DataMigrationStatus:
    needs_migrate: bool
    migration_done: bool

class BaseMigration(ABC, metaclass=abc.ABCMeta):
    index_to_drop: tuple[str, str, type[DeclarativeBase]] | None
    required_schema_version: int
    max_initial_schema_version: int
    migration_version: int
    migration_id: str
    initial_schema_version: Incomplete
    start_schema_version: Incomplete
    migration_changes: Incomplete
    def __init__(self, *, initial_schema_version: int, start_schema_version: int, migration_changes: dict[str, int]) -> None: ...
    @abstractmethod
    def migrate_data(self, instance: Recorder) -> bool: ...
    def _migrate_data(self, instance: Recorder) -> bool: ...
    @abstractmethod
    def migrate_data_impl(self, instance: Recorder) -> DataMigrationStatus: ...
    def migration_done(self, instance: Recorder, session: Session) -> None: ...
    @abstractmethod
    def needs_migrate_impl(self, instance: Recorder, session: Session) -> DataMigrationStatus: ...
    def needs_migrate(self, instance: Recorder, session: Session) -> bool: ...
    def _has_needed_index(self, session: Session) -> bool | None: ...

class BaseOffLineMigration(BaseMigration, metaclass=abc.ABCMeta):
    def migrate_all(self, instance: Recorder, session_maker: Callable[[], Session]) -> None: ...
    @database_job_retry_wrapper_method('migrate data', 10)
    def migrate_data(self, instance: Recorder) -> bool: ...
    def _ensure_index_exists(self, instance: Recorder) -> None: ...

class BaseRunTimeMigration(BaseMigration, metaclass=abc.ABCMeta):
    task = MigrationTask
    def queue_migration(self, instance: Recorder, session: Session) -> None: ...
    @retryable_database_job_method('migrate data')
    def migrate_data(self, instance: Recorder) -> bool: ...

class BaseMigrationWithQuery(BaseMigration, metaclass=abc.ABCMeta):
    @abstractmethod
    def needs_migrate_query(self) -> StatementLambdaElement: ...
    def needs_migrate_impl(self, instance: Recorder, session: Session) -> DataMigrationStatus: ...

class StatesContextIDMigration(BaseMigrationWithQuery, BaseOffLineMigration):
    required_schema_version = CONTEXT_ID_AS_BINARY_SCHEMA_VERSION
    max_initial_schema_version: Incomplete
    migration_id: str
    migration_version: int
    index_to_drop: Incomplete
    def migrate_data_impl(self, instance: Recorder) -> DataMigrationStatus: ...
    def needs_migrate_query(self) -> StatementLambdaElement: ...

class EventsContextIDMigration(BaseMigrationWithQuery, BaseOffLineMigration):
    required_schema_version = CONTEXT_ID_AS_BINARY_SCHEMA_VERSION
    max_initial_schema_version: Incomplete
    migration_id: str
    migration_version: int
    index_to_drop: Incomplete
    def migrate_data_impl(self, instance: Recorder) -> DataMigrationStatus: ...
    def needs_migrate_query(self) -> StatementLambdaElement: ...

class EventTypeIDMigration(BaseMigrationWithQuery, BaseOffLineMigration):
    required_schema_version = EVENT_TYPE_IDS_SCHEMA_VERSION
    max_initial_schema_version: Incomplete
    migration_id: str
    def migrate_data_impl(self, instance: Recorder) -> DataMigrationStatus: ...
    def needs_migrate_query(self) -> StatementLambdaElement: ...

class EntityIDMigration(BaseMigrationWithQuery, BaseOffLineMigration):
    required_schema_version = STATES_META_SCHEMA_VERSION
    max_initial_schema_version: Incomplete
    migration_id: str
    def migrate_data_impl(self, instance: Recorder) -> DataMigrationStatus: ...
    def needs_migrate_query(self) -> StatementLambdaElement: ...

class EventIDPostMigration(BaseRunTimeMigration):
    migration_id: str
    max_initial_schema_version: Incomplete
    task = MigrationTask
    migration_version: int
    def migrate_data_impl(self, instance: Recorder) -> DataMigrationStatus: ...
    @staticmethod
    def _legacy_event_id_foreign_key_exists(instance: Recorder) -> bool: ...
    def needs_migrate_impl(self, instance: Recorder, session: Session) -> DataMigrationStatus: ...

class EntityIDPostMigration(BaseMigrationWithQuery, BaseOffLineMigration):
    migration_id: str
    max_initial_schema_version: Incomplete
    index_to_drop: Incomplete
    def migrate_data_impl(self, instance: Recorder) -> DataMigrationStatus: ...
    def needs_migrate_query(self) -> StatementLambdaElement: ...

NON_LIVE_DATA_MIGRATORS: tuple[type[BaseOffLineMigration], ...]
LIVE_DATA_MIGRATORS: tuple[type[BaseRunTimeMigration], ...]

def _mark_migration_done(session: Session, migration: type[BaseMigration]) -> None: ...
def rebuild_sqlite_table(session_maker: Callable[[], Session], engine: Engine, table: type[Base]) -> bool: ...
