import json

import tensorflow as tf

from . import config
from .datasets import load_split_dataframe
from .datasets import make_custom_dataset


def main() -> None:
    config.METRICS_DIR.mkdir(parents=True, exist_ok=True)
    split_df = load_split_dataframe()
    train_df = split_df[split_df["split"] == "train"].copy()
    ds = make_custom_dataset("train", batch_size=config.BATCH_SIZE, shuffle=False)
    images, labels = next(iter(ds))
    check = {
        "split": "train",
        "batch_size_configured": config.BATCH_SIZE,
        "image_shape": [int(dim) for dim in images.shape],
        "label_shape": [int(dim) for dim in labels.shape],
        "image_dtype": images.dtype.name,
        "label_dtype": labels.dtype.name,
        "pixel_min": float(tf.reduce_min(images).numpy()),
        "pixel_max": float(tf.reduce_max(images).numpy()),
        "batch_label_min": int(tf.reduce_min(labels).numpy()),
        "batch_label_max": int(tf.reduce_max(labels).numpy()),
        "train_split_label_min": int(train_df["label"].min()),
        "train_split_label_max": int(train_df["label"].max()),
        "train_split_class_names": sorted(train_df["class_name"].unique()),
        "expected_image_shape_per_sample": [*config.IMAGE_SIZE, config.CHANNELS],
        "expected_label_range": [0, config.NUM_CLASSES - 1],
    }
    if check["image_shape"][1:] != check["expected_image_shape_per_sample"]:
        raise AssertionError(f"Unexpected image shape: {check['image_shape']}")
    if check["pixel_min"] < 0.0 or check["pixel_max"] > 1.0:
        raise AssertionError(f"Pixel range outside [0, 1]: {check['pixel_min']}..{check['pixel_max']}")
    if check["train_split_label_min"] != 0 or check["train_split_label_max"] != config.NUM_CLASSES - 1:
        raise AssertionError(
            "Training split does not cover expected label range: "
            f"{check['train_split_label_min']}..{check['train_split_label_max']}"
        )
    config.PIPELINE_CHECK_JSON.write_text(json.dumps(check, indent=2), encoding="utf-8")
    print(json.dumps(check, indent=2))


if __name__ == "__main__":
    main()
