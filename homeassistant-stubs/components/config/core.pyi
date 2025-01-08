import voluptuous as vol
from aiohttp import web as web
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, require_admin as require_admin
from homeassistant.components.sensor import async_update_suggested_units as async_update_suggested_units
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import check_config as check_config, config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.util import location as location, unit_system as unit_system
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...

class CheckConfigView(HomeAssistantView):
    url: str
    name: str
    @require_admin
    async def post(self, request: web.Request) -> web.Response: ...

@websocket_api.require_admin
@websocket_api.websocket_command({'type': 'config/core/update', INCOMPLETE: cv.country, INCOMPLETE: cv.currency, INCOMPLETE: int, INCOMPLETE: vol.Any(cv.url_no_path, None), INCOMPLETE: vol.Any(cv.url_no_path, None), INCOMPLETE: cv.language, INCOMPLETE: cv.latitude, INCOMPLETE: str, INCOMPLETE: cv.longitude, INCOMPLETE: cv.positive_int, INCOMPLETE: cv.time_zone, INCOMPLETE: bool, INCOMPLETE: unit_system.validate_unit_system})
@websocket_api.async_response
async def websocket_update_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.websocket_command({'type': 'config/core/detect'})
@websocket_api.async_response
async def websocket_detect_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
