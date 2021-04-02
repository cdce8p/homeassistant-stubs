from .const import CONTROLLER_MODES as CONTROLLER_MODES, DOMAIN as DOMAIN, PRESET_MODES as PRESET_MODES
from .knx_entity import KnxEntity as KnxEntity
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import HVAC_MODE_HEAT as HVAC_MODE_HEAT, HVAC_MODE_OFF as HVAC_MODE_OFF, PRESET_AWAY as PRESET_AWAY, SUPPORT_PRESET_MODE as SUPPORT_PRESET_MODE, SUPPORT_TARGET_TEMPERATURE as SUPPORT_TARGET_TEMPERATURE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Callable, Iterable
from xknx.devices import Climate as XknxClimate

CONTROLLER_MODES_INV: Any
PRESET_MODES_INV: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: Callable[[Iterable[Entity]], None], discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...

class KNXClimate(KnxEntity, ClimateEntity):
    _device: Any
    _unit_of_measurement: Any = ...
    def __init__(self, device: XknxClimate) -> None: ...
    @property
    def supported_features(self) -> int: ...
    async def async_update(self) -> None: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature_step(self) -> float: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def hvac_mode(self) -> str: ...
    @property
    def hvac_modes(self) -> list[str]: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def preset_modes(self) -> Union[list[str], None]: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
