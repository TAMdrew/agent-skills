---
name: youtube-repurpose
description: Use when extracting additional content value from existing ambient music uploads across the empire (QuantumFrequencies777, Sleepy Cloud Lullabies, Pure Static Noise). Transforms long-form ambient videos into Shorts clips, Spotify/podcast audio exports, Community post copy, and cross-channel derivative suggestions — all without voiceover or scripted content.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [youtube, repurpose, ambient, shorts, community-posts, cross-platform, content-multiplication]
    related_skills: [youtube-calendar, ffmpeg-workflows, youtube-seo-2026-best-practices, youtube-thumbnail-diversification]
---

# YouTube Repurpose — Ambient Music Content Multiplication

## Overview

Extracts maximum value from each ambient video upload by generating: Shorts clips (visual loop + audio segment), Community post copy, Spotify/podcast audio derivation plan, and any viable cross-channel derivative. Adapted entirely for non-scripted, music/sound content — no voiceover repurposing, no Twitter threads summarizing "key takeaways" (there are none in ambient audio).

**Core principle for ambient repurposing:** The asset IS the audio. Repurposing = re-framing the same audio/visual in different containers optimized for different surfaces (Shorts feed, playlist, Community tab, external streaming).

## When to Use

- After a long-form video goes live — generate Shorts + Community post in the same session
- Monthly content audit reveals underperforming videos with good audio — repurpose to revive them
- A video did well (high AVD, strong search ranking) — extract Shorts clips to extend its lifecycle
- Cross-channel derivative opportunity: PS "brown noise" video could become a SCL "rain + soft music" variant

**Don't use for:** generating new audio content (use `youtube-ideate` + Vertex AI/Lyria pipeline), auditing quality (use `yt-empire-audit-gate-workflow`).

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| Source video | Yes | YouTube URL, video ID, or local file path |
| Source channel | Yes | QF / SCL / PS |
| Video duration | Yes | Total length (needed for clip extraction math) |
| Performance data | No | CTR, AVD, view count — helps prioritize which sections to clip |
| Repurpose targets | No | Which outputs to generate (default: all applicable) |

## Repurposing Matrix for Ambient Channels

| Source Type | Shorts | Community Post | Spotify/Podcast | Cross-Channel Derivative |
|-------------|--------|---------------|-----------------|--------------------------|
| QF binaural (1-3hr) | ✓ 45-60s | ✓ frequency fact | ✗ (binaural ≠ standard audio) | Possible (SCL if no Hz label) |
| SCL sleep music (3-8hr) | ✓ 30-45s | ✓ sleep tip | ✓ yes | Possible (PS if ambient-only section extracted) |
| PS noise (1-10hr) | ✓ 15-30s | ✓ use-case tip | ✓ yes | Possible (SCL if nature sounds present) |

## Execution Steps

### Step 1: Source Video Analysis

1. Load the source video metadata (title, description, chapters if any, duration).
2. Identify the audio type: binaural beat (headphones required → no Spotify), static music (Spotify OK), nature/noise (Spotify OK).
3. If chapters exist, use them as natural clip boundaries. If not, apply default extraction zones:
   - Zone A (0-5% of video): Opening texture — often strongest for Shorts hook
   - Zone B (10-20%): Settled state — good for "sample" feel
   - Zone C (40-60%): Mid-point — useful for longest-session Community post (shows depth)
   - Zone D (80-90%): Near-end — avoid (listener fatigue zone in analytics)

### Step 2: Shorts Clip Extraction

**Target count:** 2-3 Shorts per long-form video.

For each clip:

1. **Select timestamp range.** Use chapter markers or zone mapping above.
2. **Determine optimal Shorts length** for ambient content:
   - 15-20s: Texture preview (PS noise, QF pure tones) — very high loop rate, good for Shorts algo
   - 30-45s: Melodic hook (SCL music) — enough to convey mood
   - 55-60s: Hz/frequency claim format (QF) — time to state benefit + let listener feel it
3. **Write Shorts title:**
   - QF: "[Hz value] Hz — [benefit] #shorts" — max 40 chars
   - SCL: "[mood adjective] Sleep Music #shorts" — max 35 chars
   - PS: "[Color] Noise for [use case] #shorts" — max 38 chars
4. **Write Shorts description** (first 125 chars carry all weight for ambient):
   - Lead with the primary keyword and benefit. Include link to full video: "Full [Xhr] version in bio ↑"
5. **Visual format note:** For ambient Shorts, looping visuals are optimal. If the parent video used a static image, use a slow zoom/Ken Burns clip of the same image. If it had a waveform visualizer, extract that segment.
6. **FFmpeg extraction command:**
   ```bash
   # Extract 45-second clip starting at 2:30
   ffmpeg -ss 00:02:30 -t 45 -i /path/to/source.mp4 \
     -vf "scale=1080:1920,setsar=1" \
     -c:v libx264 -c:a aac -b:a 192k \
     /path/to/shorts_output.mp4
   ```
   See `ffmpeg-workflows` skill for full options including GPU acceleration.

### Step 3: Community Post

Write 1 Community post per video to publish same-day as the Shorts (not same-day as long-form — stagger by 24h).

**Template by channel:**

**QF Community post:**
```
[Hz value] Hz — did you know?

[One-sentence benefit claim about the frequency — grounded, not medical]

We just posted [duration] of uninterrupted [Hz value] Hz to help you [benefit].

Link in description 👆

What do you use frequency music for? Drop it below 👇
```

**SCL Community post:**
```
Struggling to fall asleep? 🌙

We posted [duration] of [mood] sleep music for [use case].

Put it on, close your eyes, and let it do the rest.

Full video in our latest upload ⬆️

Reply with 😴 if this helps you tonight
```

