"""Response validation utilities.

This module provides validation functions for parsed responses.
"""

from dataclasses import dataclass

from src.parsing.response_parser import ParsedResponse


@dataclass
class ValidationResult:
    """Result of response validation.

    Attributes:
        is_valid: Whether the response is valid.
        errors: List of validation errors.
        warnings: List of validation warnings.
    """

    is_valid: bool
    errors: list[str]
    warnings: list[str]


def validate_response_format(response: str) -> ValidationResult:
    """Validate that a response matches the expected format.

    Args:
        response: The raw response text.

    Returns:
        ValidationResult with validation information.
    """
    raise NotImplementedError("TODO: Implement validate_response_format")


def validate_parsed_response(parsed: ParsedResponse) -> ValidationResult:
    """Validate a parsed response.

    Args:
        parsed: The parsed response.

    Returns:
        ValidationResult with validation information.
    """
    raise NotImplementedError("TODO: Implement validate_parsed_response")


def validate_score_range(score: int | None, min_val: int = 1, max_val: int = 7) -> bool:
    """Validate that a score is within the expected range.

    Args:
        score: The score to validate.
        min_val: Minimum valid score.
        max_val: Maximum valid score.

    Returns:
        True if valid, False otherwise.
    """
    raise NotImplementedError("TODO: Implement validate_score_range")


def validate_justification_length(
    justification: str | None,
    min_length: int = 0,
    max_length: int = 500,
) -> bool:
    """Validate that a justification is within length bounds.

    Args:
        justification: The justification text.
        min_length: Minimum valid length.
        max_length: Maximum valid length.

    Returns:
        True if valid, False otherwise.
    """
    raise NotImplementedError("TODO: Implement validate_justification_length")
