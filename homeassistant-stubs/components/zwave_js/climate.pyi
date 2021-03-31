from .const import DATA_CLIENT as DATA_CLIENT, DATA_UNSUBSCRIBE as DATA_UNSUBSCRIBE, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, CURRENT_HVAC_COOL as CURRENT_HVAC_COOL, CURRENT_HVAC_FAN as CURRENT_HVAC_FAN, CURRENT_HVAC_HEAT as CURRENT_HVAC_HEAT, CURRENT_HVAC_IDLE as CURRENT_HVAC_IDLE, HVAC_MODE_COOL as HVAC_MODE_COOL, HVAC_MODE_DRY as HVAC_MODE_DRY, HVAC_MODE_FAN_ONLY as HVAC_MODE_FAN_ONLY, HVAC_MODE_HEAT as HVAC_MODE_HEAT, HVAC_MODE_HEAT_COOL as HVAC_MODE_HEAT_COOL, HVAC_MODE_OFF as HVAC_MODE_OFF, PRESET_NONE as PRESET_NONE, SUPPORT_FAN_MODE as SUPPORT_FAN_MODE, SUPPORT_PRESET_MODE as SUPPORT_PRESET_MODE, SUPPORT_TARGET_TEMPERATURE as SUPPORT_TARGET_TEMPERATURE, SUPPORT_TARGET_TEMPERATURE_RANGE as SUPPORT_TARGET_TEMPERATURE_RANGE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from typing import Any, Callable
from zwave_js_server.client import Client as ZwaveClient

ZW_HVAC_MODE_MAP: dict[int, str]
HVAC_CURRENT_MAP: dict[int, str]
ATTR_FAN_STATE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: Callable) -> None: ...

class ZWaveClimate(ZWaveBaseEntity, ClimateEntity):
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def precision(self) -> float: ...
    @property
    def hvac_mode(self) -> str: ...
    @property
    def hvac_modes(self) -> list[str]: ...
    @property
    def hvac_action(self) -> Union[str, None]: ...
    @property
    def current_humidity(self) -> Union[int, None]: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature_high(self) -> Union[float, None]: ...
    @property
    def target_temperature_low(self) -> Union[float, None]: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def preset_modes(self) -> Union[list[str], None]: ...
    @property
    def fan_mode(self) -> Union[str, None]: ...
    @property
    def fan_modes(self) -> Union[list[str], None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...
    @property
    def supported_features(self) -> int: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...