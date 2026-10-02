import argparse
import json
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score
import tensorflow as tf

from . import config
from .datasets import load_split_dataframe, make_custom_dataset
from .models import build_model_a, build_model_b, parameter_storage_kb
from .utils import ensure_directories, set_global_determinism


class EpochTimer(tf.keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        self.epoch_times = []

    def on_epoch_begin(self, epoch, logs=None):
        self._start_time = time.perf_counter()

    def on_epoch_end(self, epoch, logs=None):
        self.epoch_times.append(time.perf_counter() - self._start_time)


def build_optimizer(name: str) -> tf.keras.optimizers.Optimizer:
    if name == "adam":
        return tf.keras.optimizers.Adam(learning_rate=1e-3)
    if name == "sgd":
        return tf.keras.optimizers.SGD(learning_rate=1e-2)
    if name == "sgd_momentum":
        return tf.keras.optimizers.SGD(learning_rate=1e-2, momentum=0.9)
    raise ValueError(f"Unknown optimizer: {name}")


def build_model(name: str) -> tf.keras.Model:
    if name == "model_a":
        return build_model_a()
    if name == "model_b":
        return build_model_b()
    raise ValueError(f"Unknown model: {name}")


def plot_history(history: tf.keras.callbacks.History, output_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(history.history["loss"], label="train")
    axes[0].plot(history.history["val_loss"], label="validation")
    axes[0].set_title("Loss")
    axes[0].set_xlabel("Epoch")
    axes[0].legend()
    axes[1].plot(history.history["accuracy"], label="train")
    axes[1].plot(history.history["val_accuracy"], label="validation")
    axes[1].set_title("Accuracy")
    axes[1].set_xlabel("Epoch")
    axes[1].legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close(fig)


def save_confusion_matrix(cm: np.ndarray, class_names: list[str], output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(cm, cmap="Blues")
    fig.colorbar(im, ax=ax)
    ax.set_xticks(range(len(class_names)), class_names, rotation=45, ha="right")
    ax.set_yticks(range(len(class_names)), class_names)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, int(cm[i, j]), ha="center", va="center")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close(fig)


def train_once(model_name: str, optimizer_name: str, epochs: int, batch_size: int) -> dict:
    set_global_determinism()
    df = load_split_dataframe()
    class_names = sorted(df["class_name"].unique())
    train_ds = make_custom_dataset("train", batch_size=batch_size, shuffle=True)
    val_ds = make_custom_dataset("validation", batch_size=batch_size)
    test_ds = make_custom_dataset("test", batch_size=batch_size)

    model = build_model(model_name)
    model.compile(
        optimizer=build_optimizer(optimizer_name),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    timer = EpochTimer()
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs,
        callbacks=[timer],
        shuffle=False,
        verbose=2,
    )

    y_true = np.concatenate([labels.numpy() for _, labels in test_ds], axis=0)
    y_prob = model.predict(test_ds, verbose=0)
    y_pred = np.argmax(y_prob, axis=1)

    cm = confusion_matrix(y_true, y_pred)
    metrics = {
        "model": model_name,
        "optimizer": optimizer_name,
        "epochs": epochs,
        "batch_size": batch_size,
        "trainable_parameters": int(model.count_params()),
        "fp32_parameter_storage_kb": round(parameter_storage_kb(model.count_params()), 2),
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

    stem = f"{model_name}_{optimizer_name}"
    (config.METRICS_DIR / f"{stem}_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    pd.DataFrame(history.history).assign(epoch=range(1, epochs + 1)).to_csv(
        config.METRICS_DIR / f"{stem}_history.csv",
        index=False,
    )
    plot_history(history, config.FIGURES_DIR / f"{stem}_history.png")
    save_confusion_matrix(cm, class_names, config.CONFUSION_DIR / f"{stem}_confusion_matrix.png")
    model.save(config.MODELS_DIR / f"{stem}.keras")
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="Train custom CNN models on the saved DeFungi split.")
    parser.add_argument("--model", choices=["model_a", "model_b"], default="model_a")
    parser.add_argument("--optimizer", choices=["adam", "sgd", "sgd_momentum"], default="adam")
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=config.BATCH_SIZE)
    parser.add_argument("--optimizer-comparison", action="store_true")
    args = parser.parse_args()

    ensure_directories()
    if args.optimizer_comparison:
        results = [
            train_once(args.model, optimizer_name, args.epochs, args.batch_size)
            for optimizer_name in ["adam", "sgd", "sgd_momentum"]
        ]
        out_path = config.METRICS_DIR / f"{args.model}_optimizer_comparison.json"
        out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(json.dumps(results, indent=2))
    else:
        metrics = train_once(args.model, args.optimizer, args.epochs, args.batch_size)
        print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
