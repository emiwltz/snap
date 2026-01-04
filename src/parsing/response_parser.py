"""Likert scale response parsing."""

import re
from dataclasses import dataclass
from enum import Enum


class ParseConfidence(Enum):
    """Confidence level in score extraction."""

    HIGH = "high"  # Clean numeric response
    MEDIUM = "medium"  # Number extracted from text
    LOW = "low"  # Ambiguous or inferred
    NONE = "none"  # Could not extract


@dataclass
class ParsedResponse:
    """Result of parsing an LLM response for Likert score."""

    score: int | None
    """Extracted Likert score (1-7) or None if failed."""

    is_refusal: bool
    """Whether the model refused to answer."""

    refusal_category: str | None
    """Category of refusal if applicable."""

    raw_response: str
    """Original response text."""

    confidence: ParseConfidence
    """Confidence in the extraction."""

    extraction_method: str | None = None
    """Method used to extract the score."""

    @property
    def is_valid(self) -> bool:
        """Check if response yielded a valid score."""
        return self.score is not None and 1 <= self.score <= 7


def parse_likert_response(response: str) -> ParsedResponse:
    """Extract Likert score from LLM response.

    Attempts multiple extraction strategies in order of confidence:
    1. Clean single digit (1-7)
    2. Number at start/end of response
    3. Number in context ("I rate this a 4")
    4. Keyword mapping ("strongly agree" -> 7)

    Args:
        response: Raw LLM response text.

    Returns:
        ParsedResponse with extracted score and metadata.
    """
    raise NotImplementedError


def extract_clean_number(response: str) -> int | None:
    """Extract score from clean numeric response.

    Args:
        response: Response text.

    Returns:
        Score if response is just a number 1-7, else None.
    """
    raise NotImplementedError


def extract_number_from_text(response: str) -> tuple[int | None, str | None]:
    """Extract score from text containing a number.

    Args:
        response: Response text.

    Returns:
        Tuple of (score, extraction_method) or (None, None).
    """
    raise NotImplementedError


def map_keyword_to_score(response: str) -> int | None:
    """Map Likert keywords to numeric scores.

    Args:
        response: Response text.

    Returns:
        Inferred score or None.
    """
    raise NotImplementedError
