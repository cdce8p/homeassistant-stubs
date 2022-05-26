from . import rest_api as rest_api, websocket_api as websocket_api
from .const import ATTR_MESSAGE as ATTR_MESSAGE, DOMAIN as DOMAIN, LOGBOOK_ENTITIES_FILTER as LOGBOOK_ENTITIES_FILTER, LOGBOOK_ENTRY_DOMAIN as LOGBOOK_ENTRY_DOMAIN, LOGBOOK_ENTRY_ENTITY_ID as LOGBOOK_ENTRY_ENTITY_ID, LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME, LOGBOOK_FILTERS as LOGBOOK_FILTERS
from .models import LazyEventPartialState as LazyEventPartialState
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import frontend as frontend
from homeassistant.components.recorder.filters import sqlalchemy_filter_from_include_exclude_conf as sqlalchemy_filter_from_include_exclude_conf
from homeassistant.const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, EVENT_LOGBOOK_ENTRY as EVENT_LOGBOOK_ENTRY
from homeassistant.core import Context as Context, Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.entityfilter import INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA as INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA, convert_include_exclude_filter as convert_include_exclude_filter
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

CONFIG_SCHEMA: Incomplete
LOG_MESSAGE_SCHEMA: Incomplete

def log_entry(hass: HomeAssistant, name: str, message: str, domain: Union[str, None] = ..., entity_id: Union[str, None] = ..., context: Union[Context, None] = ...) -> None: ...
def async_log_entry(hass: HomeAssistant, name: str, message: str, domain: Union[str, None] = ..., entity_id: Union[str, None] = ..., context: Union[Context, None] = ...) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _process_logbook_platform(hass: HomeAssistant, domain: str, platform: Any) -> None: ...
