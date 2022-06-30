from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_RESTORED as ATTR_RESTORED, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP

DATA_INSTANCE: str
SQLITE_URL_PREFIX: str
MYSQLDB_URL_PREFIX: str
DOMAIN: str
CONF_DB_INTEGRITY_CHECK: str
MAX_QUEUE_BACKLOG: int
MAX_ROWS_TO_PURGE: int
DB_WORKER_PREFIX: str
ALL_DOMAIN_EXCLUDE_ATTRS: Incomplete
ATTR_KEEP_DAYS: str
ATTR_REPACK: str
ATTR_APPLY_FILTER: str
KEEPALIVE_TIME: int
EXCLUDE_ATTRIBUTES: Incomplete

class SupportedDialect(StrEnum):
    SQLITE: str
    MYSQL: str
    POSTGRESQL: str
