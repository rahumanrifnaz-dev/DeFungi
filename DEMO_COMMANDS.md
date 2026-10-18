# Safe Demo Commands

Run these from the project root. They do not retrain models.

## Show Dataset And Saved Metrics

```bash
python src/demo.py
```

## Verify Imports

```bash
python -m src.verify_imports
```

## Show Environment Information

```bash
python -m src.verify_environment
```

## Show Model Parameter Checks

```bash
python -m src.model_checks
```

This constructs Model A and Model B and prints summaries. It does not train them.

## Read Saved Dataset Summary

```bash
python - <<'PY'
import json
from pathlib import Path
print(json.dumps(json.loads(Path("results/metrics/dataset_summary.json").read_text()), indent=2))
PY
```

## Compile LaTeX Report

```bash
cd report
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## DO NOT RUN DURING DEMO UNLESS REQUESTED

These commands are expensive because they train models:

```bash
python -m src.train_custom --model model_a --epochs 20
python -m src.train_custom --model model_b --epochs 20
python -m src.train_pretrained --model mobilenetv2 --epochs 20
python -m src.train_pretrained --model efficientnetb0 --epochs 20
```
