from .const import DOMAIN as DOMAIN, SERVICE_PRESS as SERVICE_PRESS
from datetime import datetime
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

SCAN_INTERVAL: Any
ENTITY_ID_FORMAT: Any
MIN_TIME_BETWEEN_SCANS: Any
_LOGGER: Any

class ButtonDeviceClass(StrEnum):
    RESTART: str
    UPDATE: str

DEVICE_CLASSES_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class ButtonEntityDescription(EntityDescription):
    device_class: Union[ButtonDeviceClass, None]

class ButtonEntity(RestoreEntity):
    entity_description: ButtonEntityDescription
    _attr_should_poll: bool
    _attr_device_class: Union[ButtonDeviceClass, None]
    _attr_state: None
    __last_pressed: Union[datetime, None]
    @property
    def device_class(self) -> Union[ButtonDeviceClass, None]: ...
    @property
    def state(self) -> Union[str, None]: ...
    async def _async_press_action(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def press(self) -> None: ...
    async def async_press(self) -> None: ...