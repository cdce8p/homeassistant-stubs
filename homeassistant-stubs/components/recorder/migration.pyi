from .const import SupportedDialect as SupportedDialect
from .db_schema import Base as Base, SCHEMA_VERSION as SCHEMA_VERSION, SchemaChanges as SchemaChanges, Statistics as Statistics, StatisticsMeta as StatisticsMeta, StatisticsRuns as StatisticsRuns, StatisticsShortTerm as StatisticsShortTerm, TABLE_STATES as TABLE_STATES
from .models import process_timestamp as process_timestamp
from .statistics import delete_statistics_duplicates as delete_statistics_duplicates, delete_statistics_meta_duplicates as delete_statistics_meta_duplicates, get_start_time as get_start_time
from .util import session_scope as session_scope
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from homeassistant.core import HomeAssistant as HomeAssistant
from sqlalchemy.engine import Engine as Engine
from sqlalchemy.orm.session import Session as Session

_LOGGER: Incomplete

def raise_if_exception_missing_str(ex: Exception, match_substrs: Iterable[str]) -> None: ...
def get_schema_version(session_maker: Callable[[], Session]) -> int: ...
def schema_is_current(current_version: int) -> bool: ...
def migrate_schema(hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], current_version: int) -> None: ...
def _create_index(session_maker: Callable[[], Session], table_name: str, index_name: str) -> None: ...
def _drop_index(session_maker: Callable[[], Session], table_name: str, index_name: str) -> None: ...
def _add_columns(session_maker: Callable[[], Session], table_name: str, columns_def: list[str]) -> None: ...
def _modify_columns(session_maker: Callable[[], Session], engine: Engine, table_name: str, columns_def: list[str]) -> None: ...
def _update_states_table_with_foreign_key_options(session_maker: Callable[[], Session], engine: Engine) -> None: ...
def _drop_foreign_key_constraints(session_maker: Callable[[], Session], engine: Engine, table: str, columns: list[str]) -> None: ...
def _apply_update(hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], new_version: int, old_version: int) -> None: ...
def _inspect_schema_version(session: Session) -> int: ...
