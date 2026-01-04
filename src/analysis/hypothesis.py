"""Hypothesis testing for experimental effects."""

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd


@dataclass
class HypothesisResult:
    """Result of hypothesis test."""

    test_name: str
    """Name of statistical test."""

    statistic: float
    """Test statistic value."""

    p_value: float
    """P-value."""

    effect_size: float
    """Effect size (Cohen's d, eta-squared, etc.)."""

    effect_size_type: str
    """Type of effect size measure."""

    significant: bool
    """Whether result is significant at alpha=0.05."""

    interpretation: str
    """Qualitative interpretation."""


class HypothesisTester:
    """Performs hypothesis tests for SNAP experiment.

    Tests for effects of experimental manipulations.
    """

    def __init__(
        self, results: pd.DataFrame, alpha: float = 0.05
    ) -> None:
        """Initialize tester with results.

        Args:
            results: DataFrame with experiment results.
            alpha: Significance level.
        """
        self.results = results
        self.alpha = alpha

    def temperature_effect(self, model_id: str) -> HypothesisResult:
        """Test effect of temperature on responses.

        Args:
            model_id: Model to analyze.

        Returns:
            HypothesisResult for temperature effect.
        """
        raise NotImplementedError

    def prompt_effect(self, model_id: str) -> HypothesisResult:
        """Test effect of system prompt on responses.

        Args:
            model_id: Model to analyze.

        Returns:
            HypothesisResult for prompt effect.
        """
        raise NotImplementedError

    def context_effect(self, model_id: str) -> HypothesisResult:
        """Test effect of context on moral responses.

        Args:
            model_id: Model to analyze.

        Returns:
            HypothesisResult for context effect.
        """
        raise NotImplementedError

    def model_comparison(
        self, model1: str, model2: str
    ) -> HypothesisResult:
        """Compare two models' response profiles.

        Args:
            model1: First model ID.
            model2: Second model ID.

        Returns:
            HypothesisResult for model difference.
        """
        raise NotImplementedError

    def anova(
        self, dv: str, factors: list[str], model_id: str | None = None
    ) -> dict[str, HypothesisResult]:
        """Perform factorial ANOVA.

        Args:
            dv: Dependent variable (score column).
            factors: List of factor column names.
            model_id: Optional model to filter by.

        Returns:
            Dict mapping factor to HypothesisResult.
        """
        raise NotImplementedError

    @staticmethod
    def cohens_d(group1: list[float], group2: list[float]) -> float:
        """Compute Cohen's d effect size.

        Args:
            group1: First group scores.
            group2: Second group scores.

        Returns:
            Cohen's d value.
        """
        raise NotImplementedError

    @staticmethod
    def interpret_effect_size(d: float) -> str:
        """Interpret Cohen's d effect size.

        Args:
            d: Cohen's d value.

        Returns:
            Qualitative interpretation.
        """
        d_abs = abs(d)
        if d_abs >= 0.8:
            return "large"
        elif d_abs >= 0.5:
            return "medium"
        elif d_abs >= 0.2:
            return "small"
        else:
            return "negligible"
