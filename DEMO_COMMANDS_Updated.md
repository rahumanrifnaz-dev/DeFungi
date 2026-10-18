# EN3150 Assignment 03 — Safe Demo Commands

**Project:** Resource-Constrained CNN Design and Transfer Learning for DeFungi Image Classification  
**Purpose:** Demonstrate the completed project, inspect saved evidence, and verify the implementation **without retraining**.  
**Reference report:** [`RandomGuess_A03_EN3150.pdf`](RandomGuess_A03_EN3150.pdf)

> **Demo safety:** Run commands from the repository root unless a section says otherwise. The primary demo commands below inspect or verify existing work; they do **not** train models. Some checks may initialize TensorFlow or construct models and can take a short time.

## Quick navigation

- [1. Environment setup](#1-environment-setup)
- [2. Recommended live demo](#2-recommended-live-demo)
- [3. Inspect saved results](#3-inspect-saved-results)
- [4. Final report](#4-final-report)
- [5. Training commands — not for live demo](#5-training-commands--not-for-live-demo)
- [6. Troubleshooting](#6-troubleshooting)

## 1. Environment setup

Open a terminal in the **project root** (the folder containing `src/`, `results/`, and `report/`).

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

If the environment has not been created yet:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

> Dependency installation is setup work, not part of the normal demo. The project status records a verified Python 3.12.3 environment; the current machine may differ.

## 2. Recommended live demo

### Step 1 — Show dataset and saved metrics

```bash
python src/demo.py
```

Uses the existing demo entry point. It is intended to show saved project information without retraining; the exact terminal output depends on the local script and available saved artifacts.

### Step 2 — Verify project imports

```bash
python -m src.verify_imports
```

Checks whether project modules can be imported in the active environment.

### Step 3 — Verify environment

```bash
python -m src.verify_environment
```

Displays or verifies the environment information used by the project.

### Step 4 — Verify custom model parameters

```bash
python -m src.model_checks
```

Builds/checks the **architectures**, not a new training run. Expected parameter counts from the final report:

| Architecture | Parameters | Design |
|---|---:|---|
| Model A | 101,829 | Standard Conv2D CNN |
| Model B | 14,272 | Depthwise-separable CNN (under 100,000) |

### Step 5 — Optional pipeline verification

```bash
python -m src.verify_pipeline
```

Use when the local DeFungi dataset and processed split files are available. It may require local data not included in the GitHub repository.

## 3. Inspect saved results

### Dataset summary

```bash
python - <<'PY'
import json
from pathlib import Path
p = Path('results/metrics/dataset_summary.json')
if p.is_file():
    print(json.dumps(json.loads(p.read_text()), indent=2))
else:
    print(f'Missing saved artifact: {p}')
PY
```

Verified dataset values reported in the final PDF:

| Item | Value |
|---|---:|
| Total usable images | 9,114 |
| Classes | H1, H2, H3, H5, H6 |
| Training | 6,379 |
| Validation | 1,367 |
| Testing | 1,368 |
| Model input | 64 × 64 × 3 |

### Final four-model comparison

```bash
python - <<'PY'
from pathlib import Path
import pandas as pd
p = Path('results/tables/final_comparison.csv')
if p.is_file():
    print(pd.read_csv(p).to_string(index=False))
else:
    print(f'Missing saved artifact: {p}')
PY
```

The final report gives these test results (rounded for display):

| Model | Parameters | Test accuracy | Serialized size (KiB) | CPU batch-1 mean (ms) |
|---|---:|---:|---:|---:|
| Model A | 101,829 | 69.59% | 1,241.37 | 2.8241 |
| Model B | 14,272 | 64.84% | 219.41 | 1.5922 |
| MobileNetV2 | 2,264,389 | 69.08% | 22,000.13 | 170.1065 |
| EfficientNet-B0 | 4,055,976 | 76.68% | 32,650.04 | 322.2855 |

**Interpretation:** EfficientNet-B0 leads in accuracy; Model B has the smallest measured footprint and lowest CPU latency in the reported environment. CPU timings are **not** physical edge-device benchmarks.

### Optimizer pilot comparison

```bash
python - <<'PY'
from pathlib import Path
import pandas as pd
p = Path('results/tables/optimizer_comparison.csv')
if p.is_file():
    print(pd.read_csv(p).to_string(index=False))
else:
    print(f'Missing saved artifact: {p}')
PY
```

In the saved five-epoch pilot, final validation losses were **Adam: 1.2509**, **SGD: 1.4039**, and **SGD with momentum: 1.3385**. Adam (learning rate **0.001**) was selected. These pilot values are not final test results.

### Saved figures and evidence

Open the existing files with your file viewer; these are **paths**, not commands:

| Evidence | File |
|---|---|
| Optimizer comparison | `results/figures/optimizer_comparison.png` |
| Model A training curves | `results/figures/model_a_training_curves.png` |
| Model B training curves | `results/figures/model_b_training_curves.png` |
| Model A confusion matrix | `results/figures/model_a_confusion_matrix_report.png` |
| Model B confusion matrix | `results/figures/model_b_confusion_matrix_report.png` |
| Final comparison data | `results/tables/final_comparison.csv` |
| Saved model evaluations | `results/raw/` |

The final PDF also contains the pretrained training curves, confusion matrices, and comparison figures. Some large model binaries and raw dataset files are intentionally excluded from Git.

## 4. Final report

**Open the submission PDF directly:**

[`RandomGuess_A03_EN3150.pdf`](RandomGuess_A03_EN3150.pdf)

**Optional: rebuild the LaTeX report** (requires a LaTeX installation and report source/figures):

```bash
cd report
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cd ..
```

This compiles the report; it does **not** train models. The uploaded final submission PDF is **14 pages** including front matter and appendices. It may not be identical to an older locally compiled `report/main.pdf`; check which report version is being presented.

## 5. Training commands — NOT for live demo


## 6. Troubleshooting

- **`ModuleNotFoundError`:** Activate the project environment, install `requirements.txt`, and run from the repository root.
- **Dataset missing:** Raw DeFungi images are not stored in Git; follow `data/README.md` before running dataset-dependent checks.
- **Saved file missing:** Verify that `results/` artifacts were included in your local checkout; do not present a missing artifact as verified by a fresh run.
- **No GPU:** The documented environment had no available GPU. Existing results can still be inspected without one.
- **LaTeX command not found:** Install a LaTeX distribution with `latexmk`, or present the existing PDF instead.

---

**Demo checklist:** Show saved dataset → verify imports/environment → check model parameters → show saved optimizer and model comparisons → open final PDF. **No retraining required.**

*This document describes the saved evidence and commands from the project materials. It does not claim that the commands were re-executed in the current environment.*
