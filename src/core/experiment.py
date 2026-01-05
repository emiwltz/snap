"""Experiment orchestration.

This module provides the main experiment runner that coordinates
API calls, parsing, and result storage.
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from src.core.condition import Condition, ExperimentConfig


@dataclass
class ExperimentResult:
    """Results from a completed experiment.

    Attributes:
        config: The experiment configuration used.
        start_time: When the experiment started.
        end_time: When the experiment completed.
        total_calls: Total API calls made.
        successful_calls: Number of successful calls.
        failed_calls: Number of failed calls.
        results: Dictionary mapping (model, condition) to parsed responses.
    """

    config: ExperimentConfig
    start_time: datetime
    end_time: datetime | None = None
    total_calls: int = 0
    successful_calls: int = 0
    failed_calls: int = 0
    results: dict[str, Any] = field(default_factory=dict)

    def save(self, path: Path) -> None:
        """Save results to disk.

        Args:
            path: Path to save the results.
        """
        raise NotImplementedError("TODO: Implement ExperimentResult.save")

    @classmethod
    def load(cls, path: Path) -> "ExperimentResult":
        """Load results from disk.

        Args:
            path: Path to load results from.

        Returns:
            Loaded ExperimentResult.
        """
        raise NotImplementedError("TODO: Implement ExperimentResult.load")


class Experiment:
    """Main experiment runner.

    Orchestrates the full experiment including condition generation,
    API calls, response parsing, and result storage.

    Attributes:
        config: Experiment configuration.
        data_dir: Directory for data storage.
    """

    def __init__(
        self,
        config: ExperimentConfig,
        data_dir: Path | None = None,
    ) -> None:
        """Initialize the experiment.

        Args:
            config: Experiment configuration.
            data_dir: Directory for data storage.
        """
        self.config = config
        self.data_dir = data_dir or Path("data")
        self._checkpoint_path: Path | None = None
        raise NotImplementedError("TODO: Implement Experiment.__init__")

    async def run(
        self,
        mode: str = "full",
        dry_run: bool = False,
        models: list[str] | None = None,
    ) -> ExperimentResult:
        """Run the experiment.

        Args:
            mode: Either "pilot" or "full".
            dry_run: If True, only estimate costs without making calls.
            models: Optional subset of models to run.

        Returns:
            ExperimentResult with all collected data.

        Raises:
            ExperimentError: If the experiment fails.
        """
        raise NotImplementedError("TODO: Implement Experiment.run")

    async def resume(self, checkpoint_path: Path) -> ExperimentResult:
        """Resume an interrupted experiment from checkpoint.

        Args:
            checkpoint_path: Path to the checkpoint file.

        Returns:
            ExperimentResult continuing from checkpoint.

        Raises:
            CheckpointError: If the checkpoint is invalid.
        """
        raise NotImplementedError("TODO: Implement Experiment.resume")

    def save_checkpoint(self, result: ExperimentResult) -> Path:
        """Save a checkpoint of current progress.

        Args:
            result: Current experiment result.

        Returns:
            Path to the saved checkpoint.
        """
        raise NotImplementedError("TODO: Implement Experiment.save_checkpoint")

    async def _run_condition(
        self,
        model: str,
        condition: Condition,
    ) -> dict[str, Any]:
        """Run a single condition for a model.

        Args:
            model: The model ID.
            condition: The experimental condition.

        Returns:
            Dictionary with response and metadata.
        """
        raise NotImplementedError("TODO: Implement Experiment._run_condition")

    def _build_prompt(self, condition: Condition) -> list[dict[str, str]]:
        """Build the prompt messages for a condition.

        Args:
            condition: The experimental condition.

        Returns:
            List of message dictionaries.
        """
        raise NotImplementedError("TODO: Implement Experiment._build_prompt")
