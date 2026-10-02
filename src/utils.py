import os
import random
from pathlib import Path

import numpy as np
import tensorflow as tf

from . import config


def ensure_directories() -> None:
    for path in [
        config.DATA_PROCESSED_DIR,
        config.METRICS_DIR,
        config.FIGURES_DIR,
        config.CONFUSION_DIR,
        config.MODELS_DIR,
        config.REPORT_DIR,
        config.REPORT_DIR / "figures",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def set_global_determinism(seed: int = config.SEED) -> None:
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


def project_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(config.PROJECT_ROOT))
    except ValueError:
        return str(path)
