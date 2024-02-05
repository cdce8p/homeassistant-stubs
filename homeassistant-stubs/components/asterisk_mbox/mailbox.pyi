from . import AsteriskData as AsteriskData
from _typeshed import Incomplete
from homeassistant.components.mailbox import CONTENT_TYPE_MPEG as CONTENT_TYPE_MPEG, Mailbox as Mailbox, StreamError as StreamError
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
SIGNAL_MESSAGE_REQUEST: str
SIGNAL_MESSAGE_UPDATE: str

async def async_get_handler(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> Mailbox: ...

class AsteriskMailbox(Mailbox):
    def __init__(self, hass: HomeAssistant, name: str) -> None: ...
    def _update_callback(self, msg: str) -> None: ...
    @property
    def media_type(self) -> str: ...
    @property
    def can_delete(self) -> bool: ...
    @property
    def has_media(self) -> bool: ...
    async def async_get_media(self, msgid: str) -> bytes: ...
    async def async_get_messages(self) -> list[dict[str, Any]]: ...
    async def async_delete(self, msgid: str) -> bool: ...
