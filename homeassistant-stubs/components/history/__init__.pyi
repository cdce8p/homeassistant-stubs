from aiohttp import web
from homeassistant.components import recorder as recorder
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.recorder.models import States as States, process_timestamp as process_timestamp, process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from homeassistant.components.recorder.util import execute as execute, session_scope as session_scope
from homeassistant.const import CONF_DOMAINS as CONF_DOMAINS, CONF_ENTITIES as CONF_ENTITIES, CONF_EXCLUDE as CONF_EXCLUDE, CONF_INCLUDE as CONF_INCLUDE, HTTP_BAD_REQUEST as HTTP_BAD_REQUEST
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State, split_entity_id as split_entity_id
from homeassistant.helpers.entityfilter import CONF_ENTITY_GLOBS as CONF_ENTITY_GLOBS, INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA as INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA
from typing import Any, Optional

DOMAIN: str
CONF_ORDER: str
STATE_KEY: str
LAST_CHANGED_KEY: str
GLOB_TO_SQL_CHARS: Any
CONFIG_SCHEMA: Any
SIGNIFICANT_DOMAINS: Any
IGNORE_DOMAINS: Any
NEED_ATTRIBUTE_DOMAINS: Any
QUERY_STATES: Any
HISTORY_BAKERY: str

def get_significant_states(hass: Any, *args: Any, **kwargs: Any): ...
def state_changes_during_period(hass: Any, start_time: Any, end_time: Optional[Any] = ..., entity_id: Optional[Any] = ...): ...
def get_last_state_changes(hass: Any, number_of_states: Any, entity_id: Any): ...
def get_states(hass: Any, utc_point_in_time: Any, entity_ids: Optional[Any] = ..., run: Optional[Any] = ..., filters: Optional[Any] = ...): ...
def get_state(hass: Any, utc_point_in_time: Any, entity_id: Any, run: Optional[Any] = ...): ...
async def async_setup(hass: Any, config: Any): ...

class HistoryPeriodView(HomeAssistantView):
    url: str = ...
    name: str = ...
    extra_urls: Any = ...
    filters: Any = ...
    use_include_order: Any = ...
    def __init__(self, filters: Any, use_include_order: Any) -> None: ...
    async def get(self, request: web.Request, datetime: Union[str, None]=...) -> web.Response: ...

def sqlalchemy_filter_from_include_exclude_conf(conf: Any): ...

class Filters:
    excluded_entities: Any = ...
    excluded_domains: Any = ...
    excluded_entity_globs: Any = ...
    included_entities: Any = ...
    included_domains: Any = ...
    included_entity_globs: Any = ...
    def __init__(self) -> None: ...
    def apply(self, query: Any): ...
    @property
    def has_config(self): ...
    def bake(self, baked_query: Any): ...
    def entity_filter(self): ...

class LazyState(State):
    entity_id: Any = ...
    state: Any = ...
    def __init__(self, row: Any) -> None: ...
    @property
    def attributes(self): ...
    @attributes.setter
    def attributes(self, value: Any) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, value: Any) -> None: ...
    @property
    def last_changed(self): ...
    @last_changed.setter
    def last_changed(self, value: Any) -> None: ...
    @property
    def last_updated(self): ...
    @last_updated.setter
    def last_updated(self, value: Any) -> None: ...
    def as_dict(self): ...
    def __eq__(self, other: Any) -> Any: ...