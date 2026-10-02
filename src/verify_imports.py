from . import config
from .models import build_model_a, build_model_b
from .utils import ensure_directories, set_global_determinism


def main() -> None:
    set_global_determinism()
    ensure_directories()
    model_a = build_model_a()
    model_b = build_model_b()
    print("Imports OK")
    print(f"Project root: {config.PROJECT_ROOT}")
    print(f"Model A parameters: {model_a.count_params()}")
    print(f"Model B parameters: {model_b.count_params()}")


if __name__ == "__main__":
    main()
