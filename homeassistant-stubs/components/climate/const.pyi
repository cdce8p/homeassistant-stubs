from _typeshed import Incomplete
from enum import IntFlag, StrEnum

class HVACMode(StrEnum):
    OFF: str
    HEAT: str
    COOL: str
    HEAT_COOL: str
    AUTO: str
    DRY: str
    FAN_ONLY: str

HVAC_MODE_OFF: str
HVAC_MODE_HEAT: str
HVAC_MODE_COOL: str
HVAC_MODE_HEAT_COOL: str
HVAC_MODE_AUTO: str
HVAC_MODE_DRY: str
HVAC_MODE_FAN_ONLY: str
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

CURRENT_HVAC_OFF: str
CURRENT_HVAC_HEAT: str
CURRENT_HVAC_COOL: str
CURRENT_HVAC_DRY: str
CURRENT_HVAC_IDLE: str
CURRENT_HVAC_FAN: str
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

SUPPORT_TARGET_TEMPERATURE: int
SUPPORT_TARGET_TEMPERATURE_RANGE: int
SUPPORT_TARGET_HUMIDITY: int
SUPPORT_FAN_MODE: int
SUPPORT_PRESET_MODE: int
SUPPORT_SWING_MODE: int
SUPPORT_AUX_HEAT: int