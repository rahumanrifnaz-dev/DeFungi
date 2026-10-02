from pathlib import Path

import pandas as pd
import tensorflow as tf

from . import config


def load_split_dataframe(split_csv: Path = config.SPLITS_CSV) -> pd.DataFrame:
    if not split_csv.exists():
        raise FileNotFoundError(
            f"Missing split file: {split_csv}. Run python -m src.data_prepare first."
        )
    return pd.read_csv(split_csv)


def _load_custom_image(path: tf.Tensor, label: tf.Tensor) -> tuple[tf.Tensor, tf.Tensor]:
    image_bytes = tf.io.read_file(path)
    image = tf.io.decode_image(image_bytes, channels=config.CHANNELS, expand_animations=False)
    image = tf.image.resize(image, config.IMAGE_SIZE)
    image = tf.cast(image, tf.float32) / 255.0
    return image, label


def make_custom_dataset(split: str, batch_size: int = config.BATCH_SIZE, shuffle: bool = False) -> tf.data.Dataset:
    df = load_split_dataframe()
    df = df[df["split"] == split].copy()
    paths = [str(config.PROJECT_ROOT / p) for p in df["path"]]
    labels = df["label"].astype("int32").to_numpy()
    ds = tf.data.Dataset.from_tensor_slices((paths, labels))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(df), seed=config.SEED, reshuffle_each_iteration=True)
    return ds.map(_load_custom_image, num_parallel_calls=tf.data.AUTOTUNE).batch(batch_size).prefetch(tf.data.AUTOTUNE)
