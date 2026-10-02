# Dataset Setup

This project uses the DeFungi image dataset from the UCI Machine Learning Repository.

- Official dataset page: <https://archive.ics.uci.edu/dataset/773/defungi>
- Task: five-class image classification
- Verified usable images in the local experiment: 9,114
- Classes: H1, H2, H3, H5, H6

Raw dataset files are not included in this repository. Download the DeFungi dataset from UCI and extract it locally so the folder layout is:

```text
data/
  raw/
    defungi/
      H1/
        *.jpg
      H2/
        *.jpg
      H3/
        *.jpg
      H5/
        *.jpg
      H6/
        *.jpg
```

The `data/raw/` directory is intentionally ignored by Git to avoid uploading thousands of image files. The lightweight processed split metadata is kept in `data/processed/`:

```text
data/processed/splits.csv
data/processed/train.csv
data/processed/validation.csv
data/processed/test.csv
```

To recreate the canonical split after placing the dataset, run from the project root:

```bash
python -m src.data_prepare --data-dir data/raw/defungi
```
