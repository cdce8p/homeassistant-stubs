import aiopulse
from .const import ACMEDA_ENTITY_REMOVE as ACMEDA_ENTITY_REMOVE, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers import device_registry as dr, entity as entity
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect

class AcmedaBase(entity.Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    roller: Incomplete
    def __init__(self, roller: aiopulse.Roller) -> None: ...
    async def async_remove_and_unregister(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def notify_update(self) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_id(self) -> str: ...
    @property
    def device_info(self) -> dr.DeviceInfo: ...
