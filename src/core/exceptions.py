"""Custom exceptions for SNAP.

This module defines the exception hierarchy used throughout
the SNAP framework.
"""


class SNAPError(Exception):
    """Base exception for all SNAP errors."""

    pass


class ConfigurationError(SNAPError):
    """Error in configuration files or settings."""

    pass


class APIError(SNAPError):
    """Error communicating with the API."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        """Initialize API error.

        Args:
            message: Error description.
            status_code: HTTP status code if applicable.
        """
        super().__init__(message)
        self.status_code = status_code


class RateLimitError(APIError):
    """Rate limit exceeded error."""

    def __init__(self, retry_after: float | None = None) -> None:
        """Initialize rate limit error.

        Args:
            retry_after: Seconds to wait before retrying.
        """
        super().__init__("Rate limit exceeded", status_code=429)
        self.retry_after = retry_after


class ParsingError(SNAPError):
    """Error parsing LLM response."""

    def __init__(self, message: str, raw_response: str) -> None:
        """Initialize parsing error.

        Args:
            message: Error description.
            raw_response: The raw response that failed to parse.
        """
        super().__init__(message)
        self.raw_response = raw_response


class ValidationError(SNAPError):
    """Error validating data or configuration."""

    pass


class ExperimentError(SNAPError):
    """Error during experiment execution."""

    pass


class CheckpointError(SNAPError):
    """Error with checkpoint save/load."""

    pass
