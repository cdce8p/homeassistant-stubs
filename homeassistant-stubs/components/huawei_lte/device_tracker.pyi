from . import HuaweiLteBaseEntity as HuaweiLteBaseEntity
from .const import DOMAIN as DOMAIN, KEY_WLAN_HOST_LIST as KEY_WLAN_HOST_LIST, UPDATE_SIGNAL as UPDATE_SIGNAL
from homeassistant.components.device_tracker.config_entry import ScannerEntity as ScannerEntity
from homeassistant.components.device_tracker.const import SOURCE_TYPE_ROUTER as SOURCE_TYPE_ROUTER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import callback as callback
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Callable

_LOGGER: Any
_DEVICE_SCAN: Any

async def async_setup_entry(hass: HomeAssistantType, config_entry: ConfigEntry, async_add_entities: Callable[[list[Entity], bool], None]) -> None: ...
def async_add_new_entities(hass: HomeAssistantType, router_url: str, async_add_entities: Callable[[list[Entity], bool], None], tracked: set[str]) -> None: ...
def _better_snakecase(text: str) -> str: ...

class HuaweiLteScannerEntity(HuaweiLteBaseEntity, ScannerEntity):
    mac: str = ...
    _is_connected: bool = ...
    _hostname: Union[str, None] = ...
    _extra_state_attributes: dict[str, Any] = ...
    def __attrs_post_init__(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    @property
    def _device_unique_id(self) -> str: ...
    @property
    def source_type(self) -> str: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_update(self) -> None: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, mac: Any, is_connected: Any, hostname: Any, extra_state_attributes: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
