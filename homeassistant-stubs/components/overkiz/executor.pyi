from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from pyoverkiz.enums import OverkizCommand
from pyoverkiz.models import Device as Device, StateDefinition as StateDefinition
from pyoverkiz.types import StateType as OverkizStateType
from typing import Any

COMMANDS_WITHOUT_DELAY: Incomplete

class OverkizExecutor:
    device_url: Incomplete
    coordinator: Incomplete
    base_device_url: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def device(self) -> Device: ...
    def linked_device(self, index: int) -> Device | None: ...
    def select_command(self, *commands: str) -> str | None: ...
    def has_command(self, *commands: str) -> bool: ...
    def select_definition_state(self, *states: str) -> StateDefinition | None: ...
    def select_state(self, *states: str) -> OverkizStateType: ...
    def has_state(self, *states: str) -> bool: ...
    def select_attribute(self, *attributes: str) -> OverkizStateType: ...
    async def async_execute_command(self, command_name: str, *args: Any) -> None: ...
    async def async_cancel_command(self, commands_to_cancel: list[OverkizCommand]) -> bool: ...
    async def async_cancel_execution(self, exec_id: str) -> None: ...
    def get_gateway_id(self) -> str: ...
