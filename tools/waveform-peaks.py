"""Print the waveform peaks for the music player's TRACKS list in index.html.

Each track gets its duration and 160 loudness values from 0 to 99, one per slice of the piece,
so the page can draw the waveform without downloading the audio. Needs ffmpeg and numpy.

    python3 tools/waveform-peaks.py assets/music/*.m4a

Paste each printed `dur` and `peaks` into the matching entry of TRACKS.
"""
import subprocess
import sys

import numpy as np

BUCKETS = 160
RATE = 22050


def peaks(path):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(RATE), "-f", "f32le", "-"],
        check=True, capture_output=True,
    ).stdout
    samples = np.frombuffer(raw, dtype=np.float32)
    slices = np.array_split(samples, BUCKETS)
    rms = np.array([np.sqrt(np.mean(np.square(s, dtype=np.float64))) if len(s) else 0.0 for s in slices])
    level = rms / max(rms.max(), 1e-9)  # loudness relative to the loudest slice
    return len(samples) / RATE, [int(round(v * 99)) for v in level]


for path in sys.argv[1:]:
    dur, values = peaks(path)
    print(f"// {path}")
    print(f"dur: {dur:.2f},")
    print(f"peaks: [{','.join(map(str, values))}]")
