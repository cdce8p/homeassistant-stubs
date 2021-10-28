from async_upnp_client.const import DeviceOrServiceType as DeviceOrServiceType, SsdpHeaders as SsdpHeaders, SsdpSource
from async_upnp_client.ssdp_listener import SsdpDevice as SsdpDevice
from async_upnp_client.utils import CaseInsensitiveDict
from collections.abc import Awaitable
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_ssdp as async_get_ssdp, bind_hass as bind_hass
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Callable, Mapping

DOMAIN: str
SCAN_INTERVAL: Any
IPV4_BROADCAST: Any
ATTR_SSDP_LOCATION: str
ATTR_SSDP_ST: str
ATTR_SSDP_NT: str
ATTR_SSDP_UDN: str
ATTR_SSDP_USN: str
ATTR_SSDP_EXT: str
ATTR_SSDP_SERVER: str
ATTR_SSDP_BOOTID: str
ATTR_SSDP_NEXTBOOTID: str
ATTR_UPNP_DEVICE_TYPE: str
ATTR_UPNP_FRIENDLY_NAME: str
ATTR_UPNP_MANUFACTURER: str
ATTR_UPNP_MANUFACTURER_URL: str
ATTR_UPNP_MODEL_DESCRIPTION: str
ATTR_UPNP_MODEL_NAME: str
ATTR_UPNP_MODEL_NUMBER: str
ATTR_UPNP_MODEL_URL: str
ATTR_UPNP_SERIAL: str
ATTR_UPNP_SERVICE_LIST: str
ATTR_UPNP_UDN: str
ATTR_UPNP_UPC: str
ATTR_UPNP_PRESENTATION_URL: str
ATTR_HA_MATCHING_DOMAINS: str
PRIMARY_MATCH_KEYS: Any
DISCOVERY_MAPPING: Any
SsdpChange: Any
SsdpCallback = Callable[[Mapping[str, Any], SsdpChange], Awaitable]
SSDP_SOURCE_SSDP_CHANGE_MAPPING: Mapping[SsdpSource, SsdpChange]
_LOGGER: Any

async def async_register_callback(hass: HomeAssistant, callback: SsdpCallback, match_dict: Union[None, dict[str, str]] = ...) -> Callable[[], None]: ...
async def async_get_discovery_info_by_udn_st(hass: HomeAssistant, udn: str, st: str) -> Union[dict[str, str], None]: ...
async def async_get_discovery_info_by_st(hass: HomeAssistant, st: str) -> list[dict[str, str]]: ...
async def async_get_discovery_info_by_udn(hass: HomeAssistant, udn: str) -> list[dict[str, str]]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_process_callbacks(callbacks: list[SsdpCallback], discovery_info: dict[str, str], ssdp_change: SsdpChange) -> None: ...
def _async_headers_match(headers: Mapping[str, Any], match_dict: dict[str, str]) -> bool: ...

class IntegrationMatchers:
    _match_by_key: Any
    def __init__(self) -> None: ...
    def async_setup(self, integration_matchers: dict[str, list[dict[str, str]]]) -> None: ...
    def async_matching_domains(self, info_with_desc: CaseInsensitiveDict) -> set[str]: ...

class Scanner:
    hass: Any
    _cancel_scan: Any
    _ssdp_listeners: Any
    _callbacks: Any
    _description_cache: Any
    integration_matchers: Any
    def __init__(self, hass: HomeAssistant, integration_matchers: IntegrationMatchers) -> None: ...
    @property
    def _ssdp_devices(self) -> list[SsdpDevice]: ...
    @property
    def _all_headers_from_ssdp_devices(self) -> dict[tuple[str, str], Mapping[str, Any]]: ...
    async def async_register_callback(self, callback: SsdpCallback, match_dict: Union[None, dict[str, str]] = ...) -> Callable[[], None]: ...
    async def async_stop(self, *_: Any) -> None: ...
    async def _async_stop_ssdp_listeners(self) -> None: ...
    async def _async_build_source_set(self) -> set[Union[IPv4Address, IPv6Address]]: ...
    async def async_scan(self, *_: Any) -> None: ...
    async def async_scan_multicast(self, *_: Any) -> None: ...
    async def async_scan_broadcast(self, *_: Any) -> None: ...
    async def async_start(self) -> None: ...
    async def _async_start_ssdp_listeners(self) -> None: ...
    def _async_get_matching_callbacks(self, combined_headers: SsdpHeaders) -> list[SsdpCallback]: ...
    async def _ssdp_listener_callback(self, ssdp_device: SsdpDevice, dst: DeviceOrServiceType, source: SsdpSource) -> None: ...
    async def _async_get_description_dict(self, location: Union[str, None]) -> Mapping[str, str]: ...
    async def _async_headers_to_discovery_info(self, headers: Mapping[str, Any]) -> dict[str, Any]: ...
    async def async_get_discovery_info_by_udn_st(self, udn: str, st: str) -> Union[dict[str, Any], None]: ...
    async def async_get_discovery_info_by_st(self, st: str) -> list[dict[str, Any]]: ...
    async def async_get_discovery_info_by_udn(self, udn: str) -> list[dict[str, Any]]: ...

def discovery_info_from_headers_and_description(info_with_desc: CaseInsensitiveDict) -> dict[str, Any]: ...
def _udn_from_usn(usn: Union[str, None]) -> Union[str, None]: ...
