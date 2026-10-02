# Final Assignment Audit

Status: PASS

## Source Verification

- Dataset inspected and verified: PASS.
- Usable DeFungi images: 9,114 across H1, H2, H3, H5, and H6.
- Unreadable images: 0.
- Stratified split verified: 6,379 train, 1,367 validation, 1,368 test.
- Duplicate paths across splits: 0.
- Saved metrics used as source of truth: PASS.
- Git initialization/push: NOT STARTED.

## Assignment Compliance

| Requirement | Status | Evidence |
|---|---|---|
| Dataset preparation and class distribution | PASS | `results/metrics/dataset_summary.json`, `report/figures/class_distribution.png` |
| Canonical train/validation/test split | PASS | `results/metrics/dataset_summary.json` |
| Model A standard CNN with parameter calculation | PASS | `src/models.py`, `results/metrics/model_parameter_checks.json`, `report/report_data.md` |
| Model B resource-constrained CNN under 100,000 parameters | PASS | 14,272 parameters; 55.75 KB FP32 parameter storage |
| Optimizer comparison | PASS | `results/metrics/optimizer_experiment_results.json` |
| Full custom-model training/evaluation | PASS | `model_a_adam_metrics.json`, `model_b_adam_metrics.json` |
| Precision, recall, confusion matrices | PASS | Saved metrics JSON files and copied report figures |
| MobileNetV2 transfer-learning model | PASS | `mobilenetv2_transfer_metrics.json` |
| EfficientNetB0 transfer-learning model | PASS | `efficientnetb0_transfer_metrics.json` |
| Final accuracy/memory/computational-cost comparison | PASS | `report/report_data.md`, final report tables |
| LaTeX report source created | PASS | `report/main.tex`, `report/sections/*.tex`, `report/references.bib` |

## Numerical Consistency

- Model A: 101,829 parameters; test accuracy 0.695906432748538.
- Model B: 14,272 parameters; test accuracy 0.6483918128654971.
- MobileNetV2: 2,264,389 total parameters; test accuracy 0.7426900584795322.
- EfficientNetB0: 4,055,976 total parameters; test accuracy 0.7726608187134503.
- Optimizer selection: Adam selected by lowest final validation loss, 1.2508898973464966.

Report tables round some displayed metrics to four decimal places, but all rounded values were derived from the exact saved outputs listed in `report/report_data.md`.

## Missing Items

None.
