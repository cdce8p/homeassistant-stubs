from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.network import is_host_valid as is_host_valid
from typing import Any

class DuneHDConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def init_device(self, host: str) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def host_already_configured(self, host: str) -> bool: ...

class CannotConnect(HomeAssistantError): ...
class AlreadyConfigured(HomeAssistantError): ...
