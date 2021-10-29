from . import BMWConnectedDriveAccount as BMWConnectedDriveAccount, BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import CONF_ACCOUNT as CONF_ACCOUNT, DATA_ENTRIES as DATA_ENTRIES
from bimmer_connected.state import VehicleState as VehicleState
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from bimmer_connected.vehicle_status import ConditionBasedServiceReport as ConditionBasedServiceReport
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_OPENING as DEVICE_CLASS_OPENING, DEVICE_CLASS_PLUG as DEVICE_CLASS_PLUG, DEVICE_CLASS_PROBLEM as DEVICE_CLASS_PROBLEM
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LENGTH_KILOMETERS as LENGTH_KILOMETERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.unit_system import UnitSystem as UnitSystem
from typing import Any

_LOGGER: Any

def _are_doors_closed(vehicle_state: VehicleState, extra_attributes: dict[str, Any], *args: Any) -> bool: ...
def _are_windows_closed(vehicle_state: VehicleState, extra_attributes: dict[str, Any], *args: Any) -> bool: ...
def _are_doors_locked(vehicle_state: VehicleState, extra_attributes: dict[str, Any], *args: Any) -> bool: ...
def _are_parking_lights_on(vehicle_state: VehicleState, extra_attributes: dict[str, Any], *args: Any) -> bool: ...
def _are_problems_detected(vehicle_state: VehicleState, extra_attributes: dict[str, Any], unit_system: UnitSystem) -> bool: ...
def _check_control_messages(vehicle_state: VehicleState, extra_attributes: dict[str, Any], *args: Any) -> bool: ...
def _is_vehicle_charging(vehicle_state: VehicleState, extra_attributes: dict[str, Any], *args: Any) -> bool: ...
def _is_vehicle_plugged_in(vehicle_state: VehicleState, extra_attributes: dict[str, Any], *args: Any) -> bool: ...
def _format_cbs_report(report: ConditionBasedServiceReport, unit_system: UnitSystem) -> dict[str, Any]: ...

class BMWRequiredKeysMixin:
    value_fn: Callable[[VehicleState, dict[str, Any], UnitSystem], bool]

class BMWBinarySensorEntityDescription(BinarySensorEntityDescription, BMWRequiredKeysMixin): ...

SENSOR_TYPES: tuple[BMWBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWConnectedDriveSensor(BMWConnectedDriveBaseEntity, BinarySensorEntity):
    entity_description: BMWBinarySensorEntityDescription
    _unit_system: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, account: BMWConnectedDriveAccount, vehicle: ConnectedDriveVehicle, description: BMWBinarySensorEntityDescription, unit_system: UnitSystem) -> None: ...
    _attr_is_on: Any
    _attr_extra_state_attributes: Any
    def update(self) -> None: ...