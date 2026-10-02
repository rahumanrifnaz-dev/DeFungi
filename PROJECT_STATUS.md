# Project Status

PROJECT IMPLEMENTATION: COMPLETE
EXPERIMENTS: COMPLETE
REPORT: COMPLETE
LATEX COMPILATION: PASS
FINAL AUDIT: PASS
GIT: INITIALIZED LOCALLY
INITIAL COMMIT: COMPLETE
GITHUB: READY

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
GITHUB REPOSITORY: READY FOR REMOTE URL
TEAM CONTRIBUTIONS: WAITING FOR MEMBERS
FINAL PUSH: WAITING
SUBMISSION AUDIT: PASS
SUBMISSION PACKAGE: READY
MOODLE SUBMISSION: NOT YET DONE

## Current Milestone

The EN3150 Assignment 03 implementation, experiments, final audit, LaTeX report, GitHub preparation documents, and Moodle-ready submission package are complete. Git has been initialized locally on the `main` branch. No GitHub remote has been added, and nothing has been pushed.

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
- Trained and evaluated the two custom CNNs for 20 epochs each:
  - Model A with Adam
  - Model B with Adam
- Trained and evaluated the Session 3 transfer-learning models on the same canonical split:
  - MobileNetV2 with ImageNet weights, 64x64 input, 3 frozen-head epochs, and 8 fine-tuning epochs
  - EfficientNet-B0 with ImageNet weights, 64x64 input, 3 frozen-head epochs, and 8 fine-tuning epochs
- Saved metrics JSON, history CSV, history plot, confusion matrix, and model file for each trained model.
- Cleaned `report/report_data.md` using saved outputs only.
- Copied report-ready figures under `report/figures/`.
- Created final LaTeX report source under `report/main.tex` and `report/references.bib`.
- Compiled final report PDF at `report/main.pdf`.
- Created final compliance audit at `FINAL_AUDIT.md`.
- Created GitHub preparation files: `.gitignore`, `data/README.md`, `GITHUB_FILE_AUDIT.md`, `MEMBER_FILES.md`, `GITHUB_WORKFLOW.md`, `COLLABORATOR_SETUP.md`, and `MEMBER_GIT_INSTRUCTIONS.md`.
- Initialized Git locally on the `main` branch without creating a remote or pushing.
- Completed final submission audit in `SUBMISSION_AUDIT.md`.
- Corrected the report wording for the optimizer experiment to match the saved Model B optimizer experiment output.
- Created Moodle-ready local submission files under `submission/`, including `submission/main.pdf` and `submission/EN3150_A03_CODE_TEMP.zip`.
- Created Session 1 compatibility/evidence checkpoint in `CODEX_SESSION_STATUS.md`.
- Exported compatibility split CSVs under `data/splits/`.
- Exported engineering evidence tables under `results/tables/`.
- Exported verification JSON files under `results/verification/`.
- Completed Session 2 custom-model artifact exports without retraining.
- Exported optimizer comparison evidence to `results/tables/optimizer_comparison.csv` and `results/figures/optimizer_comparison.png`.
- Exported raw custom-model evaluation artifacts under `results/raw/model_a/` and `results/raw/model_b/`.
- Exported custom model comparison and CPU latency tables under `results/tables/`.

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
| MobileNetV2 transfer | 2,264,389 | 1,609,285 | 27.5111 | 0.6907894736842105 | 0.723171326344764 | 0.6478240370391951 | 0.6671667868906008 |
| EfficientNet-B0 transfer | 4,055,976 | 2,043,925 | 37.1727 | 0.7668128654970761 | 0.809860625155838 | 0.7855623497534866 | 0.7895498674861267 |

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
  - Trainable parameters during fine-tuning: 1,609,285
  - Saved selected model size: 22,000.13 KiB
  - Transfer strategy: 3 frozen-head epochs at LR 0.001, then 8 fine-tune epochs of the upper 20 non-BatchNorm backbone layers at LR 0.0001.
