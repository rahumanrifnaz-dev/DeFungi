# Project Status

PROJECT IMPLEMENTATION: COMPLETE
EXPERIMENTS: COMPLETE
REPORT: COMPLETE
LATEX COMPILATION: PASS
FINAL AUDIT: PASS
GIT: INITIALIZED LOCALLY
INITIAL COMMIT: COMPLETE
GITHUB: NOT YET PUSHED

IMPLEMENTATION: COMPLETE
DATASET: COMPLETE
MODEL A: COMPLETE
MODEL B: COMPLETE
OPTIMIZER EXPERIMENTS: COMPLETE
CUSTOM MODEL EVALUATION: COMPLETE
PRETRAINED MODELS: COMPLETE
FINAL COMPARISON: COMPLETE
LATEX REPORT: COMPLETE
FINAL PDF: COMPLETE
GITHUB PREPARATION: COMPLETE
GITHUB REPOSITORY: WAITING FOR REMOTE URL
TEAM CONTRIBUTIONS: WAITING FOR MEMBERS
FINAL PUSH: WAITING

## Current Milestone

The EN3150 Assignment 03 implementation, experiments, final audit, LaTeX report, and GitHub preparation documents are complete. Git has been initialized locally on the `main` branch. No GitHub remote has been added, and nothing has been pushed.

## Completed Work

- Installed project dependencies in `.venv`.
- Downloaded the official UCI DeFungi archive from `https://archive.ics.uci.edu/static/public/773/defungi.zip`.
- Extracted the dataset under `data/raw/defungi/`.
- Generated deterministic processed splits:
  - `data/processed/splits.csv`
  - `data/processed/train.csv`
  - `data/processed/validation.csv`
  - `data/processed/test.csv`
- Verified environment, dataset statistics, split integrity, and custom pipeline behavior.
- Verified custom CNN parameter counts and model summaries.
- Ran smoke tests for Model A and Model B; both passed.
- Ran a controlled optimizer comparison; Adam was selected.
- Trained and evaluated four models for 20 epochs each:
  - Model A with Adam
  - Model B with Adam
  - MobileNetV2 transfer model
  - EfficientNetB0 transfer model
- Saved metrics JSON, history CSV, history plot, confusion matrix, and model file for each trained model.
- Cleaned `report/report_data.md` using saved outputs only.
- Copied report-ready figures under `report/figures/`.
- Created final LaTeX report source under `report/main.tex`, `report/references.bib`, and `report/sections/`.
- Compiled final report PDF at `report/main.pdf`.
- Created final compliance audit at `FINAL_AUDIT.md`.
- Created GitHub preparation files: `.gitignore`, `data/README.md`, `GITHUB_FILE_AUDIT.md`, `MEMBER_FILES.md`, `GITHUB_WORKFLOW.md`, `COLLABORATOR_SETUP.md`, and `MEMBER_GIT_INSTRUCTIONS.md`.
- Initialized Git locally on the `main` branch without creating a remote or pushing.

## Verified Environment

- Python: 3.12.3
- TensorFlow: 2.21.0
- NumPy: 2.5.3
- pandas: 3.0.6
- matplotlib: 3.11.2
- scikit-learn: 1.9.1
- Pillow: 12.3.0
- GPU available: false

## Verified Dataset

- Dataset: DeFungi, UCI Machine Learning Repository.
- Total usable images: 9,114
- Classes: H1, H2, H3, H5, H6
- Images per class:
  - H1: 4,404
  - H2: 2,334
  - H3: 819
  - H5: 818
  - H6: 739
- Split counts:
  - Train: 6,379
  - Validation: 1,367
  - Test: 1,368
- Image format/mode/dimensions:
  - JPEG: 9,114
  - RGB: 9,114
  - 500x500: 9,114
- Unreadable images: 0
- Duplicate paths in split file: 0

## Verified Model Results

| Model | Total parameters | Trainable parameters | Mean epoch time (s) | Test accuracy | Macro precision | Macro recall | Macro F1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Model A, Adam | 101,829 | 101,829 | 12.8958 | 0.695906432748538 | 0.7057296614536502 | 0.6647908943697292 | 0.6749622895035646 |
| Model B, Adam | 14,272 | 14,272 | 7.8730 | 0.6483918128654971 | 0.6430123008645605 | 0.6202374219855493 | 0.6209343583512273 |
| MobileNetV2 transfer | 2,264,389 | 6,405 | 100.5135 | 0.7426900584795322 | 0.7981119904272388 | 0.7419555816682123 | 0.766795935240905 |
| EfficientNetB0 transfer | 4,055,976 | 6,405 | 158.3490 | 0.7726608187134503 | 0.8226531718072583 | 0.7653911731210724 | 0.7825692545633167 |

## Model Size And Parameters

- Model A:
  - Trainable parameters: 101,829
  - Estimated FP32 parameter storage: 397.77 KB
- Model B:
  - Trainable parameters: 14,272
  - Parameter limit: <= 100,000
  - Estimated FP32 parameter storage: 55.75 KB
- MobileNetV2 transfer:
  - Total parameters: 2,264,389
  - Trainable parameters: 6,405
  - Saved model size: 9.25 MB
  - Transfer strategy: ImageNet backbone frozen; new five-class Dense head trained.
- EfficientNetB0 transfer:
  - Total parameters: 4,055,976
  - Trainable parameters: 6,405
  - Saved model size: 16.33 MB
  - Transfer strategy: ImageNet backbone frozen; new five-class Dense head trained.

## Optimizer Experiment

- Selected optimizer: Adam
- Selection basis: lowest final validation loss in the controlled limited-training-batch comparison using the full validation split.
- Adam final validation loss: 1.2508898973464966
- SGD final validation loss: 1.4039305448532104
- SGD with momentum final validation loss: 1.3384947776794434
- These optimizer-comparison metrics are not final model results.

## Final Report Artifacts

- Final audit: `FINAL_AUDIT.md`
- Report data: `report/report_data.md`
- LaTeX entry point: `report/main.tex`
- Bibliography: `report/references.bib`
- Report sections:
  - `report/sections/01_introduction.tex`
  - `report/sections/02_dataset.tex`
  - `report/sections/03_model_a.tex`
  - `report/sections/04_model_b.tex`
  - `report/sections/05_optimizer.tex`
  - `report/sections/06_training_evaluation.tex`
  - `report/sections/07_pretrained_models.tex`
  - `report/sections/08_final_comparison.tex`
  - `report/sections/09_conclusion.tex`
- Final PDF: `report/main.pdf`
- Report figures: `report/figures/`

## LaTeX Verification

- Command used: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- Final result: PASS
- PDF pages: 10
- Output page size: A4
- Final log check: no LaTeX errors, no citation warnings, no undefined references, no overfull boxes.

## Remaining Work

1. Create the shared GitHub repository and provide its URL.
2. Add the GitHub remote and push the existing initial commit.
3. Invite real collaborators and continue with the workflow in `GITHUB_WORKFLOW.md` and `MEMBER_GIT_INSTRUCTIONS.md`.

## Human Action Required

- None for the completed implementation, experiments, audit, and report.
