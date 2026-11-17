# Richard Shi Zhang 张时

My personal website. It's one static page with no build step: everything (markup, styles and scripts) is in [index.html](index.html), and the photos, video and music are in [assets/](assets/).

## Preview it

From this folder:

```bash
python3 -m http.server 8642 --bind 127.0.0.1
```

Then open http://localhost:8642.

## How the page behaves

| Part | What it does |
| --- | --- |
| Sky colours | Follows the visitor's own clock: day 7am–5pm, dusk 5–7am and 5–8pm, night otherwise. Add `?time=day`, `?time=dusk` or `?time=night` to the address to force one. |
| Loading screen | The 时 stroke-order board with a mullet that hops, lands on its side, then leaps again and flops onto its back; the strokes are timed to the fish and start when its animation loads. Shows on every page load and stays until 时 is fully drawn (about 3.5 s) and the page has loaded, but never more than 6 s. "Enter →" skips it. The timings are `MIN_MS` and `MAX_MS` near the bottom of index.html. |
| Music | The swallows on the staff and the track list share one player. The `TRACKS` list near the bottom of index.html has to stay in the same order as the swallows and the track rows. |
| Footer clocks | Bay Area and China time, plus approximate sunrise and sunset for Hong Kong, Beijing and Changchun. They refresh every 30 seconds. |
| Visit counts | Cookie-free counts from [GoatCounter](https://richardshizhang.goatcounter.com). |

## Still to fill in

- `[YOUR EMAIL]` in the Say hello card
- `[CONFIRM SOURCE WITH PARENTS]` and `[USC POLYMATHIC FELLOW / RENAISSANCE SCHOLAR LINE, ONCE OFFICIAL]` in About
- Instagram, GitHub and LinkedIn links (they point to the top of the page for now)
- "Longer bio →" and "Résumé →" (they point to About for now)
- The Writing posts all link to the Substack home page, not to each post

`RawAssets/` holds the original exports and isn't published. The site uses the smaller copies in `assets/`.