- EfficientNet-B0 transfer:
  - Total parameters: 4,055,976
  - Trainable parameters during fine-tuning: 2,043,925
  - Saved selected model size: 32,650.04 KiB
  - Transfer strategy: 3 frozen-head epochs at LR 0.001, then 8 fine-tune epochs of the upper 30 non-BatchNorm backbone layers at LR 0.0001.

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
- Final report source is consolidated in `report/main.tex`; older `report/sections/` files are retained in the workspace but are not the Session 4 report source.
- Final PDF: `report/main.pdf`
- Report figures: `report/figures/`

## Session 1 Evidence Artifacts

- Session checkpoint: `CODEX_SESSION_STATUS.md`
- Compatibility split files:
  - `data/splits/train.csv`
  - `data/splits/validation.csv`
  - `data/splits/test.csv`
- Evidence tables:
  - `results/tables/dataset_summary.csv`
  - `results/tables/model_a_architecture.csv`
  - `results/tables/model_b_architecture.csv`
  - `results/tables/depthwise_parameter_comparison.csv`
  - `results/tables/custom_model_static_resources.csv`
  - `results/tables/custom_model_macs.csv`
- Verification files:
  - `results/verification/split_verification.json`
  - `results/verification/custom_pipeline_check.json`
  - `results/verification/smoke_test_results.json`
  - `results/verification/model_parameter_checks.json`
  - `results/verification/session1_model_resource_verification.json`
  - `results/verification/session1_forward_pass_verification.json`

## Session 2 Custom Model Artifacts

- Optimizer comparison:
  - `results/tables/optimizer_comparison.csv`
  - `results/figures/optimizer_comparison.png`
- Model A raw outputs:
  - `results/raw/model_a/history.csv`
  - `results/raw/model_a/metrics.json`
  - `results/raw/model_a/classification_report.csv`
  - `results/raw/model_a/confusion_matrix.csv`
  - `results/raw/model_a/test_predictions.csv`
  - `results/raw/model_a/model_a_selected.keras`
- Model B raw outputs:
  - `results/raw/model_b/history.csv`
  - `results/raw/model_b/metrics.json`
  - `results/raw/model_b/classification_report.csv`
  - `results/raw/model_b/confusion_matrix.csv`
  - `results/raw/model_b/test_predictions.csv`
  - `results/raw/model_b/model_b_selected.keras`
- Report-ready custom figures:
  - `results/figures/model_a_training_curves.png`
  - `results/figures/model_b_training_curves.png`
  - `results/figures/model_a_confusion_matrix_report.png`
  - `results/figures/model_b_confusion_matrix_report.png`
- Custom comparison tables:
  - `results/tables/custom_models.csv`
  - `results/tables/custom_latency.csv`
  - `results/tables/session2_interpretation_notes.md`

## Session 3 Transfer Learning Artifacts

- MobileNetV2 raw outputs:
  - `results/raw/mobilenetv2/history.csv`
  - `results/raw/mobilenetv2/metrics.json`
  - `results/raw/mobilenetv2/classification_report.csv`
  - `results/raw/mobilenetv2/confusion_matrix.csv`
  - `results/raw/mobilenetv2/test_predictions.csv`
- EfficientNet-B0 raw outputs:
  - `results/raw/efficientnetb0/history.csv`
  - `results/raw/efficientnetb0/metrics.json`
  - `results/raw/efficientnetb0/classification_report.csv`
  - `results/raw/efficientnetb0/confusion_matrix.csv`
  - `results/raw/efficientnetb0/test_predictions.csv`
- Final comparison:
  - `results/tables/pretrained_transfer_models.csv`
  - `results/tables/pretrained_transfer_macs.csv`
  - `results/tables/pretrained_transfer_latency.csv`
  - `results/tables/final_comparison.csv`
  - `results/tables/session3_transfer_tradeoff_notes.md`

## LaTeX Verification

- Command used: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- Final result: PASS
- PDF pages: 10
- Output page size: A4
- Final log check: no LaTeX errors, no citation warnings, no undefined references, no overfull boxes.

## Remaining Work

1. Rename the temporary submission files using the lecturer's required group-number convention before Moodle upload.
2. Upload to Moodle manually and reopen the uploaded files to verify integrity.
3. Create the shared GitHub repository and provide its URL when ready to push.

## Human Action Required

- None for the completed implementation, experiments, audit, and report.
