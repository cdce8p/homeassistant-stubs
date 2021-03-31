from homeassistant.const import HTTP_OK as HTTP_OK
from multidict import MultiDict
from typing import Any

class MockStreamReader:
    def __init__(self, content: bytes) -> None: ...
    async def read(self, byte_count: int=...) -> bytes: ...

class MockRequest:
    mock_source: Union[str, None] = ...
    method: Any = ...
    url: Any = ...
    status: Any = ...
    headers: Any = ...
    query_string: Any = ...
    def __init__(self, content: bytes, mock_source: str, method: str=..., status: int=..., headers: Union[dict[str, str], None]=..., query_string: Union[str, None]=..., url: str=...) -> None: ...
    @property
    def query(self) -> MultiDict[str]: ...
    @property
    def content(self) -> MockStreamReader: ...
    async def json(self) -> Any: ...
    async def post(self) -> MultiDict[str]: ...
    async def text(self) -> str: ...