# Ten implemented pipeline references

Reviewed 2026-11-07. These are ten distinct projects/workflows, not ten different web domains. Public implementation evidence does not verify revenue, audience growth or private production reliability. No third-party source code is vendored here.

| Project | Evidence inspected | Lesson | Verification boundary |
|---|---|---|---|
| [Auto-Editor](https://auto-editor.com/docs/cookbook) | CLI recipes and source README | Silence removal with speech padding, preview and editor handoff | Docs reviewed; not installed in this session |
| [AutoCut](https://github.com/mli/autocut) | README and autocut/cut.py inspected | Editable transcript selections; merge nearby retained intervals | Source inspected; not executed |
| [Auto-Subtitle](https://github.com/m1guelpf/auto-subtitle) | README and auto_subtitle/cli.py inspected | Extract mono 16 kHz audio, transcribe, save SRT, burn captions | Source inspected; not executed |
| [CutCannon](https://github.com/lowerpower/cutcannon) | README plus bin/plan.py and bin/qa.py inspected | Versioned frozen edit plans and QA reports | Source inspected; author-reported timings are not independent measurements |
| [Remotion TikTok template](https://www.remotion.dev/templates/tiktok) | Runnable template and caption implementation documentation | Separate timed caption data from reusable animation | Documentation and source README reviewed; not rendered |
| [Short Video Maker](https://github.com/gyoridavid/short-video-maker) | README, example outputs, Docker and REST workflow documentation | Scene model, async job status and limited concurrency | Implementation documentation reviewed; not deployed |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | README and app/services/video.py inspected | Independent audio/style configuration and codec fallback | Source inspected; not executed |
| [n8n long video to shorts](https://n8n.io/workflows/9867-transform-long-videos-into-viral-shorts-with-ai-and-schedule-to-social-media-using-whisper-and-gemini/) | Published workflow and setup instructions | Separate transcription, moment selection, rendering and job polling | Workflow documentation reviewed; paid services not connected |
| [Creatomate captions workflow](https://creatomate.com/blog/how-to-automatically-add-subtitles-to-videos-with-n8n) | Step-by-step workflow and demonstrated output | Reuse one tested caption template across input videos | Vendor tutorial reviewed; service not run |
| [Shotstack rich captions](https://shotstack.io/docs/guide/architecting-an-application/rich-captions/) | Concrete JSON timeline examples and caption documentation | Explicit source aliases and timestamp-driven caption effects | API documentation reviewed; service not called |

Additional alignment reference: https://github.com/m-bain/whisperX — forced alignment can improve word timestamps. Reviewed as a component, not counted as an additional complete editing pipeline.

The reference most similar to the intended local architecture is CutCannon: transcript → versioned edit plan → render → QA. This is an architectural inference, not an endorsement of untested runtime reliability.
