import argparse
import json
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

from . import config
from .datasets import load_split_dataframe
from .train_custom import save_confusion_matrix
from .utils import ensure_directories, set_global_determinism


RAW_DIR = config.RESULTS_DIR / "raw"
TABLES_DIR = config.RESULTS_DIR / "tables"
SESSION3_NOTE_PATH = TABLES_DIR / "session3_transfer_tradeoff_notes.md"
FINAL_COMPARISON_PATH = TABLES_DIR / "final_comparison.csv"
TRANSFER_TABLE_PATH = TABLES_DIR / "pretrained_transfer_models.csv"
TRANSFER_MAC_PATH = TABLES_DIR / "pretrained_transfer_macs.csv"
TRANSFER_LATENCY_PATH = TABLES_DIR / "pretrained_transfer_latency.csv"

TRANSFER_CONFIGS = {
    "mobilenetv2": {
        "display_name": "MobileNetV2",
        "builder": tf.keras.applications.MobileNetV2,
        "preprocess": tf.keras.applications.mobilenet_v2.preprocess_input,
        "fine_tune_layers": 20,
    },
    "efficientnetb0": {
        "display_name": "EfficientNet-B0",
        "builder": tf.keras.applications.EfficientNetB0,
        "preprocess": tf.keras.applications.efficientnet.preprocess_input,
        "fine_tune_layers": 30,
    },
}


