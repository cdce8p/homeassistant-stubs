from .const import CHARGER_CURRENT_VERSION_KEY as CHARGER_CURRENT_VERSION_KEY, CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_LOCKED_UNLOCKED_KEY as CHARGER_LOCKED_UNLOCKED_KEY, CHARGER_MAX_CHARGING_CURRENT_KEY as CHARGER_MAX_CHARGING_CURRENT_KEY, CHARGER_NAME_KEY as CHARGER_NAME_KEY, CHARGER_PART_NUMBER_KEY as CHARGER_PART_NUMBER_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, CHARGER_SOFTWARE_KEY as CHARGER_SOFTWARE_KEY, CHARGER_STATUS_DESCRIPTION_KEY as CHARGER_STATUS_DESCRIPTION_KEY, CHARGER_STATUS_ID_KEY as CHARGER_STATUS_ID_KEY, CONF_STATION as CONF_STATION, ChargerStatus as ChargerStatus, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any
from wallbox import Wallbox

_LOGGER: Incomplete
PLATFORMS: Incomplete
UPDATE_INTERVAL: int
CHARGER_STATUS: dict[int, ChargerStatus]

class WallboxCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    _station: Incomplete
    _wallbox: Incomplete
    def __init__(self, station: str, wallbox: Wallbox, hass: HomeAssistant) -> None: ...
    def _authenticate(self) -> None: ...
    def _validate(self) -> None: ...
    async def async_validate_input(self) -> None: ...
    def _get_data(self) -> dict[str, Any]: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    def _set_charging_current(self, charging_current: float) -> None: ...
    async def async_set_charging_current(self, charging_current: float) -> None: ...
    def _set_lock_unlock(self, lock: bool) -> None: ...
    async def async_set_lock_unlock(self, lock: bool) -> None: ...
    def _pause_charger(self, pause: bool) -> None: ...
    async def async_pause_charger(self, pause: bool) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class InvalidAuth(HomeAssistantError): ...

class WallboxEntity(CoordinatorEntity[WallboxCoordinator]):
    @property
    def device_info(self) -> DeviceInfo: ...
