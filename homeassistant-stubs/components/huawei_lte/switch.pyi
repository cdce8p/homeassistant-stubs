from . import HuaweiLteBaseEntity as HuaweiLteBaseEntity
from .const import DOMAIN as DOMAIN, KEY_DIALUP_MOBILE_DATASWITCH as KEY_DIALUP_MOBILE_DATASWITCH
from homeassistant.components.switch import DEVICE_CLASS_SWITCH as DEVICE_CLASS_SWITCH, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Callable

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistantType, config_entry: ConfigEntry, async_add_entities: Callable[[list[Entity], bool], None]) -> None: ...

class HuaweiLteBaseSwitch(HuaweiLteBaseEntity, SwitchEntity):
    key: str
    item: str
    _raw_state: Union[str, None] = ...
    def _turn(self, state: bool) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    def device_class(self) -> str: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _available: bool = ...
    async def async_update(self) -> None: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, raw_state: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class HuaweiLteMobileDataSwitch(HuaweiLteBaseSwitch):
    key: Any = ...
    item: str = ...
    def __attrs_post_init__(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    @property
    def _device_unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    _raw_state: Any = ...
    def _turn(self, state: bool) -> None: ...
    @property
    def icon(self) -> str: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, raw_state: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
