# Report Synthesis Notes

This file is a concise synthesis from verified saved outputs. It is not the final LaTeX report.

## Dataset And Split

- Dataset: UCI DeFungi image dataset.
- Usable images: 9,114.
- Classes: H1, H2, H3, H5, H6.
- Class counts:
  - H1: 4,404
  - H2: 2,334
  - H3: 819
  - H5: 818
  - H6: 739
- Split counts:
  - Train: 6,379
  - Validation: 1,367
  - Test: 1,368
- Split verification:
  - Split rows: 9,114
  - Unique split paths: 9,114
  - Duplicate split paths: 0
  - Missing split files: 0
  - Unreadable images: 0
- All inspected images are JPEG, RGB, and 500x500.

## Models Compared

| Model | Epochs | Trainable parameters | Mean epoch time (s) | Test accuracy | Macro precision | Macro recall | Macro F1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Model A, Adam | 20 | 101,829 | 12.8958 | 0.695906432748538 | 0.7057296614536502 | 0.6647908943697292 | 0.6749622895035646 |
| Model B, Adam | 20 | 14,272 | 7.873 | 0.6483918128654971 | 0.6430123008645605 | 0.6202374219855493 | 0.6209343583512273 |
| MobileNetV2 transfer | 20 | 6,405 | 100.5135 | 0.7426900584795322 | 0.7981119904272388 | 0.7419555816682123 | 0.766795935240905 |
| EfficientNetB0 transfer | 20 | 6,405 | 158.349 | 0.7726608187134503 | 0.8226531718072583 | 0.7653911731210724 | 0.7825692545633167 |

## Main Observations

- EfficientNetB0 transfer learning produced the best final test accuracy and macro F1.
- MobileNetV2 also outperformed both custom CNNs, while requiring only 6,405 trainable parameters because the ImageNet backbone was frozen.
- Model A performed better than the lightweight Model B on accuracy and macro F1, but Model B trained faster and used far fewer parameters.
- Model B satisfies the lightweight custom-model constraint with 14,272 trainable parameters.
- Transfer learning improved predictive performance but greatly increased CPU training time per epoch.

## Optimizer Selection

- The controlled optimizer experiment selected Adam for Model B.
- Selection basis: lowest final validation loss in the controlled limited-training-batch comparison using the full validation split.
- Final validation losses in that comparison:
  - Adam: 1.2508898973464966
  - SGD: 1.4039305448532104
  - SGD with momentum: 1.3384947776794434

## Evidence Files

- Full generated evidence: `report/report_data.md`
- Dataset summary: `results/metrics/dataset_summary.json`
- Model metrics:
  - `results/metrics/model_a_adam_metrics.json`
  - `results/metrics/model_b_adam_metrics.json`
  - `results/metrics/mobilenetv2_transfer_metrics.json`
  - `results/metrics/efficientnetb0_transfer_metrics.json`
- Figures and confusion matrices are under:
  - `results/figures/`
  - `results/confusion_matrices/`
