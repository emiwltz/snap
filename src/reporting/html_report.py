"""HTML report generation."""

from pathlib import Path
from typing import Any

import pandas as pd


class HTMLReportGenerator:
    """Generates comprehensive HTML reports for SNAP experiments.

    Creates interactive reports with charts, tables, and verdicts.
    """

    def __init__(
        self,
        results: pd.DataFrame,
        analysis: dict[str, Any],
        output_dir: Path | str = "data/reports",
    ) -> None:
        """Initialize report generator.

        Args:
            results: DataFrame with experiment results.
            analysis: Dict with analysis results.
            output_dir: Directory for output files.
        """
        self.results = results
        self.analysis = analysis
        self.output_dir = Path(output_dir)

    def generate(self, filename: str = "snap_report.html") -> Path:
        """Generate complete HTML report.

        Args:
            filename: Output filename.

        Returns:
            Path to generated report.
        """
        raise NotImplementedError

    def _render_header(self) -> str:
        """Render report header section.

        Returns:
            HTML string for header.
        """
        raise NotImplementedError

    def _render_summary(self) -> str:
        """Render executive summary section.

        Returns:
            HTML string for summary.
        """
        raise NotImplementedError

    def _render_model_profiles(self) -> str:
        """Render individual model profile sections.

        Returns:
            HTML string for profiles.
        """
        raise NotImplementedError

    def _render_comparison(self) -> str:
        """Render cross-model comparison section.

        Returns:
            HTML string for comparison.
        """
        raise NotImplementedError

    def _render_reliability(self) -> str:
        """Render reliability analysis section.

        Returns:
            HTML string for reliability.
        """
        raise NotImplementedError

    def _render_sensitivity(self) -> str:
        """Render sensitivity analysis section.

        Returns:
            HTML string for sensitivity.
        """
        raise NotImplementedError

    def _render_charts(self) -> str:
        """Render interactive charts.

        Returns:
            HTML string with Plotly charts.
        """
        raise NotImplementedError

    def _create_radar_chart(self, model_id: str) -> str:
        """Create radar chart for model profile.

        Args:
            model_id: Model to visualize.

        Returns:
            Plotly chart HTML.
        """
        raise NotImplementedError

    def _create_heatmap(self) -> str:
        """Create heatmap of model similarities.

        Returns:
            Plotly chart HTML.
        """
        raise NotImplementedError
