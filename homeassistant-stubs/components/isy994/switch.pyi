from .const import DOMAIN as DOMAIN
from .entity import ISYAuxControlEntity as ISYAuxControlEntity, ISYNodeEntity as ISYNodeEntity, ISYProgramEntity as ISYProgramEntity
from .models import IsyData as IsyData
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory, EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyisy.helpers import EventListener as EventListener
from pyisy.nodes import Node as Node, NodeChangedEvent as NodeChangedEvent
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYSwitchEntity(ISYNodeEntity, SwitchEntity):
    @property
    def is_on(self) -> Union[bool, None]: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @property
    def icon(self) -> Union[str, None]: ...

class ISYSwitchProgramEntity(ISYProgramEntity, SwitchEntity):
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def icon(self) -> str: ...

class ISYEnableSwitchEntity(ISYAuxControlEntity, SwitchEntity):
    _attr_name: Incomplete
    _change_handler: Incomplete
    def __init__(self, node: Node, control: str, unique_id: str, description: EntityDescription, device_info: Union[DeviceInfo, None]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_on_update(self, event: NodeChangedEvent, key: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
