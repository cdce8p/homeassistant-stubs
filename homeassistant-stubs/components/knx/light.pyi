from .const import DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import LightSchema as LightSchema
from collections.abc import Iterable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_WHITE_VALUE as ATTR_WHITE_VALUE, LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_COLOR as SUPPORT_COLOR, SUPPORT_COLOR_TEMP as SUPPORT_COLOR_TEMP, SUPPORT_WHITE_VALUE as SUPPORT_WHITE_VALUE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Callable
from xknx.devices import Light as XknxLight

DEFAULT_COLOR: Any
DEFAULT_BRIGHTNESS: int
DEFAULT_WHITE_VALUE: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: Callable[[Iterable[Entity]], None], discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...
def _async_migrate_unique_id(hass: HomeAssistant, discovery_info: Union[DiscoveryInfoType, None]) -> None: ...

class KNXLight(KnxEntity, LightEntity):
    _device: Any
    _unique_id: Any = ...
    _min_kelvin: Any = ...
    _max_kelvin: Any = ...
    _min_mireds: Any = ...
    _max_mireds: Any = ...
    def __init__(self, device: XknxLight) -> None: ...
    def _device_unique_id(self) -> str: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def _hsv_color(self) -> Union[tuple[float, float, float], None]: ...
    @property
    def white_value(self) -> Union[int, None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def min_mireds(self) -> int: ...
    @property
    def max_mireds(self) -> int: ...
    @property
    def effect_list(self) -> Union[list[str], None]: ...
    @property
    def effect(self) -> Union[str, None]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def supported_features(self) -> int: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
