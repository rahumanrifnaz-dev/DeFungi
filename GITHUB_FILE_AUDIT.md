# GitHub File Audit

This audit records what should be committed to the public EN3150 Assignment 03 repository and what must remain local or ignored.

## Commit / Ignore Decisions

| File/Directory | Approx. size | Commit / Ignore | Reason |
|---|---:|---|---|
| `README.md` | small | COMMIT | Public setup, dataset, model, result, and report instructions. |
| `requirements.txt` | small | COMMIT | Reproducible Python dependencies. |
| `src/` | small | COMMIT | Source code for dataset preparation, models, training, evaluation, verification, and demo utilities. |
| `data/README.md` | small | COMMIT | Documents official DeFungi source and expected local raw-data folder. |
| `data/processed/*.csv` | 1.1 MB total | COMMIT | Lightweight canonical split metadata. |
| `data/splits/*.csv` | 349 KB total | COMMIT | Compatibility copy of canonical split metadata. |
| `results/tables/` | small | COMMIT | Verified summary tables, MACs, latency, optimizer, and final comparison evidence. |
| `results/figures/` | small | COMMIT | Verified generated plots used for analysis/reporting. |
| `results/verification/` | small | COMMIT | Verification JSON artifacts for split, pipeline, model checks, and smoke tests. |
| `results/raw/*/*.csv` and `results/raw/*/metrics.json` | small | COMMIT | Raw lightweight histories, reports, confusion matrices, predictions, and metrics. |
| `results/raw/**/*.keras` | 219 KB to 33 MB each | IGNORE | Trained model binaries/checkpoints are reproducible and unnecessary for GitHub review. |
| `results/models/*.keras` | 219 KB to 17 MB each | IGNORE | Trained model binaries are reproducible from source. |
| `report/main.tex` | small | COMMIT | Final LaTeX report source. |
| `report/references.bib` | small | COMMIT | Bibliography for final report. |
| `report/main.pdf` | 1.0 MB | COMMIT | Final compiled report; required for review. |
| `report/figures/` | small | COMMIT | Report-ready figures referenced by `report/main.tex`. |
| `report/sections/` | small | COMMIT | Retained report section source files, updated to final verified values. |
| `report_data.md`, `report/report_data.md` | small | COMMIT | Verified report-data summaries for reviewers. |
| `PROJECT_STATUS.md`, `CODEX_SESSION_STATUS.md` | small | COMMIT | Project/session status and final push checkpoint. |
| `FINAL_AUDIT.md`, `SUBMISSION_AUDIT.md` | small | COMMIT | Compliance and submission audit notes. |
| `viva/` | small | COMMIT | Optional but useful viva preparation notes. |
| `.venv/` | large | IGNORE | Local virtual environment, reproducible from `requirements.txt`. |
| `data/raw/defungi.zip` | 156 MB | IGNORE | Downloaded DeFungi archive; official source is documented instead. |
| `data/raw/defungi/` | thousands of images | IGNORE | Raw DeFungi dataset must not be pushed. |
| `submission/` | local package files | IGNORE | Moodle packaging artifacts and temporary ZIP/PDF copies. |
| `src/__pycache__/` | small | IGNORE | Python bytecode cache. |
| LaTeX aux files | small | IGNORE | Generated build files such as `.aux`, `.bbl`, `.log`, `.out`, `.toc`. |
| Archives `*.zip`, `*.rar`, `*.7z` | variable | IGNORE | Avoid accidental dataset/submission archive uploads. |

## Large File Review

| File | Size | Decision | Reason |
|---|---:|---|---|
| `data/raw/defungi.zip` | 156 MB | IGNORE | Raw dataset archive; users download from UCI. |
| `results/raw/efficientnetb0/efficientnetb0_best_validation.keras` | 33.4 MB | IGNORE | Reproducible checkpoint; metrics/CSV evidence committed instead. |
| `results/raw/efficientnetb0/efficientnetb0_selected.keras` | 33.4 MB | IGNORE | Reproducible selected model; metrics/CSV evidence committed instead. |
| `results/raw/mobilenetv2/mobilenetv2_best_validation.keras` | 22.5 MB | IGNORE | Reproducible checkpoint; metrics/CSV evidence committed instead. |
| `results/raw/mobilenetv2/mobilenetv2_selected.keras` | 22.5 MB | IGNORE | Reproducible selected model; metrics/CSV evidence committed instead. |
| `results/models/efficientnetb0_transfer.keras` | 17.1 MB | IGNORE | Reproducible older model artifact. |
| `results/models/mobilenetv2_transfer.keras` | 9.7 MB | IGNORE | Reproducible older model artifact. |
| `results/models/model_a_adam.keras` | 1.3 MB | IGNORE | Reproducible custom model artifact. |
| `results/models/model_b_adam.keras` | 225 KB | IGNORE | Reproducible custom model artifact. |
| `report/main.pdf` | 1.0 MB | COMMIT | Final assignment report. |
| `data/processed/splits.csv` | 610 KB | COMMIT | Lightweight canonical split metadata. |

## Safety Scan Summary

- Sensitive-value scan: no credential files or private assignments found outside ignored directories.
- Machine-specific path scan: no repository files selected for commit contain local absolute user-home paths.
- Neighbor-report scan: no neighboring-group identifiers or dataset/report terms were found in the final report or selected project content.

## Final Decision

Commit source code, README, requirements, canonical split metadata, lightweight verified results, figures, report source/PDF, audits, and viva notes. Exclude raw DeFungi images, virtual environments, archives, Python caches, LaTeX temporary files, submission ZIPs, and trained model binaries.
