import voluptuous as vol
from _typeshed import Incomplete
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.label_registry import LabelEntry as LabelEntry
from typing import Any

SUPPORTED_LABEL_THEME_COLORS: Incomplete

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/label_registry/list'})
@callback
def websocket_list_labels(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/label_registry/create', INCOMPLETE: str, INCOMPLETE: vol.Any(cv.color_hex, vol.In(SUPPORTED_LABEL_THEME_COLORS), None), INCOMPLETE: vol.Any(str, None), INCOMPLETE: vol.Any(cv.icon, None)})
@websocket_api.require_admin
@callback
def websocket_create_label(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/label_registry/delete', INCOMPLETE: str})
@websocket_api.require_admin
@callback
def websocket_delete_label(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'config/label_registry/update', INCOMPLETE: str, INCOMPLETE: vol.Any(cv.color_hex, vol.In(SUPPORTED_LABEL_THEME_COLORS), None), INCOMPLETE: vol.Any(str, None), INCOMPLETE: vol.Any(cv.icon, None), INCOMPLETE: str})
@websocket_api.require_admin
@callback
def websocket_update_label(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def _entry_dict(entry: LabelEntry) -> dict[str, Any]: ...
