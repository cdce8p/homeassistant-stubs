from .const import DOMAIN as DOMAIN
from .coordinator import TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class TechnoVEEntity(CoordinatorEntity[TechnoVEDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TechnoVEDataUpdateCoordinator, key: str) -> None: ...
