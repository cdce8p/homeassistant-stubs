from . import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime, timedelta
from homeassistant.components.recorder import get_instance as get_instance, history as history
from homeassistant.components.sensor import DEVICE_CLASS_STATE_CLASSES as DEVICE_CLASS_STATE_CLASSES, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, PERCENTAGE as PERCENTAGE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.start import async_at_start as async_at_start
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any

_LOGGER: Incomplete
STAT_AGE_COVERAGE_RATIO: str
STAT_BUFFER_USAGE_RATIO: str
STAT_SOURCE_VALUE_VALID: str
STAT_AVERAGE_LINEAR: str
STAT_AVERAGE_STEP: str
STAT_AVERAGE_TIMELESS: str
STAT_CHANGE: str
STAT_CHANGE_SAMPLE: str
STAT_CHANGE_SECOND: str
STAT_COUNT: str
STAT_COUNT_BINARY_ON: str
STAT_COUNT_BINARY_OFF: str
STAT_DATETIME_NEWEST: str
STAT_DATETIME_OLDEST: str
STAT_DATETIME_VALUE_MAX: str
STAT_DATETIME_VALUE_MIN: str
STAT_DISTANCE_95P: str
STAT_DISTANCE_99P: str
STAT_DISTANCE_ABSOLUTE: str
STAT_MEAN: str
STAT_MEAN_CIRCULAR: str
STAT_MEDIAN: str
STAT_NOISINESS: str
STAT_PERCENTILE: str
STAT_STANDARD_DEVIATION: str
STAT_SUM: str
STAT_SUM_DIFFERENCES: str
STAT_SUM_DIFFERENCES_NONNEGATIVE: str
STAT_TOTAL: str
STAT_VALUE_MAX: str
STAT_VALUE_MIN: str
STAT_VARIANCE: str
STATS_NUMERIC_SUPPORT: Incomplete
STATS_BINARY_SUPPORT: Incomplete
STATS_NOT_A_NUMBER: Incomplete
STATS_DATETIME: Incomplete
STATS_NUMERIC_RETAIN_UNIT: Incomplete
STATS_BINARY_PERCENTAGE: Incomplete
CONF_STATE_CHARACTERISTIC: str
CONF_SAMPLES_MAX_BUFFER_SIZE: str
CONF_MAX_AGE: str
CONF_KEEP_LAST_SAMPLE: str
CONF_PRECISION: str
CONF_PERCENTILE: str
DEFAULT_NAME: str
DEFAULT_PRECISION: int
ICON: str

def valid_state_characteristic_configuration(config: dict[str, Any]) -> dict[str, Any]: ...
def valid_boundary_configuration(config: dict[str, Any]) -> dict[str, Any]: ...
def valid_keep_last_sample(config: dict[str, Any]) -> dict[str, Any]: ...

_PLATFORM_SCHEMA_BASE: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class StatisticsSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_icon = ICON
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _source_entity_id: Incomplete
    is_binary: Incomplete
    _state_characteristic: Incomplete
    _samples_max_buffer_size: Incomplete
    _samples_max_age: Incomplete
    samples_keep_last: Incomplete
    _precision: Incomplete
    _percentile: Incomplete
    _value: Incomplete
    _unit_of_measurement: Incomplete
    _available: bool
    states: Incomplete
    ages: Incomplete
    attributes: Incomplete
    _state_characteristic_fn: Incomplete
    _update_listener: Incomplete
    def __init__(self, source_entity_id: str, name: str, unique_id: str | None, state_characteristic: str, samples_max_buffer_size: int | None, samples_max_age: timedelta | None, samples_keep_last: bool, precision: int, percentile: int) -> None: ...
    def _async_stats_sensor_state_listener(self, event: Event[EventStateChangedData]) -> None: ...
    def _async_stats_sensor_startup(self, _: HomeAssistant) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _add_state_to_queue(self, new_state: State) -> None: ...
    def _derive_unit_of_measurement(self, new_state: State) -> str | None: ...
    @property
    def device_class(self) -> SensorDeviceClass | None: ...
    @property
    def state_class(self) -> SensorStateClass | None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, StateType] | None: ...
    def _purge_old_states(self, max_age: timedelta) -> None: ...
    def _async_next_to_purge_timestamp(self) -> datetime | None: ...
    async def async_update(self) -> None: ...
    def _async_purge_update_and_schedule(self) -> None: ...
    def _async_cancel_update_listener(self) -> None: ...
    def _async_scheduled_update(self, now: datetime) -> None: ...
    def _fetch_states_from_database(self) -> list[State]: ...
    async def _initialize_from_database(self) -> None: ...
    def _update_attributes(self) -> None: ...
    def _update_value(self) -> None: ...
    def _callable_characteristic_fn(self, characteristic: str) -> Callable[[], StateType | datetime]: ...
    def _stat_average_linear(self) -> StateType: ...
    def _stat_average_step(self) -> StateType: ...
    def _stat_average_timeless(self) -> StateType: ...
    def _stat_change(self) -> StateType: ...
    def _stat_change_sample(self) -> StateType: ...
    def _stat_change_second(self) -> StateType: ...
    def _stat_count(self) -> StateType: ...
    def _stat_datetime_newest(self) -> datetime | None: ...
    def _stat_datetime_oldest(self) -> datetime | None: ...
    def _stat_datetime_value_max(self) -> datetime | None: ...
    def _stat_datetime_value_min(self) -> datetime | None: ...
    def _stat_distance_95_percent_of_values(self) -> StateType: ...
    def _stat_distance_99_percent_of_values(self) -> StateType: ...
    def _stat_distance_absolute(self) -> StateType: ...
    def _stat_mean(self) -> StateType: ...
    def _stat_mean_circular(self) -> StateType: ...
    def _stat_median(self) -> StateType: ...
    def _stat_noisiness(self) -> StateType: ...
    def _stat_percentile(self) -> StateType: ...
    def _stat_standard_deviation(self) -> StateType: ...
    def _stat_sum(self) -> StateType: ...
    def _stat_sum_differences(self) -> StateType: ...
    def _stat_sum_differences_nonnegative(self) -> StateType: ...
    def _stat_total(self) -> StateType: ...
    def _stat_value_max(self) -> StateType: ...
    def _stat_value_min(self) -> StateType: ...
    def _stat_variance(self) -> StateType: ...
    def _stat_binary_average_step(self) -> StateType: ...
    def _stat_binary_average_timeless(self) -> StateType: ...
    def _stat_binary_count(self) -> StateType: ...
    def _stat_binary_count_on(self) -> StateType: ...
    def _stat_binary_count_off(self) -> StateType: ...
    def _stat_binary_datetime_newest(self) -> datetime | None: ...
    def _stat_binary_datetime_oldest(self) -> datetime | None: ...
    def _stat_binary_mean(self) -> StateType: ...
