"""Tests for reliability analysis module."""

import numpy as np
import pytest

from src.analysis.reliability import (
    ReliabilityResult,
    compute_cronbach_alpha,
    compute_icc,
    compute_sem,
    compute_test_retest,
    interpret_reliability,
)


class TestComputeTestRetest:
    """Tests for compute_test_retest function."""

    def test_perfect_correlation(self) -> None:
        """Test with perfectly correlated data."""
        scores_t1 = np.array([1, 2, 3, 4, 5, 6, 7])
        scores_t2 = np.array([1, 2, 3, 4, 5, 6, 7])
        result = compute_test_retest(scores_t1, scores_t2)
        assert result.coefficient == pytest.approx(1.0, abs=0.01)

    def test_no_correlation(self) -> None:
        """Test with uncorrelated data."""
        np.random.seed(42)
        scores_t1 = np.array([1, 2, 3, 4, 5, 6, 7])
        scores_t2 = np.array([7, 1, 5, 3, 2, 6, 4])
        result = compute_test_retest(scores_t1, scores_t2)
        assert abs(result.coefficient) < 0.5

    def test_returns_reliability_result(self) -> None:
        """Test return type."""
        scores_t1 = np.array([1, 2, 3, 4, 5])
        scores_t2 = np.array([1, 2, 3, 4, 5])
        result = compute_test_retest(scores_t1, scores_t2)
        assert isinstance(result, ReliabilityResult)
        assert hasattr(result, "ci_lower")
        assert hasattr(result, "ci_upper")


class TestComputeCronbachAlpha:
    """Tests for compute_cronbach_alpha function."""

    def test_high_reliability(self) -> None:
        """Test with highly reliable items."""
        # Items that are highly correlated
        scores_matrix = np.array(
            [
                [1, 1, 1],
                [2, 2, 2],
                [3, 3, 3],
                [4, 4, 4],
                [5, 5, 5],
            ]
        )
        result = compute_cronbach_alpha(scores_matrix)
        assert result.coefficient > 0.9

    def test_returns_reliability_result(self) -> None:
        """Test return type."""
        scores_matrix = np.array(
            [
                [1, 2, 3],
                [2, 3, 4],
                [3, 4, 5],
            ]
        )
        result = compute_cronbach_alpha(scores_matrix)
        assert isinstance(result, ReliabilityResult)


class TestComputeICC:
    """Tests for compute_icc function."""

    def test_perfect_agreement(self) -> None:
        """Test with perfect inter-rater agreement."""
        scores_matrix = np.array(
            [
                [4, 4, 4],
                [5, 5, 5],
                [3, 3, 3],
            ]
        )
        result = compute_icc(scores_matrix)
        assert result.coefficient == pytest.approx(1.0, abs=0.01)

    def test_icc_type(self) -> None:
        """Test different ICC types."""
        scores_matrix = np.array(
            [
                [1, 2, 3],
                [2, 3, 4],
                [3, 4, 5],
            ]
        )
        result = compute_icc(scores_matrix, icc_type="ICC(2,1)")
        assert isinstance(result, ReliabilityResult)


class TestInterpretReliability:
    """Tests for interpret_reliability function."""

    def test_excellent_reliability(self) -> None:
        """Test interpretation of excellent reliability."""
        interpretation = interpret_reliability(0.95)
        assert "excellent" in interpretation.lower()

    def test_good_reliability(self) -> None:
        """Test interpretation of good reliability."""
        interpretation = interpret_reliability(0.80)
        assert "good" in interpretation.lower() or "acceptable" in interpretation.lower()

    def test_poor_reliability(self) -> None:
        """Test interpretation of poor reliability."""
        interpretation = interpret_reliability(0.40)
        assert "poor" in interpretation.lower() or "unacceptable" in interpretation.lower()


class TestComputeSEM:
    """Tests for compute_sem function."""

    def test_sem_calculation(self) -> None:
        """Test SEM calculation."""
        reliability = 0.80
        std = 10.0
        sem = compute_sem(reliability, std)
        # SEM = SD * sqrt(1 - reliability)
        expected = 10.0 * np.sqrt(1 - 0.80)
        assert sem == pytest.approx(expected, abs=0.01)

    def test_perfect_reliability(self) -> None:
        """Test SEM with perfect reliability."""
        sem = compute_sem(1.0, 10.0)
        assert sem == pytest.approx(0.0, abs=0.01)

    def test_zero_reliability(self) -> None:
        """Test SEM with zero reliability."""
        sem = compute_sem(0.0, 10.0)
        assert sem == pytest.approx(10.0, abs=0.01)
