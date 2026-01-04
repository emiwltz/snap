"""Custom exceptions for SNAP."""


class SNAPError(Exception):
    """Base exception for all SNAP errors."""

    pass


class APIError(SNAPError):
    """Error during API communication."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code


class ParseError(SNAPError):
    """Error parsing LLM response."""

    def __init__(self, message: str, raw_response: str | None = None) -> None:
        super().__init__(message)
        self.raw_response = raw_response


class ValidationError(SNAPError):
    """Error validating data or configuration."""

    pass


class RateLimitError(APIError):
    """Rate limit exceeded."""

    def __init__(self, message: str, retry_after: float | None = None) -> None:
        super().__init__(message, status_code=429)
        self.retry_after = retry_after


class CacheError(SNAPError):
    """Error with response cache."""

    pass


class ConfigurationError(SNAPError):
    """Error in experiment configuration."""

    pass