class EpochTimer(tf.keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        if not hasattr(self, "epoch_times"):
            self.epoch_times = []

    def on_epoch_begin(self, epoch, logs=None):
        self._start_time = time.perf_counter()

    def on_epoch_end(self, epoch, logs=None):
        self.epoch_times.append(time.perf_counter() - self._start_time)


class BestValidationCheckpoint(tf.keras.callbacks.Callback):
    def __init__(self, path: Path):
        super().__init__()
        self.path = path
        self.best_val_loss = np.inf

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        val_loss = logs.get("val_loss")
        if val_loss is None:
            return
        if float(val_loss) < self.best_val_loss:
            self.best_val_loss = float(val_loss)
            self.model.save(self.path)


def make_pretrained_dataset(
    split: str,
    image_size: tuple[int, int],
    preprocess,
    batch_size: int,
    shuffle: bool = False,
) -> tf.data.Dataset:
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
    if shuffle:
        ds = ds.shuffle(buffer_size=len(df), seed=config.SEED, reshuffle_each_iteration=True)
    return ds.map(load_image, num_parallel_calls=tf.data.AUTOTUNE).batch(batch_size).prefetch(tf.data.AUTOTUNE)


def build_transfer_model(model_name: str, image_size: tuple[int, int]) -> tuple[tf.keras.Model, tf.keras.Model]:
    cfg = TRANSFER_CONFIGS[model_name]
    backbone = cfg["builder"](
        include_top=False,
        weights="imagenet",
        input_shape=(*image_size, 3),
    )
    backbone.trainable = False

    inputs = tf.keras.Input(shape=(*image_size, 3), name="image")
    x = backbone(inputs, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D(name="gap")(x)
    x = tf.keras.layers.Dropout(0.2, name="head_dropout")(x)
    outputs = tf.keras.layers.Dense(config.NUM_CLASSES, activation="softmax", name="defungi_head")(x)
    model = tf.keras.Model(inputs, outputs, name=f"{model_name}_session3_transfer")
    return model, backbone


def set_fine_tune_subset(backbone: tf.keras.Model, last_n_layers: int) -> None:
    backbone.trainable = True
    trainable_started = False
    trainable_layers_seen = 0
    for layer in reversed(backbone.layers):
        if isinstance(layer, tf.keras.layers.BatchNormalization):
            layer.trainable = False
            continue
        if trainable_layers_seen < last_n_layers:
            layer.trainable = True
            trainable_layers_seen += 1
            trainable_started = True
        else:
            layer.trainable = False
    if not trainable_started:
        raise RuntimeError("No fine-tuning layers were enabled.")


def trainable_parameter_count(model: tf.keras.Model) -> int:
    return int(sum(np.prod(weight.shape) for weight in model.trainable_weights))


def plot_combined_history(history: pd.DataFrame, output_path: Path, title: str) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(history["epoch"], history["loss"], label="train")
    axes[0].plot(history["epoch"], history["val_loss"], label="validation")
    axes[0].set_title(f"{title} Loss")
    axes[0].set_xlabel("Epoch")
    axes[0].legend()
    axes[1].plot(history["epoch"], history["accuracy"], label="train")
    axes[1].plot(history["epoch"], history["val_accuracy"], label="validation")
    axes[1].set_title(f"{title} Accuracy")
    axes[1].set_xlabel("Epoch")
    axes[1].legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close(fig)


def evaluate_and_save(
    model_name: str,
    model: tf.keras.Model,
    history_df: pd.DataFrame,
    epoch_times: list[float],
    args,
) -> dict:
    cfg = TRANSFER_CONFIGS[model_name]
    display_name = cfg["display_name"]
    raw_dir = RAW_DIR / model_name
    raw_dir.mkdir(parents=True, exist_ok=True)

    df = load_split_dataframe()
    test_df = df[df["split"] == "test"].copy().reset_index(drop=True)
    class_names = sorted(df["class_name"].unique())
    test_ds = make_pretrained_dataset("test", args.image_size, cfg["preprocess"], args.batch_size)
    y_true = test_df["label"].astype("int32").to_numpy()
    y_prob = model.predict(test_ds, verbose=0)
    y_pred = np.argmax(y_prob, axis=1)
    cm = confusion_matrix(y_true, y_pred)

    selected_path = raw_dir / f"{model_name}_selected.keras"
    model.save(selected_path)
    model_size_mb = selected_path.stat().st_size / (1024 * 1024)
    model_size_kib = selected_path.stat().st_size / 1024

    report = classification_report(
        y_true,
        y_pred,
        target_names=class_names,
        output_dict=True,
        zero_division=0,
    )
    report_df = pd.DataFrame(report).transpose()
    predictions_df = pd.DataFrame(
        {
            "path": test_df["path"],
            "class_name": test_df["class_name"],
            "true_label": y_true,
            "predicted_label": y_pred,
            "predicted_class": [class_names[i] for i in y_pred],
            "correct": y_true == y_pred,
        }
    )
    for idx, class_name in enumerate(class_names):
        predictions_df[f"prob_{class_name}"] = y_prob[:, idx]

    metrics = {
        "model": model_name,
        "display_name": display_name,
        "input_size": list(args.image_size),
        "preprocessing": f"tf.keras.applications.{model_name if model_name == 'efficientnetb0' else 'mobilenet_v2'}.preprocess_input",
        "pretrained_weights": "ImageNet",
        "transfer_learning_strategy": (
            f"Stage 1 froze the ImageNet feature extractor and trained the DeFungi head for "
            f"{args.head_epochs} epochs at LR {args.head_lr}. Stage 2 fine-tuned the upper "
            f"{cfg['fine_tune_layers']} non-BatchNorm backbone layers plus the head for "
            f"{args.fine_tune_epochs} epochs at LR {args.fine_tune_lr}. Validation loss selected the saved checkpoint."
        ),
        "head_epochs": args.head_epochs,
        "fine_tune_epochs": args.fine_tune_epochs,
        "total_epochs": args.head_epochs + args.fine_tune_epochs,
        "batch_size": args.batch_size,
        "head_learning_rate": args.head_lr,
        "fine_tune_learning_rate": args.fine_tune_lr,
        "total_parameters": int(model.count_params()),
        "trainable_parameters": trainable_parameter_count(model),
        "serialized_model_size_mb": round(float(model_size_mb), 4),
        "serialized_model_size_kib": round(float(model_size_kib), 2),
        "epoch_times_seconds": [round(float(x), 4) for x in epoch_times],
        "mean_epoch_time_seconds": round(float(np.mean(epoch_times)), 4),
        "test_accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_precision": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "macro_recall": float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "precision_recall_averaging": "macro",
        "class_names": class_names,
        "confusion_matrix": cm.tolist(),
        "best_validation_loss": float(history_df["val_loss"].min()),
        "best_validation_epoch": int(history_df.loc[history_df["val_loss"].idxmin(), "epoch"]),
    }

    history_df.to_csv(raw_dir / "history.csv", index=False)
    (raw_dir / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    report_df.to_csv(raw_dir / "classification_report.csv")
    pd.DataFrame(cm, index=class_names, columns=class_names).to_csv(raw_dir / "confusion_matrix.csv")
    predictions_df.to_csv(raw_dir / "test_predictions.csv", index=False)

    plot_combined_history(history_df, config.FIGURES_DIR / f"{model_name}_session3_training_curve.png", display_name)
    save_confusion_matrix(cm, class_names, config.FIGURES_DIR / f"{model_name}_session3_confusion_matrix.png")
    return metrics


def run_training(args) -> None:
    ensure_directories()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    set_global_determinism()

    metrics_rows = []
    for model_name in args.models:
        cfg = TRANSFER_CONFIGS[model_name]
        print(f"Training {cfg['display_name']} at {args.image_size[0]}x{args.image_size[1]}")
        raw_dir = RAW_DIR / model_name
        raw_dir.mkdir(parents=True, exist_ok=True)
        best_path = raw_dir / f"{model_name}_best_validation.keras"

        train_ds = make_pretrained_dataset("train", args.image_size, cfg["preprocess"], args.batch_size, shuffle=True)
        val_ds = make_pretrained_dataset("validation", args.image_size, cfg["preprocess"], args.batch_size)
        model, backbone = build_transfer_model(model_name, args.image_size)
        checkpoint = BestValidationCheckpoint(best_path)
        timer = EpochTimer()

        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=args.head_lr),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )
        head_history = model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=args.head_epochs,
            callbacks=[timer, checkpoint],
            verbose=2,
            shuffle=False,
        )

        set_fine_tune_subset(backbone, cfg["fine_tune_layers"])
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=args.fine_tune_lr),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )
        fine_history = model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=args.fine_tune_epochs,
            callbacks=[timer, checkpoint],
            verbose=2,
            shuffle=False,
        )

        rows = []
        epoch_index = 1
        for stage, history in [("head", head_history.history), ("fine_tune", fine_history.history)]:
            for i in range(len(history["loss"])):
                row = {key: float(values[i]) for key, values in history.items()}
                row["epoch"] = epoch_index
                row["stage"] = stage
                rows.append(row)
                epoch_index += 1
        history_df = pd.DataFrame(rows)

        selected_model = tf.keras.models.load_model(best_path)
        metrics = evaluate_and_save(model_name, selected_model, history_df, timer.epoch_times, args)
        metrics_rows.append(metrics)
        print(json.dumps(metrics, indent=2))

    pd.DataFrame(
        [
            {
                "model": row["display_name"],
                "input_size": f"{row['input_size'][0]}x{row['input_size'][1]}",
                "total_parameters": row["total_parameters"],
                "trainable_parameters": row["trainable_parameters"],
                "serialized_model_size_kib": row["serialized_model_size_kib"],
                "mean_epoch_time_s": row["mean_epoch_time_seconds"],
                "test_accuracy": row["test_accuracy"],
                "macro_precision": row["macro_precision"],
                "macro_recall": row["macro_recall"],
                "macro_f1": row["macro_f1"],
            }
            for row in metrics_rows
        ]
    ).to_csv(TRANSFER_TABLE_PATH, index=False)


