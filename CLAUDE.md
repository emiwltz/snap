# SNAP - Simulated Neural Architecture Profiling

## Overview

SNAP is a psychometric benchmark for evaluating the stability and consistency of LLM personality/moral profiles. It tests whether models produce stable, reproducible response patterns across systematic variations.

## Project Architecture

```
snap/
├── src/                    # Core Python package
│   ├── api/               # OpenRouter client & rate limiting
│   ├── core/              # Experiment orchestration
│   ├── parsing/           # Response parsing & validation
│   ├── scoring/           # Likert scoring & normalization
│   ├── analysis/          # Statistical analysis
│   └── reporting/         # Report generation
├── config/                # YAML configurations
│   ├── models.yaml        # Target LLM models
│   ├── experiment.yaml    # Experimental design
│   ├── thresholds.yaml    # Psychometric thresholds
│   └── items/             # Test items (moral, personality)
├── data/                  # Experiment data (gitignored)
├── tests/                 # Test suite
└── scripts/               # CLI entry points
```

## Key Concepts

### Experimental Design
- **Items**: Moral (M01-M05) and Personality (P01-P05) questions
- **Paraphrases**: 3 semantic variations per item (P1, P2, P3)
- **System Prompts**: NEU (neutral), DIR (directive), PER (persona), ABS (abstract)
- **Temperatures**: 0.0, 0.5, 1.0
- **Contexts**: C0 (baseline), C1 (moral dilemma context) for moral items
- **Runs**: 3 repetitions per condition

### API Architecture
All API calls go through OpenRouter (`src/api/openrouter.py`). Single client, single format, all models.

## Commands

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Run pilot experiment (3 models)
uv run python scripts/run_experiment.py --mode pilot

# Run full experiment (all models)
uv run python scripts/run_experiment.py --mode full

# Analyze results
uv run python scripts/analyze_results.py data/processed/experiment.json

# Generate report
uv run python scripts/generate_report.py data/processed/analysis.json
```

## Development

### Code Style
- Python 3.11+
- Type hints required
- Async/await for API calls
- Pydantic for data validation
- ruff for linting

### Testing
```bash
uv run pytest                    # All tests
uv run pytest tests/unit         # Unit tests only
uv run pytest -k "parser"        # Specific tests
uv run pytest --cov=src          # With coverage
```

## Workflow

1. **Configure**: Edit `config/experiment.yaml` for parameters
2. **Pilot**: Run with 3 models to validate setup
3. **Full**: Run with all 10 models
4. **Analyze**: Compute psychometric metrics
5. **Report**: Generate HTML report with verdicts

## Custom Agents

Located in `.claude/agents/`:
- `experiment-runner.md`: Runs experiments with monitoring
- `response-analyzer.md`: Analyzes response patterns
- `stats-analyst.md`: Computes psychometric statistics
- `report-generator.md`: Generates reports

## Custom Commands

Located in `.claude/commands/`:
- `/run-pilot`: Quick pilot run
- `/run-full`: Full experiment
- `/analyze`: Analyze results
- `/status`: Check experiment status
- `/debug-model`: Debug specific model

## Psychometric Thresholds

| Metric | Minimum | Target |
|--------|---------|--------|
| Test-retest correlation | 0.60 | 0.70 |
| Inter-paraphrase correlation | 0.65 | 0.75 |
| Coefficient of variation | <15% | <10% |
| Cronbach's alpha | 0.65 | 0.75 |
| ICC | 0.60 | 0.75 |
