# log.md - rank-week-2026

Video downloads + transcripts from **Rank Week 2026** (HeyTony / rankweektraining.com),
a 5-day live SEO training. Goal: clean text transcript of each day's Zoom webinar replay.

## Status

| Day | Date    | Video      | Transcript | Verified                       |
|-----|---------|------------|------------|--------------------------------|
| 1   | Jun 15  | ✓ day1.mp4 | ✓          | ✓ clip re-transcribe match     |
| 2   | Jun 16  | ✓ day2.mp4 | ✓          | ✓ clip re-transcribe match     |
| 3   | Jun 17  | ✓ day3.mp4 | ✓          | ✓ clip re-transcribe match     |
| 4   | Jun 18  | ✓ day4.mp4 | ✓          | ✓ clip re-transcribe match     |
| 5   | Jun 19  | ✓ day5.mp4 | ✓          | ✓ clip re-transcribe match     |

## Resources

All member resources Matt shared (AI prompts, audit spreadsheet, the *Get Found* ebook, tool
links, setup videos) collected from the authenticated `/dashboard` on 2026-06-19 → see
[`resources/README.md`](resources/README.md). Auth method: reuse the logged-in Chrome session
(`yt-dlp --cookies-from-browser chrome` → cookie jar → `curl`); dashboard + `/prompts` are
server-rendered so content came straight from the HTML, the Google Sheet via `/export?format=xlsx`,
the book via Drive `uc?export=download`. The Zoom chat is **not** recoverable - replays are
speaker/screenshare view only (no chat panel rendered), Bunny serves video only, and the typed
chat lives solely in the host's Zoom cloud account.

**Playbook:** [`rankWeekPlaybook.md`](rankWeekPlaybook.md) is the full synthesized SEO knowledge
base from all 5 transcripts (every tactic, strategy, rule, do/don't, tool, and tradeoff Tony
taught), organized by theme. Built 2026-06-19 via 5 parallel per-day extractor agents merged
into one themed doc. **Section 17** adds the curated needle-movers from Diamante's 283-page
book *Get Found* (mined via 6 parallel section agents, then filtered to high-impact, mostly
net-new items: backlink tactics, Core Web Vitals numbers, page-type optimization, the
page-deletion guardrail, the funnel sequence, plus a flagged book-vs-training conflict on
schema markup). Book v2 PDF saved to `resources/downloads/getFoundBookV2.pdf`.

## Source

- Platform: `rankweektraining.com` (login required - password or magic link)
- Replays live at `https://rankweektraining.com/replay/<N>`
- Video host: **Bunny Stream**, library `664757`, embed `https://iframe.mediadelivery.net/embed/664757/<GUID>`
- Plain HLS - no DRM, no token. Grab `<GUID>` from the player iframe on the replay page.
- **Faster GUID discovery (Day 5):** the replay page is a login-gated JS SPA (curl hits the Sign In page),
  but `yt-dlp --cookies-from-browser chrome --referer "https://rankweektraining.com/" -g <replay-url>`
  reuses the logged-in Chrome session, follows the Bunny iframe, and prints the `vz-…b-cdn.net/<GUID>/original`
  URL directly - no manual iframe inspection. Same flags on the download command (below) then pull the MP4.
- Known GUIDs: Day 1 `34cc18b7-163c-4b5a-9870-2e1f4fe4835d` · Day 2 `2ced7845-30ab-4ab4-b328-b8eb2ec0cd62` · Day 3 `11387dbc-3031-4d23-98aa-7cf4a07ee126` · Day 4 `e9d52fc0-3479-454b-8c3d-dea992304d0e` · Day 5 `046e9437-dda1-436e-9ce5-31f786628dc1`
- Pull zone (for direct HLS/MP4): `vz-f28dd2f4-2b4.b-cdn.net` (visible in the dashboard thumbnail URLs)

## Pipeline (per day)

