from _typeshed import Incomplete
from functools import lru_cache
from homeassistant.util.ulid import bytes_to_ulid as bytes_to_ulid, bytes_to_ulid_or_none as bytes_to_ulid_or_none, ulid_to_bytes as ulid_to_bytes, ulid_to_bytes_or_none as ulid_to_bytes_or_none

_LOGGER: Incomplete

@lru_cache(maxsize=16)
def uuid_hex_to_bytes_or_none(uuid_hex: str | None) -> bytes | None: ...
@lru_cache(maxsize=16)
def bytes_to_uuid_hex_or_none(_bytes: bytes | None) -> str | None: ...
