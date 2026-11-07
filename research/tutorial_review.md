# V2 editing research and project notes

Review method: 20 YouTube tutorial pages. Caption material reviewed for 14 videos; descriptions/chapters reviewed for six whose caption requests were rate-limited. The zoom tutorial is chiefly a visual demonstration, so its published FFmpeg examples were used. This is not a claim to have watched 20 complete videos.

| # | Tutorial | Evidence reviewed | Application |
|---|---|---|---|
| 1 | [Master Viral Sound Design for Short-Form Content! (The Ultimate Guide)](https://www.youtube.com/watch?v=HqPDRa7i97s) | Description / chapters only | Audio hierarchy; restrained SFX |
| 2 | [3 Sound Design Secrets That Feel Like CHEATING](https://www.youtube.com/watch?v=tzfzkTAQsnE) | Caption excerpts + description | Layer motion sound and low impact |
| 3 | [The Ultimate Guide to Master Short-Form Video Editing! (Easy Guide)](https://www.youtube.com/watch?v=R9Uu0JtvyMg) | Caption excerpts + description | Shorten setup and plan payoff |
| 4 | [How to Edit ANY Video Like You’ve Done it 1,000 Times](https://www.youtube.com/watch?v=Zm7J3KqqXPk) | Caption excerpts + description | Analyze references before adding effects |
| 5 | [The ONLY 3 Sound Effects You Need to Tell Any Story](https://www.youtube.com/watch?v=JOm_EqBoW0M) | Caption excerpts + description | Whoosh, riser and impact vocabulary |
| 6 | [MASTER Short Form Content Editing | DaVinci Resolve 2026](https://www.youtube.com/watch?v=EEV3E2U0keQ) | Caption excerpts + description | Remove pauses, crop and add push-ins |
| 7 | [Create Viral Motion Graphic Titles & Sound Design - DaVinci Resolve](https://www.youtube.com/watch?v=t_PPy3H1Q64) | Description / chapters only | Pair motion with audio |
| 8 | [How To Create 10 VIRAL Caption Styles Using CapCut](https://www.youtube.com/watch?v=Q04FF5KZyt4) | Caption excerpts + description | Readable active-word accents |
| 9 | [The Power of SIMPLE Editing](https://www.youtube.com/watch?v=pdLEHfkwgV8) | Caption excerpts + description | Use a sequence that advances one idea |
| 10 | [Complete Guide to Sound Design any Video like a PRO](https://www.youtube.com/watch?v=FjpnOstqBvs) | Description / chapters only | Keep speech above effects |
| 11 | [4 CapCut Sensory Sound Design Techniques](https://www.youtube.com/watch?v=eDuEd5TMjSQ) | Description / chapters only | Break pacing at the reveal |
| 12 | [How I Sound Design My Video in Capcut (Secret Sauce)](https://www.youtube.com/watch?v=05RfJDgJ4Pw) | Caption excerpts + description | Match whoosh duration to movement |
| 13 | [Make Your Videos 10x Better with CapCut Sound Effects](https://www.youtube.com/watch?v=uG5CP9FtyCM) | Caption excerpts + description | Layer custom effects under dialogue |
| 14 | [Everything You Need to Know About Sound Design in 2025! (Complete Guide)](https://www.youtube.com/watch?v=98CzEo5PIZ4) | Caption excerpts + description | Build audio in separate passes |
| 15 | [Sound Design Master Class | Full Course | Basic to Advanced](https://www.youtube.com/watch?v=LFHtCTjwKjc) | Description / chapters only | Synthesize simple original effects |
| 16 | [EASIEST Way to Sound Design Reels | Full Breakdown](https://www.youtube.com/watch?v=CQcO3_AnqnQ) | Caption excerpts + description | Motion, foley and atmosphere roles |
| 17 | [How to Auto-Generate Subtitles for Videos using Python, OpenAI Whisper & FFMPEG](https://www.youtube.com/watch?v=cc6-3x_Dff8) | Caption excerpts + description | Audio extraction → Whisper → timed captions |
| 18 | [How to zoom and pan onto a video | Zooming and panning VFX  #ffmpeg #TheFFMPEGGuy](https://www.youtube.com/watch?v=j04M7t9Vo1Q) | Published command examples; nonverbal captions | Small centered progressive zoom |
| 19 | [The Fastest Way to Create YouTube Shorts from Long Videos (FFmpeg)](https://www.youtube.com/watch?v=bitTxzaRPMk) | Caption excerpts + description | Portrait subject reframing |
| 20 | [How To Add Alex Hormozi Captions To Reels & TikToks For FREE (Full Tutorial)](https://www.youtube.com/watch?v=CFjFRIn38Ms) | Description / chapters only | Bold short caption phrases |

## Actual changes
- Rebuilt from the source film rather than recompressing V1.
- 1080 × 1920 portrait export with subject-specific crops and gentle push-ins.
- Setup → admission → robot reveal → reaction, with pauses removed.
- Re-transcribed the dialogue with Whisper base.en and generated word-highlighted ASS captions.
- Synthesized original bass hits, whooshes and a short riser.
- Reduced montage sound beneath effects, then normalized the complete mix.
- Retained Blender attribution in the picture.

## Run
Install FFmpeg on PATH and Python 3.10+. Install numpy and faster-whisper with `python -m pip install numpy faster-whisper`.
Download https://download.blender.org/demo/movies/ToS/tears_of_steel_720p.mov as source.mp4 in this folder.
Run `python edit_v2.py`. The included transcript_v2.json lets the renderer run without transcribing again.
To regenerate the transcript: extract 13 seconds from source offset 30 into dialogue.wav (mono PCM, 16 kHz), then run transcribe_v2.py.

## Dependencies
FFmpeg and faster-whisper were already present from V1. Installed yt-dlp for this research. Downloaded Whisper base.en for the revised transcription. No paid editor or plugins used.

## Source credit
Tears of Steel — (CC) Blender Foundation | mango.blender.org. CC BY 3.0: https://creativecommons.org/licenses/by/3.0/ . This project changes the edit, framing, captions and audio treatment.

Technical references: https://ffmpeg.org/ffmpeg-filters.html and https://github.com/SYSTRAN/faster-whisper .
No prediction or guarantee of virality.

Repository reproduction instructions supersede the original folder assumptions above; see ../docs/windows_setup.md. V2 retains its original film-specific timing and experimental reframing limitations.
