"""Response parser for extracting Likert scores.

This module handles parsing LLM responses to extract
structured score data.
"""

import re
from dataclasses import dataclass


@dataclass
class ParsedResponse:
    """Parsed response from an LLM.

    Attributes:
        score: The extracted Likert score (1-7), or None if unparseable.
        is_refusal: Whether the response is a refusal.
        refusal_category: Category of refusal if applicable.
        raw_response: The original response text.
        justification: Extracted justification text, if any.
        confidence: Confidence in the extraction (0.0-1.0).
    """

    score: int | None
    is_refusal: bool
    refusal_category: str | None
    raw_response: str
    justification: str | None = None
    confidence: float = 1.0


# Regex patterns for score extraction
SCORE_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"Score:\s*(\d)", re.IGNORECASE),
    re.compile(r"^(\d)\s*[-:/]", re.MULTILINE),
    re.compile(r"\b([1-7])\b"),  # Fallback: any single digit 1-7
]


def parse_likert_response(response: str) -> ParsedResponse:
    """Extract a Likert score from an LLM response.

    Attempts to parse the response using multiple strategies,
    returning the most confident extraction.

    Args:
        response: The raw response text from the LLM.

    Returns:
        ParsedResponse with extracted data.
    """
    raise NotImplementedError("TODO: Implement parse_likert_response")


def extract_score(response: str) -> tuple[int | None, float]:
    """Extract just the numeric score from a response.

    Args:
        response: The raw response text.

    Returns:
        Tuple of (score, confidence).
    """
    raise NotImplementedError("TODO: Implement extract_score")


def extract_justification(response: str) -> str | None:
    """Extract the justification text from a response.

    Args:
        response: The raw response text.

    Returns:
        The justification text, or None if not found.
    """
    raise NotImplementedError("TODO: Implement extract_justification")


def validate_score(score: int | None) -> bool:
    """Validate that a score is in the valid range.

    Args:
        score: The score to validate.

    Returns:
        True if valid (1-7), False otherwise.
    """
    raise NotImplementedError("TODO: Implement validate_score")
