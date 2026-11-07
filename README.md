# Shortform Video Lab

FFmpeg + Whisper editing experiments for gaming Shorts and online teaching clips, with a curated collection of 20 YouTube tutorials and 10 implemented pipeline projects.

## Status

The V1 and V2 examples rendered and passed a complete FFmpeg decode check in the original session. They are **film-specific editing experiments**, with manually chosen cut points and crop positions. They do not automatically select highlights from a new recording. The external projects were researched, not all installed or tested end to end.

## Contents

- `examples/v1/`: first 720 × 1280, approximately 22-second edit, transcription script, timed captions and transcript.
- `examples/v2/`: approximately 12-second, 1080 × 1920 edit, highlighted captions, original synthesized sound effects and a revised Whisper transcript.
- `research/tutorials.json`: 20 tutorial links and review coverage.
- `research/tutorial_review.md`: tutorial research and original V2 notes.
- `research/pipelines.md` and `research/pipelines.json`: 10 implementation references, evidence and lessons.
- `docs/pipeline_design.md`: a reusable pipeline design for teaching and gaming, clearly separated from implemented functionality.
- `docs/windows_setup.md`: Windows setup and reproduction commands.
- `scripts/prepare_sample.py`: downloads the sample film and extracts the audio needed by either example.
- `scripts/check_output.py`: checks decodability and reports stream dimensions, duration and audio loudness.

## Quick start

Install Python 3.12 and FFmpeg, including `ffprobe` and the `ass` filter. Then:

```sh
python -m pip install -r requirements.txt
python scripts/prepare_sample.py --version v2
python examples/v2/edit_v2.py
python scripts/check_output.py examples/v2/AI_Is_Harmless_V2.mp4
```

The renderer uses the included transcript. To regenerate it:

```sh
python examples/v2/transcribe_v2.py
```

The first transcription run downloads the Whisper model. FFmpeg performs rendering on the CPU. See [Windows setup](docs/windows_setup.md).

## Sample outputs

The sample renders are available in the accompanying project archive:

[Download V2 project and video from ChatGPT](https://chatgpt.com/library?file_id=libfile_8b68b0a71f388191be959bd0a2f1c3f5&account_id=personal)

This link requires access to the owner's ChatGPT Library; it is not a public media-hosting link. Anyone can reproduce the examples from the freely downloadable film using the commands above. Large source films, generated media, model weights, full tutorial transcripts and third-party repositories are not committed.

## Known limitations

- Edit times and portrait crop positions are specific to *Tears of Steel*.
- V2's original zoom pipeline can distort the picture's aspect ratio. It is retained as an experiment, not a production-quality reframing implementation.
- V2 has broad, manually timed caption text for the final reaction; it is not a new aligned transcription of that shot.
- Automated QA checks technical validity; it cannot establish humor, storytelling quality or likely reach.
- A face crop can destroy the meaning of teaching footage by hiding equations. Preserve the board or slides in a dedicated teaching layout.
- No publishing, credentials, paid APIs or automatic uploads are configured.

## Attribution and ownership

Film: **Tears of Steel**, (CC) Blender Foundation | https://mango.blender.org/ . Licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). The examples change framing, editing, captions and audio treatment. Original film: https://download.blender.org/demo/movies/ToS/tears_of_steel_720p.mov .

External repositories remain owned by their authors and retain their own licenses. This repository collects links and original research summaries; it does not relicense or redistribute their code. See [THIRD_PARTY.md](THIRD_PARTY.md).
