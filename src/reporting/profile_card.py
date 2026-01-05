"""Model profile card generation.

This module generates individual profile cards for each
tested model.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


@dataclass
class ModelProfile:
    """Profile summary for a single model.

    Attributes:
        model_id: The model identifier.
        model_name: Human-readable model name.
        tier: Model tier (flagship, premium, mid, budget).
        n_responses: Total number of valid responses.
        mean_score: Overall mean score.
        stability_score: Stability metric (C1).
        sensitivity_score: Sensitivity metric (C2).
        reliability_metrics: Dictionary of reliability coefficients.
        response_distribution: Distribution across scale points.
        refusal_rate: Proportion of refusals.
    """

    model_id: str
    model_name: str
    tier: str
    n_responses: int
    mean_score: float
    stability_score: float
    sensitivity_score: float
    reliability_metrics: dict[str, float]
    response_distribution: dict[int, float]
    refusal_rate: float


def generate_profile_card(
    profile: ModelProfile,
    output_path: Path,
) -> Path:
    """Generate an HTML profile card for a model.

    Args:
        profile: The model profile data.
        output_path: Path to save the card.

    Returns:
        Path to the generated card.
    """
    raise NotImplementedError("TODO: Implement generate_profile_card")


def compute_model_profile(
    df: pd.DataFrame,
    model_id: str,
) -> ModelProfile:
    """Compute profile for a model from results.

    Args:
        df: DataFrame with experiment results.
        model_id: The model to profile.

    Returns:
        ModelProfile with computed metrics.
    """
    raise NotImplementedError("TODO: Implement compute_model_profile")


def generate_all_profile_cards(
    df: pd.DataFrame,
    output_dir: Path,
) -> list[Path]:
    """Generate profile cards for all models.

    Args:
        df: DataFrame with experiment results.
        output_dir: Directory to save cards.

    Returns:
        List of paths to generated cards.
    """
    raise NotImplementedError("TODO: Implement generate_all_profile_cards")


def render_profile_card_html(profile: ModelProfile) -> str:
    """Render profile card as HTML string.

    Args:
        profile: The model profile data.

    Returns:
        HTML string for the profile card.
    """
    raise NotImplementedError("TODO: Implement render_profile_card_html")


def generate_comparison_table(profiles: list[ModelProfile]) -> str:
    """Generate comparison table for all models.

    Args:
        profiles: List of model profiles.

    Returns:
        HTML string for the comparison table.
    """
    raise NotImplementedError("TODO: Implement generate_comparison_table")


def compute_profile_summary(profiles: list[ModelProfile]) -> dict[str, Any]:
    """Compute summary statistics across profiles.

    Args:
        profiles: List of model profiles.

    Returns:
        Dictionary with summary statistics.
    """
    raise NotImplementedError("TODO: Implement compute_profile_summary")
