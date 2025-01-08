from ... import Recorder as Recorder
from ...const import SQLITE_MAX_BIND_VARS as SQLITE_MAX_BIND_VARS
from ...db_schema import Statistics as Statistics, StatisticsBase as StatisticsBase, StatisticsMeta as StatisticsMeta, StatisticsShortTerm as StatisticsShortTerm
from ...util import database_job_retry_wrapper as database_job_retry_wrapper, execute as execute
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from sqlalchemy.engine.row import Row as Row
from sqlalchemy.orm.session import Session as Session

_LOGGER: Incomplete

def _find_duplicates(session: Session, table: type[StatisticsBase]) -> tuple[list[int], list[dict]]: ...
def _delete_duplicates_from_table(session: Session, table: type[StatisticsBase]) -> tuple[int, list[dict]]: ...
@database_job_retry_wrapper('delete statistics duplicates', 3)
def delete_statistics_duplicates(instance: Recorder, hass: HomeAssistant, session: Session) -> None: ...
def _find_statistics_meta_duplicates(session: Session) -> list[int]: ...
def _delete_statistics_meta_duplicates(session: Session) -> int: ...
@database_job_retry_wrapper('delete statistics meta duplicates', 3)
def delete_statistics_meta_duplicates(instance: Recorder, session: Session) -> None: ...
