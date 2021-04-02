from . import HuaweiLteBaseEntity as HuaweiLteBaseEntity
from .const import DOMAIN as DOMAIN, KEY_MONITORING_CHECK_NOTIFICATIONS as KEY_MONITORING_CHECK_NOTIFICATIONS, KEY_MONITORING_STATUS as KEY_MONITORING_STATUS, KEY_WLAN_WIFI_FEATURE_SWITCH as KEY_WLAN_WIFI_FEATURE_SWITCH
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any, Callable

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistantType, config_entry: ConfigEntry, async_add_entities: Callable[[list[Entity], bool], None]) -> None: ...

class HuaweiLteBaseBinarySensor(HuaweiLteBaseEntity, BinarySensorEntity):
    key: str
    item: str
    _raw_state: Union[str, None] = ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def _device_unique_id(self) -> str: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _available: bool = ...
    async def async_update(self) -> None: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, raw_state: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

CONNECTION_STATE_ATTRIBUTES: Any

class HuaweiLteMobileConnectionBinarySensor(HuaweiLteBaseBinarySensor):
    key: Any = ...
    item: str = ...
    def __attrs_post_init__(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def icon(self) -> str: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, raw_state: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class HuaweiLteBaseWifiStatusBinarySensor(HuaweiLteBaseBinarySensor):
    @property
    def is_on(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def icon(self) -> str: ...

class HuaweiLteWifiStatusBinarySensor(HuaweiLteBaseWifiStatusBinarySensor):
    key: Any = ...
    item: str = ...
    def __attrs_post_init__(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, raw_state: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class HuaweiLteWifi24ghzStatusBinarySensor(HuaweiLteBaseWifiStatusBinarySensor):
    key: Any = ...
    item: str = ...
    def __attrs_post_init__(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, raw_state: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class HuaweiLteWifi5ghzStatusBinarySensor(HuaweiLteBaseWifiStatusBinarySensor):
    key: Any = ...
    item: str = ...
    def __attrs_post_init__(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, raw_state: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class HuaweiLteSmsStorageFullBinarySensor(HuaweiLteBaseBinarySensor):
    key: Any = ...
    item: str = ...
    def __attrs_post_init__(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def icon(self) -> str: ...
    def __init__(self, router: Any, available: Any, unsub_handlers: Any, raw_state: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
