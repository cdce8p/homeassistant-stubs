import yaml
from .const import SECRET_YAML as SECRET_YAML
from .objects import Input as Input, NodeListClass as NodeListClass, NodeStrClass as NodeStrClass
from collections import OrderedDict
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from pathlib import Path
from typing import Any, Dict, Iterator, List, TextIO, TypeVar, Union

JSON_TYPE = Union[List, Dict, str]
DICT_T = TypeVar('DICT_T', bound=Dict)
_LOGGER: Any

class Secrets:
    config_dir: Any = ...
    _cache: Any = ...
    def __init__(self, config_dir: Path) -> None: ...
    def get(self, requester_path: str, secret: str) -> str: ...
    def _load_secret_yaml(self, secret_dir: Path) -> dict[str, str]: ...

class SafeLineLoader(yaml.SafeLoader):
    secrets: Any = ...
    def __init__(self, stream: Any, secrets: Union[Secrets, None]=...) -> None: ...
    def compose_node(self, parent: yaml.nodes.Node, index: int) -> yaml.nodes.Node: ...

def load_yaml(fname: str, secrets: Union[Secrets, None]=...) -> JSON_TYPE: ...
def parse_yaml(content: Union[str, TextIO], secrets: Union[Secrets, None]=...) -> JSON_TYPE: ...
def _add_reference(obj: Union[list, NodeListClass], loader: SafeLineLoader, node: yaml.nodes.Node) -> NodeListClass: ...
def _include_yaml(loader: SafeLineLoader, node: yaml.nodes.Node) -> JSON_TYPE: ...
def _is_file_valid(name: str) -> bool: ...
def _find_files(directory: str, pattern: str) -> Iterator[str]: ...
def _include_dir_named_yaml(loader: SafeLineLoader, node: yaml.nodes.Node) -> OrderedDict: ...
def _include_dir_merge_named_yaml(loader: SafeLineLoader, node: yaml.nodes.Node) -> OrderedDict: ...
def _include_dir_list_yaml(loader: SafeLineLoader, node: yaml.nodes.Node) -> list[JSON_TYPE]: ...
def _include_dir_merge_list_yaml(loader: SafeLineLoader, node: yaml.nodes.Node) -> JSON_TYPE: ...
def _ordered_dict(loader: SafeLineLoader, node: yaml.nodes.MappingNode) -> OrderedDict: ...
def _construct_seq(loader: SafeLineLoader, node: yaml.nodes.Node) -> JSON_TYPE: ...
def _env_var_yaml(loader: SafeLineLoader, node: yaml.nodes.Node) -> str: ...
def secret_yaml(loader: SafeLineLoader, node: yaml.nodes.Node) -> JSON_TYPE: ...
