# Member File Responsibilities

This file maps the real assignment responsibilities to actual project files. It is a planning guide for authentic commits by each member using their own Git identity.

## RIFNAZ.K.R.M -- 230550P

Responsible for:

- Dataset preparation files
- Canonical split generation
- Model A files
- Corresponding report section

Actual files:

- `src/data_prepare.py`
- `src/datasets.py`
- `src/config.py`
- `src/models.py`
- `data/processed/splits.csv`
- `data/processed/train.csv`
- `data/processed/validation.csv`
- `data/processed/test.csv`
- `results/metrics/dataset_summary.json`
- `results/metrics/model_parameter_checks.json`
- `results/metrics/model_a_summary.txt`
- `report/sections/02_dataset.tex`
- `report/sections/03_model_a.tex`
- `report/figures/class_distribution.png`

## PANUHARAN.S -- 230462X

Responsible for:

- Model B files
- Depthwise-separable analysis
- Parameter/storage calculations
- Corresponding report section

Actual files:

- `src/models.py`
- `src/model_checks.py`
- `results/metrics/model_parameter_checks.json`
- `results/metrics/model_b_summary.txt`
- `results/metrics/model_b_adam_metrics.json`
- `results/metrics/model_b_adam_history.csv`
- `results/figures/model_b_adam_history.png`
- `results/confusion_matrices/model_b_adam_confusion_matrix.png`
- `report/sections/04_model_b.tex`
- `report/figures/model_b_history.png`
- `report/figures/model_b_confusion_matrix.png`

## PERANAVAN.K -- 230474K

Responsible for:

- Optimizer experiments
- Custom-model training
- Evaluation
- Metrics
- Confusion matrices
- Model A/B comparison
- Corresponding report section

Actual files:

- `src/optimizer_experiment.py`
- `src/train_custom.py`
- `src/utils.py`
- `src/smoke_test.py`
- `src/verify_pipeline.py`
- `results/metrics/optimizer_experiment_results.json`
- `results/metrics/model_a_adam_metrics.json`
- `results/metrics/model_b_adam_metrics.json`
- `results/metrics/model_a_adam_history.csv`
- `results/metrics/model_b_adam_history.csv`
- `results/figures/model_a_adam_history.png`
- `results/figures/model_b_adam_history.png`
- `results/confusion_matrices/model_a_adam_confusion_matrix.png`
- `results/confusion_matrices/model_b_adam_confusion_matrix.png`
- `report/sections/05_optimizer.tex`
- `report/sections/06_training_evaluation.tex`
- `report/figures/model_a_history.png`
- `report/figures/model_a_confusion_matrix.png`
- `report/figures/model_b_history.png`
- `report/figures/model_b_confusion_matrix.png`

## LAVANATHAN.J -- 230371R

Responsible for:

- MobileNetV2
- EfficientNetB0
- Pretrained evaluation
- Final trade-off comparison
- Corresponding report section

Actual files:

- `src/train_pretrained.py`
- `results/metrics/mobilenetv2_transfer_metrics.json`
- `results/metrics/efficientnetb0_transfer_metrics.json`
- `results/metrics/mobilenetv2_transfer_history.csv`
- `results/metrics/efficientnetb0_transfer_history.csv`
- `results/figures/mobilenetv2_transfer_history.png`
- `results/figures/efficientnetb0_transfer_history.png`
- `results/confusion_matrices/mobilenetv2_transfer_confusion_matrix.png`
- `results/confusion_matrices/efficientnetb0_transfer_confusion_matrix.png`
- `report/sections/07_pretrained_models.tex`
- `report/sections/08_final_comparison.tex`
- `report/figures/mobilenetv2_history.png`
- `report/figures/mobilenetv2_confusion_matrix.png`
- `report/figures/efficientnetb0_history.png`
- `report/figures/efficientnetb0_confusion_matrix.png`

## Shared Final Documentation

Actual files:

- `README.md`
- `requirements.txt`
- `.gitignore`
- `PROJECT_STATUS.md`
- `FINAL_AUDIT.md`
- `report_data.md`
- `report/report_data.md`
- `report/main.tex`
- `report/references.bib`
- `report/main.pdf`
- `report/sections/01_introduction.tex`
- `report/sections/09_conclusion.tex`
- `GITHUB_FILE_AUDIT.md`
- `GITHUB_WORKFLOW.md`
