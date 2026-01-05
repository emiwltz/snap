"""Refusal detection for LLM responses.

This module identifies when an LLM refuses to provide
a valid response.
"""

from dataclasses import dataclass
from enum import Enum


class RefusalCategory(Enum):
    """Categories of refusal responses.

    Attributes:
        EXPLICIT: Direct refusal to answer.
        HEDGING: Excessive hedging without commitment.
        ETHICAL: Refusal based on ethical concerns.
        SCOPE: Claims the question is out of scope.
        INVALID: Response doesn't match expected format.
        TIMEOUT: API timeout or error.
    """

    EXPLICIT = "explicit"
    HEDGING = "hedging"
    ETHICAL = "ethical"
    SCOPE = "scope"
    INVALID = "invalid"
    TIMEOUT = "timeout"


@dataclass
class RefusalResult:
    """Result of refusal detection.

    Attributes:
        is_refusal: Whether the response is a refusal.
        category: The category of refusal, if any.
        confidence: Confidence in the detection (0.0-1.0).
        indicators: List of detected refusal indicators.
    """

    is_refusal: bool
    category: RefusalCategory | None
    confidence: float
    indicators: list[str]


# Keywords that indicate refusal
REFUSAL_KEYWORDS: list[str] = [
    "cannot provide",
    "unable to",
    "i cannot",
    "i won't",
    "i will not",
    "i'm not able",
    "not appropriate",
    "decline to",
    "refuse to",
]

HEDGING_KEYWORDS: list[str] = [
    "it depends",
    "context matters",
    "too complex",
    "cannot be answered",
    "no single answer",
]


def detect_refusal(response: str) -> RefusalResult:
    """Detect if a response is a refusal.

    Analyzes the response text for refusal patterns
    and categorizes the type of refusal.

    Args:
        response: The raw response text.

    Returns:
        RefusalResult with detection information.
    """
    raise NotImplementedError("TODO: Implement detect_refusal")


def classify_refusal(response: str, indicators: list[str]) -> RefusalCategory:
    """Classify a refusal into a category.

    Args:
        response: The raw response text.
        indicators: List of detected refusal indicators.

    Returns:
        The refusal category.
    """
    raise NotImplementedError("TODO: Implement classify_refusal")


def get_refusal_code(category: RefusalCategory) -> int:
    """Get the numeric code for a refusal category.

    Args:
        category: The refusal category.

    Returns:
        Numeric code (-1 for explicit, -2 for invalid, -3 for timeout).
    """
    raise NotImplementedError("TODO: Implement get_refusal_code")
