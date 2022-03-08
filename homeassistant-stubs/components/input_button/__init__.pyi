import voluptuous as vol
from homeassistant.components.button import ButtonEntity as ButtonEntity, SERVICE_PRESS as SERVICE_PRESS
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import collection as collection
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

DOMAIN: str
_LOGGER: Any
CREATE_FIELDS: Any
UPDATE_FIELDS: Any
CONFIG_SCHEMA: Any
RELOAD_SERVICE_SCHEMA: Any
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int

class InputButtonStorageCollection(collection.StorageCollection):
    CREATE_SCHEMA: Any
    UPDATE_SCHEMA: Any
    async def _process_create_data(self, data: dict) -> vol.Schema: ...
    def _get_suggested_id(self, info: dict) -> str: ...
    async def _update_data(self, data: dict, update_data: dict) -> dict: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class InputButton(ButtonEntity, RestoreEntity):
    _attr_should_poll: bool
    _config: Any
    editable: bool
    _attr_unique_id: Any
    def __init__(self, config: ConfigType) -> None: ...
    @classmethod
    def from_yaml(cls, config: ConfigType) -> ButtonEntity: ...
    @property
    def name(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
    async def async_press(self) -> None: ...
    async def async_update_config(self, config: ConfigType) -> None: ...