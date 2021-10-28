from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.config_entry_flow import DiscoveryFlowHandler as DiscoveryFlowHandler
from typing import Any

async def _async_supported(hass: HomeAssistant) -> bool: ...

class RPiPowerFlow(DiscoveryFlowHandler):
    VERSION: int
    def __init__(self) -> None: ...
    async def async_step_onboarding(self, data: Union[dict[str, Any], None] = ...) -> FlowResult: ...
