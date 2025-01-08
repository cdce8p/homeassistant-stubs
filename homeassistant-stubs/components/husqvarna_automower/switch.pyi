from . import AutomowerConfigEntry as AutomowerConfigEntry
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerControlEntity as AutomowerControlEntity, WorkAreaControlEntity as WorkAreaControlEntity, _work_area_translation_key as _work_area_translation_key, handle_sending_exception as handle_sending_exception
from _typeshed import Incomplete
from aioautomower.model import StayOutZones as StayOutZones, Zone as Zone
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerScheduleSwitchEntity(AutomowerControlEntity, SwitchEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @handle_sending_exception()
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @handle_sending_exception()
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class StayOutZoneSwitchEntity(AutomowerControlEntity, SwitchEntity):
    _attr_translation_key: str
    coordinator: Incomplete
    stay_out_zone_uid: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: AutomowerDataUpdateCoordinator, mower_id: str, stay_out_zone_uid: str) -> None: ...
    @property
    def stay_out_zones(self) -> StayOutZones: ...
    @property
    def stay_out_zone(self) -> Zone: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @handle_sending_exception(poll_after_sending=True)
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @handle_sending_exception(poll_after_sending=True)
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WorkAreaSwitchEntity(WorkAreaControlEntity, SwitchEntity):
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: AutomowerDataUpdateCoordinator, mower_id: str, work_area_id: int) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @handle_sending_exception(poll_after_sending=True)
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @handle_sending_exception(poll_after_sending=True)
    async def async_turn_on(self, **kwargs: Any) -> None: ...