```bash
GUID=<from the /replay/N page>
BASE=~/lalia/myBusiness/learning/rankWeek2026
MODEL=$BASE/models/ggml-large-v3-turbo.bin
VAD=$BASE/models/ggml-silero-v5.1.2.bin

# 1. download the original MP4 (referer is required or Bunny 403s)
yt-dlp --referer "https://rankweektraining.com/" -f source \
  -o "$BASE/videos/dayN.mp4" "https://iframe.mediadelivery.net/embed/664757/$GUID"

# 2. extract 16 kHz mono audio (what whisper.cpp wants)
ffmpeg -i "$BASE/videos/dayN.mp4" -vn -ar 16000 -ac 1 -c:a pcm_s16le /tmp/dayN.wav

# 3. transcribe - VAD skips silence (no hallucinated filler); --prompt seeds
#    capitalization + punctuation so output isn't a lowercase run-on
whisper-cli -m "$MODEL" -f /tmp/dayN.wav -l en -t 8 \
  --vad --vad-model "$VAD" \
  --prompt "Welcome to Rank Week. Today we are going to talk about SEO, ranking on Google, blog posts, metadata, and keywords. All right everybody, let's get started." \
  --output-txt --output-srt --output-vtt -of "$BASE/transcripts/dayN_transcript"

# 4. reflow the .txt to one sentence per line (readability; .srt/.vtt stay segment-based)
tr '\n' ' ' < "$BASE/transcripts/dayN_transcript.txt" \
  | sed -E 's/^[[:space:]]+//; s/[[:space:]]+/ /g' \
  | perl -pe 's/([.?!])\s+(?=[A-Z"\x27(])/$1\n/g' > /tmp/dayN_reflow.txt
mv /tmp/dayN_reflow.txt "$BASE/transcripts/dayN_transcript.txt"

rm /tmp/dayN.wav   # scratch
```

## Notes / gotchas

- **Right after a session, Bunny is still transcoding - `-f source` fails.** Day 4 was processed ~2 h after
  the live session: `yt-dlp -f source` errored `No video formats found` because only the 360p HLS rendition
  existed yet and the source/MP4-fallback URLs 404'd (higher resolutions transcode progressively, low-res
  first). The 360p media playlist already carried `#EXT-X-ENDLIST` (finalized VOD, full 1:20:41), so it was
  downloaded directly instead:
  `yt-dlp --referer "https://rankweektraining.com/" -o videos/dayN.mp4 "https://vz-f28dd2f4-2b4.b-cdn.net/$GUID/playlist.m3u8"`.
  Audio is identical across renditions (48 kHz stereo AAC ~123 kbps) and `-vn` throws the video away, so 360p
  gives the same transcript - no need to wait for the source MP4. (Want high-res video instead? Wait for
  transcoding to finish, then the original `-f source` command works as on Days 1-3.) Check completeness via
  `#EXT-X-ENDLIST` + the summed `#EXTINF` duration before trusting a just-posted replay.
- **VAD is essential.** Without `--vad`, Whisper hallucinates looped "Thank you" / "you" over the
  webinar's silent and music-only stretches (waiting room, demo pauses). Silero VAD transcribes
  speech only - clean output.
- Whisper runs on the Apple-silicon GPU (Metal) automatically - ~2 min per ~100 min of audio.
- **Capitalization prompt matters.** Without `--prompt`, Whisper can drop into a lowercase / no-
  punctuation decoding mode for an entire session (Day 2's first pass did exactly this). Seeding a
  properly punctuated prompt fixes it. Both days were finalized this way + reflowed to one sentence
  per line; Day 2 was re-transcribed once to apply it.
- Tools: `yt-dlp`, `ffmpeg`, `whisper-cpp` - all via Homebrew. Models in `models/` (gitignored,
  re-downloadable). `.wav` files are scratch.
- `.gitignore` keeps videos/models/wav out of git; only the text transcripts are trackable.

## Verification method

Re-transcribed random 40 s clips pulled directly from the MP4s and compared to the delivered
transcript at the same timestamps - matched word-for-word at Day 1 @ 1:30:00, Day 2 @ 0:25:00 &
1:10:00, Day 4 @ 0:40:00 (the "delete old blog posts / crawl budget" passage), and Day 5 @ 0:50:00
(the "top realtor in Maryland is too broad" passage) & 1:10:00 (the "surveyor / gravity form / MailChimp"
passage). Subtitle timing spans the full video length each day (Day 4 last cue @ 1:20:40 of 1:20:41;
Day 5 last cue @ 1:31:42 of 1:31:43, largest inter-cue gap only 4.3 s → no VAD over-skip). Blank spots in the
transcript = genuine silence correctly skipped by VAD (a no-VAD clip check hallucinates "you" there;
the delivered file does not).
