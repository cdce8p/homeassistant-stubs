from .const import AVAILABILITY_LATEST as AVAILABILITY_LATEST, AVAILABILITY_MODES as AVAILABILITY_MODES, CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_AVAILABILITY_MODE as CONF_AVAILABILITY_MODE, CONF_AVAILABILITY_TEMPLATE as CONF_AVAILABILITY_TEMPLATE, CONF_AVAILABILITY_TOPIC as CONF_AVAILABILITY_TOPIC, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_COMPONENTS as CONF_COMPONENTS, CONF_CONFIGURATION_URL as CONF_CONFIGURATION_URL, CONF_CONNECTIONS as CONF_CONNECTIONS, CONF_DEPRECATED_VIA_HUB as CONF_DEPRECATED_VIA_HUB, CONF_ENABLED_BY_DEFAULT as CONF_ENABLED_BY_DEFAULT, CONF_ENCODING as CONF_ENCODING, CONF_ENTITY_PICTURE as CONF_ENTITY_PICTURE, CONF_HW_VERSION as CONF_HW_VERSION, CONF_IDENTIFIERS as CONF_IDENTIFIERS, CONF_JSON_ATTRS_TEMPLATE as CONF_JSON_ATTRS_TEMPLATE, CONF_JSON_ATTRS_TOPIC as CONF_JSON_ATTRS_TOPIC, CONF_MANUFACTURER as CONF_MANUFACTURER, CONF_OBJECT_ID as CONF_OBJECT_ID, CONF_ORIGIN as CONF_ORIGIN, CONF_PAYLOAD_AVAILABLE as CONF_PAYLOAD_AVAILABLE, CONF_PAYLOAD_NOT_AVAILABLE as CONF_PAYLOAD_NOT_AVAILABLE, CONF_QOS as CONF_QOS, CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_SUGGESTED_AREA as CONF_SUGGESTED_AREA, CONF_SUPPORT_URL as CONF_SUPPORT_URL, CONF_SW_VERSION as CONF_SW_VERSION, CONF_TOPIC as CONF_TOPIC, CONF_VIA_DEVICE as CONF_VIA_DEVICE, DEFAULT_PAYLOAD_AVAILABLE as DEFAULT_PAYLOAD_AVAILABLE, DEFAULT_PAYLOAD_NOT_AVAILABLE as DEFAULT_PAYLOAD_NOT_AVAILABLE, ENTITY_PLATFORMS as ENTITY_PLATFORMS, SUPPORTED_COMPONENTS as SUPPORTED_COMPONENTS
from .util import valid_publish_topic as valid_publish_topic, valid_qos_schema as valid_qos_schema, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_ICON as CONF_ICON, CONF_MODEL as CONF_MODEL, CONF_MODEL_ID as CONF_MODEL_ID, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.helpers.entity import ENTITY_CATEGORIES_SCHEMA as ENTITY_CATEGORIES_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

SHARED_OPTIONS: Incomplete
MQTT_ORIGIN_INFO_SCHEMA: Incomplete
_MQTT_AVAILABILITY_SINGLE_SCHEMA: Incomplete
_MQTT_AVAILABILITY_LIST_SCHEMA: Incomplete
_MQTT_AVAILABILITY_SCHEMA: Incomplete

def validate_device_has_at_least_one_identifier(value: ConfigType) -> ConfigType: ...

MQTT_ENTITY_DEVICE_INFO_SCHEMA: Incomplete
MQTT_ENTITY_COMMON_SCHEMA: Incomplete
_UNIQUE_ID_SCHEMA: Incomplete

def check_unique_id(config: dict[str, Any]) -> dict[str, Any]: ...

_COMPONENT_CONFIG_SCHEMA: Incomplete
DEVICE_DISCOVERY_SCHEMA: Incomplete
