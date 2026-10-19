# Final Public Repository Audit

Repository: <https://github.com/rahumanrifnaz-dev/DeFungi>

Dataset: DeFungi

Audit date: 2026-10-02

## Summary

| Area | Status | Evidence |
|---|---|---|
| Assignment rubric | PASS | README, final report, `results/tables/`, `results/raw/`, `results/verification/` |
| Model A | PASS | Standard Conv2D CNN in `src/models.py`; 101,829 parameters |
| Model B <=100k | PASS | Depthwise-separable CNN in `src/models.py`; 14,272 parameters |
| Optimizer evidence | PASS | `results/tables/optimizer_comparison.csv`; Adam selected by lowest final validation loss |
| 20+ epoch custom training | PASS | `results/raw/model_a/history.csv`, `results/raw/model_b/history.csv` each contain 20 epochs |
| Evaluation metrics | PASS | Accuracy, macro precision, macro recall, classification reports, predictions, and confusion matrices under `results/raw/` |
| Pretrained models | PASS | MobileNetV2 and EfficientNet-B0 evidence under `results/raw/mobilenetv2/` and `results/raw/efficientnetb0/` |
| Final trade-off | PASS | `results/tables/final_comparison.csv`, report final comparison, and `results/tables/session3_transfer_tradeoff_notes.md` |
| LaTeX report | PASS | `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passes from `report/` |
| Raw data excluded | YES | No tracked `data/raw/` files; `.gitignore` excludes raw data |
| Neighbor report excluded | YES | No tracked `FeatureFour_A03_EN3150.pdf` or neighbor project content |
| Secrets | NONE | Tracked repository scan found no credential material |
| Portable paths | PASS | Tracked source/docs contain no machine-specific local paths |
| README | PASS | README identifies dataset, models, group members, setup, dataset placement, commands, results, and final report |
| Remote sync | ISSUES | Local `main` is ahead of `origin/main`; push requires GitHub authentication in the local environment |
| Final notebook | PASS | `RandomGuess_A03_EN3150.ipynb` is present, valid JSON, and self-contained without `from src` imports |
| Submission-named PDF | PASS | `RandomGuess_A03_EN3150.pdf` is present and opens as a 14-page A4 PDF |

## Detailed Checks

- Public-repository content exists locally: `README.md`, `requirements.txt`, `.gitignore`, `src/`, `data/README.md`, `data/splits/`, `results/tables/`, `results/figures/`, `results/verification/`, `report/main.tex`, `report/references.bib`, `report/sections/`, `report/figures/`, and `report/main.pdf`.
- Raw DeFungi images, dataset ZIP archives, virtual environments, Python caches, Keras checkpoints, LaTeX temporary files, submission archives, and neighbor PDFs are not tracked.
- Data preparation evidence verifies 9,114 DeFungi images across H1, H2, H3, H5, and H6 with canonical train/validation/test counts of 6,379/1,367/1,368.
- Custom input size is 64 x 64 RGB for Model A and Model B.
- The canonical split metadata is available in `data/processed/` and `data/splits/`; split overlap check passed.
- Model A and Model B constructors compile; output dimension is 5 for both models.
- Model B parameter count is 14,272, below the 100,000-parameter requirement.
- Optimizer comparison includes Adam, SGD, and SGD with momentum.
- Custom model metrics, classification reports, confusion matrices, histories, and predictions are readable.
- Transfer-learning metrics, classification reports, confusion matrices, histories, and predictions are readable.
- All figures referenced by `report/main.tex` exist.
- Final PDF is `report/main.pdf`; it is 14 A4 pages and contains DeFungi-specific content plus the correct group members.
- Submission-named final files exist: `RandomGuess_A03_EN3150.pdf` and `RandomGuess_A03_EN3150.ipynb`.
- PDF text scan found no EuroSAT or neighboring-group terms.

## Verified Final Metrics

| Model | Parameters | Test Accuracy | Macro Precision | Macro Recall |
|---|---:|---:|---:|---:|
| Model A | 101,829 | 0.695906432748538 | 0.7057296614536502 | 0.6647908943697292 |
| Model B | 14,272 | 0.6483918128654971 | 0.6430123008645605 | 0.6202374219855493 |
| MobileNetV2 | 2,264,389 | 0.6907894736842105 | 0.723171326344764 | 0.6478240370391951 |
| EfficientNet-B0 | 4,055,976 | 0.7668128654970761 | 0.809860625155838 | 0.7855623497534866 |

## Commands Run

```bash
git fetch origin
python -m compileall -q src
python -m src.verify_imports
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Remaining Issue

The local repository contains the complete final project, but `origin/main` is behind local `main`. A previous push attempt failed because GitHub HTTPS authentication was not available in the non-interactive environment. After authenticating GitHub locally, run:

