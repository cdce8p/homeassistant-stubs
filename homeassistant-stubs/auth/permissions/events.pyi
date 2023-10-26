from homeassistant.const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_LOVELACE_UPDATED as EVENT_LOVELACE_UPDATED, EVENT_PANELS_UPDATED as EVENT_PANELS_UPDATED, EVENT_RECORDER_5MIN_STATISTICS_GENERATED as EVENT_RECORDER_5MIN_STATISTICS_GENERATED, EVENT_RECORDER_HOURLY_STATISTICS_GENERATED as EVENT_RECORDER_HOURLY_STATISTICS_GENERATED, EVENT_SERVICE_REGISTERED as EVENT_SERVICE_REGISTERED, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED, EVENT_SHOPPING_LIST_UPDATED as EVENT_SHOPPING_LIST_UPDATED, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_THEMES_UPDATED as EVENT_THEMES_UPDATED
from homeassistant.helpers.area_registry import EVENT_AREA_REGISTRY_UPDATED as EVENT_AREA_REGISTRY_UPDATED
from homeassistant.helpers.device_registry import EVENT_DEVICE_REGISTRY_UPDATED as EVENT_DEVICE_REGISTRY_UPDATED
from homeassistant.helpers.entity_registry import EVENT_ENTITY_REGISTRY_UPDATED as EVENT_ENTITY_REGISTRY_UPDATED
from typing import Final

SUBSCRIBE_ALLOWLIST: Final[set[str]]