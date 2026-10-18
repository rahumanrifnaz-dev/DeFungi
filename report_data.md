# Verified Report Data

This file summarizes the verified artifacts used by the final EN3150 Assignment 03 report. It is based on saved DeFungi results only; no model retraining is required to read or use these values.

## Dataset

- Dataset: DeFungi, UCI Machine Learning Repository.
- Official source: <https://archive.ics.uci.edu/dataset/773/defungi>
- Usable images: 9,114.
- Classes: H1, H2, H3, H5, H6.
- Verified image format: RGB JPEG, 500 x 500 pixels.
- Canonical split seed: 42.
- Split counts: train 6,379; validation 1,367; test 1,368.
- Split evidence: `data/processed/*.csv`, `data/splits/*.csv`, `results/verification/split_verification.json`.

## Class Counts

| Class | Total | Train | Validation | Test |
|---|---:|---:|---:|---:|
| H1 | 4,404 | 3,082 | 661 | 661 |
| H2 | 2,334 | 1,634 | 350 | 350 |
| H3 | 819 | 573 | 123 | 123 |
| H5 | 818 | 573 | 122 | 123 |
| H6 | 739 | 517 | 111 | 111 |

## Custom Models

| Model | Parameters | Serialized size (KiB) | Mean epoch time (s) | Test accuracy | Macro precision | Macro recall | Macro F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Model A | 101,829 | 1,241.37 | 12.8958 | 0.695906432748538 | 0.7057296614536502 | 0.6647908943697292 | 0.6749622895035646 |
| Model B | 14,272 | 219.41 | 7.8730 | 0.6483918128654971 | 0.6430123008645605 | 0.6202374219855493 | 0.6209343583512273 |

Custom evidence:

- `results/raw/model_a/`
- `results/raw/model_b/`
- `results/tables/custom_models.csv`
- `results/tables/custom_latency.csv`
- `results/tables/custom_model_macs.csv`

## Optimizer Selection

The controlled optimizer pilot used Model B for five epochs with 30 training batches per epoch and the full validation split. Adam was selected by lowest final validation loss.

| Optimizer | Learning rate | Momentum | Final validation loss | Final validation accuracy |
|---|---:|---:|---:|---:|
| Adam | 0.001 | 0.0 | 1.2508898973464966 | 0.509144127368927 |
| SGD | 0.010 | 0.0 | 1.4039305448532104 | 0.4835405945777893 |
| SGD + momentum | 0.010 | 0.9 | 1.3384947776794434 | 0.4835405945777893 |

Evidence: `results/tables/optimizer_comparison.csv`.

## Transfer Learning

The final transfer-learning comparison uses Session 3 artifacts, not the earlier frozen-head run. Both pretrained models used ImageNet weights, 64 x 64 input, the canonical split membership, a five-class DeFungi head, validation-loss checkpoint selection, and no test-set model selection.

| Model | Input | Head epochs | Fine-tune epochs | Head LR | Fine-tune LR |
|---|---|---:|---:|---:|---:|
| MobileNetV2 | 64 x 64 | 3 | 8 | 0.001 | 0.0001 |
| EfficientNet-B0 | 64 x 64 | 3 | 8 | 0.001 | 0.0001 |

## Transfer-Learning Results

| Model | Parameters | Trainable during fine-tuning | Serialized size (KiB) | Mean epoch time (s) | Test accuracy | Macro precision | Macro recall | Macro F1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| MobileNetV2 | 2,264,389 | 1,609,285 | 22,000.13 | 27.5111 | 0.6907894736842105 | 0.723171326344764 | 0.6478240370391951 | 0.6671667868906008 |
| EfficientNet-B0 | 4,055,976 | 2,043,925 | 32,650.04 | 37.1727 | 0.7668128654970761 | 0.809860625155838 | 0.7855623497534866 | 0.7895498674861267 |

Evidence:

- `results/raw/mobilenetv2/`
- `results/raw/efficientnetb0/`
- `results/tables/pretrained_transfer_models.csv`
- `results/tables/pretrained_transfer_macs.csv`
- `results/tables/pretrained_transfer_latency.csv`

## Final Comparison

| Model | Parameters | Serialized size (KiB) | MACs | CPU mean latency (ms) | CPU p95 latency (ms) | Test accuracy | Macro precision | Macro recall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Model A | 101,829 | 1,241.37 | 41,296,192 | 2.8241097353748046 | 3.2042405051470264 | 0.695906432748538 | 0.7057296614536502 | 0.6647908943697292 |
| Model B | 14,272 | 219.41 | 4,621,040 | 1.592217214492848 | 2.265584255655994 | 0.6483918128654971 | 0.6430123008645605 | 0.6202374219855493 |
| MobileNetV2 | 2,264,389 | 22,000.13 | 24,454,912 | 170.10653118071787 | 198.20382995167165 | 0.6907894736842105 | 0.723171326344764 | 0.6478240370391951 |
| EfficientNet-B0 | 4,055,976 | 32,650.04 | 31,972,992 | 322.2855200798949 | 357.6918174076127 | 0.7668128654970761 | 0.809860625155838 | 0.7855623497534866 |

Evidence: `results/tables/final_comparison.csv`.

## Report Artifacts

- Final LaTeX source: `report/main.tex`.
- Bibliography: `report/references.bib`.
- Final PDF: `report/main.pdf`.
- Report figures: `report/figures/`.
