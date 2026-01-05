"""Integration tests for the full experiment pipeline."""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.core.condition import Condition, ExperimentConfig, generate_conditions
from src.core.experiment import Experiment, ExperimentResult
from src.parsing.response_parser import parse_likert_response


class TestExperimentPipeline:
    """Integration tests for experiment pipeline."""

    @pytest.fixture
    def sample_config(self) -> ExperimentConfig:
        """Create a minimal test configuration."""
        return ExperimentConfig(
            name="test_experiment",
            models=["test-model"],
            items={"moral": ["M01"], "personality": ["P01"]},
            paraphrases=["P1"],
            system_prompts=["NEU"],
            temperatures=[0.0],
            contexts={"moral": ["C0"], "personality": ["C0"]},
            runs=1,
        )

    def test_condition_generation(self, sample_config: ExperimentConfig) -> None:
        """Test that conditions are generated correctly."""
        conditions = generate_conditions(sample_config)

        # Should have 2 conditions: M01 and P01
        assert len(conditions) == 2

        # All conditions should have the expected structure
        for condition in conditions:
            assert isinstance(condition, Condition)
            assert condition.paraphrase_id == "P1"
            assert condition.system_prompt == "NEU"
            assert condition.temperature == 0.0

    def test_response_parsing_integration(self) -> None:
        """Test parsing of various response formats."""
        responses = [
            ("Score: 5\nJustification: Test", 5),
            ("score: 3", 3),
            ("My answer is 7", 7),
        ]

        for response_text, expected_score in responses:
            result = parse_likert_response(response_text)
            assert result.score == expected_score

    @pytest.mark.asyncio
    async def test_experiment_dry_run(self, sample_config: ExperimentConfig) -> None:
        """Test experiment dry run mode."""
        experiment = Experiment(sample_config)

        # Dry run should not make API calls
        with patch.object(experiment, "_run_condition") as mock_run:
            result = await experiment.run(mode="pilot", dry_run=True)

            mock_run.assert_not_called()
            assert isinstance(result, ExperimentResult)

    @pytest.mark.asyncio
    async def test_experiment_with_mocked_api(
        self, sample_config: ExperimentConfig
    ) -> None:
        """Test experiment with mocked API responses."""
        experiment = Experiment(sample_config)

        mock_response = {
            "content": "Score: 5\nJustification: Test response",
            "model": "test-model",
            "usage": {"total_tokens": 50},
        }

        with patch.object(
            experiment, "_run_condition", new_callable=AsyncMock
        ) as mock_run:
            mock_run.return_value = mock_response

            result = await experiment.run(mode="pilot")

            assert result.successful_calls > 0


class TestCheckpointing:
    """Tests for experiment checkpointing."""

    @pytest.fixture
    def temp_dir(self, tmp_path: Path) -> Path:
        """Create a temporary directory for checkpoints."""
        return tmp_path / "checkpoints"

    def test_checkpoint_save_load(self, temp_dir: Path) -> None:
        """Test saving and loading checkpoints."""
        temp_dir.mkdir(parents=True, exist_ok=True)

        # Create a mock result
        config = ExperimentConfig(
            name="test",
            models=["m1"],
            items={"moral": ["M01"]},
            paraphrases=["P1"],
            system_prompts=["NEU"],
            temperatures=[0.0],
            contexts={"moral": ["C0"]},
            runs=1,
        )

        from datetime import datetime

        result = ExperimentResult(
            config=config,
            start_time=datetime.now(),
            total_calls=10,
            successful_calls=9,
            failed_calls=1,
        )

        # Save checkpoint
        checkpoint_path = temp_dir / "checkpoint.json"
        result.save(checkpoint_path)

        # Load checkpoint
        loaded_result = ExperimentResult.load(checkpoint_path)

        assert loaded_result.total_calls == result.total_calls
        assert loaded_result.successful_calls == result.successful_calls


class TestEndToEnd:
    """End-to-end tests simulating full experiment."""

    @pytest.mark.asyncio
    async def test_minimal_experiment(self) -> None:
        """Test a minimal end-to-end experiment."""
        # This test would require actual API access in production
        # For CI, we mock the API calls

        config = ExperimentConfig(
            name="e2e_test",
            models=["claude-haiku"],
            items={"moral": ["M01"]},
            paraphrases=["P1"],
            system_prompts=["NEU"],
            temperatures=[0.0],
            contexts={"moral": ["C0"]},
            runs=1,
        )

        experiment = Experiment(config)

        # Mock the API client
        with patch("src.api.openrouter.OpenRouterClient") as MockClient:
            mock_client = MockClient.return_value
            mock_client.complete = AsyncMock(
                return_value=MagicMock(
                    content="Score: 5",
                    model="claude-haiku",
                    usage={"total_tokens": 50},
                )
            )

            result = await experiment.run(mode="pilot")

            assert result is not None
            assert result.config.name == "e2e_test"
