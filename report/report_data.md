# Verified Report Data

This is the report-local copy of the verified DeFungi result summary. The top-level `report_data.md` contains the same evidence summary for GitHub review.

## Source of Truth

- Dataset and split: `../data/processed/*.csv`, `../data/splits/*.csv`, `../results/verification/split_verification.json`.
- Custom model evidence: `../results/raw/model_a/`, `../results/raw/model_b/`, `../results/tables/custom_models.csv`.
- Transfer-learning evidence: `../results/raw/mobilenetv2/`, `../results/raw/efficientnetb0/`, `../results/tables/pretrained_transfer_models.csv`.
- Final comparison: `../results/tables/final_comparison.csv`.
- Final report: `main.tex`, `references.bib`, `main.pdf`.

## Key Verified Values

| Item | Value |
|---|---:|
| Total usable images | 9,114 |
| Train images | 6,379 |
| Validation images | 1,367 |
| Test images | 1,368 |
| Model A test accuracy | 0.695906432748538 |
| Model B test accuracy | 0.6483918128654971 |
| MobileNetV2 test accuracy | 0.6907894736842105 |
| EfficientNet-B0 test accuracy | 0.7668128654970761 |
| Model B parameters | 14,272 |
| Model B serialized size | 219.41 KiB |

## Final Comparison

| Model | Parameters | Serialized size (KiB) | MACs | CPU mean latency (ms) | Test accuracy |
|---|---:|---:|---:|---:|---:|
| Model A | 101,829 | 1,241.37 | 41,296,192 | 2.8241097353748046 | 0.695906432748538 |
| Model B | 14,272 | 219.41 | 4,621,040 | 1.592217214492848 | 0.6483918128654971 |
| MobileNetV2 | 2,264,389 | 22,000.13 | 24,454,912 | 170.10653118071787 | 0.6907894736842105 |
| EfficientNet-B0 | 4,055,976 | 32,650.04 | 31,972,992 | 322.2855200798949 | 0.7668128654970761 |

The final report uses these verified Session 3 transfer-learning values rather than the earlier frozen-head pretrained run.
