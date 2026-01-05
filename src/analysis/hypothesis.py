"""Hypothesis testing for SNAP data.

This module provides functions for statistical hypothesis
testing on experimental results.
"""

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd


@dataclass
class ANOVAResult:
    """Results from ANOVA analysis.

    Attributes:
        f_statistic: F-statistic value.
        p_value: P-value.
        df_between: Degrees of freedom between groups.
        df_within: Degrees of freedom within groups.
        eta_squared: Effect size (eta-squared).
        significant: Whether result is significant at alpha=0.05.
    """

    f_statistic: float
    p_value: float
    df_between: int
    df_within: int
    eta_squared: float
    significant: bool


@dataclass
class EffectSize:
    """Effect size statistics.

    Attributes:
        cohens_d: Cohen's d effect size.
        interpretation: Qualitative interpretation.
        ci_lower: Lower 95% CI bound.
        ci_upper: Upper 95% CI bound.
    """

    cohens_d: float
    interpretation: str
    ci_lower: float
    ci_upper: float


def run_anova(
    df: pd.DataFrame,
    dv: str,
    between: str | list[str],
) -> ANOVAResult:
    """Run one-way or factorial ANOVA.

    Args:
        df: DataFrame with experimental data.
        dv: Dependent variable column.
        between: Between-subjects factor(s).

    Returns:
        ANOVAResult with test statistics.
    """
    raise NotImplementedError("TODO: Implement run_anova")


def run_repeated_measures_anova(
    df: pd.DataFrame,
    dv: str,
    within: str | list[str],
    subject: str,
) -> ANOVAResult:
    """Run repeated measures ANOVA.

    Args:
        df: DataFrame with experimental data.
        dv: Dependent variable column.
        within: Within-subjects factor(s).
        subject: Subject identifier column.

    Returns:
        ANOVAResult with test statistics.
    """
    raise NotImplementedError("TODO: Implement run_repeated_measures_anova")


def compute_effect_sizes(
    group1: np.ndarray,
    group2: np.ndarray,
) -> EffectSize:
    """Compute effect size between two groups.

    Args:
        group1: Scores for first group.
        group2: Scores for second group.

    Returns:
        EffectSize with Cohen's d and interpretation.
    """
    raise NotImplementedError("TODO: Implement compute_effect_sizes")


def run_posthoc_tests(
    df: pd.DataFrame,
    dv: str,
    factor: str,
    correction: str = "bonferroni",
) -> pd.DataFrame:
    """Run post-hoc pairwise comparisons.

    Args:
        df: DataFrame with experimental data.
        dv: Dependent variable column.
        factor: Factor for comparisons.
        correction: Multiple comparison correction method.

    Returns:
        DataFrame with pairwise comparison results.
    """
    raise NotImplementedError("TODO: Implement run_posthoc_tests")


def run_ttest(
    group1: np.ndarray,
    group2: np.ndarray,
    paired: bool = False,
) -> dict[str, Any]:
    """Run t-test between two groups.

    Args:
        group1: Scores for first group.
        group2: Scores for second group.
        paired: Whether to run paired t-test.

    Returns:
        Dictionary with t-statistic, p-value, effect size.
    """
    raise NotImplementedError("TODO: Implement run_ttest")


def interpret_effect_size(d: float) -> str:
    """Interpret Cohen's d effect size.

    Args:
        d: Cohen's d value.

    Returns:
        Interpretation string ("small", "medium", "large").
    """
    raise NotImplementedError("TODO: Implement interpret_effect_size")


def compute_power(
    effect_size: float,
    n: int,
    alpha: float = 0.05,
) -> float:
    """Compute statistical power.

    Args:
        effect_size: Expected effect size (Cohen's d).
        n: Sample size per group.
        alpha: Significance level.

    Returns:
        Statistical power (0-1).
    """
    raise NotImplementedError("TODO: Implement compute_power")
