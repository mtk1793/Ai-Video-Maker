"""Decode a video, report stream properties and measure audio loudness."""
import argparse
import json
from pathlib import Path
import subprocess

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('video', type=Path)
    ap.add_argument('--report', type=Path)
    args = ap.parse_args()
    if not args.video.is_file():
        ap.error('Video does not exist')
    probe = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format',
                            '-of', 'json', str(args.video)], check=True, capture_output=True, text=True)
    metadata = json.loads(probe.stdout)
    streams = metadata['streams']
    if not any(s['codec_type'] == 'video' for s in streams):
        ap.error('No video stream')
    subprocess.run(['ffmpeg', '-v', 'error', '-i', str(args.video), '-f', 'null', '-'], check=True)
    report = {'file': args.video.name, 'full_decode': 'passed',
              'duration_seconds': float(metadata['format']['duration']),
              'streams': [{k: s[k] for k in ['codec_type', 'codec_name', 'width', 'height', 'r_frame_rate'] if k in s}
                          for s in streams]}
    if any(s['codec_type'] == 'audio' for s in streams):
        measured = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', str(args.video),
                                  '-vn', '-af', 'loudnorm=I=-15:TP=-1.5:LRA=9:print_format=json',
                                  '-f', 'null', '-'], check=True, capture_output=True, text=True)
        start = measured.stderr.rfind('{')
        end = measured.stderr.rfind('}')
        if start >= 0 and end > start:
            report['loudness_measurement'] = json.loads(measured.stderr[start:end+1])
    report['scope'] = 'Technical decode and measurements only; no automatic story, caption or framing approval.'
    output = json.dumps(report, indent=2) + '\n'
    if args.report:
        args.report.write_text(output, encoding='utf-8')
    print(output)

if __name__ == '__main__':
    main()
