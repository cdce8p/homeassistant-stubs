import voluptuous as vol
from . import const as const, decorators as decorators, messages as messages
from .connection import ActiveConnection as ActiveConnection
from .messages import construct_result_message as construct_result_message
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from functools import lru_cache
from homeassistant.auth.models import User as User
from homeassistant.auth.permissions.const import POLICY_READ as POLICY_READ
from homeassistant.auth.permissions.events import SUBSCRIBE_ALLOWLIST as SUBSCRIBE_ALLOWLIST
from homeassistant.const import EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, MATCH_ALL as MATCH_ALL, SIGNAL_BOOTSTRAP_INTEGRATIONS as SIGNAL_BOOTSTRAP_INTEGRATIONS
from homeassistant.core import Context as Context, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, ServiceResponse as ServiceResponse, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceNotFound as ServiceNotFound, ServiceValidationError as ServiceValidationError, TemplateError as TemplateError, Unauthorized as Unauthorized
from homeassistant.helpers import config_validation as cv, entity as entity, template as template
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entityfilter import INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA as INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA, convert_include_exclude_filter as convert_include_exclude_filter
from homeassistant.helpers.event import TrackTemplate as TrackTemplate, TrackTemplateResult as TrackTemplateResult, async_track_template_result as async_track_template_result
from homeassistant.helpers.json import ExtendedJSONEncoder as ExtendedJSONEncoder, JSON_DUMP as JSON_DUMP, find_paths_unserializable_data as find_paths_unserializable_data, json_bytes as json_bytes, json_fragment as json_fragment
from homeassistant.helpers.service import async_get_all_descriptions as async_get_all_descriptions
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration, async_get_integration_descriptions as async_get_integration_descriptions, async_get_integrations as async_get_integrations
from homeassistant.setup import async_get_loaded_integrations as async_get_loaded_integrations, async_get_setup_timings as async_get_setup_timings
from homeassistant.util.json import format_unserializable_data as format_unserializable_data
from typing import Any

ALL_SERVICE_DESCRIPTIONS_JSON_CACHE: str
_LOGGER: Incomplete

@callback
def async_register_commands(hass: HomeAssistant, async_reg: Callable[[HomeAssistant, const.WebSocketCommandHandler], None]) -> None: ...
def pong_message(iden: int) -> dict[str, Any]: ...
@callback
def _forward_events_check_permissions(send_message: Callable[[bytes | str | dict[str, Any]], None], user: User, message_id_as_bytes: bytes, event: Event) -> None: ...
@callback
def _forward_events_unconditional(send_message: Callable[[bytes | str | dict[str, Any]], None], message_id_as_bytes: bytes, event: Event) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'subscribe_events', INCOMPLETE: str})
def handle_subscribe_events(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'subscribe_bootstrap_integrations'})
def handle_subscribe_bootstrap_integrations(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'unsubscribe_events', INCOMPLETE: cv.positive_int})
def handle_unsubscribe_events(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@decorators.websocket_command({INCOMPLETE: 'call_service', INCOMPLETE: str, INCOMPLETE: str, INCOMPLETE: cv.ENTITY_SERVICE_FIELDS, INCOMPLETE: dict, INCOMPLETE: bool})
@decorators.async_response
async def handle_call_service(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def _async_get_allowed_states(hass: HomeAssistant, connection: ActiveConnection) -> list[State]: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'get_states'})
def handle_get_states(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def _send_handle_get_states_response(connection: ActiveConnection, msg_id: int, serialized_states: list[bytes]) -> None: ...
@callback
def _forward_entity_changes(send_message: Callable[[str | bytes | dict[str, Any]], None], entity_ids: set[str] | None, entity_filter: Callable[[str], bool] | None, user: User, message_id_as_bytes: bytes, event: Event[EventStateChangedData]) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'subscribe_entities', INCOMPLETE: cv.entity_ids, INCOMPLETE: INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA.schema})
def handle_subscribe_entities(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def _send_handle_entities_init_response(connection: ActiveConnection, message_id_as_bytes: bytes, serialized_states: list[bytes]) -> None: ...
async def _async_get_all_descriptions_json(hass: HomeAssistant) -> bytes: ...
@decorators.websocket_command({INCOMPLETE: 'get_services'})
@decorators.async_response
async def handle_get_services(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'get_config'})
def handle_get_config(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@decorators.websocket_command({INCOMPLETE: 'manifest/list', INCOMPLETE: [str]})
@decorators.async_response
async def handle_manifest_list(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@decorators.websocket_command({INCOMPLETE: 'manifest/get', INCOMPLETE: str})
@decorators.async_response
async def handle_manifest_get(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'integration/setup_info'})
def handle_integration_setup_info(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'ping'})
def handle_ping(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@lru_cache
def _cached_template(template_str: str, hass: HomeAssistant) -> template.Template: ...
@decorators.websocket_command({INCOMPLETE: 'render_template', INCOMPLETE: str, INCOMPLETE: cv.entity_ids, INCOMPLETE: dict, INCOMPLETE: vol.Coerce(float), INCOMPLETE: bool, INCOMPLETE: bool})
@decorators.async_response
async def handle_render_template(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def _serialize_entity_sources(entity_infos: dict[str, entity.EntityInfo]) -> dict[str, Any]: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'entity/source'})
def handle_entity_source(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@decorators.websocket_command({INCOMPLETE: 'subscribe_trigger', INCOMPLETE: cv.TRIGGER_SCHEMA, INCOMPLETE: dict})
@decorators.require_admin
@decorators.async_response
async def handle_subscribe_trigger(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@decorators.websocket_command({INCOMPLETE: 'test_condition', INCOMPLETE: cv.CONDITION_SCHEMA, INCOMPLETE: dict})
@decorators.require_admin
@decorators.async_response
async def handle_test_condition(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@decorators.websocket_command({INCOMPLETE: 'execute_script', INCOMPLETE: cv.SCRIPT_SCHEMA, INCOMPLETE: dict})
@decorators.require_admin
@decorators.async_response
async def handle_execute_script(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'fire_event', INCOMPLETE: str, INCOMPLETE: dict})
@decorators.require_admin
def handle_fire_event(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@decorators.websocket_command({INCOMPLETE: 'validate_config', INCOMPLETE: cv.match_all, INCOMPLETE: cv.match_all, INCOMPLETE: cv.match_all})
@decorators.async_response
async def handle_validate_config(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@decorators.websocket_command({INCOMPLETE: 'supported_features', INCOMPLETE: {INCOMPLETE: int}})
def handle_supported_features(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@decorators.require_admin
@decorators.websocket_command({'type': 'integration/descriptions'})
@decorators.async_response
async def handle_integration_descriptions(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
