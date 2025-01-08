import voluptuous as vol
from homeassistant import loader as loader
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import require_admin as require_admin
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry, DeviceEntryDisabler as DeviceEntryDisabler
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...
@callback
@websocket_api.websocket_command({INCOMPLETE: 'config/device_registry/list'})
def websocket_list_devices(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@require_admin
@websocket_api.websocket_command({INCOMPLETE: 'config/device_registry/update', INCOMPLETE: vol.Any(str, None), INCOMPLETE: str, INCOMPLETE: vol.Any(DeviceEntryDisabler.USER.value, None), INCOMPLETE: [str], INCOMPLETE: vol.Any(str, None)})
@callback
def websocket_update_device(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.websocket_command({'type': 'config/device_registry/remove_config_entry', 'config_entry_id': str, 'device_id': str})
@websocket_api.async_response
async def websocket_remove_config_entry_from_device(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
