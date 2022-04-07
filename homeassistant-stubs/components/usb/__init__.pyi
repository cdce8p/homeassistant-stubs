from .const import DOMAIN as DOMAIN
from .models import USBDevice as USBDevice
from .utils import usb_device_from_port as usb_device_from_port
from homeassistant import config_entries as config_entries
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api.connection import ActiveConnection as ActiveConnection
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from homeassistant.helpers import discovery_flow as discovery_flow, system_info as system_info
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.frame import report as report
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_usb as async_get_usb
from pyudev import Device as Device
from serial.tools.list_ports_common import ListPortInfo as ListPortInfo
from typing import Any

_LOGGER: Any
REQUEST_SCAN_COOLDOWN: int

class UsbServiceInfo(BaseServiceInfo):
    device: str
    vid: str
    pid: str
    serial_number: Union[str, None]
    manufacturer: Union[str, None]
    description: Union[str, None]
    def __getitem__(self, name: str) -> Any: ...
    def __init__(self, device, vid, pid, serial_number, manufacturer, description) -> None: ...

def human_readable_device_name(device: str, serial_number: Union[str, None], manufacturer: Union[str, None], description: Union[str, None], vid: Union[str, None], pid: Union[str, None]) -> str: ...
def get_serial_by_id(dev_path: str) -> str: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _fnmatch_lower(name: Union[str, None], pattern: str) -> bool: ...

class USBDiscovery:
    hass: Any
    usb: Any
    seen: Any
    observer_active: bool
    _request_debouncer: Any
    def __init__(self, hass: HomeAssistant, usb: list[dict[str, str]]) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_start(self, event: Event) -> None: ...
    async def _async_start_monitor(self) -> None: ...
    def _device_discovered(self, device: Device) -> None: ...
    def _async_process_discovered_usb_device(self, device: USBDevice) -> None: ...
    def _async_process_ports(self, ports: list[ListPortInfo]) -> None: ...
    def scan_serial(self) -> None: ...
    async def _async_scan_serial(self) -> None: ...
    async def async_request_scan_serial(self) -> None: ...

async def websocket_usb_scan(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...