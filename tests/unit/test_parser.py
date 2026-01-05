"""Tests for response parser."""

import pytest

from src.parsing.response_parser import (
    ParsedResponse,
    extract_justification,
    extract_score,
    parse_likert_response,
    validate_score,
)


class TestParseLikertResponse:
    """Tests for parse_likert_response function."""

    def test_standard_format(self) -> None:
        """Test parsing standard Score: N format."""
        response = "Score: 5\nJustification: This is my reasoning."
        result = parse_likert_response(response)
        assert result.score == 5
        assert not result.is_refusal
        assert result.justification is not None

    def test_score_only(self) -> None:
        """Test parsing response with score only."""
        response = "Score: 3"
        result = parse_likert_response(response)
        assert result.score == 3
        assert result.justification is None

    def test_lowercase_format(self) -> None:
        """Test parsing with lowercase 'score'."""
        response = "score: 7"
        result = parse_likert_response(response)
        assert result.score == 7

    def test_invalid_score_range(self) -> None:
        """Test handling of scores outside 1-7 range."""
        response = "Score: 10"
        result = parse_likert_response(response)
        assert result.score is None or not validate_score(result.score)

    def test_no_score_found(self) -> None:
        """Test handling when no score is found."""
        response = "I cannot provide a numerical response."
        result = parse_likert_response(response)
        assert result.score is None

    def test_refusal_detection(self) -> None:
        """Test detection of refusal responses."""
        response = "I cannot provide a score for this question."
        result = parse_likert_response(response)
        assert result.is_refusal


class TestExtractScore:
    """Tests for extract_score function."""

    def test_explicit_format(self) -> None:
        """Test extraction from explicit format."""
        score, confidence = extract_score("Score: 4")
        assert score == 4
        assert confidence > 0.8

    def test_inline_score(self) -> None:
        """Test extraction from inline format."""
        score, confidence = extract_score("My answer is 6 because...")
        assert score == 6

    def test_multiple_numbers(self) -> None:
        """Test handling of multiple numbers in response."""
        # Should prefer the explicit score format
        score, _ = extract_score("Score: 5. On a scale of 1 to 7, I chose 5.")
        assert score == 5


class TestExtractJustification:
    """Tests for extract_justification function."""

    def test_standard_justification(self) -> None:
        """Test extraction of standard justification."""
        response = "Score: 4\nJustification: Because of X, Y, and Z."
        justification = extract_justification(response)
        assert justification is not None
        assert "Because" in justification

    def test_no_justification(self) -> None:
        """Test handling when no justification present."""
        response = "Score: 4"
        justification = extract_justification(response)
        assert justification is None


class TestValidateScore:
    """Tests for validate_score function."""

    @pytest.mark.parametrize("score", [1, 2, 3, 4, 5, 6, 7])
    def test_valid_scores(self, score: int) -> None:
        """Test that valid scores pass validation."""
        assert validate_score(score) is True

    @pytest.mark.parametrize("score", [0, 8, -1, 10])
    def test_invalid_scores(self, score: int) -> None:
        """Test that invalid scores fail validation."""
        assert validate_score(score) is False

    def test_none_score(self) -> None:
        """Test that None fails validation."""
        assert validate_score(None) is False
