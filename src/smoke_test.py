import argparse
import json
import math

import tensorflow as tf

from . import config
from .datasets import make_custom_dataset
from .models import build_model_a, build_model_b
from .train_custom import build_optimizer
from .utils import ensure_directories, set_global_determinism


def build_model(name: str) -> tf.keras.Model:
    if name == "model_a":
        return build_model_a()
    if name == "model_b":
        return build_model_b()
    raise ValueError(f"Unknown model: {name}")


def run_smoke(model_name: str, optimizer_name: str, train_batches: int, validation_batches: int) -> dict:
    set_global_determinism()
    train_ds = make_custom_dataset("train", shuffle=True).take(train_batches)
    val_ds = make_custom_dataset("validation").take(validation_batches)
    model = build_model(model_name)
    model.compile(
        optimizer=build_optimizer(optimizer_name),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    history = model.fit(train_ds, validation_data=val_ds, epochs=1, verbose=2, shuffle=False)
    losses = history.history.get("loss", [])
    val_losses = history.history.get("val_loss", [])
    all_losses = losses + val_losses
    if not all(math.isfinite(float(value)) for value in all_losses):
        raise AssertionError(f"Non-finite loss encountered during {model_name} smoke test.")
    return {
        "model": model_name,
        "optimizer": optimizer_name,
        "train_batches": train_batches,
        "validation_batches": validation_batches,
        "epochs": 1,
        "history": {key: [float(v) for v in values] for key, values in history.history.items()},
        "passed": True,
        "note": "Smoke-test metrics are for pipeline verification only and are not final experimental results.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run short Model A/B training smoke tests.")
    parser.add_argument("--optimizer", choices=["adam", "sgd", "sgd_momentum"], default="adam")
    parser.add_argument("--train-batches", type=int, default=3)
    parser.add_argument("--validation-batches", type=int, default=1)
    args = parser.parse_args()

    ensure_directories()
    results = [
        run_smoke("model_a", args.optimizer, args.train_batches, args.validation_batches),
        run_smoke("model_b", args.optimizer, args.train_batches, args.validation_batches),
    ]
    out_path = config.METRICS_DIR / "smoke_test_results.json"
    out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
