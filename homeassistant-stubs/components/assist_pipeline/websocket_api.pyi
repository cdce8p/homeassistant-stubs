import voluptuous as vol
from .const import DEFAULT_PIPELINE_TIMEOUT as DEFAULT_PIPELINE_TIMEOUT, DEFAULT_WAKE_WORD_TIMEOUT as DEFAULT_WAKE_WORD_TIMEOUT, DOMAIN as DOMAIN, EVENT_RECORDING as EVENT_RECORDING, SAMPLE_CHANNELS as SAMPLE_CHANNELS, SAMPLE_RATE as SAMPLE_RATE, SAMPLE_WIDTH as SAMPLE_WIDTH
from .error import PipelineNotFound as PipelineNotFound
from .pipeline import AudioSettings as AudioSettings, DeviceAudioQueue as DeviceAudioQueue, PipelineData as PipelineData, PipelineError as PipelineError, PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, PipelineInput as PipelineInput, PipelineRun as PipelineRun, PipelineStage as PipelineStage, WakeWordSettings as WakeWordSettings, async_get_pipeline as async_get_pipeline
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import conversation as conversation, stt as stt, tts as tts, websocket_api as websocket_api
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_SECONDS as ATTR_SECONDS, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import config_validation as cv
from typing import Any, Final

_LOGGER: Incomplete
CAPTURE_RATE: Final[int]
CAPTURE_WIDTH: Final[int]
CAPTURE_CHANNELS: Final[int]
MAX_CAPTURE_TIMEOUT: Final[float]

@callback
def async_register_websocket_api(hass: HomeAssistant) -> None: ...
@websocket_api.websocket_command(vol.All(websocket_api.BASE_COMMAND_MESSAGE_SCHEMA.extend({INCOMPLETE: 'assist_pipeline/run', INCOMPLETE: Incomplete, INCOMPLETE: Incomplete, INCOMPLETE: dict, INCOMPLETE: str, INCOMPLETE: vol.Any(str, None), INCOMPLETE: vol.Any(str, None), INCOMPLETE: vol.Any(float, int)}), cv.key_value_schemas('start_stage', {INCOMPLETE: vol.Schema({INCOMPLETE: {INCOMPLETE: int, INCOMPLETE: vol.Any(float, int), INCOMPLETE: vol.Any(float, int), INCOMPLETE: int, INCOMPLETE: int, INCOMPLETE: float, INCOMPLETE: bool}}, extra=vol.ALLOW_EXTRA), INCOMPLETE: vol.Schema({INCOMPLETE: {INCOMPLETE: int, INCOMPLETE: str}}, extra=vol.ALLOW_EXTRA), INCOMPLETE: vol.Schema({INCOMPLETE: {'text': str}}, extra=vol.ALLOW_EXTRA), INCOMPLETE: vol.Schema({INCOMPLETE: {'text': str}}, extra=vol.ALLOW_EXTRA)})))
@websocket_api.async_response
async def websocket_run(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
@websocket_api.websocket_command({INCOMPLETE: 'assist_pipeline/pipeline_debug/list', INCOMPLETE: str})
def websocket_list_runs(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
@websocket_api.websocket_command({INCOMPLETE: 'assist_pipeline/device/list'})
def websocket_list_devices(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
@websocket_api.websocket_command({INCOMPLETE: 'assist_pipeline/pipeline_debug/get', INCOMPLETE: str, INCOMPLETE: str})
def websocket_get_run(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'assist_pipeline/language/list'})
@callback
def websocket_list_languages(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.websocket_command({INCOMPLETE: 'assist_pipeline/device/capture', INCOMPLETE: str, INCOMPLETE: vol.All(vol.Coerce(float), vol.Range(min=0, min_included=False, max=MAX_CAPTURE_TIMEOUT))})
@websocket_api.async_response
async def websocket_device_capture(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
