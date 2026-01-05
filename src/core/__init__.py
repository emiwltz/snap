"""Core module for experiment orchestration."""

from src.core.condition import Condition, generate_conditions
from src.core.exceptions import SNAPError
from src.core.experiment import Experiment, ExperimentResult
from src.core.matrix import ResultMatrix

__all__ = [
    "Condition",
    "generate_conditions",
    "Experiment",
    "ExperimentResult",
    "ResultMatrix",
    "SNAPError",
]
