# SNAP — Simulated Neural Architecture Profiling

## Objectif
Benchmark psychométrique pour LLM : mesurer la stabilité (C1) et la sensibilité contextuelle (C2) des profils moraux/personnalité.

## Stack technique
- Python 3.11+
- OpenRouter API (tous les modèles passent par là)
- SQLite pour stockage local
- Pandas/NumPy pour analyse
- Jinja2 pour templates prompts

## Commandes essentielles
```bash
# Installation
uv sync  # ou pip install -r requirements.txt

# Lancer le pilote (3 modèles, ~4,860 appels)
python scripts/run_experiment.py --mode pilot

# Lancer le POC complet (10 modèles, ~16,200 appels)
python scripts/run_experiment.py --mode full

# Analyser les résultats
python scripts/analyze_results.py

# Générer le rapport
python scripts/generate_report.py
```

## Variables d'environnement requises
- `OPENROUTER_API_KEY` : Clé API OpenRouter
- `SNAP_DATA_DIR` : Répertoire data (default: ./data)

## Architecture des données

### Modèles cibles (via OpenRouter)
1. openai/gpt-5.2
2. anthropic/claude-3.5-sonnet
3. anthropic/claude-3-opus
4. anthropic/claude-3-haiku
5. google/gemini-pro-1.5
6. mistralai/mistral-large
7. x-ai/grok-2
8. qwen/qwen-2.5-72b
9. zhipu/glm-4
10. moonshot/kimi-k2

### Design expérimental
- 10 items (5 moraux + 5 personnalité)
- 3 paraphrases par item (P1, P2, P3)
- 4 system prompts (NEU, DIR, PER, ABS)
- 3 températures (0.0, 0.5, 1.0)
- 2 contextes (items moraux uniquement)
- 3 runs par condition
- **Total : 1,620 appels/modèle → 16,200 appels POC**

## Conventions de code
- Type hints obligatoires
- Docstrings Google style
- Tests pour toute nouvelle fonction
- Logging via `loguru`
- Erreurs custom dans `src/core/exceptions.py`

## IMPORTANT
- **NE JAMAIS hardcoder de clés API** — utiliser .env
- **TOUJOURS vérifier le coût estimé** avant de lancer une expérience
- **COMMITER les configs YAML** mais PAS les données raw

## Workflow recommandé
1. Modifier config/experiment.yaml pour ajuster les paramètres
2. Tester avec `--mode pilot --dry-run` d'abord
3. Vérifier les logs dans data/logs/
4. Lancer l'expérience réelle
5. Analyser avec les scripts dédiés

## Structure des réponses attendues
Format Likert 1-7 avec justification optionnelle :
```
Score: 5
Justification: [texte court]
```

## Gestion des refus
- Code -1 : Refus explicite
- Code -2 : Réponse invalide
- Code -3 : Timeout/erreur API
Les refus sont loggés mais exclus des analyses statistiques.
