from .const import DEFAULT_PROGRAM_STRING as DEFAULT_PROGRAM_STRING, DOMAIN as DOMAIN, FILTER_INSTEON_TYPE as FILTER_INSTEON_TYPE, FILTER_NODE_DEF_ID as FILTER_NODE_DEF_ID, FILTER_STATES as FILTER_STATES, FILTER_UOM as FILTER_UOM, FILTER_ZWAVE_CAT as FILTER_ZWAVE_CAT, ISY994_NODES as ISY994_NODES, ISY994_PROGRAMS as ISY994_PROGRAMS, ISY994_VARIABLES as ISY994_VARIABLES, ISY_GROUP_PLATFORM as ISY_GROUP_PLATFORM, KEY_ACTIONS as KEY_ACTIONS, KEY_STATUS as KEY_STATUS, NODE_FILTERS as NODE_FILTERS, PLATFORMS as PLATFORMS, PROGRAM_PLATFORMS as PROGRAM_PLATFORMS, SENSOR_AUX as SENSOR_AUX, SUBNODE_CLIMATE_COOL as SUBNODE_CLIMATE_COOL, SUBNODE_CLIMATE_HEAT as SUBNODE_CLIMATE_HEAT, SUBNODE_EZIO2X4_SENSORS as SUBNODE_EZIO2X4_SENSORS, SUBNODE_FANLINC_LIGHT as SUBNODE_FANLINC_LIGHT, SUBNODE_IOLINC_RELAY as SUBNODE_IOLINC_RELAY, TYPE_CATEGORY_SENSOR_ACTUATORS as TYPE_CATEGORY_SENSOR_ACTUATORS, TYPE_EZIO2X4 as TYPE_EZIO2X4, UOM_DOUBLE_TEMP as UOM_DOUBLE_TEMP, UOM_ISYV4_DEGREES as UOM_ISYV4_DEGREES, _LOGGER as _LOGGER
from .entity import ISYEntity as ISYEntity
from _typeshed import Incomplete
from collections.abc import Sequence
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from pyisy.nodes import Group as Group, Node as Node, Nodes as Nodes
from pyisy.programs import Programs as Programs
from pyisy.variables import Variables as Variables

BINARY_SENSOR_UOMS: Incomplete
BINARY_SENSOR_ISY_STATES: Incomplete

def _check_for_node_def(hass_isy_data: dict, node: Union[Group, Node], single_platform: Union[Platform, None] = ...) -> bool: ...
def _check_for_insteon_type(hass_isy_data: dict, node: Union[Group, Node], single_platform: Union[Platform, None] = ...) -> bool: ...
def _check_for_zwave_cat(hass_isy_data: dict, node: Union[Group, Node], single_platform: Union[Platform, None] = ...) -> bool: ...
def _check_for_uom_id(hass_isy_data: dict, node: Union[Group, Node], single_platform: Union[Platform, None] = ..., uom_list: Union[list[str], None] = ...) -> bool: ...
def _check_for_states_in_uom(hass_isy_data: dict, node: Union[Group, Node], single_platform: Union[Platform, None] = ..., states_list: Union[list[str], None] = ...) -> bool: ...
def _is_sensor_a_binary_sensor(hass_isy_data: dict, node: Union[Group, Node]) -> bool: ...
def _categorize_nodes(hass_isy_data: dict, nodes: Nodes, ignore_identifier: str, sensor_identifier: str) -> None: ...
def _categorize_programs(hass_isy_data: dict, programs: Programs) -> None: ...
def _categorize_variables(hass_isy_data: dict, variables: Variables, identifier: str) -> None: ...
async def migrate_old_unique_ids(hass: HomeAssistant, platform: str, entities: Sequence[ISYEntity]) -> None: ...
def convert_isy_value_to_hass(value: Union[int, float, None], uom: Union[str, None], precision: Union[int, str], fallback_precision: Union[int, None] = ...) -> Union[float, int, None]: ...
