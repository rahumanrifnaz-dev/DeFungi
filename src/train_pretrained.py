import argparse
import json
import time

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score

from . import config
from .datasets import load_split_dataframe
from .models import parameter_storage_kb
from .train_custom import EpochTimer, plot_history, save_confusion_matrix
from .utils import ensure_directories, set_global_determinism


PRETRAINED_CONFIGS = {
    "mobilenetv2": {
        "size": (224, 224),
        "builder": tf.keras.applications.MobileNetV2,
        "preprocess": tf.keras.applications.mobilenet_v2.preprocess_input,
    },
    "efficientnetb0": {
        "size": (224, 224),
        "builder": tf.keras.applications.EfficientNetB0,
        "preprocess": tf.keras.applications.efficientnet.preprocess_input,
    },
}


def make_pretrained_dataset(split: str, image_size: tuple[int, int], preprocess, batch_size: int) -> tf.data.Dataset:
    df = load_split_dataframe()
    df = df[df["split"] == split].copy()
    paths = [str(config.PROJECT_ROOT / p) for p in df["path"]]
    labels = df["label"].astype("int32").to_numpy()

    def load_image(path, label):
        image = tf.io.decode_image(tf.io.read_file(path), channels=3, expand_animations=False)
        image = tf.image.resize(image, image_size)
        image = preprocess(tf.cast(image, tf.float32))
        return image, label

    ds = tf.data.Dataset.from_tensor_slices((paths, labels))
    if split == "train":
        ds = ds.shuffle(buffer_size=len(df), seed=config.SEED, reshuffle_each_iteration=True)
    return ds.map(load_image, num_parallel_calls=tf.data.AUTOTUNE).batch(batch_size).prefetch(tf.data.AUTOTUNE)


def build_transfer_model(model_name: str) -> tf.keras.Model:
    cfg = PRETRAINED_CONFIGS[model_name]
    backbone = cfg["builder"](
        include_top=False,
        weights="imagenet",
        input_shape=(*cfg["size"], 3),
    )
    backbone.trainable = False
    inputs = tf.keras.Input(shape=(*cfg["size"], 3))
    x = backbone(inputs, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    outputs = tf.keras.layers.Dense(config.NUM_CLASSES, activation="softmax")(x)
    model = tf.keras.Model(inputs, outputs, name=f"{model_name}_transfer")
    model.backbone_name = backbone.name
    return model


def main() -> None:
    parser = argparse.ArgumentParser(description="Train lightweight pretrained models on saved DeFungi split.")
    parser.add_argument("--model", choices=sorted(PRETRAINED_CONFIGS), required=True)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=config.BATCH_SIZE)
    args = parser.parse_args()

    ensure_directories()
    set_global_determinism()
    cfg = PRETRAINED_CONFIGS[args.model]
    df = load_split_dataframe()
    class_names = sorted(df["class_name"].unique())

    train_ds = make_pretrained_dataset("train", cfg["size"], cfg["preprocess"], args.batch_size)
    val_ds = make_pretrained_dataset("validation", cfg["size"], cfg["preprocess"], args.batch_size)
    test_ds = make_pretrained_dataset("test", cfg["size"], cfg["preprocess"], args.batch_size)

    model = build_transfer_model(args.model)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    timer = EpochTimer()
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=args.epochs,
        callbacks=[timer],
        verbose=2,
        shuffle=False,
    )

    y_true = np.concatenate([labels.numpy() for _, labels in test_ds], axis=0)
    y_pred = np.argmax(model.predict(test_ds, verbose=0), axis=1)
    cm = confusion_matrix(y_true, y_pred)
    model_path = config.MODELS_DIR / f"{args.model}_transfer.keras"
    model.save(model_path)
    trainable_parameters = int(np.sum([np.prod(v.shape) for v in model.trainable_weights]))

    metrics = {
        "model": args.model,
        "transfer_learning_strategy": "ImageNet backbone frozen; new five-class Dense head trained.",
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "total_parameters": int(model.count_params()),
        "trainable_parameters": trainable_parameters,
        "fp32_trainable_parameter_storage_kb": round(parameter_storage_kb(trainable_parameters), 2),
        "model_size_mb": round(model_path.stat().st_size / (1024 * 1024), 2),
        "epoch_times_seconds": [round(x, 4) for x in timer.epoch_times],
        "mean_training_time_per_epoch_seconds": round(float(np.mean(timer.epoch_times)), 4),
        "history": {k: [float(v) for v in values] for k, values in history.history.items()},
        "test_accuracy": float(accuracy_score(y_true, y_pred)),
        "precision_macro": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall_macro": float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "precision_recall_averaging": "macro",
        "per_class_metrics": classification_report(
            y_true,
            y_pred,
            target_names=class_names,
            output_dict=True,
            zero_division=0,
        ),
        "confusion_matrix": cm.tolist(),
        "class_names": class_names,
    }
    out_path = config.METRICS_DIR / f"{args.model}_transfer_metrics.json"
    out_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    pd.DataFrame(history.history).assign(epoch=range(1, args.epochs + 1)).to_csv(
        config.METRICS_DIR / f"{args.model}_transfer_history.csv",
        index=False,
    )
    plot_history(history, config.FIGURES_DIR / f"{args.model}_transfer_history.png")
    save_confusion_matrix(cm, class_names, config.CONFUSION_DIR / f"{args.model}_transfer_confusion_matrix.png")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
