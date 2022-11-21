from _typeshed import Incomplete
from aiohttp import StreamReader as StreamReader
from homeassistant.components.stt import AudioBitRates as AudioBitRates, AudioChannels as AudioChannels, AudioCodecs as AudioCodecs, AudioFormats as AudioFormats, AudioSampleRates as AudioSampleRates, Provider as Provider, SpeechMetadata as SpeechMetadata, SpeechResult as SpeechResult, SpeechResultState as SpeechResultState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

SUPPORT_LANGUAGES: Incomplete

async def async_get_engine(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Provider: ...

class DemoProvider(Provider):
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def supported_formats(self) -> list[AudioFormats]: ...
    @property
    def supported_codecs(self) -> list[AudioCodecs]: ...
    @property
    def supported_bit_rates(self) -> list[AudioBitRates]: ...
    @property
    def supported_sample_rates(self) -> list[AudioSampleRates]: ...
    @property
    def supported_channels(self) -> list[AudioChannels]: ...
    async def async_process_audio_stream(self, metadata: SpeechMetadata, stream: StreamReader) -> SpeechResult: ...