def shape_to_string(shape) -> str:
    try:
        return "x".join("None" if dim is None else str(int(dim)) for dim in shape)
    except TypeError:
        return str(shape)


def layer_output_shape(layer):
    output = layer.output
    if isinstance(output, (list, tuple)):
        output = output[0]
    return tuple(output.shape)


def iter_layers(model: tf.keras.Model):
    for layer in model.layers:
        if isinstance(layer, tf.keras.Model):
            yield from iter_layers(layer)
        else:
            yield layer


def estimate_model_macs(model: tf.keras.Model, model_label: str) -> tuple[int, list[dict]]:
    rows = []
    total = 0
    for layer in iter_layers(model):
        macs = 0
        note = "Not included in MAC total."
        try:
            output_shape = layer_output_shape(layer)
        except Exception:
            output_shape = ()
        if isinstance(layer, tf.keras.layers.Conv2D):
            kernel_h, kernel_w, in_channels, out_channels = layer.kernel.shape
            out_h, out_w = output_shape[1], output_shape[2]
            macs = int(out_h * out_w * out_channels * kernel_h * kernel_w * in_channels)
            note = "Conv2D MACs exclude bias, activation, normalization, and pooling cost."
        elif isinstance(layer, tf.keras.layers.DepthwiseConv2D):
            depthwise_kernel = getattr(layer, "depthwise_kernel", None)
            if depthwise_kernel is None:
                depthwise_kernel = layer.kernel
            kernel_h, kernel_w, in_channels, depth_multiplier = depthwise_kernel.shape
            out_h, out_w = output_shape[1], output_shape[2]
            macs = int(out_h * out_w * in_channels * depth_multiplier * kernel_h * kernel_w)
            note = "DepthwiseConv2D MACs exclude bias, activation, normalization, and pooling cost."
        elif isinstance(layer, tf.keras.layers.Dense):
            in_units, out_units = layer.kernel.shape
            macs = int(in_units * out_units)
            note = "Dense MACs exclude bias and activation cost."
        total += macs
        rows.append(
            {
                "model": model_label,
                "layer": layer.name,
                "class": layer.__class__.__name__,
                "output_shape": shape_to_string(output_shape),
                "macs": macs,
                "note": note,
            }
        )
    rows.append(
        {
            "model": model_label,
            "layer": "TOTAL_INCLUDED",
            "class": "",
            "output_shape": "",
            "macs": total,
            "note": "Conv/DepthwiseConv/Dense MAC estimate only.",
        }
    )
    return total, rows


