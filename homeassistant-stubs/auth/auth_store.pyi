from . import models as models
from .const import ACCESS_TOKEN_EXPIRATION as ACCESS_TOKEN_EXPIRATION, GROUP_ID_ADMIN as GROUP_ID_ADMIN, GROUP_ID_READ_ONLY as GROUP_ID_READ_ONLY, GROUP_ID_USER as GROUP_ID_USER, REFRESH_TOKEN_EXPIRATION as REFRESH_TOKEN_EXPIRATION
from .permissions import system_policies as system_policies
from .permissions.models import PermissionLookup as PermissionLookup
from .permissions.types import PolicyType as PolicyType
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from typing import Any

STORAGE_VERSION: int
STORAGE_KEY: str
GROUP_NAME_ADMIN: str
GROUP_NAME_USER: str
GROUP_NAME_READ_ONLY: str
INITIAL_LOAD_SAVE_DELAY: int
DEFAULT_SAVE_DELAY: int

class AuthStore:
    hass: Incomplete
    _loaded: bool
    _users: Incomplete
    _groups: Incomplete
    _perm_lookup: Incomplete
    _store: Incomplete
    _token_id_to_user_id: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_get_groups(self) -> list[models.Group]: ...
    async def async_get_group(self, group_id: str) -> models.Group | None: ...
    async def async_get_users(self) -> list[models.User]: ...
    async def async_get_user(self, user_id: str) -> models.User | None: ...
    async def async_create_user(self, name: str | None, is_owner: bool | None = None, is_active: bool | None = None, system_generated: bool | None = None, credentials: models.Credentials | None = None, group_ids: list[str] | None = None, local_only: bool | None = None) -> models.User: ...
    async def async_link_user(self, user: models.User, credentials: models.Credentials) -> None: ...
    async def async_remove_user(self, user: models.User) -> None: ...
    async def async_update_user(self, user: models.User, name: str | None = None, is_active: bool | None = None, group_ids: list[str] | None = None, local_only: bool | None = None) -> None: ...
    async def async_activate_user(self, user: models.User) -> None: ...
    async def async_deactivate_user(self, user: models.User) -> None: ...
    async def async_remove_credentials(self, credentials: models.Credentials) -> None: ...
    async def async_create_refresh_token(self, user: models.User, client_id: str | None = None, client_name: str | None = None, client_icon: str | None = None, token_type: str = ..., access_token_expiration: timedelta = ..., expire_at: float | None = None, credential: models.Credentials | None = None) -> models.RefreshToken: ...
    def async_remove_refresh_token(self, refresh_token: models.RefreshToken) -> None: ...
    def async_get_refresh_token(self, token_id: str) -> models.RefreshToken | None: ...
    def async_get_refresh_token_by_token(self, token: str) -> models.RefreshToken | None: ...
    def async_get_refresh_tokens(self) -> list[models.RefreshToken]: ...
    def async_log_refresh_token_usage(self, refresh_token: models.RefreshToken, remote_ip: str | None = None) -> None: ...
    def async_set_expiry(self, refresh_token: models.RefreshToken, *, enable_expiry: bool) -> None: ...
    async def async_load(self) -> None: ...
    def _build_token_id_to_user_id(self) -> None: ...
    def _async_schedule_save(self, delay: float = ...) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, Any]]]: ...
    def _set_defaults(self) -> None: ...

def _system_admin_group() -> models.Group: ...
def _system_user_group() -> models.Group: ...
def _system_read_only_group() -> models.Group: ...
