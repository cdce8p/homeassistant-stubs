from .common import AvmWrapper as AvmWrapper, FritzBoxBaseEntity as FritzBoxBaseEntity, FritzData as FritzData, FritzDevice as FritzDevice, FritzDeviceBase as FritzDeviceBase, SwitchInfo as SwitchInfo, device_filter_out_from_trackers as device_filter_out_from_trackers
from .const import DATA_FRITZ as DATA_FRITZ, DOMAIN as DOMAIN, MeshRoles as MeshRoles, SWITCH_TYPE_DEFLECTION as SWITCH_TYPE_DEFLECTION, SWITCH_TYPE_PORTFORWARD as SWITCH_TYPE_PORTFORWARD, SWITCH_TYPE_PROFILE as SWITCH_TYPE_PROFILE, SWITCH_TYPE_WIFINETWORK as SWITCH_TYPE_WIFINETWORK, WIFI_STANDARD as WIFI_STANDARD
from _typeshed import Incomplete
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Incomplete

async def _async_deflection_entities_list(avm_wrapper: AvmWrapper, device_friendly_name: str) -> list[FritzBoxDeflectionSwitch]: ...
async def _async_port_entities_list(avm_wrapper: AvmWrapper, device_friendly_name: str, local_ip: str) -> list[FritzBoxPortSwitch]: ...
async def _async_wifi_entities_list(avm_wrapper: AvmWrapper, device_friendly_name: str) -> list[FritzBoxWifiSwitch]: ...
async def _async_profile_entities_list(avm_wrapper: AvmWrapper, data_fritz: FritzData) -> list[FritzBoxProfileSwitch]: ...
async def async_all_entities_list(avm_wrapper: AvmWrapper, device_friendly_name: str, data_fritz: FritzData, local_ip: str) -> list[Entity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxBaseCoordinatorSwitch(CoordinatorEntity, SwitchEntity):
    coordinator: AvmWrapper
    entity_description: SwitchEntityDescription
    _attr_has_entity_name: bool
    _device_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_name: str, description: SwitchEntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def data(self) -> dict[str, Any]: ...
    @property
    def available(self) -> bool: ...
    async def _async_handle_turn_on_off(self, turn_on: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class FritzBoxBaseSwitch(FritzBoxBaseEntity):
    _attr_is_on: bool | None
    _description: Incomplete
    _friendly_name: Incomplete
    _icon: Incomplete
    _type: Incomplete
    _update: Incomplete
    _switch: Incomplete
    _name: Incomplete
    _unique_id: Incomplete
    _attributes: Incomplete
    _is_available: bool
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, switch_info: SwitchInfo) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    async def async_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_handle_turn_on_off(self, turn_on: bool) -> None: ...

class FritzBoxPortSwitch(FritzBoxBaseSwitch, SwitchEntity):
    _avm_wrapper: Incomplete
    _attributes: Incomplete
    connection_type: Incomplete
    port_mapping: Incomplete
    _idx: Incomplete
    _attr_entity_category: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, port_mapping: dict[str, Any] | None, port_name: str, idx: int, connection_type: str) -> None: ...
    _is_available: bool
    _attr_is_on: Incomplete
    async def _async_fetch_update(self) -> None: ...
    async def _async_switch_on_off_executor(self, turn_on: bool) -> bool: ...

class FritzBoxDeflectionSwitch(FritzBoxBaseCoordinatorSwitch):
    _attr_entity_category: Incomplete
    deflection_id: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, deflection_id: int) -> None: ...
    @property
    def data(self) -> dict[str, Any]: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    @property
    def is_on(self) -> bool | None: ...
    async def _async_handle_turn_on_off(self, turn_on: bool) -> None: ...

class FritzBoxProfileSwitch(FritzDeviceBase, SwitchEntity):
    _attr_icon: str
    _attr_is_on: bool
    _name: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_category: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device: FritzDevice) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_handle_turn_on_off(self, turn_on: bool) -> bool: ...

class FritzBoxWifiSwitch(FritzBoxBaseSwitch, SwitchEntity):
    _avm_wrapper: Incomplete
    _attributes: Incomplete
    _attr_entity_category: Incomplete
    _network_num: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, network_num: int, network_name: str) -> None: ...
    _is_available: bool
    _attr_is_on: Incomplete
    async def _async_fetch_update(self) -> None: ...
    async def _async_switch_on_off_executor(self, turn_on: bool) -> None: ...
