from . import AirzoneCloudConfigEntry as AirzoneCloudConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT_API: Incomplete
TO_REDACT_CONFIG: Incomplete
TO_REDACT_COORD: Incomplete

def gather_ids(api_data: dict[str, Any]) -> dict[str, Any]: ...
def redact_keys(data: Any, ids: dict[str, Any]) -> Any: ...
def redact_values(data: Any, ids: dict[str, Any]) -> Any: ...
def redact_all(data: dict[str, Any], ids: dict[str, Any], to_redact: list[str]) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: AirzoneCloudConfigEntry) -> dict[str, Any]: ...
