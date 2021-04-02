from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_COMMAND as ATTR_COMMAND, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_IDLE as STATE_IDLE, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import Entity as Entity, ToggleEntity as ToggleEntity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Optional

_LOGGER: Any
DOMAIN: str
SCAN_INTERVAL: Any
ATTR_BATTERY_ICON: str
ATTR_CLEANED_AREA: str
ATTR_FAN_SPEED: str
ATTR_FAN_SPEED_LIST: str
ATTR_PARAMS: str
ATTR_STATUS: str
SERVICE_CLEAN_SPOT: str
SERVICE_LOCATE: str
SERVICE_RETURN_TO_BASE: str
SERVICE_SEND_COMMAND: str
SERVICE_SET_FAN_SPEED: str
SERVICE_START_PAUSE: str
SERVICE_START: str
SERVICE_PAUSE: str
SERVICE_STOP: str
STATE_CLEANING: str
STATE_DOCKED: str
STATE_RETURNING: str
STATE_ERROR: str
STATES: Any
DEFAULT_NAME: str
SUPPORT_TURN_ON: int
SUPPORT_TURN_OFF: int
SUPPORT_PAUSE: int
SUPPORT_STOP: int
SUPPORT_RETURN_HOME: int
SUPPORT_FAN_SPEED: int
SUPPORT_BATTERY: int
SUPPORT_STATUS: int
SUPPORT_SEND_COMMAND: int
SUPPORT_LOCATE: int
SUPPORT_CLEAN_SPOT: int
SUPPORT_MAP: int
SUPPORT_STATE: int
SUPPORT_START: int

def is_on(hass: Any, entity_id: Any): ...
async def async_setup(hass: Any, config: Any): ...
async def async_setup_entry(hass: Any, entry: Any): ...
async def async_unload_entry(hass: Any, entry: Any): ...

class _BaseVacuum(Entity):
    @property
    def supported_features(self) -> None: ...
    @property
    def battery_level(self) -> None: ...
    @property
    def battery_icon(self) -> None: ...
    @property
    def fan_speed(self) -> None: ...
    @property
    def fan_speed_list(self) -> None: ...
    @property
    def capability_attributes(self): ...
    @property
    def state_attributes(self): ...
    def stop(self, **kwargs: Any) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    def return_to_base(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    def clean_spot(self, **kwargs: Any) -> None: ...
    async def async_clean_spot(self, **kwargs: Any) -> None: ...
    def locate(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    def set_fan_speed(self, fan_speed: Any, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: Any, **kwargs: Any) -> None: ...
    def send_command(self, command: Any, params: Optional[Any] = ..., **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Any, params: Optional[Any] = ..., **kwargs: Any) -> None: ...

class VacuumEntity(_BaseVacuum, ToggleEntity):
    @property
    def status(self) -> None: ...
    @property
    def battery_icon(self): ...
    @property
    def state_attributes(self): ...
    def turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def start_pause(self, **kwargs: Any) -> None: ...
    async def async_start_pause(self, **kwargs: Any) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_start(self) -> None: ...

class VacuumDevice(VacuumEntity):
    def __init_subclass__(cls, **kwargs: Any) -> None: ...

class StateVacuumEntity(_BaseVacuum):
    @property
    def state(self) -> None: ...
    @property
    def battery_icon(self): ...
    def start(self) -> None: ...
    async def async_start(self) -> None: ...
    def pause(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...

class StateVacuumDevice(StateVacuumEntity):
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
