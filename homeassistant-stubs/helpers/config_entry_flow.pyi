from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any, Awaitable, Callable, Union

DiscoveryFunctionType = Callable[[], Union[Awaitable[bool], bool]]

class DiscoveryFlowHandler(config_entries.ConfigFlow):
    VERSION: int = ...
    CONNECTION_CLASS: Any = ...
    def __init__(self, domain: str, title: str, discovery_function: DiscoveryFunctionType, connection_class: str) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None]=...) -> dict[str, Any]: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None]=...) -> dict[str, Any]: ...
    async def async_step_discovery(self, discovery_info: dict[str, Any]) -> dict[str, Any]: ...
    async_step_zeroconf: Any = ...
    async_step_ssdp: Any = ...
    async_step_mqtt: Any = ...
    async_step_homekit: Any = ...
    async_step_dhcp: Any = ...
    async def async_step_import(self, _: Union[dict[str, Any], None]) -> dict[str, Any]: ...

def register_discovery_flow(domain: str, title: str, discovery_function: DiscoveryFunctionType, connection_class: str) -> None: ...

class WebhookFlowHandler(config_entries.ConfigFlow):
    VERSION: int = ...
    def __init__(self, domain: str, title: str, description_placeholder: dict, allow_multiple: bool) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None]=...) -> dict[str, Any]: ...

def register_webhook_flow(domain: str, title: str, description_placeholder: dict, allow_multiple: bool=...) -> None: ...
async def webhook_async_remove_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> None: ...