"""Likert scale scoring utilities."""

from dataclasses import dataclass
from typing import Any


@dataclass
class ScoringResult:
    """Result of scoring a set of responses."""

    scores: list[int | None]
    """Individual scores."""

    mean: float | None
    """Mean score (excluding None values)."""

    std: float | None
    """Standard deviation."""

    valid_count: int
    """Number of valid (non-None) scores."""

    total_count: int
    """Total number of scores."""

    @property
    def validity_rate(self) -> float:
        """Proportion of valid scores."""
        return self.valid_count / self.total_count if self.total_count > 0 else 0.0


class LikertScorer:
    """Handles Likert scale scoring and aggregation.

    Computes statistics over sets of Likert responses.
    """

    def __init__(
        self,
        min_score: int = 1,
        max_score: int = 7,
        reverse_items: list[str] | None = None,
    ) -> None:
        """Initialize Likert scorer.

        Args:
            min_score: Minimum scale value.
            max_score: Maximum scale value.
            reverse_items: List of item IDs to reverse score.
        """
        self.min_score = min_score
        self.max_score = max_score
        self.reverse_items = reverse_items or []

    def score(self, scores: list[int | None]) -> ScoringResult:
        """Compute statistics for a list of scores.

        Args:
            scores: List of Likert scores (None for missing).

        Returns:
            ScoringResult with statistics.
        """
        raise NotImplementedError

    def reverse_score(self, score: int) -> int:
        """Reverse a score on the scale.

        Args:
            score: Original score.

        Returns:
            Reversed score.
        """
        return self.max_score - score + self.min_score

    def aggregate_by_item(
        self, results: list[dict[str, Any]]
    ) -> dict[str, ScoringResult]:
        """Aggregate scores by item ID.

        Args:
            results: List of result dicts with "item_id" and "score".

        Returns:
            Dict mapping item_id to ScoringResult.
        """
        raise NotImplementedError

    def aggregate_by_dimension(
        self, results: list[dict[str, Any]], item_dimensions: dict[str, str]
    ) -> dict[str, ScoringResult]:
        """Aggregate scores by dimension.

        Args:
            results: List of result dicts.
            item_dimensions: Mapping of item_id to dimension.

        Returns:
            Dict mapping dimension to ScoringResult.
        """
        raise NotImplementedError

    def compute_profile(
        self, results: list[dict[str, Any]], item_dimensions: dict[str, str]
    ) -> dict[str, float]:
        """Compute dimension profile from scores.

        Args:
            results: List of result dicts.
            item_dimensions: Mapping of item_id to dimension.

        Returns:
            Dict mapping dimension to mean score.
        """
        raise NotImplementedError
