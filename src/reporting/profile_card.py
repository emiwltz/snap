"""Model profile cards for visualization."""

from dataclasses import dataclass
from typing import Any


@dataclass
class DimensionScore:
    """Score for a single dimension."""

    dimension: str
    mean: float
    std: float
    ci_lower: float
    ci_upper: float
    interpretation: str


@dataclass
class ProfileCard:
    """Visual profile card for a model.

    Contains all information needed to render a model's
    psychological profile.
    """

    model_id: str
    """Model identifier."""

    model_name: str
    """Human-readable model name."""

    verdict: str
    """SNAP verdict (SNAP, UNSTABLE, BORDERLINE)."""

    moral_scores: list[DimensionScore]
    """Scores for moral dimensions."""

    personality_scores: list[DimensionScore]
    """Scores for personality dimensions."""

    reliability_metrics: dict[str, float]
    """Reliability coefficients."""

    sensitivity_metrics: dict[str, float]
    """Sensitivity to manipulations."""

    coherence_rate: float
    """Overall response coherence rate."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dict with all profile data.
        """
        raise NotImplementedError

    def to_html(self) -> str:
        """Render as HTML card.

        Returns:
            HTML string for profile card.
        """
        raise NotImplementedError

    def to_markdown(self) -> str:
        """Render as Markdown.

        Returns:
            Markdown string for profile.
        """
        raise NotImplementedError


class ProfileCardGenerator:
    """Generates profile cards from analysis results."""

    def __init__(self, analysis: dict[str, Any]) -> None:
        """Initialize generator.

        Args:
            analysis: Analysis results dict.
        """
        self.analysis = analysis

    def generate(self, model_id: str) -> ProfileCard:
        """Generate profile card for a model.

        Args:
            model_id: Model to generate card for.

        Returns:
            ProfileCard instance.
        """
        raise NotImplementedError

    def generate_all(self) -> list[ProfileCard]:
        """Generate cards for all models.

        Returns:
            List of ProfileCard instances.
        """
        raise NotImplementedError

    def _compute_dimension_scores(
        self, model_id: str, category: str
    ) -> list[DimensionScore]:
        """Compute scores for dimensions.

        Args:
            model_id: Model to analyze.
            category: "moral" or "personality".

        Returns:
            List of DimensionScore instances.
        """
        raise NotImplementedError

    def _interpret_score(self, score: float, dimension: str) -> str:
        """Generate interpretation for a score.

        Args:
            score: Score value.
            dimension: Dimension name.

        Returns:
            Interpretation string.
        """
        raise NotImplementedError
