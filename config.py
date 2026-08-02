"""
==========================================
AI Lifting Risk Detection System
Configuration File
==========================================
"""

from pathlib import Path

# --------------------------------------------------
# ROOT DIRECTORY
# --------------------------------------------------

ROOT = Path(__file__).resolve().parent

# --------------------------------------------------
# DATASET
# --------------------------------------------------

DATASET_DIR = ROOT / "dataset"

IMAGE_DIR = DATASET_DIR / "images"

VIDEO_DIR = DATASET_DIR / "videos"

CSV_DIR = DATASET_DIR / "csv"

LABEL_DIR = DATASET_DIR / "labels"

# --------------------------------------------------
# MODEL
# --------------------------------------------------

MODEL_DIR = ROOT / "models"

YOLO_MODEL = MODEL_DIR / "yolo11n-pose.pt"

CLASSIFIER_MODEL = MODEL_DIR / "lifting_classifier.pt"

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

OUTPUT_DIR = ROOT / "output"

LOG_DIR = ROOT / "logs"

SCREENSHOT_DIR = OUTPUT_DIR / "screenshots"

VIDEO_OUTPUT_DIR = OUTPUT_DIR / "videos"

# --------------------------------------------------
# CAMERA
# --------------------------------------------------

CAMERA_ID = 0

FRAME_WIDTH = 1280

FRAME_HEIGHT = 720

FPS = 30

# --------------------------------------------------
# DISPLAY
# --------------------------------------------------

WINDOW_NAME = "AI Lifting Risk Detection"

FONT_SCALE = 0.8

LINE_THICKNESS = 2

# --------------------------------------------------
# POSE SETTINGS
# --------------------------------------------------

POSE_CONFIDENCE = 0.5

POSE_IOU = 0.45

# --------------------------------------------------
# RISK LEVEL
# --------------------------------------------------

SAFE_COLOR = (0,255,0)

WARNING_COLOR = (0,255,255)

DANGER_COLOR = (0,0,255)

SAFE_THRESHOLD = 0.40

WARNING_THRESHOLD = 0.70

# --------------------------------------------------
# TRAINING
# --------------------------------------------------

BATCH_SIZE = 32

EPOCHS = 100

LEARNING_RATE = 0.001

NUM_CLASSES = 3

DEVICE = "cuda"

# --------------------------------------------------
# DATABASE
# --------------------------------------------------

DATABASE = ROOT / "database.db"

# --------------------------------------------------
# REPORT
# --------------------------------------------------

EXPORT_DIR = ROOT / "reports"

# --------------------------------------------------
# CREATE FOLDERS AUTOMATICALLY
# --------------------------------------------------

folders = [

    DATASET_DIR,

    IMAGE_DIR,

    VIDEO_DIR,

    CSV_DIR,

    LABEL_DIR,

    MODEL_DIR,

    OUTPUT_DIR,

    LOG_DIR,

    SCREENSHOT_DIR,

    VIDEO_OUTPUT_DIR,

    EXPORT_DIR,

]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)