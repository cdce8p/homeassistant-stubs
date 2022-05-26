from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import Integration as Integration, MAX_LOAD_CONCURRENTLY as MAX_LOAD_CONCURRENTLY, async_get_config_flows as async_get_config_flows, async_get_integration as async_get_integration, bind_hass as bind_hass
from homeassistant.util.async_ import gather_with_concurrency as gather_with_concurrency
from homeassistant.util.json import load_json as load_json
from typing import Any

_LOGGER: Incomplete
TRANSLATION_LOAD_LOCK: str
TRANSLATION_FLATTEN_CACHE: str
LOCALE_EN: str

def recursive_flatten(prefix: Any, data: dict[str, Any]) -> dict[str, Any]: ...
def component_translation_path(component: str, language: str, integration: Integration) -> Union[str, None]: ...
def load_translations_files(translation_files: dict[str, str]) -> dict[str, dict[str, Any]]: ...
def _merge_resources(translation_strings: dict[str, dict[str, Any]], components: set[str], category: str) -> dict[str, dict[str, Any]]: ...
def _build_resources(translation_strings: dict[str, dict[str, Any]], components: set[str], category: str) -> dict[str, Union[dict[str, Any], str]]: ...
async def async_get_component_strings(hass: HomeAssistant, language: str, components: set[str]) -> dict[str, Any]: ...

class _TranslationCache:
    hass: Incomplete
    loaded: Incomplete
    cache: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_fetch(self, language: str, category: str, components: set[str]) -> list[dict[str, dict[str, Any]]]: ...
    async def _async_load(self, language: str, components: set[str]) -> None: ...
    def _build_category_cache(self, language: str, components: set[str], translation_strings: dict[str, dict[str, Any]]) -> None: ...

async def async_get_translations(hass: HomeAssistant, language: str, category: str, integrations: Union[Iterable[str], None] = ..., config_flow: Union[bool, None] = ...) -> dict[str, Any]: ...
