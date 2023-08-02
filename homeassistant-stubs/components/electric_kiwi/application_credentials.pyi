from .const import OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, OAUTH2_TOKEN as OAUTH2_TOKEN
from .oauth2 import ElectricKiwiLocalOAuth2Implementation as ElectricKiwiLocalOAuth2Implementation
from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer, ClientCredential as ClientCredential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

async def async_get_auth_implementation(hass: HomeAssistant, auth_domain: str, credential: ClientCredential) -> config_entry_oauth2_flow.AbstractOAuth2Implementation: ...
async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer: ...
async def async_get_description_placeholders(hass: HomeAssistant) -> dict[str, str]: ...