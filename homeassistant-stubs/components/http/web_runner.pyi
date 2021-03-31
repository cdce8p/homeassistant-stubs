from aiohttp import web
from ssl import SSLContext

class HomeAssistantTCPSite(web.BaseSite):
    def __init__(self, runner: web.BaseRunner, host: Union[None, str, list[str]], port: int, *, shutdown_timeout: float=..., ssl_context: Union[SSLContext, None]=..., backlog: int=..., reuse_address: Union[bool, None]=..., reuse_port: Union[bool, None]=...) -> None: ...
    @property
    def name(self) -> str: ...
    async def start(self) -> None: ...