import json
import io

from . import config
from .models import build_model_a, build_model_b, parameter_storage_kb, separable_conv_parameter_count
from .utils import ensure_directories, set_global_determinism


def save_summary(model, path):
    buffer = io.StringIO()
    model.summary(print_fn=lambda line: buffer.write(line + "\n"))
    path.write_text(buffer.getvalue(), encoding="utf-8")


def main() -> None:
    set_global_determinism()
    ensure_directories()

    model_a = build_model_a()
    model_b = build_model_b()

    model_a_params = model_a.count_params()
    model_b_params = model_b.count_params()

    if model_a_params != 101_829:
        raise AssertionError(f"Model A parameter count is {model_a_params}, expected 101829.")
    if model_b_params > 100_000:
        raise AssertionError(f"Model B parameter count is {model_b_params}, expected <= 100000.")

    report = {
        "model_a": {
            "trainable_parameters": model_a_params,
            "expected_trainable_parameters": 101_829,
            "fp32_parameter_storage_kb": round(parameter_storage_kb(model_a_params), 2),
            "notes": [
                "ReLU is hardware-friendly because it mainly uses a simple max(0, x) operation.",
                "Global Average Pooling reduces parameters compared with Flatten followed by large Dense layers.",
            ],
        },
        "model_b": {
            "trainable_parameters": model_b_params,
            "parameter_limit": 100_000,
            "fp32_parameter_storage_kb": round(parameter_storage_kb(model_b_params), 2),
            "standard_conv_formula": "(kernel_h * kernel_w * input_channels + bias) * output_channels",
            "separable_conv_formula": "Keras SeparableConv2D with use_bias=True: depthwise kernel_h * kernel_w * input_channels; pointwise input_channels * output_channels; bias output_channels",
            "sepconv_examples": {
                "3_to_32": separable_conv_parameter_count(3, 32),
                "32_to_64": separable_conv_parameter_count(32, 64),
                "64_to_96": separable_conv_parameter_count(64, 96),
            },
        },
    }

    out_path = config.METRICS_DIR / "model_parameter_checks.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    save_summary(model_a, config.METRICS_DIR / "model_a_summary.txt")
    save_summary(model_b, config.METRICS_DIR / "model_b_summary.txt")
    model_a.summary()
    model_b.summary()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
