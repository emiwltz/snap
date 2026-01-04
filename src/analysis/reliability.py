"""Reliability analysis (Cronbach's alpha, ICC, test-retest)."""

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd


@dataclass
class ReliabilityResult:
    """Result of reliability analysis."""

    coefficient: float
    """Reliability coefficient value."""

    ci_lower: float
    """95% CI lower bound."""

    ci_upper: float
    """95% CI upper bound."""

    metric_name: str
    """Name of the reliability metric."""

    n_items: int
    """Number of items/measurements."""

    interpretation: str
    """Qualitative interpretation."""


class ReliabilityAnalyzer:
    """Computes reliability metrics for SNAP experiment.

    Implements various psychometric reliability measures.
    """

    def __init__(self, results: pd.DataFrame) -> None:
        """Initialize analyzer with results.

        Args:
            results: DataFrame with experiment results.
        """
        self.results = results

    def cronbach_alpha(
        self, items: list[str], model_id: str | None = None
    ) -> ReliabilityResult:
        """Compute Cronbach's alpha for internal consistency.

        Args:
            items: List of item IDs to include.
            model_id: Optional model to filter by.

        Returns:
            ReliabilityResult with alpha coefficient.
        """
        raise NotImplementedError

    def test_retest(
        self, model_id: str, run1: int = 1, run2: int = 2
    ) -> ReliabilityResult:
        """Compute test-retest reliability.

        Args:
            model_id: Model to analyze.
            run1: First run number.
            run2: Second run number.

        Returns:
            ReliabilityResult with correlation coefficient.
        """
        raise NotImplementedError

    def inter_paraphrase(
        self, model_id: str, item_id: str
    ) -> ReliabilityResult:
        """Compute inter-paraphrase correlation.

        Args:
            model_id: Model to analyze.
            item_id: Item to analyze.

        Returns:
            ReliabilityResult with correlation.
        """
        raise NotImplementedError

    def icc(
        self, model_id: str, icc_type: str = "ICC(2,1)"
    ) -> ReliabilityResult:
        """Compute Intraclass Correlation Coefficient.

        Args:
            model_id: Model to analyze.
            icc_type: Type of ICC (ICC(1,1), ICC(2,1), ICC(3,1)).

        Returns:
            ReliabilityResult with ICC.
        """
        raise NotImplementedError

    def split_half(
        self, model_id: str, method: str = "odd_even"
    ) -> ReliabilityResult:
        """Compute split-half reliability.

        Args:
            model_id: Model to analyze.
            method: Split method (odd_even, random, first_second).

        Returns:
            ReliabilityResult with Spearman-Brown corrected coefficient.
        """
        raise NotImplementedError

    @staticmethod
    def interpret_reliability(coefficient: float) -> str:
        """Interpret reliability coefficient.

        Args:
            coefficient: Reliability value.

        Returns:
            Qualitative interpretation string.
        """
        if coefficient >= 0.9:
            return "excellent"
        elif coefficient >= 0.8:
            return "good"
        elif coefficient >= 0.7:
            return "acceptable"
        elif coefficient >= 0.6:
            return "questionable"
        elif coefficient >= 0.5:
            return "poor"
        else:
            return "unacceptable"
