"""Tests for Likert scoring module."""

import pytest

from src.scoring.likert import (
    LikertScale,
    LikertScore,
    categorize_score,
    is_extreme,
    is_neutral,
    reverse_score,
    score_response,
)


class TestLikertScale:
    """Tests for LikertScale class."""

    def test_default_scale(self) -> None:
        """Test default 1-7 scale."""
        scale = LikertScale()
        assert scale.min_value == 1
        assert scale.max_value == 7
        assert scale.midpoint == 4

    def test_is_valid(self) -> None:
        """Test score validation."""
        scale = LikertScale()
        assert scale.is_valid(1) is True
        assert scale.is_valid(7) is True
        assert scale.is_valid(0) is False
        assert scale.is_valid(8) is False

    def test_get_label(self) -> None:
        """Test label retrieval."""
        scale = LikertScale(
            labels={
                1: "Strongly disagree",
                4: "Neutral",
                7: "Strongly agree",
            }
        )
        assert "disagree" in scale.get_label(1).lower()


class TestScoreResponse:
    """Tests for score_response function."""

    def test_valid_score(self) -> None:
        """Test processing valid score."""
        result = score_response(5)
        assert result == 5

    def test_none_score(self) -> None:
        """Test processing None score."""
        result = score_response(None)
        assert result is None

    def test_reverse_scoring(self) -> None:
        """Test reverse scoring."""
        result = score_response(7, reverse=True)
        assert result == 1

        result = score_response(1, reverse=True)
        assert result == 7


class TestReverseScore:
    """Tests for reverse_score function."""

    @pytest.mark.parametrize(
        "original,expected",
        [
            (1, 7),
            (2, 6),
            (3, 5),
            (4, 4),
            (5, 3),
            (6, 2),
            (7, 1),
        ],
    )
    def test_reverse_mapping(self, original: int, expected: int) -> None:
        """Test correct reverse score mapping."""
        assert reverse_score(original) == expected


class TestCategorizeScore:
    """Tests for categorize_score function."""

    def test_low_scores(self) -> None:
        """Test categorization of low scores."""
        assert "low" in categorize_score(1).lower()
        assert "low" in categorize_score(2).lower()

    def test_neutral_score(self) -> None:
        """Test categorization of neutral score."""
        assert "neutral" in categorize_score(4).lower()

    def test_high_scores(self) -> None:
        """Test categorization of high scores."""
        assert "high" in categorize_score(6).lower()
        assert "high" in categorize_score(7).lower()


class TestIsExtreme:
    """Tests for is_extreme function."""

    def test_extreme_scores(self) -> None:
        """Test detection of extreme scores."""
        assert is_extreme(1) is True
        assert is_extreme(7) is True

    def test_non_extreme_scores(self) -> None:
        """Test non-extreme scores."""
        assert is_extreme(4) is False
        assert is_extreme(3) is False
        assert is_extreme(5) is False


class TestIsNeutral:
    """Tests for is_neutral function."""

    def test_neutral_score(self) -> None:
        """Test detection of neutral score."""
        assert is_neutral(4) is True

    def test_non_neutral_scores(self) -> None:
        """Test non-neutral scores."""
        assert is_neutral(1) is False
        assert is_neutral(7) is False
        assert is_neutral(3) is False


class TestLikertScoreEnum:
    """Tests for LikertScore enum."""

    def test_enum_values(self) -> None:
        """Test enum has correct values."""
        assert LikertScore.STRONGLY_DISAGREE == 1
        assert LikertScore.NEUTRAL == 4
        assert LikertScore.STRONGLY_AGREE == 7

    def test_enum_comparison(self) -> None:
        """Test enum comparison."""
        assert LikertScore.AGREE > LikertScore.DISAGREE
