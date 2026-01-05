"""Reliability analysis for SNAP data.

This module provides functions for computing psychometric
reliability coefficients.
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class ReliabilityResult:
    """Results from reliability analysis.

    Attributes:
        coefficient: The reliability coefficient value.
        ci_lower: Lower bound of 95% confidence interval.
        ci_upper: Upper bound of 95% confidence interval.
        n: Number of observations.
        interpretation: Qualitative interpretation.
    """

    coefficient: float
    ci_lower: float
    ci_upper: float
    n: int
    interpretation: str


def compute_test_retest(
    scores_t1: np.ndarray,
    scores_t2: np.ndarray,
) -> ReliabilityResult:
    """Compute test-retest reliability.

    Calculates Pearson correlation between repeated measurements.

    Args:
        scores_t1: Scores from first measurement.
        scores_t2: Scores from second measurement.

    Returns:
        ReliabilityResult with correlation coefficient.
    """
    raise NotImplementedError("TODO: Implement compute_test_retest")


def compute_cronbach_alpha(scores_matrix: np.ndarray) -> ReliabilityResult:
    """Compute Cronbach's alpha for internal consistency.

    Args:
        scores_matrix: Matrix of items x observations.

    Returns:
        ReliabilityResult with alpha coefficient.
    """
    raise NotImplementedError("TODO: Implement compute_cronbach_alpha")


def compute_icc(
    scores_matrix: np.ndarray,
    icc_type: str = "ICC(2,1)",
) -> ReliabilityResult:
    """Compute intraclass correlation coefficient.

    Args:
        scores_matrix: Matrix of raters/runs x subjects.
        icc_type: Type of ICC to compute (e.g., "ICC(2,1)", "ICC(3,k)").

    Returns:
        ReliabilityResult with ICC value.
    """
    raise NotImplementedError("TODO: Implement compute_icc")


def compute_inter_paraphrase_reliability(
    df: pd.DataFrame,
    model: str,
) -> ReliabilityResult:
    """Compute inter-paraphrase reliability for a model.

    Measures consistency across semantically equivalent items.

    Args:
        df: DataFrame with experimental data.
        model: Model ID to analyze.

    Returns:
        ReliabilityResult with correlation coefficient.
    """
    raise NotImplementedError("TODO: Implement compute_inter_paraphrase_reliability")


def compute_split_half_reliability(
    scores: np.ndarray,
    method: str = "odd_even",
) -> ReliabilityResult:
    """Compute split-half reliability.

    Args:
        scores: Array of item scores.
        method: Split method ("odd_even", "random", "first_half").

    Returns:
        ReliabilityResult with Spearman-Brown corrected coefficient.
    """
    raise NotImplementedError("TODO: Implement compute_split_half_reliability")


def interpret_reliability(coefficient: float) -> str:
    """Interpret a reliability coefficient.

    Args:
        coefficient: The reliability coefficient.

    Returns:
        Qualitative interpretation string.
    """
    raise NotImplementedError("TODO: Implement interpret_reliability")


def compute_sem(reliability: float, std: float) -> float:
    """Compute standard error of measurement.

    Args:
        reliability: Reliability coefficient.
        std: Standard deviation of scores.

    Returns:
        Standard error of measurement.
    """
    raise NotImplementedError("TODO: Implement compute_sem")
