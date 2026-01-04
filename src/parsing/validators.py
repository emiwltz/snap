"""Response validation utilities."""

from dataclasses import dataclass
from enum import Enum


class ValidationStatus(Enum):
    """Status of response validation."""

    VALID = "valid"
    INVALID_SCORE = "invalid_score"  # Score out of range
    REFUSAL = "refusal"  # Model refused
    EMPTY = "empty"  # Empty response
    MALFORMED = "malformed"  # Unparseable response
    TIMEOUT = "timeout"  # Response timed out
    ERROR = "error"  # API error


@dataclass
class ValidationResult:
    """Result of response validation."""

    status: ValidationStatus
    """Validation status."""

    is_valid: bool
    """Whether response is valid."""

    message: str | None = None
    """Human-readable validation message."""


class ResponseValidator:
    """Validates LLM responses for SNAP experiment.

    Checks that responses meet the expected format and constraints.
    """

    def __init__(
        self,
        min_score: int = 1,
        max_score: int = 7,
        max_response_length: int = 500,
    ) -> None:
        """Initialize validator.

        Args:
            min_score: Minimum valid Likert score.
            max_score: Maximum valid Likert score.
            max_response_length: Maximum response length before warning.
        """
        self.min_score = min_score
        self.max_score = max_score
        self.max_response_length = max_response_length

    def validate(self, response: str, score: int | None) -> ValidationResult:
        """Validate a response and extracted score.

        Args:
            response: Raw response text.
            score: Extracted score (or None).

        Returns:
            ValidationResult with status.
        """
        raise NotImplementedError

    def validate_score_range(self, score: int) -> bool:
        """Check if score is in valid range.

        Args:
            score: Score to validate.

        Returns:
            True if score is valid.
        """
        return self.min_score <= score <= self.max_score

    def is_empty_response(self, response: str) -> bool:
        """Check if response is effectively empty.

        Args:
            response: Response text.

        Returns:
            True if response is empty or whitespace only.
        """
        return not response or not response.strip()

    def is_verbose_response(self, response: str) -> bool:
        """Check if response is unusually verbose.

        Args:
            response: Response text.

        Returns:
            True if response exceeds max length.
        """
        return len(response) > self.max_response_length
