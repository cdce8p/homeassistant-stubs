from .const import ATTR_EVENT_ID as ATTR_EVENT_ID, ATTR_EVENT_SCORE as ATTR_EVENT_SCORE, DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DEFAULT_BRAND as DEFAULT_BRAND, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .models import PermRequired as PermRequired, ProtectEventMixin as ProtectEventMixin, ProtectRequiredKeysMixin as ProtectRequiredKeysMixin
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Sequence
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED
from pyunifiprotect.data import Event as Event, ModelType, NVR as NVR, ProtectAdoptableDeviceModel, ProtectModelWithId as ProtectModelWithId
from typing import Any

_LOGGER: Incomplete

def _async_device_entities(data: ProtectData, klass: type[ProtectDeviceEntity], model_type: ModelType, descs: Sequence[ProtectRequiredKeysMixin], unadopted_descs: Sequence[ProtectRequiredKeysMixin], ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[ProtectDeviceEntity]: ...
def async_all_device_entities(data: ProtectData, klass: type[ProtectDeviceEntity], camera_descs: Sequence[ProtectRequiredKeysMixin] | None = None, light_descs: Sequence[ProtectRequiredKeysMixin] | None = None, sense_descs: Sequence[ProtectRequiredKeysMixin] | None = None, viewer_descs: Sequence[ProtectRequiredKeysMixin] | None = None, lock_descs: Sequence[ProtectRequiredKeysMixin] | None = None, chime_descs: Sequence[ProtectRequiredKeysMixin] | None = None, all_descs: Sequence[ProtectRequiredKeysMixin] | None = None, unadopted_descs: Sequence[ProtectRequiredKeysMixin] | None = None, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[ProtectDeviceEntity]: ...

class ProtectDeviceEntity(Entity):
    device: ProtectAdoptableDeviceModel
    _attr_should_poll: bool
    data: Incomplete
    _async_get_ufp_enabled: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    _attr_attribution: Incomplete
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel, description: EntityDescription | None = None) -> None: ...
    async def async_update(self) -> None: ...
    _attr_device_info: Incomplete
    def _async_set_device_info(self) -> None: ...
    _attr_available: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    def _async_get_state_attrs(self) -> tuple[Any, ...]: ...
    def _async_updated_event(self, device: ProtectAdoptableDeviceModel | NVR) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class ProtectNVREntity(ProtectDeviceEntity):
    device: NVR
    def __init__(self, entry: ProtectData, device: NVR, description: EntityDescription | None = None) -> None: ...
    _attr_device_info: Incomplete
    def _async_set_device_info(self) -> None: ...
    _attr_available: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...

class EventEntityMixin(ProtectDeviceEntity):
    _unrecorded_attributes: Incomplete
    entity_description: ProtectEventMixin
    _event: Incomplete
    def __init__(self, *args: Any, **kwarg: Any) -> None: ...
    _attr_extra_state_attributes: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
