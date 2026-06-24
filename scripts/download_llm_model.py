"""Download the Bielik GGUF model used by the LLM worker."""

import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import consts


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {dest.name} from Hugging Face...")
    urllib.request.urlretrieve(url, dest)


def main() -> None:
    dest = consts.LLM_MODEL_FILE
    if dest.exists():
        print(f"{dest.name} already present, skipping.")
        return
    try:
        download(consts.LLM_MODEL_URL, dest)
        print(f"Saved to {dest}")
    except Exception as exc:
        print(f"Failed to download {dest.name}: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
