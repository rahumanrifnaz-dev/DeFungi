# EN3150 Assignment 03 — Project Status

> **Implementation and report: complete according to recorded workspace checks.** This status has been reconciled with the uploaded final report `RandomGuess_A03_EN3150.pdf`. GitHub publishing and Moodle upload remain **unverified** here.

## Status at a Glance

| Area | Status | Evidence / qualification |
|---|---|---|
| Dataset preparation | Complete | 9,114 DeFungi images, five classes, stratified split |
| Model A and Model B | Complete | Both trained for 20 epochs and evaluated |
| Optimizer comparison | Complete | Adam selected using controlled pilot validation loss |
| Pretrained models | Complete | MobileNetV2 and EfficientNet-B0, two-stage transfer learning |
| Final comparison | Complete | Accuracy, parameter count, serialized size, MACs and CPU latency |
| Report | Complete | Uploaded 14-page PDF with figures, tables, references and appendices |
| Local verification | Previously passed | Recorded environment, import, pipeline, model and LaTeX checks |
| GitHub remote | Not independently verified | Previous status reports configured `origin` and blocked HTTPS push |
| Moodle submission | Not verified | Manual submission and filename check still required |

## Final Report Reference

- **Report title:** Resource-Constrained CNN Design and Transfer Learning for DeFungi Image Classification
- **Course:** EN3150 — Assignment 03, University of Moratuwa, Department of Electronic and Telecommunication Engineering
- **Submission PDF:** [`RandomGuess_A03_EN3150.pdf`](RandomGuess_A03_EN3150.pdf)
- **Report structure:** Introduction; Dataset and Data Preparation; Custom CNN Architectures; Optimizer Selection and Tuning; Custom CNN Training and Evaluation; Lightweight State-of-the-Art Models; Final Comparison; Discussion; Conclusion; References; and Appendices A–B.
- **Group:** Lavanathan.J (230371R), Panuharan.S (230462X), Peranavan.K (230474K), Rifnaz.K.R.M (230550P).

## Key Findings from the Final PDF

| Model | Parameters | Test accuracy | Serialized size (KiB) | MACs | Mean CPU batch-1 latency (ms) |
|---|---:|---:|---:|---:|---:|
| Model A | 101,829 | 69.59% | 1,241.37 | 41,296,192 | 2.8241 |
| Model B | 14,272 | 64.84% | 219.41 | 4,621,040 | 1.5922 |
| MobileNetV2 | 2,264,389 | 69.08% | 22,000.13 | 24,454,912 | 170.1065 |
| EfficientNet-B0 | 4,055,976 | 76.68% | 32,650.04 | 31,972,992 | 322.2855 |

- **Best measured accuracy:** EfficientNet-B0 (76.68%).
- **Smallest measured resource footprint:** Model B, with 14,272 parameters and the lowest included MAC estimate and measured CPU latency.
- **Model B versus Model A:** 85.98% fewer parameters, 82.33% smaller serialized model, 88.81% fewer included MACs, and 43.62% lower mean CPU latency; test accuracy decreases by approximately 4.75 percentage points.
- **Dataset:** H1 (4,404), H2 (2,334), H3 (819), H5 (818), H6 (739); training 6,379, validation 1,367, test 1,368; input resolution 64×64.
- **Training:** Adam (learning rate 0.001) for custom CNNs; pretrained models used three classifier-head epochs and eight fine-tuning epochs (learning rates 0.001 and 0.0001).
- **Interpretation:** The report does not establish physical edge-device energy consumption or microcontroller latency. Reported CPU latency comes from the tested computer.

## Current Milestone

The uploaded final report documents completed custom-model experiments, optimizer selection, two transfer-learning baselines, and a four-model resource comparison. The existing workspace status records successful local checks and a completed LaTeX build. This update aligns the summary and page count with the **uploaded final PDF**, while leaving external publishing and submission status explicitly unconfirmed.

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
- Initialized Git locally on the `main` branch; the previous status records a configured remote, but successful publishing has not been independently verified.
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
- Current uploaded submission PDF pages: **14** (cover, contents, abstract, 11 numbered report pages plus appendix content). The older 10-page count in the workspace status is superseded for this uploaded PDF.
- Output page size: A4
- Final log check: no LaTeX errors, no citation warnings, no undefined references, no overfull boxes.

## Remaining Work

1. Rename the temporary submission files using the lecturer's required group-number convention before Moodle upload.
2. Upload to Moodle manually and reopen the uploaded files to verify integrity.
3. Verify that the existing GitHub remote has received the intended commits and that README links and report artifacts display correctly; the uploaded PDF does not establish remote push status.

## Human Action Required

- Confirm GitHub push/publication and Moodle submission outside this local review.
- Confirm the group-number filename convention required by the lecturer before upload.
