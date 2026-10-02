from pathlib import Path

SEED = 42
IMAGE_SIZE = (64, 64)
CHANNELS = 3
NUM_CLASSES = 5
BATCH_SIZE = 32

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw" / "defungi"
DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"
METRICS_DIR = RESULTS_DIR / "metrics"
FIGURES_DIR = RESULTS_DIR / "figures"
CONFUSION_DIR = RESULTS_DIR / "confusion_matrices"
MODELS_DIR = RESULTS_DIR / "models"
REPORT_DIR = PROJECT_ROOT / "report"

SPLITS_CSV = DATA_PROCESSED_DIR / "splits.csv"
TRAIN_CSV = DATA_PROCESSED_DIR / "train.csv"
VALIDATION_CSV = DATA_PROCESSED_DIR / "validation.csv"
TEST_CSV = DATA_PROCESSED_DIR / "test.csv"
DATASET_SUMMARY_JSON = METRICS_DIR / "dataset_summary.json"
ENVIRONMENT_JSON = METRICS_DIR / "environment_info.json"
PIPELINE_CHECK_JSON = METRICS_DIR / "custom_pipeline_check.json"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
