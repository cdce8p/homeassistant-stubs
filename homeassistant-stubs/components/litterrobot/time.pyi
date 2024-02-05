from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import datetime, time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic

@dataclass(frozen=True)
class RequiredKeysMixin(Generic[_RobotT]):
    value_fn: Callable[[_RobotT], time | None]
    set_fn: Callable[[_RobotT, time], Coroutine[Any, Any, bool]]
    def __init__(self, value_fn, set_fn) -> None: ...

@dataclass(frozen=True)
class RobotTimeEntityDescription(TimeEntityDescription, RequiredKeysMixin[_RobotT]):
    def __init__(self, value_fn, set_fn, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

def _as_local_time(start: datetime | None) -> time | None: ...

LITTER_ROBOT_3_SLEEP_START: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotTimeEntity(LitterRobotEntity[_RobotT], TimeEntity):
    entity_description: RobotTimeEntityDescription[_RobotT]
    @property
    def native_value(self) -> time | None: ...
    async def async_set_value(self, value: time) -> None: ...
