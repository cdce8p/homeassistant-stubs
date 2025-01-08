import voluptuous as vol
from . import config_validation as cv
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from typing import Any, Generic
from typing_extensions import TypeVar

_FlowManagerT = TypeVar('_FlowManagerT', bound=data_entry_flow.FlowManager[Any, Any], default=data_entry_flow.FlowManager)

class _BaseFlowManagerView(HomeAssistantView, Generic[_FlowManagerT]):
    _flow_mgr: Incomplete
    def __init__(self, flow_mgr: _FlowManagerT) -> None: ...
    def _prepare_result_json(self, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...

class FlowManagerIndexView(_BaseFlowManagerView[_FlowManagerT]):
    @RequestDataValidator(vol.Schema({INCOMPLETE: str, INCOMPLETE: cv.boolean}, extra=vol.ALLOW_EXTRA))
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...
    async def _post_impl(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...
    def get_context(self, data: dict[str, Any]) -> dict[str, Any]: ...

class FlowManagerResourceView(_BaseFlowManagerView[_FlowManagerT]):
    async def get(self, request: web.Request, /, flow_id: str) -> web.Response: ...
    @RequestDataValidator(vol.Schema(dict), allow_empty=True)
    async def post(self, request: web.Request, data: dict[str, Any], flow_id: str) -> web.Response: ...
    async def delete(self, request: web.Request, flow_id: str) -> web.Response: ...
