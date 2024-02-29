from .const import DOMAIN as DOMAIN
from .coordinator import ImapDataUpdateCoordinator as ImapDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

REDACT_CONFIG: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
def _async_get_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...