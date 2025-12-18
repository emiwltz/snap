
# SNAP
**A benchmark to evaluate the psychological profile of LLMs**  
_Presentation / research repo for collaborators & contributors_

> SNAP is a research project exploring whether we can **measure stable, reproducible patterns** in LLM responses that resemble a “psychological profile” (personality-like traits, values, ideology, moral reasoning, social style) — **without claiming** those constructs are “real” inside the model.

---

## Important disclaimer (read first)
This is a **personal research project**. Results must be interpreted with caution.

Even in humans, the scientific validity of “personality” constructs is debated; mainstream instruments (e.g., Big Five) tend to predict behavior **weakly** (often ~5–10% variance explained), and stability across context/time is contested. If profiling has limited predictive power for humans, applying it to LLMs should be approached with **even more skepticism**.

### What SNAP does **NOT** claim
- LLMs have “real” personalities, inner psychological states, or continuous identity
- Measured profiles have strong predictive validity
- Human psychometric constructs transfer cleanly to artificial systems
- Results should inform **high-stakes** deployment decisions

### What SNAP *is* trying to do
A pragmatic question:
- **Can we measure stable, reproducible response patterns** that are useful for **comparison**, **tracking**, and **limited prediction**, while explicitly acknowledging the approach’s limits?

---

## Core idea
LLM benchmarks mostly measure **capability** (reasoning, coding, knowledge).  
SNAP aims to measure **behavioral/psychological tendencies**:
- ethical positions (utilitarian vs deontological tendencies, etc.)
- value priorities (universalism, security, achievement…)
- political/ideological leanings (left-right, libertarian-authoritarian…)
- interaction style (warmth, directness, formality…)
- behavioral tendencies (risk aversion, cooperation, assertiveness…)

---

## Operational definition
In SNAP, **“psychological profile”** is an umbrella term:

> **Psychological profile (LLM)** = measurable patterns in an LLM’s responses related to personality traits, value systems, ideological orientations, moral reasoning, behavioral tendencies, and social interaction styles.

This definition is deliberately **agnostic**: we do not assume “real psychology”, only that outputs can be characterized along human-analog dimensions.

---

## Dimensions we target (initial set)
| Dimension | What it means (in SNAP) | Example instruments / paradigms |
|---|---|---|
| Personality traits | Stable response patterns resembling traits (e.g., openness, conscientiousness) | Big Five (IPIP-NEO), HEXACO |
| Value systems | Value priorities guiding judgments | Schwartz PVQ-RR, Moral Foundations Questionnaire |
| Political ideology | Positions on socio-political issues | Political Compass, issue-based questionnaires |
| Moral reasoning | Ethical decision patterns | Trolley problems, Moral Machine scenarios |
| Behavioral tendencies | Interaction strategies & risk/cooperation tendencies | Game-theoretic scenarios, negotiation tasks |
| Social style | Tone/relational patterns | Interaction analysis, style classification |

This list is **extensible**.

---

# Project structure: two phases

## Phase 1 — POC (current)
**Goal:** Validate whether profiling is even feasible.  
The benchmark should not exist if LLM responses are too unstable.

### Validation logic (gate condition)
Profiling is only meaningful if responses are:
1. **Coherent / persistent** under controlled variations  
2. (Secondary) **Nuanced**, not mechanically rigid

**If coherence/persistence fails →** pivot or abandon the “psychological profiling” approach.

## Phase 2 — Benchmark (only if Phase 1 passes)
**Goal:** Build the standardized benchmark, scoring protocol, and publish first model profiles.

---

# Phase 1: what is already known vs what must be tested

## Established (from literature): inter-model differentiation ✅
Different LLMs (GPT-family, Claude, Llama, Mistral, etc.) show **distinct profiles** (values, political orientation, personality-like outputs). This seems reproducible.

## Central open criterion: coherence & persistence ❓
Does a given model keep “the same profile” when we vary:
- prompt reformulations (same question, different wording)
- system prompt (neutral vs directive vs persona vs none)
- temperature (0.0–0.3 vs 0.5–0.7 vs 0.9–1.0)
- minor context details (names, locations, non-significant scenario changes)

### Nuance sub-criterion (secondary)
If stable, is the stability “intelligent”?
- different justifications (not copy/paste arguments)
- sensitivity to stakes (adapts to scenario specifics)
- occasional nuance / exceptions / edge cases

