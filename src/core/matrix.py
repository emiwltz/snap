"""Experiment matrix for organizing results."""

from typing import Any

import pandas as pd

from src.core.condition import Condition
from src.core.experiment import ExperimentResult


class ExperimentMatrix:
    """Organizes experiment results into analyzable matrices.

    Provides views of the data organized by different experimental factors.
    """

    def __init__(self, results: list[ExperimentResult]) -> None:
        """Initialize matrix from results.

        Args:
            results: List of experiment results.
        """
        self.results = results
        self._df: pd.DataFrame | None = None

    def to_dataframe(self) -> pd.DataFrame:
        """Convert results to pandas DataFrame.

        Returns:
            DataFrame with one row per result.
        """
        raise NotImplementedError

    def pivot_by_run(self, model_id: str) -> pd.DataFrame:
        """Create matrix with runs as columns.

        Args:
            model_id: Model to filter by.

        Returns:
            DataFrame pivoted by run number.
        """
        raise NotImplementedError

    def pivot_by_paraphrase(self, model_id: str) -> pd.DataFrame:
        """Create matrix with paraphrases as columns.

        Args:
            model_id: Model to filter by.

        Returns:
            DataFrame pivoted by paraphrase.
        """
        raise NotImplementedError

    def pivot_by_temperature(self, model_id: str) -> pd.DataFrame:
        """Create matrix with temperatures as columns.

        Args:
            model_id: Model to filter by.

        Returns:
            DataFrame pivoted by temperature.
        """
        raise NotImplementedError

    def get_scores_for_condition(
        self, condition_key: str, model_id: str
    ) -> list[int | None]:
        """Get all scores for a condition across runs.

        Args:
            condition_key: Condition identifier (without run number).
            model_id: Model to filter by.

        Returns:
            List of scores for each run.
        """
        raise NotImplementedError

    def filter_by_model(self, model_id: str) -> "ExperimentMatrix":
        """Create new matrix filtered to single model.

        Args:
            model_id: Model to filter by.

        Returns:
            New ExperimentMatrix with filtered results.
        """
        raise NotImplementedError

    def summary_stats(self) -> dict[str, Any]:
        """Compute summary statistics.

        Returns:
            Dictionary of summary statistics.
        """
        raise NotImplementedError
