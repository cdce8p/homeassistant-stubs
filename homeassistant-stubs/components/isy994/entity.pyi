from . import _async_isy_to_configuration_url as _async_isy_to_configuration_url
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_SUGGESTED_AREA as ATTR_SUGGESTED_AREA, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from pyisy.helpers import EventListener as EventListener, NodeProperty as NodeProperty
from pyisy.nodes import Node as Node
from pyisy.programs import Program as Program
from typing import Any

class ISYEntity(Entity):
    _name: Union[str, None]
    _attr_should_poll: bool
    _node: Incomplete
    _attrs: Incomplete
    _change_handler: Incomplete
    _control_handler: Incomplete
    def __init__(self, node: Node) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_on_update(self, event: NodeProperty) -> None: ...
    def async_on_control(self, event: NodeProperty) -> None: ...
    @property
    def device_info(self) -> Union[DeviceInfo, None]: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def old_unique_id(self) -> Union[str, None]: ...
    @property
    def name(self) -> str: ...

class ISYNodeEntity(ISYEntity):
    @property
    def extra_state_attributes(self) -> dict: ...
    async def async_send_node_command(self, command: str) -> None: ...
    async def async_send_raw_node_command(self, command: str, value: Union[Any, None] = ..., unit_of_measurement: Union[str, None] = ..., parameters: Union[Any, None] = ...) -> None: ...
    async def async_get_zwave_parameter(self, parameter: Any) -> None: ...
    async def async_set_zwave_parameter(self, parameter: Any, value: Union[Any, None], size: Union[int, None]) -> None: ...
    async def async_rename_node(self, name: str) -> None: ...

class ISYProgramEntity(ISYEntity):
    _name: Incomplete
    _actions: Incomplete
    def __init__(self, name: str, status: Union[Any, None], actions: Program = ...) -> None: ...
    @property
    def extra_state_attributes(self) -> dict: ...
