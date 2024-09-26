from . import RoborockConfigEntry as RoborockConfigEntry
from .const import DOMAIN as DOMAIN, GET_MAPS_SERVICE_NAME as GET_MAPS_SERVICE_NAME
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from homeassistant.components.vacuum import STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_ERROR as STATE_ERROR, STATE_IDLE as STATE_IDLE, STATE_PAUSED as STATE_PAUSED, STATE_RETURNING as STATE_RETURNING, StateVacuumEntity as StateVacuumEntity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

STATE_CODE_TO_STATE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockVacuum(RoborockCoordinatedEntityV1, StateVacuumEntity):
    _attr_icon: str
    _attr_supported_features: Incomplete
    _attr_translation_key = DOMAIN
    _attr_name: Incomplete
    _attr_fan_speed_list: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator) -> None: ...
    @property
    def state(self) -> str | None: ...
    @property
    def battery_level(self) -> int | None: ...
    @property
    def fan_speed(self) -> str | None: ...
    async def async_start(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_clean_spot(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: str, params: dict[str, Any] | list[Any] | None = None, **kwargs: Any) -> None: ...
    async def get_maps(self) -> ServiceResponse: ...
