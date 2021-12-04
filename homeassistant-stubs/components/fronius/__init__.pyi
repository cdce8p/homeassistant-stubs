from .const import DOMAIN as DOMAIN, FroniusDeviceInfo as FroniusDeviceInfo, SOLAR_NET_ID_SYSTEM as SOLAR_NET_ID_SYSTEM
from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase, FroniusInverterUpdateCoordinator as FroniusInverterUpdateCoordinator, FroniusLoggerUpdateCoordinator as FroniusLoggerUpdateCoordinator, FroniusMeterUpdateCoordinator as FroniusMeterUpdateCoordinator, FroniusOhmpilotUpdateCoordinator as FroniusOhmpilotUpdateCoordinator, FroniusPowerFlowUpdateCoordinator as FroniusPowerFlowUpdateCoordinator, FroniusStorageUpdateCoordinator as FroniusStorageUpdateCoordinator
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from pyfronius import Fronius
from typing import Any, TypeVar

_LOGGER: Any
PLATFORMS: list[str]
FroniusCoordinatorType = TypeVar('FroniusCoordinatorType', bound=FroniusCoordinatorBase)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_update_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class FroniusSolarNet:
    hass: Any
    cleanup_callbacks: Any
    config_entry: Any
    coordinator_lock: Any
    fronius: Any
    host: Any
    solar_net_device_id: Any
    system_device_info: Any
    inverter_coordinators: Any
    logger_coordinator: Any
    meter_coordinator: Any
    ohmpilot_coordinator: Any
    power_flow_coordinator: Any
    storage_coordinator: Any
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, fronius: Fronius) -> None: ...
    async def init_devices(self) -> None: ...
    async def _create_solar_net_device(self) -> DeviceInfo: ...
    async def _get_inverter_infos(self) -> list[FroniusDeviceInfo]: ...
    @staticmethod
    async def _init_optional_coordinator(coordinator: FroniusCoordinatorType) -> Union[FroniusCoordinatorType, None]: ...