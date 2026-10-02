# Submission Audit

Status: PASS

This audit was performed for the final Moodle preparation phase. No model retraining was performed and no verified experiment result files were modified.

## Assignment Requirement Checklist

| Area | Requirement | Status | Evidence |
|---|---|---|---|
| Dataset | Image dataset used | PASS | DeFungi images verified in `results/metrics/dataset_summary.json`. |
| Dataset | Not CIFAR-10 | PASS | README/report identify DeFungi only. |
| Dataset | DeFungi dataset | PASS | UCI DeFungi source documented in README, report, and `data/README.md`. |
| Dataset | Images resized to maximum 64x64 for custom Models A/B | PASS | `src/datasets.py`, `src/config.py`, report dataset section. |
| Dataset | Train split approximately 70% | PASS | 6,379 of 9,114 images. |
| Dataset | Validation split approximately 15% | PASS | 1,367 of 9,114 images. |
| Dataset | Test split approximately 15% | PASS | 1,368 of 9,114 images. |
| Dataset | One reproducible canonical split | PASS | `data/processed/*.csv`, seed 42. |
| Dataset | Same sample membership reused across relevant models | PASS | Custom and pretrained datasets load from the same split CSVs. |
| Model A | Standard Conv2D layers | PASS | `src/models.py`, `report/sections/03_model_a.tex`. |
| Model A | MaxPooling used | PASS | `src/models.py`, Model A architecture table. |
| Model A | Kernel sizes stated | PASS | Model A table and parameter calculation. |
| Model A | Filter numbers stated | PASS | Model A table. |
| Model A | Dense units stated | PASS | Model A table. |
| Model A | Trainable parameters calculated | PASS | 101,829 in report and metrics. |
| Model A | Hardware-aware activation justification included | PASS | ReLU/Softmax/GAP discussion in report. |
| Model B | Depthwise separable convolution used | PASS | `SeparableConv2D` in `src/models.py`. |
| Model B | Parameter calculation included | PASS | `report/sections/04_model_b.tex`. |
| Model B | Total trainable parameters <= 100,000 | PASS | 14,272 parameters. |
| Model B | Efficiency explanation included | PASS | Model B and final comparison report sections. |
| Optimizer | Chosen optimizer stated | PASS | Adam. |
| Optimizer | Learning rate stated | PASS | 0.001. |
| Optimizer | Reason stated | PASS | Lowest final validation loss. |
| Optimizer | Compared with standard SGD | PASS | Optimizer table. |
| Optimizer | Compared with SGD + Momentum | PASS | Optimizer table. |
| Optimizer | Momentum explained | PASS | Momentum equations in report. |
| Training | Model A trained at least 20 epochs | PASS | Saved `model_a_adam_metrics.json`. |
| Training | Model B trained at least 20 epochs | PASS | Saved `model_b_adam_metrics.json`. |
| Training | Training loss recorded | PASS | History CSV/JSON files and plots. |
| Training | Validation loss recorded | PASS | History CSV/JSON files and plots. |
| Training | Loss plots included | PASS | `results/figures/` and `report/figures/`. |
| Evaluation | Test accuracy Model A | PASS | 0.695906432748538. |
| Evaluation | Test accuracy Model B | PASS | 0.6483918128654971. |
| Evaluation | Confusion matrix Model A | PASS | Metrics JSON and figure. |
| Evaluation | Confusion matrix Model B | PASS | Metrics JSON and figure. |
| Evaluation | Precision | PASS | Macro precision reported for all models. |
| Evaluation | Recall | PASS | Macro recall reported for all models. |
| Model A vs B | Trainable parameters | PASS | Comparison table. |
| Model A vs B | Estimated model size KB | PASS | 397.77 KB and 55.75 KB. |
| Model A vs B | Training time per epoch | PASS | 12.8958 s and 7.8730 s. |
| Model A vs B | Test accuracy | PASS | Comparison table. |
| Model A vs B | Trade-off discussion | PASS | Training/evaluation section. |
| Pretrained | Two models used | PASS | MobileNetV2 and EfficientNet-B0. |
| Pretrained | MobileNetV2 | PASS | Source, metrics, figure, report section. |
| Pretrained | EfficientNet-B0 | PASS | Source, metrics, figure, report section. |
| Pretrained | Same underlying dataset split membership | PASS | Pretrained loader uses split CSVs. |
| Pretrained | Fine-tuning/transfer-learning method explained | PASS | Frozen ImageNet backbone and new head described. |
| Pretrained | Test metrics reported | PASS | Accuracy, precision, recall, F1. |
| Pretrained | Total parameters reported | PASS | MobileNetV2 2,264,389; EfficientNet-B0 4,055,976. |
| Pretrained | Serialized model sizes reported | PASS | 22,000.13 KiB and 32,650.04 KiB. |
| Final comparison | Model B compared with pretrained models | PASS | Final comparison table. |
| Final comparison | Accuracy discussed | PASS | Final comparison section. |
| Final comparison | Memory footprint discussed | PASS | Final comparison section. |
| Final comparison | Computational cost discussed | PASS | Epoch-time indicator included. |
| Report | All four names/index numbers present | PASS | Title page and contributions table. |
| Report | All required sections present | PASS | `report/sections/`. |
| Report | Figures referenced correctly | PASS | Final LaTeX build and PDF image list. |
| Report | Tables readable | PASS | No overfull table warnings in final log scan. |
| Report | References present | PASS | Bibliography appears in PDF text. |
| Report | No fake values | PASS | Values cross-checked against saved metrics. |
| Report | No placeholders | PASS | Placeholder scan found only legitimate LaTeX `tabularx` column specifier. |
| Report | Final PDF compiles | PASS | `latexmk` completed successfully. |
| Code | Complete | PASS | Source files for all stages present. |
| Code | Commented | PASS | Important utilities and reports are understandable; no large refactor needed. |
| Code | Runnable | PASS | Import checks, help commands, compileall, and split loading passed. |
| Code | File paths portable | PASS | Project-relative paths used; no machine-specific absolute paths found. |
| Code | Sensitive-value scan | PASS | Credential-like pattern scan passed. |
| Code | No missing imports | PASS | `python -m src.verify_imports` passed. |

