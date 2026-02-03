# SNAP - Simulated Neural Architecture Profiling

Psychometric benchmark for Large Language Models measuring stability (C1) and contextual sensitivity (C2) of moral/personality profiles.

<<<<<<< HEAD
## Quick Start
=======
## Overview

SNAP (Simulated Neural Architecture Profiling) applies rigorous psychometric methodology to Large Language Models, treating them as psychological subjects to assess the stability and coherence of their response patterns. Unlike traditional benchmarks that focus on accuracy or capability, SNAP evaluates whether models can maintain consistent "psychological profiles" under systematic experimental variations.

### Core Research Questions

SNAP addresses fundamental questions about LLM behavior:

- **Stability**: Do models give consistent responses across repeated queries with identical conditions?
- **Coherence**: Do semantically equivalent questions (paraphrases) yield similar responses?
- **Sensitivity**: How do responses change with context, prompting style, and temperature?
- **Reliability**: Can models pass standard psychometric reliability tests designed for humans?

### Why This Matters

As LLMs are increasingly used in applications requiring consistent behavior (chatbots, assistants, decision support), understanding their stability across conditions is critical. A model that gives radically different moral judgments based on minor prompt variations or temperature changes may be unsuitable for high-stakes applications.

## Research Questions

SNAP investigates four primary research questions:

1. **Profile Stability**: Can LLMs maintain a stable psychological profile under controlled variations in prompting, temperature, and context? We measure this using test-retest reliability (correlation across runs) and coefficient of variation.

2. **Model Comparison**: Which models show the highest test-retest reliability and internal consistency? We compare 10 models across 3 major families (OpenAI, Anthropic, Google) plus open-source alternatives.

3. **Contextual Sensitivity**: How sensitive are moral and personality responses to:
   - Paraphrasing (semantic equivalence)
   - System prompt framing (neutral, directive, persona, abstract)
   - Temperature settings (deterministic vs. stochastic)
   - Contextual priming (baseline vs. moral dilemma context)

4. **Family Patterns**: Do different model families (GPT, Claude, Gemini) exhibit distinct stability patterns? For example, do instruction-tuned models show higher variance than base models?

## Experimental Design

SNAP uses a **fully factorial within-subjects design** where each model is tested across all combinations of experimental variables. This allows us to measure both main effects and interactions.

### Independent Variables

#### 1. Items (Test Questions)
- **Moral Items** (M01-M05): Questions about ethical decision-making, harm prevention, fairness, authority, and purity
- **Personality Items** (P01-P05): Big Five personality dimensions (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)
- **Format**: 5-point Likert scale ("Strongly Disagree" to "Strongly Agree")
- **Source**: Items adapted from validated psychometric instruments (MFQ-30, Big Five Inventory)

#### 2. Paraphrases (Semantic Variations)
Each item has **3 paraphrases** (P1, P2, P3) that preserve semantic meaning while varying:
- Word choice and phrasing
- Sentence structure
- Complexity level

**Purpose**: Measure inter-paraphrase reliability—a stable model should give similar responses to semantically equivalent questions.

#### 3. System Prompts (Framing)
Four distinct system prompt styles:
- **NEU (Neutral)**: Minimal framing, factual tone
- **DIR (Directive)**: Explicit instructions to respond thoughtfully
- **PER (Persona)**: Role-playing as a helpful assistant
- **ABS (Abstract)**: Meta-level framing about reasoning

**Purpose**: Assess sensitivity to prompt engineering and framing effects.

#### 4. Temperature
Three sampling temperatures:
- **0.0**: Deterministic (greedy decoding)
- **0.5**: Moderate randomness
- **1.0**: High randomness

**Purpose**: Measure stability across sampling strategies. Reliable responses should be stable even at higher temperatures.

#### 5. Context (Moral Items Only)
- **C0 (Baseline)**: Item presented in isolation
- **C1 (Moral Dilemma)**: Item preceded by a moral dilemma scenario

**Purpose**: Test context-dependency—does prior context shift moral judgments?

#### 6. Runs (Repetitions)
Each condition is repeated **3 times** to measure test-retest reliability.

**Purpose**: Assess consistency across independent trials. High reliability requires stable responses across runs.

### Target Models

All models accessed via **OpenRouter API** for consistent infrastructure:

