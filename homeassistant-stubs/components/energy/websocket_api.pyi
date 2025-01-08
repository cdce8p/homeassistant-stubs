import voluptuous as vol
from .const import DOMAIN as DOMAIN
from .data import DEVICE_CONSUMPTION_SCHEMA as DEVICE_CONSUMPTION_SCHEMA, ENERGY_SOURCE_SCHEMA as ENERGY_SOURCE_SCHEMA, EnergyManager as EnergyManager, EnergyPreferencesUpdate as EnergyPreferencesUpdate, async_get_manager as async_get_manager
from .types import EnergyPlatform as EnergyPlatform, GetSolarForecastType as GetSolarForecastType, SolarForecastType as SolarForecastType
from .validate import async_validate as async_validate
from collections.abc import Callable, Coroutine
from homeassistant.components import recorder as recorder, websocket_api as websocket_api
from homeassistant.components.recorder.statistics import StatisticsRow as StatisticsRow
from homeassistant.const import UnitOfEnergy as UnitOfEnergy
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from homeassistant.helpers.singleton import singleton as singleton
from typing import Any

type EnergyWebSocketCommandHandler = Callable[[HomeAssistant, websocket_api.ActiveConnection, dict[str, Any], EnergyManager], None]
type AsyncEnergyWebSocketCommandHandler = Callable[[HomeAssistant, websocket_api.ActiveConnection, dict[str, Any], EnergyManager], Coroutine[Any, Any, None]]
@callback
def async_setup(hass: HomeAssistant) -> None: ...
@singleton('energy_platforms')
async def async_get_energy_platforms(hass: HomeAssistant) -> dict[str, GetSolarForecastType]: ...
def _ws_with_manager(func: AsyncEnergyWebSocketCommandHandler | EnergyWebSocketCommandHandler) -> websocket_api.AsyncWebSocketCommandHandler: ...
@websocket_api.websocket_command({INCOMPLETE: 'energy/get_prefs'})
@websocket_api.async_response
@_ws_with_manager
@callback
def ws_get_prefs(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], manager: EnergyManager) -> None: ...
@websocket_api.require_admin
@websocket_api.websocket_command({INCOMPLETE: 'energy/save_prefs', INCOMPLETE: ENERGY_SOURCE_SCHEMA, INCOMPLETE: [DEVICE_CONSUMPTION_SCHEMA]})
@websocket_api.async_response
@_ws_with_manager
async def ws_save_prefs(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], manager: EnergyManager) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'energy/info'})
@websocket_api.async_response
async def ws_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'energy/validate'})
@websocket_api.async_response
async def ws_validate(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'energy/solar_forecast'})
@websocket_api.async_response
@_ws_with_manager
async def ws_solar_forecast(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], manager: EnergyManager) -> None: ...
@websocket_api.websocket_command({INCOMPLETE: 'energy/fossil_energy_consumption', INCOMPLETE: str, INCOMPLETE: str, INCOMPLETE: [str], INCOMPLETE: str, INCOMPLETE: vol.Any('5minute', 'hour', 'day', 'month')})
@websocket_api.async_response
async def ws_get_fossil_energy_consumption(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
