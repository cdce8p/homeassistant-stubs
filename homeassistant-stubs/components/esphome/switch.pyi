from . import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import SwitchInfo, SwitchState
from homeassistant.components.switch import DEVICE_CLASSES as DEVICE_CLASSES, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeSwitch(EsphomeEntity[SwitchInfo, SwitchState], SwitchEntity):
    @property
    def assumed_state(self) -> bool: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
