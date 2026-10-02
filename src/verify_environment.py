import json
import platform
import sys

import matplotlib
import numpy as np
import pandas as pd
import sklearn
import tensorflow as tf
from PIL import Image

from . import config


def main() -> None:
    config.METRICS_DIR.mkdir(parents=True, exist_ok=True)
    info = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "tensorflow": tf.__version__,
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "matplotlib": matplotlib.__version__,
        "scikit_learn": sklearn.__version__,
        "pillow": Image.__version__,
        "tensorflow_physical_gpus": [device.name for device in tf.config.list_physical_devices("GPU")],
        "tensorflow_physical_cpus": [device.name for device in tf.config.list_physical_devices("CPU")],
        "gpu_available": bool(tf.config.list_physical_devices("GPU")),
    }
    config.ENVIRONMENT_JSON.write_text(json.dumps(info, indent=2), encoding="utf-8")
    print(json.dumps(info, indent=2))


if __name__ == "__main__":
    main()
