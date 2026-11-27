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
| Sky colours | Follows the hour in the city shown on the hero clock (Los Angeles until someone flips it): day 7am–5pm, dusk 5–7am and 5–8pm, night otherwise. Add `?time=day`, `?time=dusk` or `?time=night` to the address to force one until the clock is first flipped. |
| City clock | Under "See the work" in the hero, as `LAX/Los Angeles 洛杉矶 · 10:36 PM`. Hovering with a mouse, tapping, or Enter/Space flips it departure-board style to the next stop (LAX, SJC, JFK, HKG, PEK, CGQ, then back to LAX) and repaints the sky for that city's hour. Edit the stops in the `CITIES` array in the "City clock in the hero" script. Reduced motion swaps the text without the flip. |
| Hero polaroids | Three pinned photos joined by threads, top right in the hero (in a row beside "See the work" between 821 and 1099 px wide, and under the bio on phones). Hovering or focusing one, or hovering or tapping its phrase in the bio, straightens it, brings its colour back and sets its threads moving. Each polaroid is a `<span class="pin">` and an `<a class="node">` sharing a `data-node`; place it with `--x`/`--y` (desktop), `--mx`/`--my` (tablet) and `--px`/`--py` (phone), and list its threads in `data-edges` on `.graph`. Add `?node=music` to the address to straighten one. Research and writing don't have one yet. |
| Nav scrolls | Resting the mouse on a section link in the top bar, or tabbing to it, unrolls a small hanging scroll under the bar with a photo and one line. Moving away, Escape or a click elsewhere rolls it up. Touch screens skip them and the links just jump. The photos load after the page, and only where a mouse can hover. Writing has no scroll yet. Add `?ns=music` to the address to open one. |
| Loading screen | The 时 stroke-order board with a mullet that hops, lands on its side, then leaps again and flops onto its back; the strokes are timed to the fish and start when its animation loads. Shows on every page load and stays until 时 is fully drawn (about 3.5 s) and the page has loaded, but never more than 6 s. "Enter →" skips it. The timings are `MIN_MS` and `MAX_MS` near the bottom of index.html. |
| Music | The swallows on the staff and the track list share one player. The card under the staff draws the playing piece as an ink stroke, thick where it's loud and red as far as you've listened. Click or drag on it to skip, or focus it and use the arrow keys (5 s), Page Up/Down (30 s), Home and End. Scroll the card out of view while a piece is loaded and the same controls dock in the bottom-right corner (a bar along the bottom on phones); × pauses and closes it. So nothing clicks, the sound fades in when it starts (80 ms), fades out before it pauses or changes piece (150 ms), and dips out and back in around a skip (40 ms); the lengths are `FADE_IN`, `FADE_OUT` and `DIP` in the player script. On phones each swallow has an invisible tap area about three swallows wide and 44 px tall. The `TRACKS` list near the bottom of index.html has to stay in the same order as the swallows and the track rows. Each entry's `dur` and `peaks` come from `python3 tools/waveform-peaks.py assets/music/*.m4a` (needs ffmpeg and numpy); a track without `peaks` shows a plain bar. |
| Writing | The newest four Substack posts, read from the feed when the page loads (through rss2json.com, because Substack's feed doesn't let other sites read it), skipping the "Start here" post. If that fails or takes more than 8 s, the four rows written in the HTML stay, so refresh them now and then. The script is "Writing: latest posts" at the bottom of index.html. |
| Footer clocks | Bay Area and China time, plus approximate sunrise and sunset for Hong Kong, Beijing and Changchun. They refresh every 30 seconds. |
| Sundays page | The 时 whose 日 turns into the sun (click it to replay), and the round timer: 45 minutes of work with the sun above the horizon, 10 minutes to talk below it. While it runs, the tab title shows the time left, as `44:59 · Work · Sundays in LA` (`⏸ 6:00 · Talk paused · …` when paused). When work or talk ends, a bell rings, a note drops in at the top of the card, and the next part starts by itself. The bell is `assets/bell.mp3`, my recreation of my high school's period-end bell; if it can't load, three soft synthesized notes ring instead. Each bell is booked ahead on the audio clock and a background worker keeps the countdown ticking, so both stay on time when the tab is in the background. Under the clock are Pause/Resume, "Skip phase", Reset and "Mute bell" (unmuting rings once so you hear it's on). The timer is saved in the browser (`sundays-timer` in localStorage), so it carries on through a reload or a closed tab, but a running timer that nobody has had open for 12 hours starts over. Browsers only allow sound after a click, so after a reload the page asks for a tap or click before the bell can ring again. "Preview at 60×" runs a minute every second. The lengths are `DUR` at the top of the timer script in sundays.html. Not tried yet on an iPhone, where a locked screen or the silent switch will likely keep the bell quiet. |
| Say hello card | In the footer. The email row shows "Email · tap to show"; clicking it puts the address together and turns the row into a mailto link. The address is stored reversed in two pieces (`data-u` and `data-d` on `#email`), so it never appears in the page source for scrapers to find. |
| Visit counts | Cookie-free counts from [GoatCounter](https://richardshizhang.goatcounter.com). |

## Still to fill in

- `[More to come: ...]` at the bottom of sundays.html
- "Longer bio →" and "Résumé →" (they point to About for now)

`RawAssets/` holds the original exports and isn't published. The site uses the smaller copies in `assets/`; `assets/img/small/` has 480 px copies for the polaroids and scrolls.
