from . import statistics as statistics, websocket_api as websocket_api
from .const import CONF_DB_INTEGRITY_CHECK as CONF_DB_INTEGRITY_CHECK, DATA_INSTANCE as DATA_INSTANCE, DOMAIN as DOMAIN, EXCLUDE_ATTRIBUTES as EXCLUDE_ATTRIBUTES, SQLITE_URL_PREFIX as SQLITE_URL_PREFIX
from .core import Recorder as Recorder
from .services import async_register_services as async_register_services
from .tasks import AddRecorderPlatformTask as AddRecorderPlatformTask
from _typeshed import Incomplete
from homeassistant.const import CONF_EXCLUDE as CONF_EXCLUDE, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entityfilter import INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA as INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA, INCLUDE_EXCLUDE_FILTER_SCHEMA_INNER as INCLUDE_EXCLUDE_FILTER_SCHEMA_INNER, convert_include_exclude_filter as convert_include_exclude_filter
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

_LOGGER: Incomplete
DEFAULT_URL: str
DEFAULT_DB_FILE: str
DEFAULT_DB_INTEGRITY_CHECK: bool
DEFAULT_DB_MAX_RETRIES: int
DEFAULT_DB_RETRY_WAIT: int
DEFAULT_COMMIT_INTERVAL: int
CONF_AUTO_PURGE: str
CONF_AUTO_REPACK: str
CONF_DB_URL: str
CONF_DB_MAX_RETRIES: str
CONF_DB_RETRY_WAIT: str
CONF_PURGE_KEEP_DAYS: str
CONF_PURGE_INTERVAL: str
CONF_EVENT_TYPES: str
CONF_COMMIT_INTERVAL: str
EXCLUDE_SCHEMA: Incomplete
FILTER_SCHEMA: Incomplete
ALLOW_IN_MEMORY_DB: bool

def validate_db_url(db_url: str) -> Any: ...

CONFIG_SCHEMA: Incomplete

def get_instance(hass: HomeAssistant) -> Recorder: ...
def is_entity_recorded(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _process_recorder_platform(hass: HomeAssistant, domain: str, platform: Any) -> None: ...