| Model | ID | Tier | Description |
|-------|------|------|-------------|
| GPT-5.2 | `openai/gpt-5.2` | Premium | OpenAI flagship |
| Claude 3 Opus | `anthropic/claude-3-opus` | Flagship | Anthropic flagship |
| Claude 3.5 Sonnet | `anthropic/claude-3.5-sonnet` | Premium | Anthropic balanced |
| Claude 3 Haiku | `anthropic/claude-3-haiku` | Budget | Anthropic fast |
| Gemini Pro 1.5 | `google/gemini-pro-1.5` | Premium | Google flagship |
| Mistral Large | `mistralai/mistral-large` | Mid | Mistral flagship |
| Grok-2 | `x-ai/grok-2` | Budget | xAI conversational |
| Qwen 2.5 72B | `qwen/qwen-2.5-72b-instruct` | Mid | Alibaba large |
| GLM-4 | `zhipu/glm-4` | Budget | Zhipu AI |
| Kimi K2 | `moonshot/moonshot-v1-128k` | Budget | Moonshot long context |

### Sample Size

**Total queries per model**:
- 5 moral items × 3 paraphrases × 4 prompts × 3 temps × 2 contexts × 3 runs = **1,620 queries**
- 5 personality items × 3 paraphrases × 4 prompts × 3 temps × 3 runs = **810 queries**
- **Total: 2,430 queries per model**
- **Full experiment: 24,300 queries across 10 models**

## Installation
>>>>>>> f3e20e8 (improved readme)

### Prerequisites

