import aiohttp
from aiohttp import web
from homeassistant.const import EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.frame import warn_use as warn_use
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Awaitable

DATA_CONNECTOR: str
DATA_CONNECTOR_NOTVERIFY: str
DATA_CLIENTSESSION: str
DATA_CLIENTSESSION_NOTVERIFY: str
SERVER_SOFTWARE: Any

def async_get_clientsession(hass: HomeAssistant, verify_ssl: bool=...) -> aiohttp.ClientSession: ...
def async_create_clientsession(hass: HomeAssistant, verify_ssl: bool=..., auto_cleanup: bool=..., **kwargs: Any) -> aiohttp.ClientSession: ...
async def async_aiohttp_proxy_web(hass: HomeAssistant, request: web.BaseRequest, web_coro: Awaitable[aiohttp.ClientResponse], buffer_size: int=..., timeout: int=...) -> Union[web.StreamResponse, None]: ...
async def async_aiohttp_proxy_stream(hass: HomeAssistant, request: web.BaseRequest, stream: aiohttp.StreamReader, content_type: Union[str, None], buffer_size: int=..., timeout: int=...) -> web.StreamResponse: ...