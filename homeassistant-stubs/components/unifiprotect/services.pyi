from .const import ATTR_MESSAGE as ATTR_MESSAGE, DOMAIN as DOMAIN
from .data import async_ufp_instance_for_config_entry_ids as async_ufp_instance_for_config_entry_ids
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_NAME as ATTR_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_extract_referenced_entity_ids as async_extract_referenced_entity_ids
from homeassistant.util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from pyunifiprotect.api import ProtectApiClient as ProtectApiClient
from pyunifiprotect.data import Camera
from typing import Any

SERVICE_ADD_DOORBELL_TEXT: str
SERVICE_REMOVE_DOORBELL_TEXT: str
SERVICE_SET_PRIVACY_ZONE: str
SERVICE_REMOVE_PRIVACY_ZONE: str
SERVICE_SET_DEFAULT_DOORBELL_TEXT: str
SERVICE_SET_CHIME_PAIRED: str
ALL_GLOBAL_SERIVCES: Incomplete
DOORBELL_TEXT_SCHEMA: Incomplete
CHIME_PAIRED_SCHEMA: Incomplete
REMOVE_PRIVACY_ZONE_SCHEMA: Incomplete

def _async_get_ufp_instance(hass: HomeAssistant, device_id: str) -> ProtectApiClient: ...
def _async_get_ufp_camera(hass: HomeAssistant, call: ServiceCall) -> Camera: ...
def _async_get_protect_from_call(hass: HomeAssistant, call: ServiceCall) -> set[ProtectApiClient]: ...
async def _async_service_call_nvr(hass: HomeAssistant, call: ServiceCall, method: str, *args: Any, **kwargs: Any) -> None: ...
async def add_doorbell_text(hass: HomeAssistant, call: ServiceCall) -> None: ...
async def remove_doorbell_text(hass: HomeAssistant, call: ServiceCall) -> None: ...
async def set_default_doorbell_text(hass: HomeAssistant, call: ServiceCall) -> None: ...
async def remove_privacy_zone(hass: HomeAssistant, call: ServiceCall) -> None: ...
def _async_unique_id_to_mac(unique_id: str) -> str: ...
async def set_chime_paired_doorbells(hass: HomeAssistant, call: ServiceCall) -> None: ...
def async_setup_services(hass: HomeAssistant) -> None: ...
def async_cleanup_services(hass: HomeAssistant) -> None: ...
