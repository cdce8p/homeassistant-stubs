from .helpers import async_get_node_from_device_id as async_get_node_from_device_id
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant as HomeAssistant
from zwave_js_server.model.node import Node as Node

class DeviceConfigFileChangedFlow(RepairsFlow):
    node: Incomplete
    def __init__(self, node: Node) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = ...) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = ...) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...