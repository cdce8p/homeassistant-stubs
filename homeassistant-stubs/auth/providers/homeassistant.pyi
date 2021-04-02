from . import AUTH_PROVIDERS as AUTH_PROVIDERS, AUTH_PROVIDER_SCHEMA as AUTH_PROVIDER_SCHEMA, AuthProvider as AuthProvider, LoginFlow as LoginFlow
from ..models import Credentials as Credentials, UserMeta as UserMeta
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

STORAGE_VERSION: int
STORAGE_KEY: str

def _disallow_id(conf: dict[str, Any]) -> dict[str, Any]: ...

CONFIG_SCHEMA: Any

def async_get_provider(hass: HomeAssistant) -> HassAuthProvider: ...

class InvalidAuth(HomeAssistantError): ...
class InvalidUser(HomeAssistantError): ...

class Data:
    hass: Any = ...
    _store: Any = ...
    _data: Any = ...
    is_legacy: bool = ...
    def __init__(self, hass: HomeAssistant) -> None: ...
    def normalize_username(self, username: str) -> str: ...
    async def async_load(self) -> None: ...
    @property
    def users(self) -> list[dict[str, str]]: ...
    def validate_login(self, username: str, password: str) -> None: ...
    def hash_password(self, password: str, for_storage: bool=...) -> bytes: ...
    def add_auth(self, username: str, password: str) -> None: ...
    def async_remove_auth(self, username: str) -> None: ...
    def change_password(self, username: str, new_password: str) -> None: ...
    async def async_save(self) -> None: ...

class HassAuthProvider(AuthProvider):
    DEFAULT_TITLE: str = ...
    data: Any = ...
    _init_lock: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_login_flow(self, context: Union[dict, None]) -> LoginFlow: ...
    async def async_validate_login(self, username: str, password: str) -> None: ...
    async def async_add_auth(self, username: str, password: str) -> None: ...
    async def async_remove_auth(self, username: str) -> None: ...
    async def async_change_password(self, username: str, new_password: str) -> None: ...
    async def async_get_or_create_credentials(self, flow_result: dict[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...
    async def async_will_remove_credentials(self, credentials: Credentials) -> None: ...

class HassLoginFlow(LoginFlow):
    async def async_step_init(self, user_input: Union[dict[str, str], None]=...) -> dict[str, Any]: ...
