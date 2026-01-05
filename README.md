# SNAP - Simulated Neural Architecture Profiling

Psychometric benchmark for Large Language Models measuring stability (C1) and contextual sensitivity (C2) of moral/personality profiles.

## Quick Start

```bash
# Install dependencies
uv sync  # or: pip install -e ".[dev]"

# Configure environment
cp .env.example .env
# Edit .env with your OPENROUTER_API_KEY

# Run pilot experiment (3 models, ~4,860 API calls)
python scripts/run_experiment.py --mode pilot --dry-run  # Preview first
python scripts/run_experiment.py --mode pilot

# Run full experiment (10 models, ~16,200 API calls)
python scripts/run_experiment.py --mode full

# Analyze results
python scripts/analyze_results.py

# Generate report
python scripts/generate_report.py
```

## Architecture

```
snap/
├── config/           # YAML configuration files
│   ├── models.yaml       # Target LLM models
│   ├── experiment.yaml   # Experimental design
│   ├── items/            # Psychometric items
│   └── prompts/          # System prompts & templates
├── src/              # Source code
│   ├── api/              # OpenRouter client
│   ├── core/             # Experiment orchestration
│   ├── parsing/          # Response parsing
│   ├── scoring/          # Likert scoring
│   ├── analysis/         # Statistical analysis
│   └── reporting/        # Report generation
├── data/             # Data storage (gitignored)
│   ├── raw/              # Raw API responses
│   ├── processed/        # Processed data
│   ├── logs/             # Experiment logs
│   └── reports/          # Generated reports
└── scripts/          # CLI entry points
```

## Experimental Design

- **10 items**: 5 moral (M01-M05) + 5 personality (P01-P05)
- **3 paraphrases** per item (P1, P2, P3)
- **4 system prompts**: NEU (neutral), DIR (directive), PER (permissive), ABS (abstract)
- **3 temperatures**: 0.0, 0.5, 1.0
- **2 contexts**: C0 (baseline), C1 (dilemma - moral only)
- **3 runs** per condition

**Total**: 1,620 API calls per model, 16,200 for full POC (10 models)

## Models (via OpenRouter)

| Model | OpenRouter ID | Tier |
|-------|---------------|------|
| GPT-5.2 | openai/gpt-5.2 | premium |
| Claude Opus | anthropic/claude-3-opus | flagship |
| Claude Sonnet | anthropic/claude-3.5-sonnet | premium |
| Claude Haiku | anthropic/claude-3-haiku | budget |
| Gemini Pro | google/gemini-pro-1.5 | premium |
| Mistral Large | mistralai/mistral-large | mid |
| Grok-2 | x-ai/grok-2 | budget |
| Qwen 72B | qwen/qwen-2.5-72b-instruct | mid |
| GLM-4 | zhipu/glm-4 | budget |
| Kimi K2 | moonshot/moonshot-v1-128k | budget |

## Response Format

Expected Likert response (1-7):
```
Score: 5
Justification: [optional brief text]
```

Refusal codes:
- `-1`: Explicit refusal
- `-2`: Invalid response
- `-3`: Timeout/API error

## Metrics

- **C1 (Stability)**: Test-retest correlation, ICC, Cronbach's α
- **C2 (Sensitivity)**: Effect sizes across system prompts, contexts

## License

MIT
