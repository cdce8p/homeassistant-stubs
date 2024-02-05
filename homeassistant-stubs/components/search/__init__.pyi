from _typeshed import Incomplete
from homeassistant.components import automation as automation, group as group, person as person, script as script, websocket_api as websocket_api
from homeassistant.components.homeassistant import scene as scene
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers import device_registry as dr, entity_registry as er
from homeassistant.helpers.entity import EntityInfo as EntityInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

DOMAIN: str
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def websocket_search_related(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

class Searcher:
    DONT_RESOLVE: Incomplete
    EXIST_AS_ENTITY: Incomplete
    hass: Incomplete
    _device_reg: Incomplete
    _entity_reg: Incomplete
    _sources: Incomplete
    results: Incomplete
    _to_resolve: Incomplete
    def __init__(self, hass: HomeAssistant, device_reg: dr.DeviceRegistry, entity_reg: er.EntityRegistry, entity_sources: dict[str, EntityInfo]) -> None: ...
    def async_search(self, item_type: str, item_id: str) -> dict[str, set[str]]: ...
    def _add_or_resolve(self, item_type: str, item_id: str) -> None: ...
    def _resolve_area(self, area_id: str) -> None: ...
    def _resolve_automation(self, automation_entity_id: str) -> None: ...
    def _resolve_automation_blueprint(self, blueprint_path: str) -> None: ...
    def _resolve_config_entry(self, config_entry_id: str) -> None: ...
    def _resolve_device(self, device_id: str) -> None: ...
    def _resolve_entity(self, entity_id: str) -> None: ...
    def _resolve_group(self, group_entity_id: str) -> None: ...
    def _resolve_person(self, person_entity_id: str) -> None: ...
    def _resolve_scene(self, scene_entity_id: str) -> None: ...
    def _resolve_script(self, script_entity_id: str) -> None: ...
    def _resolve_script_blueprint(self, blueprint_path: str) -> None: ...