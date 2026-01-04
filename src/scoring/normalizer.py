"""Score normalization utilities."""

from enum import Enum
from typing import Any

import numpy as np


class NormalizationMethod(Enum):
    """Score normalization methods."""

    NONE = "none"  # No normalization
    Z_SCORE = "z_score"  # Standardize to mean=0, std=1
    MIN_MAX = "min_max"  # Scale to [0, 1]
    PERCENT_RANK = "percent_rank"  # Convert to percentile
    IPSATIVE = "ipsative"  # Within-subject centering


class ScoreNormalizer:
    """Normalizes scores for cross-model comparison.

    Applies various normalization methods to make scores
    comparable across different models and conditions.
    """

    def __init__(self, method: NormalizationMethod = NormalizationMethod.Z_SCORE) -> None:
        """Initialize normalizer.

        Args:
            method: Normalization method to use.
        """
        self.method = method
        self._reference_stats: dict[str, Any] = {}

    def fit(self, scores: list[float]) -> "ScoreNormalizer":
        """Fit normalizer to reference distribution.

        Args:
            scores: Reference scores.

        Returns:
            Self for chaining.
        """
        raise NotImplementedError

    def transform(self, scores: list[float]) -> list[float]:
        """Transform scores using fitted parameters.

        Args:
            scores: Scores to normalize.

        Returns:
            Normalized scores.
        """
        raise NotImplementedError

    def fit_transform(self, scores: list[float]) -> list[float]:
        """Fit and transform in one step.

        Args:
            scores: Scores to normalize.

        Returns:
            Normalized scores.
        """
        return self.fit(scores).transform(scores)

    def _z_score(self, scores: list[float]) -> list[float]:
        """Apply z-score normalization.

        Args:
            scores: Raw scores.

        Returns:
            Z-score normalized scores.
        """
        raise NotImplementedError

    def _min_max(self, scores: list[float]) -> list[float]:
        """Apply min-max normalization.

        Args:
            scores: Raw scores.

        Returns:
            Normalized scores in [0, 1].
        """
        raise NotImplementedError

    def _percent_rank(self, scores: list[float]) -> list[float]:
        """Convert to percentile ranks.

        Args:
            scores: Raw scores.

        Returns:
            Percentile ranks.
        """
        raise NotImplementedError

    def _ipsative(self, scores: list[float]) -> list[float]:
        """Apply ipsative (within-subject) centering.

        Args:
            scores: Raw scores.

        Returns:
            Mean-centered scores.
        """
        raise NotImplementedError
