## PJMatch

Desktop app for sign language recognition (CSLR / ISLR).

### Requirements

- Python >= 3.14
- [uv](https://docs.astral.sh/uv/)

### Running

```bash
uv sync
uv run python scripts/download_checkpoints.py   # downloads model weights from GitHub Releases
uv run pjmatch.py
```

Prediction logs are written to `~/.pjmatch/prediction_log.txt`.

### Models

Model weights (`checkpoints/*.pth`) are hosted in [GitHub Releases](https://github.com/PJMatch/desktop-app/releases), not in the repository. The `download_checkpoints.py` script fetches them automatically.

The `mediapipe_tasks/` files are included in the repository.

### Publishing (maintainers)

**Push to a new GitHub repo:**

```bash
git remote add origin https://github.com/PJMatch/desktop-app.git
git push -u origin main
```

**Upload model weights to Releases:**

1. Go to the repo on GitHub → **Releases** → **Create a new release**
2. Tag: `v0.1.0` (must match `RELEASE` in `scripts/download_checkpoints.py`)
3. Attach both files with exact names:
   - `cslr_model.pth`
   - `islr_model.pth`
4. Publish release

Verify downloads work:

```bash
curl -I https://github.com/PJMatch/desktop-app/releases/download/v0.1.0/cslr_model.pth
curl -I https://github.com/PJMatch/desktop-app/releases/download/v0.1.0/islr_model.pth
```

Both should return `HTTP/2 302` (redirect to the file).

### Other scripts

```bash
uv run evaluate.py      # model evaluation
uv run camera_label.py  # camera labeling
uv run cam_test.py      # camera test
```
