import dataclasses
import voluptuous as vol
from . import area_registry as area_registry, device_registry as device_registry, entity_registry as entity_registry, floor_registry as floor_registry, label_registry as label_registry, template as template, translation as translation
from .entity import Entity as Entity
from .group import expand_entity_ids as expand_entity_ids
from .selector import TargetSelector as TargetSelector
from .typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Iterable
from homeassistant.auth.permissions.const import CAT_ENTITIES as CAT_ENTITIES, POLICY_CONTROL as POLICY_CONTROL
from homeassistant.const import ATTR_AREA_ID as ATTR_AREA_ID, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_FLOOR_ID as ATTR_FLOOR_ID, ATTR_LABEL_ID as ATTR_LABEL_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_SERVICE as CONF_SERVICE, CONF_SERVICE_DATA as CONF_SERVICE_DATA, CONF_SERVICE_DATA_TEMPLATE as CONF_SERVICE_DATA_TEMPLATE, CONF_SERVICE_TEMPLATE as CONF_SERVICE_TEMPLATE, CONF_TARGET as CONF_TARGET, ENTITY_MATCH_ALL as ENTITY_MATCH_ALL, ENTITY_MATCH_NONE as ENTITY_MATCH_NONE
from homeassistant.core import Context as Context, EntityServiceResponse as EntityServiceResponse, HassJob as HassJob, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, TemplateError as TemplateError, Unauthorized as Unauthorized, UnknownUser as UnknownUser
from homeassistant.loader import Integration as Integration, async_get_integrations as async_get_integrations, bind_hass as bind_hass
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.yaml import load_yaml_dict as load_yaml_dict
from homeassistant.util.yaml.loader import JSON_TYPE as JSON_TYPE
from types import ModuleType
from typing import Any, TypeGuard, TypeVar, TypedDict

_EntityT = TypeVar('_EntityT', bound=Entity)
CONF_SERVICE_ENTITY_ID: str
_LOGGER: Incomplete
SERVICE_DESCRIPTION_CACHE: str
ALL_SERVICE_DESCRIPTIONS_CACHE: str

def _base_components() -> dict[str, ModuleType]: ...
def _validate_option_or_feature(option_or_feature: str, label: str) -> Any: ...
def validate_attribute_option(attribute_option: str) -> Any: ...
def validate_supported_feature(supported_feature: str) -> Any: ...

_FIELD_SCHEMA: Incomplete
_SERVICE_SCHEMA: Incomplete
_SERVICES_SCHEMA: Incomplete

class ServiceParams(TypedDict):
    domain: str
    service: str
    service_data: dict[str, Any]
    target: dict | None

class ServiceTargetSelector:
    __slots__: Incomplete
    entity_ids: Incomplete
    device_ids: Incomplete
    area_ids: Incomplete
    floor_ids: Incomplete
    label_ids: Incomplete
    def __init__(self, service_call: ServiceCall) -> None: ...
    @property
    def has_any_selector(self) -> bool: ...

@dataclasses.dataclass(slots=True)
class SelectedEntities:
    referenced: set[str] = ...
    indirectly_referenced: set[str] = ...
    missing_devices: set[str] = ...
    missing_areas: set[str] = ...
    missing_floors: set[str] = ...
    missing_labels: set[str] = ...
    referenced_devices: set[str] = ...
    referenced_areas: set[str] = ...
    def log_missing(self, missing_entities: set[str]) -> None: ...
    def __init__(self, referenced, indirectly_referenced, missing_devices, missing_areas, missing_floors, missing_labels, referenced_devices, referenced_areas) -> None: ...

def call_from_config(hass: HomeAssistant, config: ConfigType, blocking: bool = False, variables: TemplateVarsType = None, validate_config: bool = True) -> None: ...
async def async_call_from_config(hass: HomeAssistant, config: ConfigType, blocking: bool = False, variables: TemplateVarsType = None, validate_config: bool = True, context: Context | None = None) -> None: ...
def async_prepare_call_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType = None, validate_config: bool = False) -> ServiceParams: ...
def extract_entity_ids(hass: HomeAssistant, service_call: ServiceCall, expand_group: bool = True) -> set[str]: ...
async def async_extract_entities(hass: HomeAssistant, entities: Iterable[_EntityT], service_call: ServiceCall, expand_group: bool = True) -> list[_EntityT]: ...
async def async_extract_entity_ids(hass: HomeAssistant, service_call: ServiceCall, expand_group: bool = True) -> set[str]: ...
def _has_match(ids: str | list[str] | None) -> TypeGuard[str | list[str]]: ...
def async_extract_referenced_entity_ids(hass: HomeAssistant, service_call: ServiceCall, expand_group: bool = True) -> SelectedEntities: ...
async def async_extract_config_entry_ids(hass: HomeAssistant, service_call: ServiceCall, expand_group: bool = True) -> set[str]: ...
def _load_services_file(hass: HomeAssistant, integration: Integration) -> JSON_TYPE: ...
def _load_services_files(hass: HomeAssistant, integrations: Iterable[Integration]) -> list[JSON_TYPE]: ...
async def async_get_all_descriptions(hass: HomeAssistant) -> dict[str, dict[str, Any]]: ...
def remove_entity_service_fields(call: ServiceCall) -> dict[Any, Any]: ...
def async_set_service_schema(hass: HomeAssistant, domain: str, service: str, schema: dict[str, Any]) -> None: ...
def _get_permissible_entity_candidates(call: ServiceCall, entities: dict[str, Entity], entity_perms: None | Callable[[str, str], bool], target_all_entities: bool, all_referenced: set[str] | None) -> list[Entity]: ...
async def entity_service_call(hass: HomeAssistant, registered_entities: dict[str, Entity], func: str | HassJob, call: ServiceCall, required_features: Iterable[int] | None = None) -> EntityServiceResponse | None: ...
async def _handle_entity_call(hass: HomeAssistant, entity: Entity, func: str | HassJob, data: dict | ServiceCall, context: Context) -> ServiceResponse: ...
async def _async_admin_handler(hass: HomeAssistant, service_job: HassJob[[ServiceCall], Awaitable[None] | None], call: ServiceCall) -> None: ...
def async_register_admin_service(hass: HomeAssistant, domain: str, service: str, service_func: Callable[[ServiceCall], Awaitable[None] | None], schema: vol.Schema = ...) -> None: ...
def verify_domain_control(hass: HomeAssistant, domain: str) -> Callable[[Callable[[ServiceCall], Any]], Callable[[ServiceCall], Any]]: ...

class ReloadServiceHelper:
    _service_func: Incomplete
    _service_running: bool
    _service_condition: Incomplete
    def __init__(self, service_func: Callable[[ServiceCall], Awaitable]) -> None: ...
    async def execute_service(self, service_call: ServiceCall) -> None: ...
