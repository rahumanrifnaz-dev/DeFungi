# Final Rubric Audit

This audit maps the completed DeFungi project evidence to the EN3150 Assignment 03 marking sections. It does not assign marks; it records coverage and remaining risk.

| Section | Max Marks | Requirement | Evidence | Status | Remaining Risk |
|---|---:|---|---|---|---|
| Custom Architecture Design | 20 | Model A standard Conv2D CNN with pooling, parameters, shapes, activation justification | `src/models.py`, `results/tables/model_a_architecture.csv`, `report/main.tex` | COMPLETE | None beyond normal grading judgment |
| Custom Architecture Design | 20 | Model B depthwise-separable CNN under 100,000 trainable parameters | `src/models.py`, `results/tables/model_b_architecture.csv`, Model B assert/checks, 14,272 parameters | COMPLETE | None |
| Custom Architecture Design | 20 | Parameter formulas and layer-wise calculations | `results/tables/depthwise_parameter_comparison.csv`, `report/main.tex` | COMPLETE | None |
| Optimizer Selection & Tuning | 15 | Compare SGD, SGD with momentum, and Adam with recorded LR/momentum | `results/tables/optimizer_comparison.csv`, `results/metrics/optimizer_experiment_results.json` | COMPLETE | Pilot uses limited batches, documented as optimizer-selection evidence |
| Optimizer Selection & Tuning | 15 | Explain momentum and measured validation behavior | `report/main.tex` optimizer section | COMPLETE | None |
| Custom Model Training & Evaluation | 25 | Model A and Model B trained for at least 20 epochs | `results/raw/model_a/history.csv`, `results/raw/model_b/history.csv` | COMPLETE | None |
| Custom Model Training & Evaluation | 25 | Training/validation curves, test metrics, precision, recall, confusion matrices | `results/figures/`, `results/raw/model_a/`, `results/raw/model_b/`, `report/figures/` | COMPLETE | None |
| Custom Model Training & Evaluation | 25 | Model A vs Model B resource comparison | `results/tables/custom_models.csv`, `results/tables/custom_latency.csv`, `results/tables/custom_model_macs.csv` | COMPLETE | None |
| SOTA Fine-Tuning & Evaluation | 20 | Two lightweight pretrained models: MobileNetV2 and EfficientNet-B0 | `src/session3_transfer.py`, `results/raw/mobilenetv2/`, `results/raw/efficientnetb0/` | COMPLETE | 64x64 input is smaller than standard ImageNet practice, documented |
| SOTA Fine-Tuning & Evaluation | 20 | Same split membership, transfer strategy, test metrics, parameters, model size | `data/splits/`, `results/tables/pretrained_transfer_models.csv`, `results/tables/pretrained_transfer_latency.csv` | COMPLETE | None |
| Final Comparison & Discussion | 20 | Model B vs MobileNetV2 vs EfficientNet-B0 and all-four final table | `results/tables/final_comparison.csv`, `report/main.tex` | COMPLETE | None |
| Final Comparison & Discussion | 20 | Accuracy, memory footprint, computational cost, limitations, error analysis | `report/main.tex`, `results/tables/session3_transfer_tradeoff_notes.md` | COMPLETE | No physical edge-device energy measurement; documented limitation |

## Key Verification Results

- Dataset: 9,114 usable DeFungi images across H1, H2, H3, H5, and H6.
- Split: train 6,379; validation 1,367; test 1,368; no overlap in saved split metadata.
- Model A: 101,829 parameters; test accuracy 0.695906432748538.
- Model B: 14,272 parameters; test accuracy 0.6483918128654971.
- MobileNetV2: 2,264,389 parameters; test accuracy 0.6907894736842105.
- EfficientNet-B0: 4,055,976 parameters; test accuracy 0.7668128654970761.
- Final report: `RandomGuess_A03_EN3150.pdf` and `report/main.pdf`.
- Self-contained notebook: `RandomGuess_A03_EN3150.ipynb`.

## Overall Status

PROJECT STATUS: COMPLETE

Remaining human action: authenticate GitHub locally and push if the repository must be synchronized remotely.
