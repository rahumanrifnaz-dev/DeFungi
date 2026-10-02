import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, UnidentifiedImageError
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from . import config
from .utils import ensure_directories, project_relative, set_global_determinism


def find_class_dirs(data_dir: Path) -> list[Path]:
    if not data_dir.exists():
        raise FileNotFoundError(
            f"Dataset folder not found: {data_dir}\n"
            "Download/extract UCI DeFungi and place it at data/raw/defungi/."
        )
    class_dirs = sorted([p for p in data_dir.iterdir() if p.is_dir()])
    if len(class_dirs) != config.NUM_CLASSES:
        raise ValueError(
            f"Expected {config.NUM_CLASSES} class folders, found {len(class_dirs)} in {data_dir}: "
            f"{[p.name for p in class_dirs]}"
        )
    return class_dirs


def inspect_images(data_dir: Path) -> tuple[pd.DataFrame, list[dict]]:
    rows = []
    unreadable = []
    class_dirs = find_class_dirs(data_dir)

    for class_dir in class_dirs:
        image_paths = sorted(
            p for p in class_dir.rglob("*") if p.is_file() and p.suffix.lower() in config.IMAGE_EXTENSIONS
        )
        for image_path in tqdm(image_paths, desc=f"Inspecting {class_dir.name}"):
            try:
                with Image.open(image_path) as image:
                    width, height = image.size
                    mode = image.mode
                    image_format = image.format
                    image.verify()
                rows.append(
                    {
                        "path": project_relative(image_path),
                        "class_name": class_dir.name,
                        "extension": image_path.suffix.lower(),
                        "width": int(width),
                        "height": int(height),
                        "mode": mode,
                        "format": image_format,
                    }
                )
            except (UnidentifiedImageError, OSError) as exc:
                unreadable.append(
                    {
                        "path": project_relative(image_path),
                        "class_name": class_dir.name,
                        "error": str(exc),
                    }
                )

    if not rows:
        raise ValueError(f"No readable images found under {data_dir}")

    return pd.DataFrame(rows), unreadable


def make_stratified_splits(df: pd.DataFrame) -> pd.DataFrame:
    train_df, temp_df = train_test_split(
        df,
        test_size=0.30,
        random_state=config.SEED,
        stratify=df["class_name"],
    )
    val_df, test_df = train_test_split(
        temp_df,
        test_size=0.50,
        random_state=config.SEED,
        stratify=temp_df["class_name"],
    )

    train_df = train_df.assign(split="train")
    val_df = val_df.assign(split="validation")
    test_df = test_df.assign(split="test")
    split_df = pd.concat([train_df, val_df, test_df], ignore_index=True)
    class_names = sorted(split_df["class_name"].unique())
    label_map = {name: idx for idx, name in enumerate(class_names)}
    split_df["label"] = split_df["class_name"].map(label_map)
    return split_df.sort_values(["split", "class_name", "path"]).reset_index(drop=True)


def validate_splits(split_df: pd.DataFrame) -> dict:
    total_rows = len(split_df)
    unique_paths = split_df["path"].nunique()
    duplicate_paths = split_df[split_df.duplicated("path", keep=False)]["path"].tolist()
    split_counts = split_df["split"].value_counts().to_dict()
    per_split_class_counts = (
        split_df.groupby(["split", "class_name"]).size().unstack(fill_value=0).to_dict(orient="index")
    )
    if unique_paths != total_rows:
        raise AssertionError(f"Split validation failed: {total_rows - unique_paths} duplicate path entries found.")
    if set(split_counts) != {"train", "validation", "test"}:
        raise AssertionError(f"Split validation failed: expected train/validation/test, got {sorted(split_counts)}")
    return {
        "total_rows": int(total_rows),
        "unique_paths": int(unique_paths),
        "duplicate_paths": duplicate_paths,
        "split_counts": {k: int(v) for k, v in sorted(split_counts.items())},
        "per_split_class_counts": {
            split: {klass: int(count) for klass, count in counts.items()}
            for split, counts in sorted(per_split_class_counts.items())
        },
    }


def save_distribution_figure(split_df: pd.DataFrame) -> None:
    counts = split_df.groupby(["class_name", "split"]).size().unstack(fill_value=0)
    counts = counts[["train", "validation", "test"]]

    ax = counts.plot(kind="bar", figsize=(9, 5))
    ax.set_xlabel("Class")
    ax.set_ylabel("Readable images")
    ax.set_title("DeFungi class distribution by split")
    ax.legend(title="Split")
    plt.tight_layout()
    plt.savefig(config.FIGURES_DIR / "class_distribution.png", dpi=200)
    plt.close()


def build_summary(split_df: pd.DataFrame, unreadable: list[dict]) -> dict:
    class_counts = Counter(split_df["class_name"])
    split_counts = Counter(split_df["split"])
    dimension_counts = Counter(zip(split_df["width"], split_df["height"]))
    mode_counts = Counter(split_df["mode"])
    extension_counts = Counter(split_df["extension"])
    format_counts = Counter(split_df["format"])
    dimensions_by_class: dict[str, dict[str, int]] = defaultdict(dict)
    for class_name, class_df in split_df.groupby("class_name"):
        dims = Counter(zip(class_df["width"], class_df["height"]))
        dimensions_by_class[class_name] = {
            f"{width}x{height}": int(count) for (width, height), count in dims.most_common(10)
        }
    return {
        "seed": config.SEED,
        "image_size_for_custom_models": [*config.IMAGE_SIZE, config.CHANNELS],
        "normalization": "pixel values scaled to [0, 1] during dataset loading",
        "total_usable_images": int(len(split_df)),
        "class_names": sorted(split_df["class_name"].unique()),
        "images_per_class": {k: int(v) for k, v in sorted(class_counts.items())},
        "split_counts": {k: int(v) for k, v in sorted(split_counts.items())},
        "image_extensions": {k: int(v) for k, v in sorted(extension_counts.items())},
        "image_formats": {str(k): int(v) for k, v in sorted(format_counts.items())},
        "image_modes": {k: int(v) for k, v in sorted(mode_counts.items())},
        "image_dimensions": {
            f"{width}x{height}": int(count) for (width, height), count in dimension_counts.most_common()
        },
        "typical_image_dimensions": [
            {"width": int(width), "height": int(height), "count": int(count)}
            for (width, height), count in dimension_counts.most_common(10)
        ],
        "dimensions_by_class_top_10": dimensions_by_class,
        "unreadable_count": len(unreadable),
        "unreadable_images": unreadable,
        "split_validation": validate_splits(split_df),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect DeFungi images and create saved stratified splits.")
    parser.add_argument("--data-dir", type=Path, default=config.DATA_RAW_DIR)
    args = parser.parse_args()

    set_global_determinism()
    ensure_directories()

    image_df, unreadable = inspect_images(args.data_dir)
    split_df = make_stratified_splits(image_df)
    split_df.to_csv(config.SPLITS_CSV, index=False)
    split_df[split_df["split"] == "train"].to_csv(config.TRAIN_CSV, index=False)
    split_df[split_df["split"] == "validation"].to_csv(config.VALIDATION_CSV, index=False)
    split_df[split_df["split"] == "test"].to_csv(config.TEST_CSV, index=False)

    summary = build_summary(split_df, unreadable)
    config.DATASET_SUMMARY_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    save_distribution_figure(split_df)

    print(json.dumps(summary, indent=2))
    print(f"Saved split metadata to {config.SPLITS_CSV}")


if __name__ == "__main__":
    main()
