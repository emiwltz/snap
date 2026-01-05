"""Experimental condition generation.

This module handles the generation of experimental conditions
from the factorial design specification.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Condition:
    """A single experimental condition.

    Represents one unique combination of experimental variables
    that defines a single API call.

    Attributes:
        item_id: Item identifier (e.g., "M01", "P03").
        paraphrase_id: Paraphrase variant (P1, P2, P3).
        system_prompt: System prompt condition (NEU, DIR, PER, ABS).
        temperature: Sampling temperature (0.0, 0.5, 1.0).
        context_id: Context condition (C0, C1).
        run_number: Run number for replication (1, 2, 3).
    """

    item_id: str
    paraphrase_id: str
    system_prompt: str
    temperature: float
    context_id: str
    run_number: int

    def to_dict(self) -> dict[str, Any]:
        """Convert condition to dictionary.

        Returns:
            Dictionary representation of the condition.
        """
        raise NotImplementedError("TODO: Implement Condition.to_dict")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Condition":
        """Create condition from dictionary.

        Args:
            data: Dictionary with condition parameters.

        Returns:
            New Condition instance.
        """
        raise NotImplementedError("TODO: Implement Condition.from_dict")


@dataclass
class ExperimentConfig:
    """Configuration for experiment design.

    Attributes:
        name: Experiment name.
        models: List of model IDs to test.
        items: Dictionary of item lists by category.
        paraphrases: List of paraphrase IDs.
        system_prompts: List of system prompt IDs.
        temperatures: List of temperature values.
        contexts: Dictionary of context lists by category.
        runs: Number of runs per condition.
    """

    name: str
    models: list[str]
    items: dict[str, list[str]]
    paraphrases: list[str]
    system_prompts: list[str]
    temperatures: list[float]
    contexts: dict[str, list[str]]
    runs: int


def load_config(path: Path) -> ExperimentConfig:
    """Load experiment configuration from YAML file.

    Args:
        path: Path to the configuration file.

    Returns:
        Loaded ExperimentConfig.

    Raises:
        ConfigurationError: If the configuration is invalid.
    """
    raise NotImplementedError("TODO: Implement load_config")


def generate_conditions(config: ExperimentConfig) -> list[Condition]:
    """Generate all experimental conditions from configuration.

    Creates the full factorial combination of all experimental
    variables specified in the configuration.

    Args:
        config: Experiment configuration.

    Returns:
        List of all Condition instances.
    """
    raise NotImplementedError("TODO: Implement generate_conditions")


def filter_conditions_for_mode(
    conditions: list[Condition],
    mode: str,
    config: ExperimentConfig,
) -> list[Condition]:
    """Filter conditions for pilot or full mode.

    Args:
        conditions: Full list of conditions.
        mode: Either "pilot" or "full".
        config: Experiment configuration.

    Returns:
        Filtered list of conditions.
    """
    raise NotImplementedError("TODO: Implement filter_conditions_for_mode")


def estimate_api_calls(conditions: list[Condition], models: list[str]) -> int:
    """Estimate total API calls for given conditions and models.

    Args:
        conditions: List of experimental conditions.
        models: List of model IDs.

    Returns:
        Total number of API calls.
    """
    raise NotImplementedError("TODO: Implement estimate_api_calls")


def estimate_cost(
    conditions: list[Condition],
    models: list[str],
    model_tiers: dict[str, str],
    tier_costs: dict[str, float],
) -> float:
    """Estimate total cost for the experiment.

    Args:
        conditions: List of experimental conditions.
        models: List of model IDs.
        model_tiers: Mapping of model IDs to tier names.
        tier_costs: Mapping of tier names to cost per 1k tokens.

    Returns:
        Estimated total cost in USD.
    """
    raise NotImplementedError("TODO: Implement estimate_cost")
