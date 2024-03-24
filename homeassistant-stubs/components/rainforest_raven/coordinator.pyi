from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioraven.data import DeviceInfo as RAVEnDeviceInfo
from aioraven.serial import RAVEnSerialDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete

async def _get_meter_data(device: RAVEnSerialDevice, meter: bytes) -> dict[str, dict[str, Any]]: ...
async def _get_all_data(device: RAVEnSerialDevice, meter_macs: list[str]) -> dict[str, dict[str, Any]]: ...

class RAVEnDataCoordinator(DataUpdateCoordinator):
    _raven_device: RAVEnSerialDevice | None
    _device_info: RAVEnDeviceInfo | None
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    @property
    def device_fw_version(self) -> str | None: ...
    @property
    def device_hw_version(self) -> str | None: ...
    @property
    def device_mac_address(self) -> str | None: ...
    @property
    def device_manufacturer(self) -> str | None: ...
    @property
    def device_model(self) -> str | None: ...
    @property
    def device_name(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo | None: ...
    async def async_shutdown(self) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    async def _cleanup_device(self) -> None: ...
    async def _get_device(self) -> RAVEnSerialDevice: ...
