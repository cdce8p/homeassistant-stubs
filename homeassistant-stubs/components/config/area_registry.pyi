import voluptuous as vol
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/area_registry/list'})
@callback
def websocket_list_areas(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/area_registry/create', INCOMPLETE: list, INCOMPLETE: str, INCOMPLETE: str, INCOMPLETE: [str], INCOMPLETE: str, INCOMPLETE: vol.Any(str, None)})
@websocket_api.require_admin
@callback
def websocket_create_area(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/area_registry/delete', INCOMPLETE: str})
@websocket_api.require_admin
@callback
def websocket_delete_area(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/area_registry/update', INCOMPLETE: list, INCOMPLETE: str, INCOMPLETE: vol.Any(str, None), INCOMPLETE: vol.Any(str, None), INCOMPLETE: [str], INCOMPLETE: str, INCOMPLETE: vol.Any(str, None)})
@websocket_api.require_admin
@callback
def websocket_update_area(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
