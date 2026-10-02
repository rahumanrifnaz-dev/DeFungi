import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
METRICS_DIR = PROJECT_ROOT / "results" / "metrics"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def metric_row(label: str, data: dict) -> dict:
    return {
        "model": label,
        "parameters": data.get("total_parameters", data.get("trainable_parameters")),
        "trainable": data.get("trainable_parameters"),
        "size": (
            f"{data['model_size_mb']} MB"
            if "model_size_mb" in data
            else f"{data['fp32_parameter_storage_kb']} KB FP32"
        ),
        "accuracy": data["test_accuracy"],
        "precision": data["precision_macro"],
        "recall": data["recall_macro"],
        "epoch_time": data["mean_training_time_per_epoch_seconds"],
    }


def print_table(rows: list[dict]) -> None:
    headers = ["Model", "Params", "Trainable", "Size", "Accuracy", "Precision", "Recall", "s/epoch"]
    widths = [18, 12, 10, 16, 10, 10, 10, 9]
    print(" ".join(h.ljust(w) for h, w in zip(headers, widths)))
    print("-" * sum(widths))
    for row in rows:
        values = [
            row["model"],
            f"{row['parameters']:,}",
            f"{row['trainable']:,}",
            row["size"],
            f"{row['accuracy']:.4f}",
            f"{row['precision']:.4f}",
            f"{row['recall']:.4f}",
            f"{row['epoch_time']:.4f}",
        ]
        print(" ".join(value.ljust(width) for value, width in zip(values, widths)))


def main() -> None:
    dataset = load_json(METRICS_DIR / "dataset_summary.json")
    optimizer = load_json(METRICS_DIR / "optimizer_experiment_results.json")
    model_a = load_json(METRICS_DIR / "model_a_adam_metrics.json")
    model_b = load_json(METRICS_DIR / "model_b_adam_metrics.json")
    mobilenet = load_json(METRICS_DIR / "mobilenetv2_transfer_metrics.json")
    efficientnet = load_json(METRICS_DIR / "efficientnetb0_transfer_metrics.json")

    print("EN3150 Assignment 03 Demo")
    print()
    print("Dataset: DeFungi")
    print(f"Usable images: {dataset['total_usable_images']:,}")
    print(f"Classes: {', '.join(dataset['class_names'])}")
    print(f"Class counts: {dataset['images_per_class']}")
    print(f"Split counts: {dataset['split_counts']}")
    print()
    print("Optimizer comparison:")
    print(f"Selected optimizer: {optimizer['selected_optimizer']}")
    print(f"Basis: {optimizer['selection_basis']}")
    for result in optimizer["results"]:
        final_val_loss = result["history"]["val_loss"][-1]
        print(f"  {result['optimizer']}: final val_loss = {final_val_loss:.4f}")
    print()
    print("Final comparison:")
    rows = [
        metric_row("Model A", model_a),
        metric_row("Model B", model_b),
        metric_row("MobileNetV2", mobilenet),
        metric_row("EfficientNetB0", efficientnet),
    ]
    print_table(rows)


if __name__ == "__main__":
    main()
