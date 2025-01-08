import voluptuous as vol
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import category_registry as cr, config_validation as cv
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/category_registry/list', INCOMPLETE: str})
@callback
def websocket_list_categories(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/category_registry/create', INCOMPLETE: str, INCOMPLETE: str, INCOMPLETE: vol.Any(cv.icon, None)})
@websocket_api.require_admin
@callback
def websocket_create_category(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/category_registry/delete', INCOMPLETE: str, INCOMPLETE: str})
@websocket_api.require_admin
@callback
def websocket_delete_category(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/category_registry/update', INCOMPLETE: str, INCOMPLETE: str, INCOMPLETE: str, INCOMPLETE: vol.Any(cv.icon, None)})
@websocket_api.require_admin
@callback
def websocket_update_category(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def _entry_dict(entry: cr.CategoryEntry) -> dict[str, Any]: ...
