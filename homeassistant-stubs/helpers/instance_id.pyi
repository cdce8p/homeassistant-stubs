from . import singleton as singleton, storage as storage
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant

DATA_KEY: str
DATA_VERSION: int
LEGACY_UUID_FILE: str
_LOGGER: Incomplete

@singleton.singleton(DATA_KEY)
async def async_get(hass: HomeAssistant) -> str: ...
