from ..helpers.frame import MissingIntegrationFrame as MissingIntegrationFrame, get_integration_frame as get_integration_frame
from typing import Any, Callable

def deprecated_substitute(substitute_name: str) -> Callable[..., Callable]: ...
def get_deprecated(config: dict[str, Any], new_name: str, old_name: str, default: Union[Any, None]=...) -> Union[Any, None]: ...
def deprecated_function(replacement: str) -> Callable[..., Callable]: ...