"""Descriptive statistics for SNAP data.

This module provides functions for computing descriptive
statistics on experimental results.
"""

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd


@dataclass
class DescriptiveStats:
    """Descriptive statistics for a set of scores.

    Attributes:
        n: Number of valid observations.
        mean: Arithmetic mean.
        std: Standard deviation.
        median: Median value.
        min: Minimum value.
        max: Maximum value.
        cv: Coefficient of variation (%).
        skewness: Skewness of distribution.
        kurtosis: Kurtosis of distribution.
    """

    n: int
    mean: float
    std: float
    median: float
    min: float
    max: float
    cv: float
    skewness: float
    kurtosis: float


def compute_descriptive_stats(scores: np.ndarray) -> DescriptiveStats:
    """Compute descriptive statistics for a score array.

    Args:
        scores: Array of scores.

    Returns:
        DescriptiveStats with computed values.
    """
    raise NotImplementedError("TODO: Implement compute_descriptive_stats")


def compute_cv(scores: np.ndarray) -> float:
    """Compute coefficient of variation.

    Args:
        scores: Array of scores.

    Returns:
        CV as percentage.
    """
    raise NotImplementedError("TODO: Implement compute_cv")


def compute_distribution_stats(scores: np.ndarray) -> dict[str, float]:
    """Compute distribution statistics.

    Args:
        scores: Array of scores.

    Returns:
        Dictionary with skewness, kurtosis, normality test results.
    """
    raise NotImplementedError("TODO: Implement compute_distribution_stats")


def summarize_by_condition(
    df: pd.DataFrame,
    value_col: str,
    group_cols: list[str],
) -> pd.DataFrame:
    """Summarize scores by condition.

    Args:
        df: DataFrame with experimental data.
        value_col: Column containing scores.
        group_cols: Columns to group by.

    Returns:
        Summary DataFrame with stats per condition.
    """
    raise NotImplementedError("TODO: Implement summarize_by_condition")


def summarize_by_model(df: pd.DataFrame, value_col: str = "score") -> pd.DataFrame:
    """Summarize scores by model.

    Args:
        df: DataFrame with experimental data.
        value_col: Column containing scores.

    Returns:
        Summary DataFrame with stats per model.
    """
    raise NotImplementedError("TODO: Implement summarize_by_model")


def compute_response_distribution(
    scores: np.ndarray,
    scale_points: list[int] | None = None,
) -> dict[int, float]:
    """Compute response distribution across scale points.

    Args:
        scores: Array of scores.
        scale_points: List of valid scale points.

    Returns:
        Dictionary mapping scale points to proportions.
    """
    raise NotImplementedError("TODO: Implement compute_response_distribution")


def detect_response_patterns(
    scores: np.ndarray,
) -> dict[str, Any]:
    """Detect problematic response patterns.

    Args:
        scores: Array of scores.

    Returns:
        Dictionary with pattern detection results.
    """
    raise NotImplementedError("TODO: Implement detect_response_patterns")
