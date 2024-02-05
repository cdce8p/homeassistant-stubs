from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

class CertExpiryException(HomeAssistantError): ...
class TemporaryFailure(CertExpiryException): ...
class ValidationFailure(CertExpiryException): ...
class ResolveFailed(TemporaryFailure): ...
class ConnectionTimeout(TemporaryFailure): ...
class ConnectionRefused(TemporaryFailure): ...
