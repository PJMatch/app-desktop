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

LLM_MODEL_DIR = resource_path("llm_model")
LLM_MODEL_FILENAME = "minitron-Bielik-7B-v3.0-Instruct-GGUF.Q4_K_M.gguf"
LLM_MODEL_FILE = LLM_MODEL_DIR / LLM_MODEL_FILENAME
LLM_MODEL_URL = (
	"https://huggingface.co/speakleash/Bielik-Minitron-7B-v3.0-Instruct-GGUF/"
	"resolve/main/minitron-Bielik-7B-v3.0-Instruct-GGUF.Q4_K_M.gguf"
)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
BIELIK_MODEL_NAME = "bielik"
BIELIK_IDLE_SECONDS = 5.0
BIELIK_REQUEST_TIMEOUT = 120
BIELIK_PROMPT_TEMPLATE = (
	"Jesteś profesjonalnym tłumaczem Polskiego Języka Migowego (PJM). "
	"Zamień podane surowe glosy na naturalne, poprawne gramatycznie zdanie w języku polskim.\n\n"
	"BEZWZGLĘDNE ZASADY:\n"
	"1. Nie dodawaj żadnych słów, których nie ma w glosach. Jeśli nie jesteś pewien, czy coś dodać, NIE DODAWAJ tego.\n"
	"2. Ignoruj bezpośrednie powtórzenia (np. jeśli widzisz 'MAMA MAMA KUPIĆ', potraktuj to jako 'MAMA KUPIĆ').\n"
	"3. Zwróć TYLKO I WYŁĄCZNIE przetłumaczone zdanie. Nie dodawaj żadnych wstępów (np. 'Oto zdanie:'), komentarzy ani cudzysłowów.\n"
	"4. Odmieniaj słowa przez przypadki i używaj odpowiednich czasów, aby brzmiało to naturalnie.\n\n"
	"Glosy do przetłumaczenia: {glosses}"
)

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
