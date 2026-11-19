# Richard Shi Zhang 张时

My personal website. Static pages with no build step: the home page is [index.html](index.html), the Sundays in LA page is [sundays.html](sundays.html), and the photos, video and music are in [assets/](assets/). Each page keeps its markup, styles and scripts in the one file.

## Preview it

From this folder:

```bash
python3 tools/serve.py
```

Then open http://localhost:8642. This is Python's built-in file server plus byte ranges, which GitHub Pages also sends. Without them the browser can't seek in the music, so the player's waveform can't skip ahead or back.

## How the page behaves

| Part | What it does |
| --- | --- |
| Sky colours | Follows the visitor's own clock: day 7am–5pm, dusk 5–7am and 5–8pm, night otherwise. Add `?time=day`, `?time=dusk` or `?time=night` to the address to force one. |
| Time-of-day slider | Under "See the work" in the hero. It starts at the visitor's current time; dragging it repaints the page for that hour until "Back to now". |
| Loading screen | The 时 stroke-order board with a mullet that hops, lands on its side, then leaps again and flops onto its back; the strokes are timed to the fish and start when its animation loads. Shows on every page load and stays until 时 is fully drawn (about 3.5 s) and the page has loaded, but never more than 6 s. "Enter →" skips it. The timings are `MIN_MS` and `MAX_MS` near the bottom of index.html. |
| Music | The swallows on the staff and the track list share one player. The card under the staff draws the playing piece as an ink stroke, thick where it's loud and red as far as you've listened. Click or drag on it to skip, or focus it and use the arrow keys (5 s), Page Up/Down (30 s), Home and End. Scroll the card out of view while a piece is loaded and the same controls dock in the bottom-right corner (a bar along the bottom on phones); × pauses and closes it. The `TRACKS` list near the bottom of index.html has to stay in the same order as the swallows and the track rows. Each entry's `dur` and `peaks` come from `python3 tools/waveform-peaks.py assets/music/*.m4a` (needs ffmpeg and numpy); a track without `peaks` shows a plain bar. |
| Footer clocks | Bay Area and China time, plus approximate sunrise and sunset for Hong Kong, Beijing and Changchun. They refresh every 30 seconds. |
| Sundays page | The 时 whose 日 turns into the sun (click it to replay), and the round timer: 45 minutes of work with the sun above the horizon, 10 minutes to talk below it. "Preview at 60×" runs a minute every second. |
| Visit counts | Cookie-free counts from [GoatCounter](https://richardshizhang.goatcounter.com). |

## Still to fill in

- `[YOUR EMAIL]` in the Say hello card
- `[More to come: ...]` at the bottom of sundays.html
- Instagram, GitHub and LinkedIn links (they point to the top of the page for now)
- "Longer bio →" and "Résumé →" (they point to About for now)
- The Writing posts all link to the Substack home page, not to each post

`RawAssets/` holds the original exports and isn't published. The site uses the smaller copies in `assets/`.
