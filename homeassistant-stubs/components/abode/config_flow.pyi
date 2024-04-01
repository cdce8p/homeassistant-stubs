from .const import CONF_POLLING as CONF_POLLING, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from typing import Any

CONF_MFA: str

class AbodeFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data_schema: Incomplete
    mfa_data_schema: Incomplete
    _mfa_code: Incomplete
    _password: Incomplete
    _polling: bool
    _username: Incomplete
    def __init__(self) -> None: ...
    async def _async_abode_login(self, step_id: str) -> ConfigFlowResult: ...
    async def _async_abode_mfa_login(self) -> ConfigFlowResult: ...
    async def _async_create_entry(self) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_mfa(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
