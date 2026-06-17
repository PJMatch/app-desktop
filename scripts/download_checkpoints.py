"""Download checkpoint files from GitHub Releases."""

import sys
import urllib.request
from pathlib import Path

REPO = "PJMatch/desktop-app"
RELEASE = "v0.1.0"

CHECKPOINTS = {
    "cslr_model.pth": (
        f"https://github.com/{REPO}/releases/download/{RELEASE}/cslr_model.pth"
    ),
    "islr_model.pth": (
        f"https://github.com/{REPO}/releases/download/{RELEASE}/islr_model.pth"
    ),
}


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {dest.name} from GitHub Releases...")
    urllib.request.urlretrieve(url, dest)


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    checkpoint_dir = root / "checkpoints"

    for name, url in CHECKPOINTS.items():
        dest = checkpoint_dir / name
        if dest.exists():
            print(f"{name} already present, skipping.")
            continue
        try:
            download(url, dest)
            print(f"Saved to {dest}")
        except Exception as exc:
            print(f"Failed to download {name}: {exc}", file=sys.stderr)
            print(
                f"Upload {name} to a GitHub Release tagged {RELEASE} "
                f"at https://github.com/{REPO}/releases",
                file=sys.stderr,
            )
            sys.exit(1)


if __name__ == "__main__":
    main()
