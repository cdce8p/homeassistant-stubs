from ..config_flow import CodeInvalid as CodeInvalid, NestAuthError as NestAuthError, register_flow_implementation as register_flow_implementation
from .const import DOMAIN as DOMAIN
from homeassistant.core import callback as callback

def initialize(hass, client_id, client_secret) -> None: ...
async def generate_auth_url(client_id, flow_id): ...
async def resolve_auth_code(hass, client_id, client_secret, code): ...
