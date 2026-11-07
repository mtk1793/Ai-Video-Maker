# Windows setup

The sample scripts were executed on Linux; these Windows instructions have not been executed in this session.

1. Install Python 3.12 from python.org and enable its PATH option.
2. Install FFmpeg from the official download page: https://ffmpeg.org/download.html . Put its `bin` directory on PATH.
3. Open PowerShell in the repository folder.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ffmpeg -version
ffprobe -version
ffmpeg -filters | Select-String ' ass '
.\.venv\Scripts\python.exe scripts/prepare_sample.py --version v2
.\.venv\Scripts\python.exe examples/v2/edit_v2.py
.\.venv\Scripts\python.exe scripts/check_output.py examples/v2/AI_Is_Harmless_V2.mp4
```

Preparation downloads the original film (about 355 MiB), keeps it in a local cache, places a copy in the chosen example folder and extracts mono 16 kHz PCM audio. Downloads and renders are ignored by Git.

To regenerate the word transcript rather than use the included JSON:

```powershell
.\.venv\Scripts\python.exe examples/v2/transcribe_v2.py
```

To reproduce V1, use `--version v1` and run `examples/v1/edit.py`.

These are sample renderers. Replacing the input film without changing the sample-specific edit decisions will not produce a sensible automatic edit.
