"""Experimental condition generation."""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.experiment import ExperimentConfig


@dataclass(frozen=True)
class Condition:
    """Represents a single experimental condition.

    A condition is a unique combination of all experimental variables
    for a single API call.
    """

    item_id: str
    """Item identifier (e.g., M01, P03)."""

    paraphrase_id: str
    """Paraphrase variant (P1, P2, P3)."""

    system_prompt: str
    """System prompt type (NEU, DIR, PER, ABS)."""

    temperature: float
    """Sampling temperature (0.0, 0.5, 1.0)."""

    context_id: str
    """Context variant (C0, C1 for moral items)."""

    run_number: int
    """Repetition number (1, 2, 3)."""

    def __str__(self) -> str:
        """Return string representation."""
        return (
            f"{self.item_id}_{self.paraphrase_id}_{self.system_prompt}_"
            f"T{self.temperature}_{self.context_id}_R{self.run_number}"
        )

    @property
    def condition_key(self) -> str:
        """Return unique key for this condition (excludes run number)."""
        return (
            f"{self.item_id}_{self.paraphrase_id}_{self.system_prompt}_"
            f"T{self.temperature}_{self.context_id}"
        )

    @property
    def is_moral(self) -> bool:
        """Check if this is a moral item."""
        return self.item_id.startswith("M")

    @property
    def is_personality(self) -> bool:
        """Check if this is a personality item."""
        return self.item_id.startswith("P")


def generate_conditions(config: "ExperimentConfig") -> list[Condition]:
    """Generate all experimental conditions from configuration.

    Creates the full factorial combination of all experimental variables.

    Args:
        config: Experiment configuration with variable definitions.

    Returns:
        List of all Condition objects to be tested.
    """
    raise NotImplementedError


def count_conditions(config: "ExperimentConfig") -> int:
    """Count total number of conditions without generating them.

    Args:
        config: Experiment configuration.

    Returns:
        Total number of conditions.
    """
    raise NotImplementedError
