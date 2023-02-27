from homeassistant.components.bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, async_discovered_service_info as async_discovered_service_info
from homeassistant.components.bluetooth.match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher, LOCAL_NAME as LOCAL_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def bluetooth_callback_matcher(local_name: str, address: str) -> BluetoothCallbackMatcher: ...
def async_find_existing_service_info(hass: HomeAssistant, local_name: str, address: str) -> Union[BluetoothServiceInfoBleak, None]: ...
def short_address(address: str) -> str: ...
def human_readable_name(name: Union[str, None], local_name: str, address: str) -> str: ...