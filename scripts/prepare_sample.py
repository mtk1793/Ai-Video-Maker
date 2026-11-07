"""Prepare the attributed Blender sample for either film-specific renderer."""
import argparse
from pathlib import Path
import shutil
import subprocess
import urllib.request

URL = 'https://download.blender.org/demo/movies/ToS/tears_of_steel_720p.mov'
ROOT = Path(__file__).resolve().parents[1]

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--version', choices=['v1', 'v2'], default='v2')
    ap.add_argument('--source', type=Path, help='Use an existing local copy instead of downloading')
    args = ap.parse_args()
    for tool in ['ffmpeg', 'ffprobe']:
        if not shutil.which(tool):
            ap.error(f'{tool} is not on PATH')
    target = ROOT / 'examples' / args.version
    cache = ROOT / '.cache'
    cache.mkdir(exist_ok=True)
    source = args.source.resolve() if args.source else cache / 'tears_of_steel_720p.mov'
    if args.source and not source.is_file():
        ap.error(f'Source does not exist: {source}')
    if not source.exists():
        temporary = source.with_suffix('.download')
        print('Downloading Tears of Steel (about 355 MiB), CC BY 3.0 ...', flush=True)
        try:
            with urllib.request.urlopen(URL, timeout=60) as response, temporary.open('wb') as out:
                shutil.copyfileobj(response, out)
            subprocess.run(['ffprobe', '-v', 'error', str(temporary)], check=True)
            temporary.replace(source)
        finally:
            temporary.unlink(missing_ok=True)
    destination = target / 'source.mp4'
    if not destination.exists():
        shutil.copyfile(source, destination)
    start, duration, name = (30, 90, 'audio.wav') if args.version == 'v1' else (30, 13, 'dialogue.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(start), '-i', str(destination),
                    '-t', str(duration), '-ar', '16000', '-ac', '1', '-c:a', 'pcm_s16le',
                    str(target / name)], check=True)
    print(f'Prepared {args.version}: {destination}')
    print('Film credit: (CC) Blender Foundation | mango.blender.org | CC BY 3.0')

if __name__ == '__main__':
    main()
