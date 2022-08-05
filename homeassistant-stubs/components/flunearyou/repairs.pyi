from .const import DOMAIN as DOMAIN
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant as HomeAssistant

class FluNearYouFixFlow(RepairsFlow):
    async def async_step_init(self, user_input: Union[dict[str, str], None] = ...) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, str], None] = ...) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str) -> FluNearYouFixFlow: ...
