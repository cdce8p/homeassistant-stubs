from .const import CONF_RTSP_TRANSPORT as CONF_RTSP_TRANSPORT, CONF_USE_WALLCLOCK_AS_TIMESTAMPS as CONF_USE_WALLCLOCK_AS_TIMESTAMPS, FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, HLS_PROVIDER as HLS_PROVIDER, OUTPUT_FORMATS as OUTPUT_FORMATS, RTSP_TRANSPORTS as RTSP_TRANSPORTS, SOURCE_TIMEOUT as SOURCE_TIMEOUT
from .core import StreamOutput
from _typeshed import Incomplete
from collections.abc import Callable, Mapping
from homeassistant.core import HomeAssistant
from typing import Any

def create_stream(hass: HomeAssistant, stream_source: str, options: dict[str, Union[str, bool]], stream_label: Union[str, None] = ...) -> Stream: ...

class Stream:
    hass: Incomplete
    source: Incomplete
    options: Incomplete
    _stream_label: Incomplete
    keepalive: bool
    access_token: Incomplete
    _thread: Incomplete
    _thread_quit: Incomplete
    _outputs: Incomplete
    _fast_restart_once: bool
    _keyframe_converter: Incomplete
    _available: bool
    _update_callback: Incomplete
    _logger: Incomplete
    _diagnostics: Incomplete
    def __init__(self, hass: HomeAssistant, source: str, options: dict[str, str], stream_label: Union[str, None] = ...) -> None: ...
    def endpoint_url(self, fmt: str) -> str: ...
    def outputs(self) -> Mapping[str, StreamOutput]: ...
    def add_provider(self, fmt: str, timeout: int = ...) -> StreamOutput: ...
    def remove_provider(self, provider: StreamOutput) -> None: ...
    def check_idle(self) -> None: ...
    @property
    def available(self) -> bool: ...
    def set_update_callback(self, update_callback: Callable[[], None]) -> None: ...
    def _async_update_state(self, available: bool) -> None: ...
    def start(self) -> None: ...
    def update_source(self, new_source: str) -> None: ...
    def _run_worker(self) -> None: ...
    def stop(self) -> None: ...
    def _stop(self) -> None: ...
    async def async_record(self, video_path: str, duration: int = ..., lookback: int = ...) -> None: ...
    async def async_get_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    def get_diagnostics(self) -> dict[str, Any]: ...
