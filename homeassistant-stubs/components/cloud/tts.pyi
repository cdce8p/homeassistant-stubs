from .assist_pipeline import async_migrate_cloud_pipeline_engine as async_migrate_cloud_pipeline_engine
from .client import CloudClient as CloudClient
from .const import DATA_PLATFORMS_SETUP as DATA_PLATFORMS_SETUP, DOMAIN as DOMAIN, TTS_ENTITY_UNIQUE_ID as TTS_ENTITY_UNIQUE_ID
from .prefs import CloudPreferences as CloudPreferences
from _typeshed import Incomplete
from hass_nabucasa import Cloud as Cloud
from homeassistant.components.tts import ATTR_AUDIO_OUTPUT as ATTR_AUDIO_OUTPUT, ATTR_VOICE as ATTR_VOICE, CONF_LANG as CONF_LANG, Provider as Provider, TextToSpeechEntity as TextToSpeechEntity, TtsAudioType as TtsAudioType, Voice as Voice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

ATTR_GENDER: str
DEPRECATED_VOICES: Incomplete
SUPPORT_LANGUAGES: Incomplete
_LOGGER: Incomplete

def validate_lang(value: dict[str, Any]) -> dict[str, Any]: ...

PLATFORM_SCHEMA: Incomplete

async def async_get_engine(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> CloudProvider: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CloudTTSEntity(TextToSpeechEntity):
    _attr_name: str
    _attr_unique_id = TTS_ENTITY_UNIQUE_ID
    cloud: Incomplete
    def __init__(self, cloud: Cloud[CloudClient]) -> None: ...
    async def _sync_prefs(self, prefs: CloudPreferences) -> None: ...
    @property
    def default_language(self) -> str: ...
    @property
    def default_options(self) -> dict[str, Any]: ...
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def supported_options(self) -> list[str]: ...
    async def async_added_to_hass(self) -> None: ...
    def async_get_supported_voices(self, language: str) -> list[Voice] | None: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...

class CloudProvider(Provider):
    cloud: Incomplete
    name: str
    _language: Incomplete
    _gender: Incomplete
    def __init__(self, cloud: Cloud[CloudClient], language: str | None, gender: str | None) -> None: ...
    async def _sync_prefs(self, prefs: CloudPreferences) -> None: ...
    @property
    def default_language(self) -> str | None: ...
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def supported_options(self) -> list[str]: ...
    def async_get_supported_voices(self, language: str) -> list[Voice] | None: ...
    @property
    def default_options(self) -> dict[str, Any]: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...

def handle_deprecated_voice(hass: HomeAssistant, original_voice: str | None) -> str | None: ...
