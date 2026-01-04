# SNAP - Simulated Neural Architecture Profiling

A psychometric benchmark to evaluate the stability and consistency of LLM personality and moral profiles.

## Overview

SNAP tests whether Large Language Models produce stable, reproducible response patterns across systematic experimental variations. It applies psychometric methodology to assess:

- **Stability**: Do models give consistent responses across repeated queries?
- **Coherence**: Do semantically equivalent questions yield similar responses?
- **Sensitivity**: How do responses change with context, prompting, and temperature?

## Research Questions

1. Can LLMs maintain a stable psychological profile under controlled variations?
2. Which models show the highest test-retest reliability?
3. How sensitive are moral/personality responses to contextual framing?
4. Do different model families exhibit distinct stability patterns?

## Experimental Design

### Variables
- **Items**: 5 moral + 5 personality questions
- **Paraphrases**: 3 semantic variations per item
- **System Prompts**: Neutral, Directive, Persona, Abstract
- **Temperatures**: 0.0, 0.5, 1.0
- **Contexts**: Baseline + moral dilemma framing
- **Runs**: 3 repetitions

### Models (via OpenRouter)
- GPT-5.2
- Claude 3 Opus, Sonnet, Haiku
- Gemini Pro 1.5
- Mistral Large
- Grok-2
- Qwen 2.5 72B
- GLM-4
- Kimi K2

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/snap.git
cd snap

# Install with uv
uv sync

# Configure API key
cp .env.example .env
# Edit .env with your OpenRouter API key
```

## Usage

```bash
# Run pilot experiment (3 models)
uv run python scripts/run_experiment.py --mode pilot

# Run full experiment
uv run python scripts/run_experiment.py --mode full

# Analyze results
uv run python scripts/analyze_results.py

# Generate report
uv run python scripts/generate_report.py
```

## Project Structure

```
snap/
├── config/           # Experiment configuration
├── src/              # Core library
│   ├── api/          # OpenRouter client
│   ├── core/         # Experiment orchestration
│   ├── parsing/      # Response parsing
│   ├── scoring/      # Likert scoring
│   ├── analysis/     # Statistical analysis
│   └── reporting/    # Report generation
├── data/             # Experiment data
├── tests/            # Test suite
└── scripts/          # CLI tools
```

## Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Test-retest | Correlation across runs | r > 0.70 |
| Inter-paraphrase | Correlation across paraphrases | r > 0.75 |
| CV | Response variability | < 10% |
| Cronbach's α | Internal consistency | > 0.75 |
| ICC | Intraclass correlation | > 0.75 |

## Status

**Phase 1: POC** - Currently implementing core infrastructure

## Author

Emilien Waltz (@ewaltz)

## License

MIT