def benchmark_latency(model: tf.keras.Model, image_size: tuple[int, int], warmup: int, runs: int) -> dict:
    sample = tf.random.uniform((1, image_size[0], image_size[1], 3), dtype=tf.float32)
    for _ in range(warmup):
        _ = model(sample, training=False)
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        _ = model(sample, training=False)
        times.append((time.perf_counter() - start) * 1000)
    return {
        "warmup_runs": warmup,
        "timed_runs": runs,
        "batch_size": 1,
        "mean_ms": float(np.mean(times)),
        "p95_ms": float(np.percentile(times, 95)),
        "min_ms": float(np.min(times)),
        "max_ms": float(np.max(times)),
    }


def load_metrics(model_name: str) -> dict:
    return json.loads((RAW_DIR / model_name / "metrics.json").read_text(encoding="utf-8"))


def run_finalize(args) -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    mac_rows = []
    latency_rows = []
    transfer_rows = []

    for model_name, cfg in TRANSFER_CONFIGS.items():
        metrics = load_metrics(model_name)
        model_path = RAW_DIR / model_name / f"{model_name}_selected.keras"
        model = tf.keras.models.load_model(model_path)
        label = cfg["display_name"]
        macs, rows = estimate_model_macs(model, label)
        mac_rows.extend(rows)
        latency = benchmark_latency(model, tuple(metrics["input_size"]), args.warmup_runs, args.timed_runs)
        latency_rows.append(
            {
                "model": label,
                "threads_intra_op": "default",
                "threads_inter_op": "default",
                **latency,
                "benchmark_input": f"in-memory random tensor with shape 1x{metrics['input_size'][0]}x{metrics['input_size'][1]}x3",
                "excludes": "disk I/O and image decoding/loading",
                "limitations": "CPU timing on this machine only; not a direct edge-device latency or energy measurement.",
            }
        )
        transfer_rows.append(
            {
                "model": label,
                "parameters": metrics["total_parameters"],
                "serialized_model_size": metrics["serialized_model_size_kib"],
                "MACs": macs,
                "CPU_mean_latency": latency["mean_ms"],
                "CPU_p95_latency": latency["p95_ms"],
                "test_accuracy": metrics["test_accuracy"],
                "macro_precision": metrics["macro_precision"],
                "macro_recall": metrics["macro_recall"],
            }
        )

    pd.DataFrame(mac_rows).to_csv(TRANSFER_MAC_PATH, index=False)
    pd.DataFrame(latency_rows).to_csv(TRANSFER_LATENCY_PATH, index=False)

    custom_models = pd.read_csv(TABLES_DIR / "custom_models.csv")
    custom_latency = pd.read_csv(TABLES_DIR / "custom_latency.csv")
    custom_rows = []
    for _, row in custom_models.iterrows():
        latency = custom_latency[custom_latency["model"] == row["model"]].iloc[0]
        custom_rows.append(
            {
                "model": row["model"],
                "parameters": int(row["trainable_parameters"]),
                "serialized_model_size": float(row["serialized_size_kib"]),
                "MACs": int(row["MACs"]),
                "CPU_mean_latency": float(latency["mean_ms"]),
                "CPU_p95_latency": float(latency["p95_ms"]),
                "test_accuracy": float(row["test_accuracy"]),
                "macro_precision": float(row["macro_precision"]),
                "macro_recall": float(row["macro_recall"]),
            }
        )

    final_df = pd.DataFrame(custom_rows + transfer_rows)
    final_df.to_csv(FINAL_COMPARISON_PATH, index=False)
    write_tradeoff_notes(final_df)
    print(final_df.to_string(index=False))