- **Python 3.11+** (tested on 3.11, 3.12)
- **uv** package manager ([installation guide](https://github.com/astral-sh/uv))
- **OpenRouter API key** ([get one here](https://openrouter.ai/))

### Setup

```bash
<<<<<<< HEAD
# Install dependencies
uv sync  # or: pip install -e ".[dev]"

# Configure environment
cp .env.example .env
# Edit .env with your OPENROUTER_API_KEY
=======
# 1. Clone repository
git clone https://github.com/yourusername/snap.git
cd snap

# 2. Install dependencies with uv
uv sync

# This creates a virtual environment and installs:
# - OpenAI SDK (for OpenRouter API)
# - Pydantic (data validation)
# - PyYAML (config parsing)
# - NumPy, SciPy (statistical analysis)
# - Pytest (testing)

# 3. Configure API credentials
cp .env.example .env

# 4. Edit .env and add your OpenRouter API key
# OPENROUTER_API_KEY=sk-or-v1-...
```

### Verify Installation

```bash
# Run test suite to verify setup
uv run pytest

# Should see all tests passing:
# tests/unit/test_parser.py ✓
# tests/unit/test_scorer.py ✓
# tests/integration/test_api.py ✓ (requires API key)
```
>>>>>>> f3e20e8 (improved readme)

# Run pilot experiment (3 models, ~4,860 API calls)
python scripts/run_experiment.py --mode pilot --dry-run  # Preview first
python scripts/run_experiment.py --mode pilot

<<<<<<< HEAD
# Run full experiment (10 models, ~16,200 API calls)
python scripts/run_experiment.py --mode full

# Analyze results
python scripts/analyze_results.py

# Generate report
python scripts/generate_report.py
=======
### Quick Start: Pilot Experiment

Run a pilot with 3 models to validate your setup:

```bash
uv run python scripts/run_experiment.py --mode pilot

# Pilot mode tests:
# - claude-sonnet (balanced performance/cost)
# - gpt-5.2 (flagship performance)
# - qwen-72b (open-source baseline)
#
# Estimated time: 45-60 minutes
# Estimated cost: ~$5-10 (depends on rate limits)
```

**Output**: Raw responses saved to `data/raw/pilot_YYYYMMDD_HHMMSS.json`

### Full Experiment

Run the complete experiment across all 10 models:

```bash
uv run python scripts/run_experiment.py --mode full

# Full mode processes all models
# Estimated time: 6-8 hours (with rate limiting)
# Estimated cost: $50-100
#
# Uses exponential backoff for rate limits
# Resumes from checkpoint if interrupted
```

**Output**: Raw responses saved to `data/raw/full_YYYYMMDD_HHMMSS.json`

### Analysis Pipeline

```bash
# 1. Analyze results (compute psychometric metrics)
uv run python scripts/analyze_results.py data/raw/experiment.json

# This computes:
# - Test-retest reliability (Pearson correlation across runs)
# - Inter-paraphrase reliability (correlation across paraphrases)
# - Coefficient of variation (CV) for each condition
# - Cronbach's alpha (internal consistency)
# - ICC (intraclass correlation coefficient)
# - Effect sizes for experimental manipulations

# Output: data/processed/analysis.json

# 2. Generate HTML report with verdicts
uv run python scripts/generate_report.py data/processed/analysis.json

# Creates interactive HTML report with:
# - Overall stability verdict per model (PASS/FAIL/BORDERLINE)
# - Metric tables and visualizations
# - Condition-specific breakdowns
# - Comparison across models

# Output: data/reports/report_YYYYMMDD_HHMMSS.html
```

### Advanced Options

```bash
# Run specific models only
uv run python scripts/run_experiment.py --models claude-opus,gpt-5.2

# Resume from checkpoint
uv run python scripts/run_experiment.py --resume data/raw/checkpoint.json

# Adjust rate limits
uv run python scripts/run_experiment.py --rate-limit 10  # 10 req/min

# Dry run (validate config without API calls)
uv run python scripts/run_experiment.py --dry-run
>>>>>>> f3e20e8 (improved readme)
```

## Architecture

```
snap/
<<<<<<< HEAD
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
=======
├── config/                      # Experiment configuration (YAML)
│   ├── models.yaml              # Target models and OpenRouter IDs
│   ├── experiment.yaml          # Experimental design parameters
│   ├── thresholds.yaml          # Psychometric thresholds
│   └── items/                   # Test items and paraphrases
│       ├── moral.yaml           # Moral Foundation items (M01-M05)
│       └── personality.yaml     # Big Five items (P01-P05)
│
├── src/                         # Core Python package
│   ├── api/                     # OpenRouter API client
│   │   ├── client.py            # Async API client with rate limiting
│   │   └── rate_limiter.py      # Exponential backoff
│   │
│   ├── core/                    # Experiment orchestration
│   │   ├── experiment.py        # Main experiment runner
│   │   ├── condition.py         # Condition generation
│   │   └── checkpoint.py        # Resume functionality
│   │
│   ├── parsing/                 # Response parsing
│   │   ├── parser.py            # Extract Likert responses
│   │   └── validator.py         # Validate response format
│   │
│   ├── scoring/                 # Likert scoring
│   │   ├── scorer.py            # Convert text to numeric scores
│   │   └── normalizer.py        # Reverse-scoring for negated items
│   │
│   ├── analysis/                # Statistical analysis
│   │   ├── reliability.py       # Test-retest, inter-paraphrase
│   │   ├── consistency.py       # Cronbach's alpha, ICC
│   │   ├── variability.py       # Coefficient of variation
│   │   └── effects.py           # ANOVA for experimental effects
│   │
│   └── reporting/               # Report generation
│       ├── report.py            # HTML report builder
│       ├── verdicts.py          # Stability verdicts
│       └── templates/           # Jinja2 templates
│
├── data/                        # Experiment data (gitignored)
│   ├── raw/                     # Raw API responses (JSON)
│   ├── processed/               # Analyzed results (JSON)
│   └── reports/                 # Generated HTML reports
│
├── tests/                       # Test suite
│   ├── unit/                    # Unit tests for components
│   │   ├── test_parser.py
│   │   ├── test_scorer.py
│   │   └── test_reliability.py
│   └── integration/             # Integration tests
│       └── test_api.py
│
├── scripts/                     # CLI entry points
│   ├── run_experiment.py        # Main experiment runner
│   ├── analyze_results.py       # Analysis pipeline
│   └── generate_report.py       # Report generator
│
├── .env.example                 # Environment template
├── pyproject.toml               # Project dependencies (uv/pip)
├── CLAUDE.md                    # Claude Code instructions
└── README.md                    # This file
```

## Psychometric Metrics

SNAP applies standard psychometric reliability measures to LLM responses. Each metric has **minimum** and **target** thresholds based on human psychometric standards.

### 1. Test-Retest Reliability

**Definition**: Pearson correlation of responses across the 3 independent runs for each condition.

**Interpretation**:
- Measures stability across repeated queries with identical conditions
- High test-retest reliability indicates the model gives consistent answers

**Thresholds**:
- **Minimum**: r ≥ 0.60 (acceptable)
- **Target**: r ≥ 0.70 (good)
- **Excellent**: r ≥ 0.80

**Human Benchmark**: Validated personality/moral inventories typically achieve r = 0.70-0.90

---

### 2. Inter-Paraphrase Reliability

**Definition**: Pearson correlation of responses across the 3 paraphrases (P1, P2, P3) of each item.

**Interpretation**:
- Measures coherence across semantically equivalent questions
- Low inter-paraphrase reliability suggests sensitivity to superficial wording changes

**Thresholds**:
- **Minimum**: r ≥ 0.65 (acceptable)
- **Target**: r ≥ 0.75 (good)
- **Excellent**: r ≥ 0.85

**Rationale**: Semantically identical questions should yield nearly identical responses.

---

### 3. Coefficient of Variation (CV)

**Definition**: Standard deviation divided by mean, expressed as percentage.

**Interpretation**:
- Measures relative variability of responses
- Low CV indicates tight clustering around the mean response

**Thresholds**:
- **Target**: CV < 10% (low variability)
- **Acceptable**: CV < 15%
- **Problematic**: CV ≥ 20%

**Computation**: CV = (σ / μ) × 100%

---

### 4. Cronbach's Alpha (α)

**Definition**: Internal consistency of the 5-item moral/personality scales.

**Interpretation**:
- Measures whether items in a scale (e.g., all 5 moral items) tap the same underlying construct
- High alpha suggests coherent psychological profile

**Thresholds**:
- **Minimum**: α ≥ 0.65 (acceptable)
- **Target**: α ≥ 0.75 (good)
- **Excellent**: α ≥ 0.85

**Human Benchmark**: Published scales typically achieve α = 0.70-0.95

---

### 5. Intraclass Correlation Coefficient (ICC)

**Definition**: Proportion of variance due to between-item differences vs. within-item variability.

**Interpretation**:
- Measures absolute agreement across raters/runs
- Stricter than Pearson correlation (penalizes systematic shifts)

**Thresholds**:
- **Minimum**: ICC ≥ 0.60 (acceptable)
- **Target**: ICC ≥ 0.75 (good)
- **Excellent**: ICC ≥ 0.90

**Model**: ICC(2,1) - two-way random effects, single measure

---

### Verdict System

Each model receives an overall stability verdict:

- **PASS**: All metrics meet target thresholds
- **BORDERLINE**: All metrics meet minimum thresholds, but some below target
- **FAIL**: One or more metrics below minimum threshold

Models are also ranked by a **composite stability score** (weighted average of metrics).

## Methodology Details

### Response Collection

Each query to a model follows this structure:

```
System Prompt: [NEU/DIR/PER/ABS]
Context: [Optional moral dilemma for C1 condition]
User Prompt: [Item text + paraphrase]

Example:
"On a scale from 1 (Strongly Disagree) to 5 (Strongly Agree),
please respond to the following statement:

It is morally acceptable to harm one person to save many others.

Respond with ONLY a number from 1-5."
```

### Parsing & Validation

Responses are parsed using regex patterns to extract the numeric Likert score (1-5):
- Valid: "3", "I choose 4", "My response is: 2"
- Invalid: "It depends", "I cannot answer", non-numeric responses

Invalid responses are flagged and excluded from analysis. Models with >10% invalid response rate are flagged as unreliable.

### Statistical Analysis

1. **Descriptive Statistics**: Mean, SD, CV per condition
2. **Reliability**: Pearson correlations for test-retest and inter-paraphrase
3. **Internal Consistency**: Cronbach's alpha for 5-item scales
4. **Agreement**: ICC(2,1) for absolute agreement across runs
5. **Effect Sizes**: η² (eta-squared) for experimental manipulations
6. **ANOVA**: Mixed-effects models for main effects and interactions

### Quality Control

- Rate limiting with exponential backoff (respects API limits)
- Checkpointing every 100 queries (resume on failure)
- Response validation (reject malformed responses)
- Outlier detection (flag responses >3 SD from mean)
- Duplicate detection (ensure no duplicate queries)

---

## Output Examples

### Raw Response (JSON)

```json
{
  "model": "claude-sonnet",
  "item": "M01",
  "paraphrase": "P1",
  "system_prompt": "NEU",
  "temperature": 0.0,
  "context": "C0",
  "run": 1,
  "raw_response": "3",
  "parsed_score": 3,
  "valid": true,
  "timestamp": "2025-01-15T14:32:11Z"
}
```

### Analysis Results (JSON)

```json
{
  "model": "claude-sonnet",
  "metrics": {
    "test_retest": 0.78,
    "inter_paraphrase": 0.82,
    "cv_mean": 8.4,
    "cronbach_alpha_moral": 0.71,
    "cronbach_alpha_personality": 0.68,
    "icc": 0.75
  },
  "verdict": "PASS",
  "rank": 2,
  "composite_score": 0.76
}
```

### HTML Report

The generated report includes:
- **Executive Summary**: Overall verdict and ranking
- **Metric Tables**: All 5 metrics per model with color-coded thresholds
- **Visualizations**: Radar charts, heatmaps, correlation matrices
- **Condition Breakdowns**: Metric values per temperature, prompt, etc.
- **Raw Data**: Downloadable CSV exports

---

## Development

### Code Style

- **Python 3.11+** with type hints
- **ruff** for linting and formatting
- **Async/await** for all API calls
- **Pydantic** for data validation
- **Minimal dependencies** (no heavy ML frameworks)

### Running Tests

```bash
# All tests
uv run pytest

# Unit tests only
uv run pytest tests/unit

# Integration tests (requires API key)
uv run pytest tests/integration

# Specific test file
uv run pytest tests/unit/test_parser.py

# With coverage
uv run pytest --cov=src --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Adding New Models

1. Add model to `config/models.yaml`:
```yaml
- id: new-model
  openrouter_id: provider/model-name
  tier: mid
  description: Model description
```

2. Run pilot test:
```bash
uv run python scripts/run_experiment.py --models new-model --mode pilot
```

### Adding New Items

1. Add item to `config/items/moral.yaml` or `personality.yaml`:
```yaml
- id: M06
  construct: Care
  paraphrases:
    P1: "Question text variant 1"
    P2: "Question text variant 2"
    P3: "Question text variant 3"
  reverse_scored: false
```

2. Update experiment config to include new items

---

## Troubleshooting

### API Rate Limits

**Symptom**: `429 Too Many Requests` errors

**Solution**:
```bash
# Increase delay between requests
uv run python scripts/run_experiment.py --rate-limit 5  # 5 req/min
```

### Invalid Responses

**Symptom**: High percentage of unparseable responses for a model

**Possible Causes**:
- Model refusing to give numeric scores (safety filters)
- Model providing explanations instead of numbers
- Prompt format incompatible with model

**Solution**: Check raw responses in `data/raw/` and adjust prompt template in `src/core/experiment.py`

### Out of Memory

**Symptom**: Process killed during analysis

**Solution**: Process models one at a time:
```bash
uv run python scripts/run_experiment.py --models claude-opus
uv run python scripts/run_experiment.py --models gpt-5.2
# ... etc
```

### Checkpoint Resume Not Working

**Symptom**: Experiment restarts from beginning despite checkpoint

**Solution**: Explicitly pass checkpoint file:
```bash
uv run python scripts/run_experiment.py --resume data/raw/checkpoint_TIMESTAMP.json
```

---

## Roadmap

- [ ] Phase 1: Core infrastructure ✓
- [ ] Phase 2: Pilot validation (3 models)
- [ ] Phase 3: Full experiment (10 models)
- [ ] Phase 4: Statistical analysis
- [ ] Phase 5: Publication prep
- [ ] Phase 6: Public dataset release

---

## Contributing

Contributions welcome! Areas of interest:

- Additional psychometric metrics (split-half reliability, parallel forms)
- More sophisticated prompt variations
- Cross-lingual stability testing
- Adversarial prompt injections
- Longitudinal stability (model updates over time)

Please open an issue before major changes.

---

## Citation

If you use SNAP in your research, please cite:

```bibtex
@software{snap2025,
  title={SNAP: Simulated Neural Architecture Profiling},
  author={Waltz, Emilien},
  year={2025},
  url={https://github.com/yourusername/snap}
}
```

## Author

Emilien Waltz (@ewaltz)
>>>>>>> f3e20e8 (improved readme)

## License

MIT