**PS Community post:**
```
[Color] noise for [use case] 🎧

[One-sentence description of the texture/benefit — e.g., "Steady brown noise to block distractions and lock in deep work."]

[Duration] version now live.

Do you use [noise type] noise for sleep or focus? Let us know below 👇
```

### Step 4: Spotify / Podcast Audio Export (SCL and PS only)

Binaural content (QF) is NOT suitable for Spotify — it requires stereo headphones and platform compression degrades the binaural effect.

For SCL and PS:
1. **Export audio-only WAV** at 44.1kHz / 24-bit:
   ```bash
   ffmpeg -i /path/to/source.mp4 -vn -c:a pcm_s24le -ar 44100 /path/to/export.wav
   ```
2. **Trim to standard podcast segment** (30min or 60min slice):
   ```bash
   ffmpeg -ss 00:00:00 -t 3600 -i export.wav -c copy output_60min.wav
   ```
3. **Normalize loudness** to -14 LUFS (Spotify standard):
   ```bash
   ffmpeg -i output_60min.wav -af loudnorm=I=-14:TP=-1:LRA=11 output_normalized.wav
   ```
   See `songsee` skill for full loudness audit workflow.
4. **Tag metadata** (Artist = channel name, Title = video title, Genre = "Ambient / Sleep / White Noise")
5. **Upload channel:** DistroKid, TuneCore, or direct Spotify for Podcasters (for podcast-format ambient channels)

### Step 5: Cross-Channel Derivative Check

Assess whether the source audio could serve a different empire channel with minor re-framing:

| If source is... | And contains... | Derivative opportunity |
|----------------|-----------------|----------------------|
| QF binaural 432 Hz + soft music bed | A quiet music layer underneath | SCL version: Strip binaural, release as pure ambient sleep music |
| PS brown noise | With occasional soft rain layered | SCL version: Highlight rain, re-title as "Rain + Brown Noise Sleep" |
| SCL sleep music | Very minimal, almost drone-like | QF version: Layer 528 Hz tone at -18dB, re-title as "528 Hz Healing Sleep Music" |

**Cross-channel derivative rules:**
- MUST change title, description, and thumbnail — never identical metadata
- MUST have at least a 6-week gap between posting original and derivative
- MUST tag the derivative's description: "A different take on ambient [use case] — explore more on [channel]" (links to sister channel for cross-promotion)
- Run through `yt-empire-duplicate-detection` before uploading derivative to confirm signature difference

## Output Template

```markdown
## Repurpose Package: "[Video Title]"

**Source channel:** [QF / SCL / PS]
**Source URL:** [YouTube URL]
**Duration:** [Xhr]
**Audio type:** [Binaural / Music / Noise / Nature]

---

### Shorts Plan (2-3 clips)

**Clip 1**
- Timestamp: [MM:SS – MM:SS] ([X seconds])
- Title: "[Shorts title]"
- Description (first 125 chars): "[Description]"
- Visual note: [Looping zoom / waveform clip / static crop]
- FFmpeg command: `ffmpeg -ss [time] -t [secs] -i [source] -vf "scale=1080:1920,setsar=1" [output]`
- Post date: [Parent video date + 24h]

**Clip 2**
- [Same format]

---

### Community Post

**Post date:** [Shorts date + 0-24h]
**Copy:**
> [Full community post text — ready to paste]

---

### Spotify/Podcast Export

**Eligible:** [Yes / No — binaural not eligible]
[If yes:]
- Export duration: [30min / 60min slice]
- Normalization target: -14 LUFS
- Distribution channel: [DistroKid / TuneCore / Spotify for Podcasters]
- FFmpeg commands: [Listed above — reference or inline]

---

### Cross-Channel Derivative

**Opportunity:** [Yes / No]
[If yes:]
- Source: [Channel] | Derivative target: [Channel]
- Re-framing: [How the audio changes — or doesn't — and how metadata changes]
- Earliest post date: [Source date + 6 weeks]
- Duplicate check: Run `yt-empire-duplicate-detection` before scheduling
```

## Common Pitfalls

1. **Posting binaural to Spotify.** QF binaural audio loses its effect entirely on Spotify (compressed, lossy, mono-fold risk). Only SCL and PS are Spotify-eligible from this empire.
2. **Same-day Shorts + long-form.** Shorts posted the same day as the parent long-form split impressions. Always lag by 24h minimum.
3. **Cross-channel derivative too soon.** Posting a SCL derivative of a QF video within 2 weeks causes the algorithm to flag similar audio. 6-week gap is the minimum safe window.
4. **Community post keyword bloat.** Community posts are indexed but have very limited SEO value — don't stuff them with keywords. Write naturally for the audience, include one clear CTA, one link reference.
5. **Skipping `yt-empire-duplicate-detection` for derivatives.** Even with title changes, if the audio fingerprint is identical or near-identical, YouTube can suppress the derivative. Always check before uploading.
6. **Exporting at wrong loudness.** Spotify normalizes to -14 LUFS. Content above that gets attenuated; content far below sounds weak. Normalize during export, not after.

## Verification Checklist

- [ ] Audio type confirmed (binaural vs music vs noise) — affects Spotify eligibility
- [ ] Shorts clips extracted with correct aspect ratio (1080x1920) for vertical
- [ ] Shorts titles follow channel formula and are ≤ 40 chars
- [ ] Community post ready to paste, CTA included, no keyword stuffing
- [ ] Spotify export: WAV 44.1kHz, -14 LUFS normalized (SCL/PS only)
- [ ] Cross-channel derivative: 6-week gap enforced + `yt-empire-duplicate-detection` queued
- [ ] All Shorts scheduled 24-48h after parent long-form
