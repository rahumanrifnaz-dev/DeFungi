import json
from pathlib import Path

from . import config


def load_json(path: Path):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return None


def append_json_section(lines: list[str], title: str, path: Path) -> None:
    lines.append(f"## {title}")
    data = load_json(path)
    if data is None:
        lines.append(f"Not generated yet. Expected file: `{path.relative_to(config.PROJECT_ROOT)}`")
        lines.append("")
        return
    lines.append("```json")
    lines.append(json.dumps(data, indent=2))
    lines.append("```")
    lines.append("")


def append_text_section(lines: list[str], title: str, path: Path) -> None:
    lines.append(f"## {title}")
    if not path.exists():
        lines.append(f"Not generated yet. Expected file: `{path.relative_to(config.PROJECT_ROOT)}`")
        lines.append("")
        return
    lines.append("```text")
    lines.append(path.read_text(encoding="utf-8"))
    lines.append("```")
    lines.append("")


def append_history_section(lines: list[str], title: str, path: Path) -> None:
    lines.append(f"## {title}")
    if not path.exists():
        lines.append(f"Not generated yet. Expected file: `{path.relative_to(config.PROJECT_ROOT)}`")
        lines.append("")
        return
    lines.append("```csv")
    lines.extend(path.read_text(encoding="utf-8").strip().splitlines())
    lines.append("```")
    lines.append("")


def append_artifact_list(lines: list[str], title: str, paths: list[Path]) -> None:
    lines.append(f"## {title}")
    existing_paths = [path for path in paths if path.exists()]
    if not existing_paths:
        lines.append("No artifacts generated yet.")
        lines.append("")
        return
    for path in existing_paths:
        size_kb = path.stat().st_size / 1024
        lines.append(f"- `{path.relative_to(config.PROJECT_ROOT)}` ({size_kb:.1f} KB)")
    lines.append("")


def metric_path(stem: str) -> Path:
    return config.METRICS_DIR / stem


def main() -> None:
    config.REPORT_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Report Data",
        "",
        "This file is generated from verified project outputs only. Missing sections mean the corresponding code has not been executed yet.",
        "",
    ]
    append_json_section(lines, "Environment", config.ENVIRONMENT_JSON)
    append_json_section(lines, "Dataset Statistics", config.DATASET_SUMMARY_JSON)
    append_json_section(lines, "Custom Pipeline Check", config.PIPELINE_CHECK_JSON)
    append_json_section(lines, "Model Parameter Checks", config.METRICS_DIR / "model_parameter_checks.json")
    append_json_section(lines, "Smoke Test Results", metric_path("smoke_test_results.json"))
    append_json_section(lines, "Optimizer Experiment Results", metric_path("optimizer_experiment_results.json"))
    append_text_section(lines, "Model A Summary", metric_path("model_a_summary.txt"))
    append_text_section(lines, "Model B Summary", metric_path("model_b_summary.txt"))

    for path in sorted(config.METRICS_DIR.glob("*_metrics.json")):
        append_json_section(lines, path.stem.replace("_", " ").title(), path)

    for path in sorted(config.METRICS_DIR.glob("*_history.csv")):
        append_history_section(lines, f"{path.stem.replace('_', ' ').title()} CSV", path)
    append_artifact_list(
        lines,
        "Generated Figures",
        sorted(config.FIGURES_DIR.glob("*.png")) + sorted(config.CONFUSION_DIR.glob("*.png")),
    )
    append_artifact_list(lines, "Saved Models", sorted(config.MODELS_DIR.glob("*.keras")))
    append_artifact_list(
        lines,
        "Processed Split Files",
        [config.SPLITS_CSV, config.TRAIN_CSV, config.VALIDATION_CSV, config.TEST_CSV],
    )

    output_path = config.REPORT_DIR / "report_data.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
