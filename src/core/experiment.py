"""Experiment orchestration."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.core.condition import Condition


@dataclass
class ExperimentConfig:
    """Configuration for an experiment run."""

    name: str
    """Experiment name."""

    models: list[str]
    """List of model IDs to test."""

    items: dict[str, list[str]]
    """Items by category (moral, personality)."""

    paraphrases: list[str]
    """Paraphrase variants."""

    system_prompts: list[str]
    """System prompt types."""

    temperatures: list[float]
    """Temperature values."""

    contexts: dict[str, list[str]]
    """Context variants by category."""

    runs: int
    """Number of repetitions."""

    api_config: dict[str, Any] = field(default_factory=dict)
    """API configuration (rate limits, timeouts, etc.)."""


@dataclass
class ExperimentResult:
    """Result of a single condition evaluation."""

    condition: Condition
    """The experimental condition."""

    model_id: str
    """Model that generated the response."""

    raw_response: str
    """Raw API response."""

    score: int | None
    """Extracted Likert score (1-7) or None if failed."""

    is_refusal: bool
    """Whether the model refused to answer."""

    latency_ms: float
    """Response latency in milliseconds."""

    cached: bool
    """Whether response was from cache."""

    error: str | None = None
    """Error message if failed."""


class Experiment:
    """Orchestrates a complete SNAP experiment.

    Handles condition generation, API calls, caching, and result collection.
    """

    def __init__(self, config: ExperimentConfig) -> None:
        """Initialize experiment.

        Args:
            config: Experiment configuration.
        """
        self.config = config
        self._results: list[ExperimentResult] = []
        self._conditions: list[Condition] = []

    @classmethod
    def from_yaml(cls, config_path: Path) -> "Experiment":
        """Load experiment from YAML configuration.

        Args:
            config_path: Path to experiment.yaml.

        Returns:
            Configured Experiment instance.
        """
        raise NotImplementedError

    async def run(self, mode: str = "full") -> list[ExperimentResult]:
        """Run the experiment.

        Args:
            mode: Either "pilot" or "full".

        Returns:
            List of all experiment results.
        """
        raise NotImplementedError

    async def run_condition(
        self, condition: Condition, model_id: str
    ) -> ExperimentResult:
        """Run a single experimental condition.

        Args:
            condition: The condition to evaluate.
            model_id: Model to use.

        Returns:
            Result of the evaluation.
        """
        raise NotImplementedError

    def save_results(self, output_path: Path) -> None:
        """Save results to JSON file.

        Args:
            output_path: Path to output file.
        """
        raise NotImplementedError

    @property
    def progress(self) -> tuple[int, int]:
        """Return (completed, total) condition count."""
        raise NotImplementedError
