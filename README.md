# EN3150 Assignment 03

## Resource-Constrained CNN for Edge Image Classification

This project implements an image-classification pipeline for EN3150 Assignment 03 using TensorFlow/Keras. It compares a standard custom CNN, a resource-constrained depthwise separable CNN, and two pretrained lightweight models on the DeFungi dataset.

## Dataset

- Dataset: DeFungi
- Source: UCI Machine Learning Repository
- Official page: <https://archive.ics.uci.edu/dataset/773/defungi>
- Task: five-class image classification
- Classes: H1, H2, H3, H5, H6
- Verified usable images: 9,114
- Custom CNN input: 64 x 64 x 3
- Split: stratified 70/15/15 target split

Verified split counts:

| Split | Images |
|---|---:|
| Train | 6,379 |
| Validation | 1,367 |
| Test | 1,368 |

Raw DeFungi images are not included in this repository. See `data/README.md` for dataset placement instructions.

## Models

### Model A

Standard CNN with three Conv2D blocks, global average pooling, and a dense classifier.

### Model B

Depthwise separable CNN designed for resource-constrained deployment. It uses 14,272 trainable parameters and 55.75 KB estimated FP32 parameter storage.

### Pretrained Models

- MobileNetV2 with frozen ImageNet backbone
- EfficientNetB0 with frozen ImageNet backbone

## Group Members

| Member | Index | Main Contribution |
|---|---|---|
| Rifnaz.K.R.M | 230550P | Dataset Preparation + Model A |
| Panuharan.S | 230462X | Model B + Efficiency Analysis |
| Peranavan.K | 230474K | Optimizer Comparison + Training/Evaluation |
| Lavanathan.J | 230371R | Pretrained Models + Final Comparison |

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── PROJECT_STATUS.md
├── FINAL_AUDIT.md
├── report_data.md
├── data/
│   ├── README.md
│   └── processed/
├── src/
├── results/
│   ├── confusion_matrices/
│   ├── figures/
│   └── metrics/
├── report/
│   ├── main.tex
│   ├── main.pdf
│   ├── references.bib
│   ├── figures/
│   └── sections/
├── GITHUB_FILE_AUDIT.md
├── MEMBER_FILES.md
└── GITHUB_WORKFLOW.md
```

The local folders `.venv/`, `data/raw/`, and `results/models/` are intentionally excluded from Git.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activate with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Dataset Setup

Download DeFungi from the UCI page and extract it locally as:

```text
data/raw/defungi/
├── H1/
├── H2/
├── H3/
├── H5/
└── H6/
```

Then create or refresh the canonical split:

```bash
python -m src.data_prepare --data-dir data/raw/defungi
```

The processed split CSV files are kept in `data/processed/` for reproducibility.

## Running The Project

Run commands from the project root:

```bash
python -m src.verify_imports
python -m src.verify_environment
python -m src.data_prepare --data-dir data/raw/defungi
python -m src.verify_pipeline
python -m src.model_checks
python -m src.smoke_test --train-batches 3 --validation-batches 1
python -m src.optimizer_experiment --epochs 5 --train-batches 30
python -m src.train_custom --model model_a --epochs 20
python -m src.train_custom --model model_b --epochs 20
python -m src.train_pretrained --model mobilenetv2 --epochs 20
python -m src.train_pretrained --model efficientnetb0 --epochs 20
python -m src.make_report_data
```

Expensive training does not need to be rerun to inspect the completed submission; verified metrics and figures are already saved under `results/`.

## Results

| Model | Test Accuracy | Macro Precision | Macro Recall | Parameters / Size Indicator |
|---|---:|---:|---:|---|
| Model A | 0.6959 | 0.7057 | 0.6648 | 101,829 parameters |
| Model B | 0.6484 | 0.6430 | 0.6202 | 14,272 parameters, 55.75 KB FP32 |
| MobileNetV2 | 0.7427 | 0.7981 | 0.7420 | 2,264,389 total parameters, 9.25 MB saved model |
| EfficientNetB0 | 0.7727 | 0.8227 | 0.7654 | 4,055,976 total parameters, 16.33 MB saved model |

The same canonical split was reused across all models. Adam with learning rate 0.001 was selected from the controlled optimizer comparison.

## Report

- LaTeX source: `report/main.tex`
- Final PDF: `report/main.pdf`
- Bibliography: `report/references.bib`
- Report data: `report/report_data.md` and top-level `report_data.md`

To rebuild the report:

```bash
cd report
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Notes

- Raw dataset files are excluded from GitHub.
- Trained `.keras` model binaries are excluded by default because they are reproducible from the source code.
- Verified metrics, figures, processed split CSVs, source files, and the final PDF are kept for review.
