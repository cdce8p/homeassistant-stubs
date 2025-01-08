from .registry import BaseRegistryItems as BaseRegistryItems
from dataclasses import dataclass, field
from datetime import datetime
from functools import lru_cache
from homeassistant.util import dt as dt_util, slugify as slugify

@dataclass(slots=True, frozen=True, kw_only=True)
class NormalizedNameBaseRegistryEntry:
    name: str
    normalized_name: str = field(init=False)
    created_at: datetime = field(default_factory=dt_util.utcnow)
    modified_at: datetime = field(default_factory=dt_util.utcnow)
    def __post_init__(self) -> None: ...

@lru_cache(maxsize=1024)
def normalize_name(name: str) -> str: ...

class NormalizedNameBaseRegistryItems[_VT: NormalizedNameBaseRegistryEntry](BaseRegistryItems[_VT]):
    _normalized_names: dict[str, _VT]
    def __init__(self) -> None: ...
    def _unindex_entry(self, key: str, replacement_entry: _VT | None = None) -> None: ...
    def _index_entry(self, key: str, entry: _VT) -> None: ...
    def get_by_name(self, name: str) -> _VT | None: ...
    def generate_id_from_name(self, name: str) -> str: ...
