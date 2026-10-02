# GitHub File Audit

This audit identifies which project artifacts should be committed and which should remain local or ignored.

| File/Directory | Size | Keep / Ignore | Reason |
|---|---:|---|---|
| `src/` | 184 KB | KEEP | Source code for dataset preparation, models, training, evaluation, verification, and report data generation. |
| `README.md` | small | KEEP | Project setup, reproducibility, and results summary. |
| `requirements.txt` | small | KEEP | Python dependency list. |
| `PROJECT_STATUS.md` | small | KEEP | Final project status and verified values. |
| `FINAL_AUDIT.md` | small | KEEP | Final assignment compliance audit. |
| `report_data.md` | 10 KB | KEEP | Top-level copy of the verified report data for GitHub review. |
| `report/report_data.md` | 10 KB | KEEP | Canonical report data used by the report. |
| `data/processed/` | 1.2 MB | KEEP | Lightweight split metadata needed for reproducibility. |
| `results/metrics/` | 88 KB | KEEP | Verified metrics, histories, summaries, and audits. |
| `results/figures/` | 500 KB | KEEP | Training history and class-distribution figures. |
| `results/confusion_matrices/` | 220 KB | KEEP | Confusion matrix figures for evaluation. |
| `report/` source files | small | KEEP | LaTeX report source, bibliography, and sections. |
| `report/figures/` | 500 KB | KEEP | Report-ready copied figures. |
| `report/main.pdf` | 764 KB | KEEP | Final compiled assignment report. |
| `.gitignore` | small | KEEP | Prevents accidental upload of generated, raw, or large files. |
| `MEMBER_FILES.md` | small | KEEP | Maps real group-member responsibilities to files. |
| `GITHUB_WORKFLOW.md` | small | KEEP | Safe collaboration workflow for the real group members. |
| `.venv/` | 2.5 GB | IGNORE | Local Python virtual environment, reproducible with `requirements.txt`. |
| `data/raw/defungi.zip` | 150 MB | IGNORE | Downloaded dataset archive; should not be uploaded to GitHub. |
| `data/raw/defungi/` | 170 MB | IGNORE | Raw DeFungi image dataset; users should download from UCI. |
| `results/models/*.keras` | 28 MB | IGNORE | Trained model binaries; reproducible from source and metrics are already preserved. |
| `src/__pycache__/` | small | IGNORE | Python bytecode cache. |
| `report/main.bbl` and LaTeX aux files | small | IGNORE | Generated LaTeX temporary/build files; report can be rebuilt from source. |

Credential scan result: no credential-like assignments, OAuth secrets, authorization headers, or private keys were found in source/docs/results outside ignored raw/model/environment directories.

Machine-specific path scan result: no `/home/...`, Windows user paths, or desktop-specific absolute paths were found in source/docs/results outside ignored directories.

Large file policy: raw data, archives, virtual environments, and trained model binaries are ignored. Verified metrics, figures, processed split CSVs, report source, and final PDF are kept.

## Proposed Repository Summary Before Git Initialization

### Files To Commit

- Project documentation: `README.md`, `requirements.txt`, `PROJECT_STATUS.md`, `FINAL_AUDIT.md`, `report_data.md`, `GITHUB_FILE_AUDIT.md`, `MEMBER_FILES.md`, `GITHUB_WORKFLOW.md`
- Dataset instructions and lightweight split metadata: `data/README.md`, `data/processed/splits.csv`, `data/processed/train.csv`, `data/processed/validation.csv`, `data/processed/test.csv`
- Source code: `src/*.py`
- Verified results: `results/metrics/`, `results/figures/`, `results/confusion_matrices/`
- Final report: `report/main.tex`, `report/main.pdf`, `report/references.bib`, `report/sections/`, `report/figures/`, `report/report_data.md`

### Files To Ignore

- Local environment: `.venv/`, `venv/`, `env/`
- Raw dataset and archives: `data/raw/`, `*.zip`, `*.rar`, `*.7z`
- Trained model binaries: `results/models/*.keras`, plus any `*.h5`
- Python caches: `__pycache__/`, `*.pyc`
- LaTeX build files: `*.aux`, `*.bbl`, `*.blg`, `*.fdb_latexmk`, `*.fls`, `*.log`, `*.out`, `*.toc`
- IDE/OS/Jupyter cache files

### Large Files

- `.venv/`: 2.5 GB, ignored.
- `data/raw/defungi.zip`: 150 MB, ignored.
- `data/raw/defungi/`: 170 MB, ignored.
- `results/models/*.keras`: 28 MB total, ignored.
- `report/main.pdf`: 764 KB, kept.
- `data/processed/`: 1.2 MB, kept.

### Member File Distribution

- Rifnaz.K.R.M -- 230550P: dataset preparation, canonical split, Model A, dataset and Model A report sections.
- Panuharan.S -- 230462X: Model B, depthwise separable analysis, efficiency/parameter calculations, Model B report section.
- Peranavan.K -- 230474K: optimizer comparison, custom model training/evaluation, metrics/confusion matrices, Model A/B comparison report section.
- Lavanathan.J -- 230371R: MobileNetV2, EfficientNetB0, pretrained evaluation, final comparison report section.

Audit decision: PASS. The repository is ready for local Git initialization, with raw data, virtual environment files, and trained model binaries excluded by `.gitignore`.