def write_tradeoff_notes(final_df: pd.DataFrame) -> None:
    best_acc = final_df.loc[final_df["test_accuracy"].idxmax()]
    smallest_model = final_df.loc[final_df["serialized_model_size"].idxmin()]
    lowest_macs = final_df.loc[final_df["MACs"].idxmin()]
    lowest_latency = final_df.loc[final_df["CPU_mean_latency"].idxmin()]
    model_b = final_df[final_df["model"] == "Model B"].iloc[0]
    pretrained = final_df[final_df["model"].isin(["MobileNetV2", "EfficientNet-B0"])]

    lines = [
        "# Session 3 Transfer Learning Trade-off Notes",
        "",
        "## Accuracy",
        f"- Highest measured test accuracy: {best_acc['model']} ({best_acc['test_accuracy']:.4f}).",
        f"- Model B test accuracy: {model_b['test_accuracy']:.4f}.",
    ]
    for _, row in pretrained.iterrows():
        lines.append(
            f"- {row['model']} improved over Model B by {row['test_accuracy'] - model_b['test_accuracy']:.4f} absolute accuracy."
        )
    lines.extend(
        [
            "",
            "## Memory Footprint",
            f"- Smallest serialized model in the measured artifacts: {smallest_model['model']} ({smallest_model['serialized_model_size']:.2f} KiB).",
            "- Parameter count and serialized model size are related but not identical; saved model metadata and layer state also affect disk footprint.",
            "",
            "## Computational Cost",
            f"- Lowest included Conv/Dense MAC estimate: {lowest_macs['model']} ({int(lowest_macs['MACs'])} MACs).",
            f"- Lowest measured CPU mean latency: {lowest_latency['model']} ({lowest_latency['CPU_mean_latency']:.4f} ms).",
            "- A smaller parameter count does not automatically imply lower latency, lower RAM, or lower energy. Only MACs and CPU latency were measured here.",
            "",
            "## Limitations",
            "- Single canonical split.",
            "- Single seed for the split/training setup.",
            "- Limited hyperparameter search.",
            "- No physical edge-device or microcontroller energy measurement.",
            "- Possible class imbalance in DeFungi.",
            "- ImageNet transfer learning uses external prior visual knowledge.",
            "- Transfer models were constrained to 64x64 input, which is smaller than standard ImageNet transfer-learning practice.",
            "- CPU benchmark is not equivalent to microcontroller inference and excludes disk I/O and image decoding.",
        ]
    )
    SESSION3_NOTE_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args():
    parser = argparse.ArgumentParser(description="Session 3 transfer learning experiments and tables.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    train_parser = subparsers.add_parser("train")
    train_parser.add_argument("--models", nargs="+", choices=sorted(TRANSFER_CONFIGS), default=sorted(TRANSFER_CONFIGS))
    train_parser.add_argument("--head-epochs", type=int, default=3)
    train_parser.add_argument("--fine-tune-epochs", type=int, default=8)
    train_parser.add_argument("--head-lr", type=float, default=1e-3)
    train_parser.add_argument("--fine-tune-lr", type=float, default=1e-4)
    train_parser.add_argument("--batch-size", type=int, default=config.BATCH_SIZE)
    train_parser.add_argument("--image-size", type=int, nargs=2, default=config.IMAGE_SIZE)

    final_parser = subparsers.add_parser("finalize")
    final_parser.add_argument("--warmup-runs", type=int, default=20)
    final_parser.add_argument("--timed-runs", type=int, default=200)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "train":
        args.image_size = tuple(args.image_size)
        run_training(args)
    elif args.command == "finalize":
        run_finalize(args)


if __name__ == "__main__":
    main()
