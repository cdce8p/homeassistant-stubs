from .const import DOMAIN as DOMAIN
from datetime import time
from homeassistant.helpers.entity import Entity, EntityDescription

__all__ = ['DOMAIN', 'TimeEntity', 'TimeEntityDescription']

class TimeEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...
    def __replace__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

class TimeEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: TimeEntityDescription
    _attr_native_value: time | None
    _attr_device_class: None
    _attr_state: None
    def device_class(self) -> None: ...
    def state_attributes(self) -> None: ...
    @property
    def state(self) -> str | None: ...
    def native_value(self) -> time | None: ...
    def set_value(self, value: time) -> None: ...
    async def async_set_value(self, value: time) -> None: ...
