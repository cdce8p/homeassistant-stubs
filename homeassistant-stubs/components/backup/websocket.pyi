from .const import DOMAIN as DOMAIN
from .manager import BackupManager as BackupManager
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_register_websocket_handlers(hass: HomeAssistant) -> None: ...
async def handle_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def handle_remove(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def handle_create(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...