from _typeshed import Incomplete
from enum import IntFlag, StrEnum
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants

class HVACMode(StrEnum):
    OFF: str
    HEAT: str
    COOL: str
    HEAT_COOL: str
    AUTO: str
    DRY: str
    FAN_ONLY: str

_DEPRECATED_HVAC_MODE_OFF: Incomplete
_DEPRECATED_HVAC_MODE_HEAT: Incomplete
_DEPRECATED_HVAC_MODE_COOL: Incomplete
_DEPRECATED_HVAC_MODE_HEAT_COOL: Incomplete
_DEPRECATED_HVAC_MODE_AUTO: Incomplete
_DEPRECATED_HVAC_MODE_DRY: Incomplete
_DEPRECATED_HVAC_MODE_FAN_ONLY: Incomplete
HVAC_MODES: Incomplete
PRESET_NONE: str
PRESET_ECO: str
PRESET_AWAY: str
PRESET_BOOST: str
PRESET_COMFORT: str
PRESET_HOME: str
PRESET_SLEEP: str
PRESET_ACTIVITY: str
FAN_ON: str
FAN_OFF: str
FAN_AUTO: str
FAN_LOW: str
FAN_MEDIUM: str
FAN_HIGH: str
FAN_TOP: str
FAN_MIDDLE: str
FAN_FOCUS: str
FAN_DIFFUSE: str
SWING_ON: str
SWING_OFF: str
SWING_BOTH: str
SWING_VERTICAL: str
SWING_HORIZONTAL: str

class HVACAction(StrEnum):
    COOLING: str
    DRYING: str
    FAN: str
    HEATING: str
    IDLE: str
    OFF: str
    PREHEATING: str

_DEPRECATED_CURRENT_HVAC_OFF: Incomplete
_DEPRECATED_CURRENT_HVAC_HEAT: Incomplete
_DEPRECATED_CURRENT_HVAC_COOL: Incomplete
_DEPRECATED_CURRENT_HVAC_DRY: Incomplete
_DEPRECATED_CURRENT_HVAC_IDLE: Incomplete
_DEPRECATED_CURRENT_HVAC_FAN: Incomplete
CURRENT_HVAC_ACTIONS: Incomplete
ATTR_AUX_HEAT: str
ATTR_CURRENT_HUMIDITY: str
ATTR_CURRENT_TEMPERATURE: str
ATTR_FAN_MODES: str
ATTR_FAN_MODE: str
ATTR_PRESET_MODE: str
ATTR_PRESET_MODES: str
ATTR_HUMIDITY: str
ATTR_MAX_HUMIDITY: str
ATTR_MIN_HUMIDITY: str
ATTR_MAX_TEMP: str
ATTR_MIN_TEMP: str
ATTR_HVAC_ACTION: str
ATTR_HVAC_MODES: str
ATTR_HVAC_MODE: str
ATTR_SWING_MODES: str
ATTR_SWING_MODE: str
ATTR_TARGET_TEMP_HIGH: str
ATTR_TARGET_TEMP_LOW: str
ATTR_TARGET_TEMP_STEP: str
DEFAULT_MIN_TEMP: int
DEFAULT_MAX_TEMP: int
DEFAULT_MIN_HUMIDITY: int
DEFAULT_MAX_HUMIDITY: int
DOMAIN: str
SERVICE_SET_AUX_HEAT: str
SERVICE_SET_FAN_MODE: str
SERVICE_SET_PRESET_MODE: str
SERVICE_SET_HUMIDITY: str
SERVICE_SET_HVAC_MODE: str
SERVICE_SET_SWING_MODE: str
SERVICE_SET_TEMPERATURE: str

class ClimateEntityFeature(IntFlag):
    TARGET_TEMPERATURE: int
    TARGET_TEMPERATURE_RANGE: int
    TARGET_HUMIDITY: int
    FAN_MODE: int
    PRESET_MODE: int
    SWING_MODE: int
    AUX_HEAT: int
    TURN_OFF: int
    TURN_ON: int

_DEPRECATED_SUPPORT_TARGET_TEMPERATURE: Incomplete
_DEPRECATED_SUPPORT_TARGET_TEMPERATURE_RANGE: Incomplete
_DEPRECATED_SUPPORT_TARGET_HUMIDITY: Incomplete
_DEPRECATED_SUPPORT_FAN_MODE: Incomplete
_DEPRECATED_SUPPORT_PRESET_MODE: Incomplete
_DEPRECATED_SUPPORT_SWING_MODE: Incomplete
_DEPRECATED_SUPPORT_AUX_HEAT: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
