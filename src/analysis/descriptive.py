"""Descriptive statistics computation."""

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd


@dataclass
class DescriptiveResult:
    """Result of descriptive analysis."""

    mean: float
    std: float
    median: float
    min: float
    max: float
    n: int
    cv: float  # Coefficient of variation
    skewness: float
    kurtosis: float


class DescriptiveStats:
    """Computes descriptive statistics for experiment results.

    Provides summary statistics at various levels of aggregation.
    """

    def __init__(self, results: pd.DataFrame) -> None:
        """Initialize with results DataFrame.

        Args:
            results: DataFrame with experiment results.
        """
        self.results = results

    def compute(self, scores: list[float]) -> DescriptiveResult:
        """Compute descriptive statistics for scores.

        Args:
            scores: List of numeric scores.

        Returns:
            DescriptiveResult with statistics.
        """
        raise NotImplementedError

    def by_model(self) -> dict[str, DescriptiveResult]:
        """Compute statistics grouped by model.

        Returns:
            Dict mapping model_id to DescriptiveResult.
        """
        raise NotImplementedError

    def by_item(self) -> dict[str, DescriptiveResult]:
        """Compute statistics grouped by item.

        Returns:
            Dict mapping item_id to DescriptiveResult.
        """
        raise NotImplementedError

    def by_condition(self) -> dict[str, DescriptiveResult]:
        """Compute statistics grouped by condition.

        Returns:
            Dict mapping condition factors to DescriptiveResult.
        """
        raise NotImplementedError

    def cross_tabulation(
        self, row_var: str, col_var: str
    ) -> pd.DataFrame:
        """Create cross-tabulation of means.

        Args:
            row_var: Variable for rows.
            col_var: Variable for columns.

        Returns:
            Pivot table of means.
        """
        raise NotImplementedError

    def summary_table(self) -> pd.DataFrame:
        """Generate summary statistics table.

        Returns:
            DataFrame with summary statistics.
        """
        raise NotImplementedError
