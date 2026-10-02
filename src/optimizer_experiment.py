import argparse
import json
import time

import tensorflow as tf

from . import config
from .datasets import make_custom_dataset
from .models import build_model_b
from .train_custom import build_optimizer
from .utils import ensure_directories, set_global_determinism


def run_optimizer(optimizer_name: str, epochs: int, train_batches: int, validation_batches: int) -> dict:
    set_global_determinism()
    train_ds = make_custom_dataset("train", shuffle=True).take(train_batches)
    val_ds = make_custom_dataset("validation")
    if validation_batches > 0:
        val_ds = val_ds.take(validation_batches)
    model = build_model_b()
    optimizer = build_optimizer(optimizer_name)
    model.compile(optimizer=optimizer, loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    start = time.perf_counter()
    history = model.fit(train_ds, validation_data=val_ds, epochs=epochs, verbose=2, shuffle=False)
    elapsed = time.perf_counter() - start
    cfg = optimizer.get_config()
    return {
        "model": "model_b",
        "optimizer": optimizer_name,
        "learning_rate": float(tf.keras.backend.get_value(optimizer.learning_rate)),
        "momentum": float(cfg.get("momentum", 0.0)),
        "epochs": epochs,
        "train_batches_per_epoch": train_batches,
        "validation_batches_per_epoch": validation_batches if validation_batches > 0 else "all",
        "elapsed_seconds": round(elapsed, 4),
        "history": {key: [float(v) for v in values] for key, values in history.history.items()},
        "note": "Controlled optimizer comparison on a limited subset; not a final model result.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Controlled optimizer comparison for custom CNN training.")
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--train-batches", type=int, default=30)
    parser.add_argument("--validation-batches", type=int, default=0)
    args = parser.parse_args()

    ensure_directories()
    results = [
        run_optimizer("adam", args.epochs, args.train_batches, args.validation_batches),
        run_optimizer("sgd", args.epochs, args.train_batches, args.validation_batches),
        run_optimizer("sgd_momentum", args.epochs, args.train_batches, args.validation_batches),
    ]
    selected = min(results, key=lambda item: item["history"]["val_loss"][-1])
    output = {
        "selected_optimizer": selected["optimizer"],
        "selection_basis": "lowest final validation loss in the controlled limited-training-batch comparison using the full validation split",
        "results": results,
    }
    out_path = config.METRICS_DIR / "optimizer_experiment_results.json"
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
