import voluptuous as vol
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ERR_NOT_FOUND as ERR_NOT_FOUND, require_admin as require_admin
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import config_validation as cv, entity_registry as er
from homeassistant.helpers.json import json_dumps as json_dumps
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/entity_registry/list'})
@callback
def websocket_list_entities(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

_ENTITY_CATEGORIES_JSON: Incomplete

@websocket_api.websocket_command({INCOMPLETE: 'config/entity_registry/list_for_display'})
@callback
def websocket_list_entities_for_display(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/entity_registry/get', INCOMPLETE: cv.entity_id})
@callback
def websocket_get_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/entity_registry/get_entries', INCOMPLETE: cv.entity_ids})
@callback
def websocket_get_entities(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@require_admin
@websocket_api.websocket_command({INCOMPLETE: 'config/entity_registry/update', INCOMPLETE: cv.entity_id, INCOMPLETE: list, INCOMPLETE: vol.Any(str, None), INCOMPLETE: cv.schema_with_slug_keys(vol.Any(str, None)), INCOMPLETE: vol.Any(str, None), INCOMPLETE: vol.Any(str, None), INCOMPLETE: [str], INCOMPLETE: vol.Any(str, None), INCOMPLETE: str, INCOMPLETE: vol.Any(None, vol.All(vol.Coerce(er.RegistryEntryDisabler), er.RegistryEntryDisabler.USER.value)), INCOMPLETE: vol.Any(None, vol.All(vol.Coerce(er.RegistryEntryHider), er.RegistryEntryHider.USER.value)), INCOMPLETE: str, INCOMPLETE: vol.Any(None, dict)})
@callback
def websocket_update_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@require_admin
@websocket_api.websocket_command({INCOMPLETE: 'config/entity_registry/remove', INCOMPLETE: cv.entity_id})
@callback
def websocket_remove_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
