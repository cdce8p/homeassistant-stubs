from .const import DOMAIN as DOMAIN
from .project import KNXProject as KNXProject
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.signal_type import SignalType as SignalType
from typing import Final, TypedDict
from xknx import XKNX as XKNX
from xknx.dpt import DPTArray as DPTArray, DPTBase as DPTBase, DPTBinary as DPTBinary
from xknx.telegram import Telegram as Telegram

STORAGE_VERSION: Final[int]
STORAGE_KEY: Final[Incomplete]
SIGNAL_KNX_TELEGRAM: SignalType[Telegram, TelegramDict]

class DecodedTelegramPayload(TypedDict):
    dpt_main: int | None
    dpt_sub: int | None
    dpt_name: str | None
    unit: str | None
    value: str | int | float | bool | None

class TelegramDict(DecodedTelegramPayload):
    destination: str
    destination_name: str
    direction: str
    payload: int | tuple[int, ...] | None
    source: str
    source_name: str
    telegramtype: str
    timestamp: str

class Telegrams:
    hass: Incomplete
    project: Incomplete
    _history_store: Incomplete
    _jobs: Incomplete
    _xknx_telegram_cb_handle: Incomplete
    recent_telegrams: Incomplete
    def __init__(self, hass: HomeAssistant, xknx: XKNX, project: KNXProject, log_size: int) -> None: ...
    async def load_history(self) -> None: ...
    async def save_history(self) -> None: ...
    async def _xknx_telegram_cb(self, telegram: Telegram) -> None: ...
    def async_listen_telegram(self, action: Callable[[TelegramDict], None], name: str = 'KNX telegram listener') -> CALLBACK_TYPE: ...
    def telegram_to_dict(self, telegram: Telegram) -> TelegramDict: ...

def decode_telegram_payload(payload: DPTArray | DPTBinary, transcoder: type[DPTBase]) -> DecodedTelegramPayload: ...
