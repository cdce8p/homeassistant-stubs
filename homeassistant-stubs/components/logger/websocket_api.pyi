from .const import LOGSEVERITY as LOGSEVERITY
from .helpers import LogPersistance as LogPersistance, LogSettingsType as LogSettingsType, LoggerSetting as LoggerSetting, async_get_domain_config as async_get_domain_config, get_logger as get_logger
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api.connection import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from homeassistant.setup import async_get_loaded_integrations as async_get_loaded_integrations
from typing import Any

def async_load_websocket_api(hass: HomeAssistant) -> None: ...
def handle_integration_log_info(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_integration_log_level(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
async def handle_module_log_level(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
