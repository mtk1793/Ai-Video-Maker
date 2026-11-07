# Reusable pipeline design

This document describes the next architecture. Features below are a design, not claims that the example scripts implement them.

## Stages and saved results

| Stage | Saved result | Purpose |
|---|---|---|
| Inspect input | `media.json` | Dimensions, timebase, frame rate, duration, audio streams and source checksum |
| Transcribe | `words.json`, `transcript.txt` | Cache speech and word times; preserve original timestamps |
| Select moments | `candidates.json` | Complete, self-contained moments with setup and payoff |
| Edit plan | `plans/v001.json` | Ordered source intervals, crop/layout, captions, audio and effect decisions |
| Preview | `preview.mp4`, contact sheet | Inspect the edit before the expensive final export |
| Render | `final.mp4`, `.srt` | Execute the plan deterministically |
| QA | `qa.json` | Decode, duration, A/V timing, loudness, caption coverage, word boundaries and framing |

An edit plan should carry explicit seconds and a source checksum. Saving a revised transcript must not silently change a previously approved cut. Corrections to technical vocabulary should be separate from raw recognition output.

## Teaching layout

Keep formulas, diagrams, slide labels and the complete worked step visible. Place the webcam separately when helpful. Use transcript-based selection around a question, explanation and answer. Do not remove a quiet writing step merely because speech stopped. Use a configurable vocabulary list for engineering terms.

## Gaming layout

Preserve the action and relevant HUD. Select moments using scene/action changes, audio events and commentary together. Keep reaction context. Caption speech, not invented dialogue over silent action. Use effects only where they support an event.

## Reliability

Cache transcription, resume failed stages, record versions and FFmpeg commands, check input ranges, keep generated files out of Git, and render one job at a time on small machines. Keep source media unchanged. Human review decides whether the clip tells a coherent story.

## Evidence boundary

The linked projects demonstrate implementation approaches through code, documentation, examples or author-reported measurements. Their revenue, audience retention and private production reliability were not independently verified. No claims of guaranteed virality are made.
