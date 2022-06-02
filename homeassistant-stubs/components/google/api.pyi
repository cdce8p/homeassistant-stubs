import aiohttp
from .const import CONF_CALENDAR_ACCESS as CONF_CALENDAR_ACCESS, DATA_CONFIG as DATA_CONFIG, DEFAULT_FEATURE_ACCESS as DEFAULT_FEATURE_ACCESS, DOMAIN as DOMAIN, FeatureAccess as FeatureAccess
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from gcal_sync.auth import AbstractAuth
from homeassistant.components.application_credentials import AuthImplementation as AuthImplementation
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.util import dt as dt
from oauth2client.client import Credentials as Credentials, DeviceFlowInfo as DeviceFlowInfo, OAuth2WebServerFlow
from typing import Any

_LOGGER: Incomplete
EVENT_PAGE_SIZE: int
EXCHANGE_TIMEOUT_SECONDS: int
DEVICE_AUTH_CREDS: str

class OAuthError(Exception): ...

class DeviceAuth(AuthImplementation):
    async def async_resolve_external_data(self, external_data: Any) -> dict: ...

class DeviceFlow:
    _hass: Incomplete
    _oauth_flow: Incomplete
    _device_flow_info: Incomplete
    _exchange_task_unsub: Incomplete
    def __init__(self, hass: HomeAssistant, oauth_flow: OAuth2WebServerFlow, device_flow_info: DeviceFlowInfo) -> None: ...
    @property
    def verification_url(self) -> str: ...
    @property
    def user_code(self) -> str: ...
    async def start_exchange_task(self, finished_cb: Callable[[Union[Credentials, None]], Awaitable[None]]) -> None: ...

def get_feature_access(hass: HomeAssistant, config_entry: Union[ConfigEntry, None] = ...) -> FeatureAccess: ...
async def async_create_device_flow(hass: HomeAssistant, client_id: str, client_secret: str, access: FeatureAccess) -> DeviceFlow: ...

class ApiAuthImpl(AbstractAuth):
    _session: Incomplete
    def __init__(self, websession: aiohttp.ClientSession, session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def async_get_access_token(self) -> str: ...

class AccessTokenAuthImpl(AbstractAuth):
    _access_token: Incomplete
    def __init__(self, websession: aiohttp.ClientSession, access_token: str) -> None: ...
    async def async_get_access_token(self) -> str: ...