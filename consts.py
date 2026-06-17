"""Module holding const values and app path helpers."""

import sys
from pathlib import Path


def resource_path(relative_path: str) -> Path:
	"""Return a bundled-resource path that works from source and PyInstaller."""
	base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
	return base_path / relative_path


def writable_path(*parts: str) -> Path:
	"""Return a user-writable application path for logs and other runtime files."""
	return Path.home() / ".pjmatch" / Path(*parts)


TASKS_DIR = resource_path("mediapipe_tasks")
CONFIG_FILE = resource_path("config.yaml")
UI_FILE = resource_path("res/ui/main_window.ui")
PREDICTION_LOG_FILE = writable_path("prediction_log.txt")

SLIDING_WINDOW_LENGTH_CSLR = 220
STRIDE_CSLR = 15

SLIDING_WINDOW_LENGTH_ISLR = 30
STRIDE_ISLR = 5
ISLR_CONFIDENCE_THRESHOLD = 0.75
ISLR_CUMULATIVE_THRESHOLD = 1.9

VOTE_THRESHOLD = 3

POSE_LEN = 33
FACE_LEN = 478
LH_LEN = 21
RH_LEN = 21
TOTAL_V = POSE_LEN + FACE_LEN + LH_LEN + RH_LEN
TESTING_VIDEO_PATH = r"local"
