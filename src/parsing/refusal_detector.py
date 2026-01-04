"""Detection and classification of model refusals."""

from dataclasses import dataclass
from enum import Enum


class RefusalCategory(Enum):
    """Categories of model refusal."""

    NONE = "none"  # Not a refusal
    ETHICAL = "ethical"  # Refuses on ethical grounds
    CAPABILITY = "capability"  # Claims inability
    CLARIFICATION = "clarification"  # Asks for more info
    DEFLECTION = "deflection"  # Redirects without answering
    SAFETY = "safety"  # Safety/content policy
    OTHER = "other"  # Unclassified refusal


@dataclass
class RefusalResult:
    """Result of refusal detection."""

    is_refusal: bool
    """Whether the response is a refusal."""

    category: RefusalCategory
    """Category of refusal."""

    confidence: float
    """Confidence score (0-1)."""

    matched_pattern: str | None = None
    """Pattern that triggered detection."""


class RefusalDetector:
    """Detects and classifies model refusals.

    Uses pattern matching and heuristics to identify when a model
    has refused to provide a Likert rating.
    """

    # Common refusal patterns
    ETHICAL_PATTERNS: list[str] = [
        r"cannot.*ethic",
        r"not.*comfortable",
        r"inappropriate",
        r"decline.*answer",
    ]

    CAPABILITY_PATTERNS: list[str] = [
        r"(as an? )?ai",
        r"cannot.*have.*opinion",
        r"don't.*have.*preference",
        r"not.*capable",
    ]

    CLARIFICATION_PATTERNS: list[str] = [
        r"could you.*clarify",
        r"more.*context",
        r"what do you mean",
        r"depends on",
    ]

    def __init__(self) -> None:
        """Initialize refusal detector."""
        self._compiled_patterns: dict[RefusalCategory, list[object]] = {}

    def detect(self, response: str) -> RefusalResult:
        """Detect if response is a refusal.

        Args:
            response: LLM response text.

        Returns:
            RefusalResult with classification.
        """
        raise NotImplementedError

    def _check_patterns(
        self, response: str, category: RefusalCategory
    ) -> tuple[bool, str | None, float]:
        """Check response against patterns for a category.

        Args:
            response: Response text.
            category: Refusal category to check.

        Returns:
            Tuple of (matched, pattern, confidence).
        """
        raise NotImplementedError

    def _compute_confidence(self, response: str, matches: int) -> float:
        """Compute confidence score.

        Args:
            response: Response text.
            matches: Number of pattern matches.

        Returns:
            Confidence score 0-1.
        """
        raise NotImplementedError
