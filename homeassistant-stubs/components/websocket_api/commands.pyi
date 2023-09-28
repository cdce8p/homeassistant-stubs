from . import const as const, decorators as decorators, messages as messages
from .connection import ActiveConnection as ActiveConnection
from .messages import construct_event_message as construct_event_message, construct_result_message as construct_result_message
from collections.abc import Callable as Callable
from homeassistant.auth.models import User as User
from homeassistant.auth.permissions.const import POLICY_READ as POLICY_READ
from homeassistant.const import EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, MATCH_ALL as MATCH_ALL, SIGNAL_BOOTSTRAP_INTEGRATIONS as SIGNAL_BOOTSTRAP_INTEGRATIONS
from homeassistant.core import Context as Context, Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceNotFound as ServiceNotFound, TemplateError as TemplateError, Unauthorized as Unauthorized
from homeassistant.helpers import entity as entity, template as template
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.event import EventStateChangedData as EventStateChangedData, TrackTemplate as TrackTemplate, TrackTemplateResult as TrackTemplateResult, async_track_template_result as async_track_template_result
from homeassistant.helpers.json import ExtendedJSONEncoder as ExtendedJSONEncoder, JSON_DUMP as JSON_DUMP, find_paths_unserializable_data as find_paths_unserializable_data, json_dumps as json_dumps
from homeassistant.helpers.service import async_get_all_descriptions as async_get_all_descriptions
from homeassistant.helpers.typing import EventType as EventType
from homeassistant.loader import Integration as Integration, IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration, async_get_integration_descriptions as async_get_integration_descriptions, async_get_integrations as async_get_integrations
from homeassistant.setup import DATA_SETUP_TIME as DATA_SETUP_TIME, async_get_loaded_integrations as async_get_loaded_integrations
from homeassistant.util.json import format_unserializable_data as format_unserializable_data
from typing import Any

ALL_SERVICE_DESCRIPTIONS_JSON_CACHE: str

def async_register_commands(hass: HomeAssistant, async_reg: Callable[[HomeAssistant, const.WebSocketCommandHandler], None]) -> None: ...
def pong_message(iden: int) -> dict[str, Any]: ...
def _forward_events_check_permissions(send_message: Callable[[str | dict[str, Any] | Callable[[], str]], None], user: User, msg_id: int, event: Event) -> None: ...
def _forward_events_unconditional(send_message: Callable[[str | dict[str, Any] | Callable[[], str]], None], msg_id: int, event: Event) -> None: ...
def handle_subscribe_events(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def handle_subscribe_bootstrap_integrations(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def handle_unsubscribe_events(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_call_service(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def _async_get_allowed_states(hass: HomeAssistant, connection: ActiveConnection) -> list[State]: ...
def handle_get_states(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def _send_handle_get_states_response(connection: ActiveConnection, msg_id: int, serialized_states: list[str]) -> None: ...
def _forward_entity_changes(send_message: Callable[[str | dict[str, Any] | Callable[[], str]], None], entity_ids: set[str], user: User, msg_id: int, event: Event) -> None: ...
def handle_subscribe_entities(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def _send_handle_entities_init_response(connection: ActiveConnection, msg_id: int, serialized_states: list[str]) -> None: ...
async def _async_get_all_descriptions_json(hass: HomeAssistant) -> str: ...
async def handle_get_services(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def handle_get_config(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_manifest_list(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_manifest_get(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def handle_integration_setup_info(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def handle_ping(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def _cached_template(template_str: str, hass: HomeAssistant) -> template.Template: ...
async def handle_render_template(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def _serialize_entity_sources(entity_infos: dict[str, entity.EntityInfo]) -> dict[str, Any]: ...
def handle_entity_source(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_subscribe_trigger(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_test_condition(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_execute_script(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def handle_fire_event(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_validate_config(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def handle_supported_features(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_integration_descriptions(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
