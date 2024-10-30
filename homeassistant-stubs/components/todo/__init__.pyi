import dataclasses
import datetime
from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_DUE as ATTR_DUE, ATTR_DUE_DATE as ATTR_DUE_DATE, ATTR_DUE_DATETIME as ATTR_DUE_DATETIME, ATTR_ITEM as ATTR_ITEM, ATTR_RENAME as ATTR_RENAME, ATTR_STATUS as ATTR_STATUS, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, TodoItemStatus as TodoItemStatus, TodoListEntityFeature as TodoListEntityFeature, TodoServices as TodoServices
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from homeassistant.components import frontend as frontend, websocket_api as websocket_api
from homeassistant.components.websocket_api import ERR_NOT_FOUND as ERR_NOT_FOUND, ERR_NOT_SUPPORTED as ERR_NOT_SUPPORTED
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.json import JsonValueType as JsonValueType
from typing import Any

_LOGGER: Incomplete
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete

@dataclasses.dataclass
class TodoItemFieldDescription:
    service_field: str
    todo_item_field: str
    validation: Callable[[Any], Any]
    required_feature: TodoListEntityFeature
    def __init__(self, service_field, todo_item_field, validation, required_feature) -> None: ...

TODO_ITEM_FIELDS: Incomplete
TODO_ITEM_FIELD_SCHEMA: Incomplete
TODO_ITEM_FIELD_VALIDATIONS: Incomplete

def _validate_supported_features(supported_features: int | None, call_data: dict[str, Any]) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

@dataclasses.dataclass
class TodoItem:
    summary: str | None = ...
    uid: str | None = ...
    status: TodoItemStatus | None = ...
    due: datetime.date | datetime.datetime | None = ...
    description: str | None = ...
    def __init__(self, summary=..., uid=..., status=..., due=..., description=...) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class TodoListEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _attr_todo_items: list[TodoItem] | None
    _update_listeners: list[Callable[[list[JsonValueType] | None], None]] | None
    @property
    def state(self) -> int | None: ...
    def todo_items(self) -> list[TodoItem] | None: ...
    async def async_create_todo_item(self, item: TodoItem) -> None: ...
    async def async_update_todo_item(self, item: TodoItem) -> None: ...
    async def async_delete_todo_items(self, uids: list[str]) -> None: ...
    async def async_move_todo_item(self, uid: str, previous_uid: str | None = None) -> None: ...
    def async_subscribe_updates(self, listener: Callable[[list[JsonValueType] | None], None]) -> CALLBACK_TYPE: ...
    def async_update_listeners(self) -> None: ...
    def _async_write_ha_state(self) -> None: ...

async def websocket_handle_subscribe_todo_items(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _api_items_factory(obj: Iterable[tuple[str, Any]]) -> dict[str, str]: ...
async def websocket_handle_todo_item_list(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def websocket_handle_todo_item_move(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _find_by_uid_or_summary(value: str, items: list[TodoItem] | None) -> TodoItem | None: ...
async def _async_add_todo_item(entity: TodoListEntity, call: ServiceCall) -> None: ...
async def _async_update_todo_item(entity: TodoListEntity, call: ServiceCall) -> None: ...
async def _async_remove_todo_items(entity: TodoListEntity, call: ServiceCall) -> None: ...
async def _async_get_todo_items(entity: TodoListEntity, call: ServiceCall) -> dict[str, Any]: ...
async def _async_remove_completed_items(entity: TodoListEntity, _: ServiceCall) -> None: ...