---

# Experimental protocol (Phase 1)

## Objective
Measure how much each variable (prompt/system/temperature/context) affects the **coherence** of the model’s expressed profile.

## Test families
- **Moral dilemmas:** trolley problems, classic dilemmas, Moral Machine-style cases
- **Psychometric-style items:** adapted Big Five / values items (careful about validity)
- **Political positioning:** divisive issues, left-right, libertarian-authoritarian

## Metrics (initial)
- **Coherence rate:** % of answers keeping the same position across variations
- **Variable sensitivity:** which variable changes the answer most?
- **Justification diversity:** argument variety vs rigidity
- **Instability threshold:** where/when the model flips (temp? system prompt? wording?)

---

# Repository goals (what we want to build here)
This repo is meant to host:
- Prompt sets + variation generators
- Experiment runners (multi-model, multi-parameter sweeps)
- Result schemas (JSONL/CSV), analysis notebooks/scripts
- Reproducible reports for Phase 1 (go/no-go)
- If Phase 1 passes: benchmark design + scoring protocols + model profile cards

---

# Project status
_Update this section frequently._

- **Current phase:** Phase 1 (POC)
- **Focus:** coherence/persistence testing under controlled variations
- **Last updated:** `YYYY-MM-DD`
- **Next milestone:** first full experimental run on N models × M tasks × K variations

---

# How to contribute
SNAP is open to contributions in several tracks. Pick one, open an issue, then a PR.

## 1) Experimental design & methodology
- Propose stronger coherence metrics
- Define “significant vs minor” variations
- Suggest thresholds (what coherence rate is acceptable?)
- Help separate “formulation artifacts” from real signals

## 2) Psychometrics & critical review
- Critique instrument transfer (Big Five/Schwartz/MFQ → LLM)
- Propose LLM-specific instruments or alternative constructs
- Design validation strategies (construct validity, test-retest, measurement invariance)

## 3) Engineering
- API runner (batched calls, caching, rate limits, retries)
- Prompt variation generator
- Data pipeline (JSONL → analysis-ready tables)
- Reproducibility tooling (configs, seeds, versioning, provenance)

## 4) Analysis & visualization
- Coherence dashboards
- Sensitivity analysis (by variable, by task family)
- Drift tracking across model versions

## 5) Model access / funding
- API credits or access to closed models
- Compute resources for systematic testing

---

# Contribution workflow (suggested)
1. **Open an issue** describing:
   - goal
   - proposed approach
   - acceptance criteria (what “done” means)
2. Create a branch: `feature/<short-name>` or `research/<short-name>`
3. Add tests or reproducibility notes where relevant
4. Submit PR with:
   - what changed
   - how to run / reproduce
   - sample output

---

# Reproducibility & provenance (non-negotiable)
Every experimental artifact should record:
- model name + **version/date** (when available)
- provider (API), system prompt used, temperature, top_p, etc.
- exact prompt text + variation id
- timestamps + run id
- parsing/scoring version

> Models evolve: “GPT-4 March 2023” is not “GPT-4 December 2025”. Versioning is part of the problem, not a footnote.

---

# Open questions (tracked)
## Protocol
- What counts as a “minor” vs “significant” prompt change?
- What coherence threshold validates Phase 1?
- How to quantify “nuance” without smuggling subjectivity?

## Validity
- Are human questionnaires appropriate at all for LLMs?
- How to detect “wording artifacts” vs actual stable tendencies?
- Should we develop LLM-native measures?

## Temporality
- How to compare profiles across model updates?
- Do we need a standardized “snapshot” protocol per release?

## Practical constraints
- API costs scale quickly with systematic sweeps
- Access to certain models is limited or expensive

---

# Ethical notes
- SNAP is **not** an alignment/safety certification.
- Do not use SNAP outputs for high-stakes decisions.
- Avoid anthropomorphic framing in conclusions (“the model believes…”).
- Prefer “the model outputs patterns consistent with…”.

---

# License
TBD (recommendation: pick a license early once you’re ready for external contributions).

---

# Credits
- **Author / maintainer:** Émilien Waltz (ewaltz)
- **Project name history:** SoulBench → SNAP

---

# Contact / collaboration
Open an issue with the tag:
- `design` / `psychometrics` / `engineering` / `analysis` / `funding`
and include what you want to work on + your background.