## Numerical Consistency

All final report values were cross-checked against `results/metrics/*.json`, `data/processed/*.csv`, and the verified report data files.

- Dataset total: 9,114.
- Class counts: H1 4,404; H2 2,334; H3 819; H5 818; H6 739.
- Split counts: train 6,379; validation 1,367; test 1,368.
- Model A: 101,829 parameters; 397.77 KB; 12.8958 s/epoch; accuracy 0.695906432748538; macro precision 0.7057296614536502; macro recall 0.6647908943697292.
- Model B: 14,272 parameters; 55.75 KB; 7.8730 s/epoch; accuracy 0.6483918128654971; macro precision 0.6430123008645605; macro recall 0.6202374219855493.
- MobileNetV2: 2,264,389 total parameters; 22,000.13 KiB serialized selected model; 27.5111 s/epoch; accuracy 0.6907894736842105; macro precision 0.723171326344764; macro recall 0.6478240370391951.
- EfficientNet-B0: 4,055,976 total parameters; 32,650.04 KiB serialized selected model; 37.1727 s/epoch; accuracy 0.7668128654970761; macro precision 0.809860625155838; macro recall 0.7855623497534866.

One genuine inconsistency was fixed: the optimizer experiment was incorrectly described as using Model A in `report_data.md` and `report/sections/05_optimizer.tex`. The saved optimizer experiment uses Model B, so only those report-source occurrences were corrected and `report/main.pdf` was rebuilt.

## Placeholder / TODO Search

Search terms checked: TODO, TBD, PLACEHOLDER, INSERT, FIXME, XXX, your name, group number here, add figure, add result, example value, dummy, temporary debugging, and `print("test")`.

Result: PASS. The only hit was the legitimate LaTeX `tabularx` column specification `lXXX`; no unfinished placeholder was found.

## Plagiarism-Risk Review

Status: PASS.

The report text was reviewed for long copied passages, copied abstracts, copied documentation wording, citation-free borrowed technical explanations, and placeholder-like generic text. No long copied passage was found. External ideas for DeFungi, MobileNetV2, and EfficientNet-B0 are cited in the report.

## Code Quality Check

Status: PASS.

- Function names are meaningful.
- Random seed is centralized in `src/config.py`.
- Paths are project-relative.
- Datasets use the canonical split CSVs.
- No accidental split overlap was found.
- No credential-like patterns were found.
- No expensive retraining was run during this audit.

## Reproducibility Checks

| Check | Status |
|---|---|
| `python -m src.verify_imports` | PASS |
| `python -m src.verify_environment` | PASS |
| `python -m src.train_custom --help` | PASS |
| `python -m src.train_pretrained --help` | PASS |
| `python -m src.optimizer_experiment --help` | PASS |
| `python -m compileall -q src` | PASS |
| Canonical split loading and overlap check | PASS |
| Final LaTeX build | PASS |

## PDF Final Check

Status: PASS.

- `report/main.pdf` exists.
- PDF is 14 A4 pages.
- Title page contains the university, department, assignment, title, and all four students.
- Figures are embedded.
- References are present.
- No undefined references/citations or missing images were found in the final log scan.

## Warnings / Human Actions

- WARNING: No verified group number was found in the project. A rename reminder is included at `submission/RENAME_BEFORE_UPLOAD.txt`.
- Moodle upload is not done and must be completed by a real group member.
