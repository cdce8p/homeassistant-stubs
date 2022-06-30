from .const import CONF_ALL_UPDATES as CONF_ALL_UPDATES, CONF_OVERRIDE_CHOST as CONF_OVERRIDE_CHOST, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEVICES_FOR_SUBSCRIBE as DEVICES_FOR_SUBSCRIBE, DEVICES_THAT_ADOPT as DEVICES_THAT_ADOPT, DOMAIN as DOMAIN, MIN_REQUIRED_PROTECT_V as MIN_REQUIRED_PROTECT_V, OUTDATED_LOG_MESSAGE as OUTDATED_LOG_MESSAGE, PLATFORMS as PLATFORMS
from .data import ProtectData as ProtectData, async_ufp_instance_for_config_entry_ids as async_ufp_instance_for_config_entry_ids
from .discovery import async_start_discovery as async_start_discovery
from .migrate import async_migrate_data as async_migrate_data
from .services import async_cleanup_services as async_cleanup_services, async_setup_services as async_setup_services
from .utils import _async_unifi_mac_from_hass as _async_unifi_mac_from_hass, async_get_devices as async_get_devices
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_options_updated(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
