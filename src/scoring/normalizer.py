"""Score normalization utilities.

This module provides functions for normalizing and transforming
Likert scores for analysis.
"""

from typing import Sequence

import numpy as np


def normalize_scores(
    scores: Sequence[float | None],
    method: str = "zscore",
) -> np.ndarray:
    """Normalize a sequence of scores.

    Args:
        scores: Sequence of scores (may contain None for missing values).
        method: Normalization method ("zscore", "minmax", "percentile").

    Returns:
        Numpy array of normalized scores (NaN for missing values).
    """
    raise NotImplementedError("TODO: Implement normalize_scores")


def zscore_normalize(scores: np.ndarray) -> np.ndarray:
    """Z-score normalize scores.

    Args:
        scores: Array of scores.

    Returns:
        Z-score normalized scores.
    """
    raise NotImplementedError("TODO: Implement zscore_normalize")


def minmax_normalize(
    scores: np.ndarray,
    min_val: float = 1.0,
    max_val: float = 7.0,
) -> np.ndarray:
    """Min-max normalize scores to 0-1 range.

    Args:
        scores: Array of scores.
        min_val: Minimum possible score.
        max_val: Maximum possible score.

    Returns:
        Min-max normalized scores (0-1 range).
    """
    raise NotImplementedError("TODO: Implement minmax_normalize")


def percentile_normalize(scores: np.ndarray) -> np.ndarray:
    """Convert scores to percentile ranks.

    Args:
        scores: Array of scores.

    Returns:
        Percentile ranks (0-100).
    """
    raise NotImplementedError("TODO: Implement percentile_normalize")


def handle_missing(
    scores: Sequence[float | None],
    method: str = "nan",
) -> np.ndarray:
    """Handle missing values in score sequences.

    Args:
        scores: Sequence of scores with possible None values.
        method: How to handle missing ("nan", "mean", "median", "drop").

    Returns:
        Numpy array with missing values handled.
    """
    raise NotImplementedError("TODO: Implement handle_missing")


def aggregate_scores(
    scores: np.ndarray,
    method: str = "mean",
    axis: int | None = None,
) -> float | np.ndarray:
    """Aggregate scores using specified method.

    Args:
        scores: Array of scores.
        method: Aggregation method ("mean", "median", "mode").
        axis: Axis to aggregate along (None for all).

    Returns:
        Aggregated score(s).
    """
    raise NotImplementedError("TODO: Implement aggregate_scores")
