---
name: youtube-ideate
description: Use when generating ranked video idea briefs for any of the 3 ambient music channels (QuantumFrequencies777, Sleepy Cloud Lullabies, Pure Static Noise). Produces 10 data-informed concepts scored by search demand, production feasibility, channel fit, and non-cannibalization. Each idea includes a working title, keyword rationale, thumbnail concept, and audio/visual production notes adapted to Vertex AI Lyria / generative ambient workflows.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [youtube, ideate, ambient, music, content-ideas, keyword, vertex-ai, lyria]
    related_skills: [youtube-competitor-recon, youtube-seo-2026-best-practices, youtube-empire-daily-content-pipeline, vertex-ai-generative-media]
---

# YouTube Ideate — Ambient Music Content Ideas

## Overview

Generates 10 ranked video ideas for ambient music channels, grounded in search demand signals, competitor gap analysis, and the specific niche rules for each channel. Each idea ships with a full production brief — working title variants, keyword rationale, audio generation prompt (Lyria/Vertex AI), thumbnail concept, and expected traffic strategy.

**This skill is ambient-music-native.** It does NOT generate scripted video ideas. All output assumes: no voiceover, generative or stock audio/visuals, algorithmic upload pipeline.

## When to Use

- Monthly content planning session (run after `youtube-competitor-recon` if you have fresh gap data)
- Channel has run out of scheduled uploads for the next 7 days
- Exploring a new Hz/frequency/use-case sub-niche before committing
- Testing new format (e.g., Shorts, 30-min power nap version, new visual style)
- User asks "what should we make next?" for QF, SCL, or PS

**Don't use for:** auditing existing content, competitor analysis, thumbnail QA.

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| Target channel | Yes | QF (QuantumFrequencies777), SCL (Sleepy Cloud Lullabies), or PS (Pure Static Noise) |
| Competitor gaps | No | Output from `youtube-competitor-recon` (feed directly if available) |
| Seed topics | No | Specific Hz values, moods, or use cases to prioritize |
| Content to avoid | No | Topics already scheduled or over-saturated in backlog |
| Volume target | No | How many ideas needed (default: 10) |

## Channel Niche Rules (MUST enforce)

### QF — QuantumFrequencies777
- **Core:** Binaural beats, solfeggio frequencies, Hz-labeled meditation/healing content
- **Audience:** Meditation practitioners, self-healing seekers, spiritually-oriented (18-45)
- **Key Hz values:** 40 Hz (gamma focus), 432 Hz, 528 Hz (DNA/love), 963 Hz (pineal), 7.83 Hz (Schumann), 285 Hz (tissue repair)
- **Title formula:** "[Hz value] Hz — [Benefit claim] | [Duration]"
- **Durations:** 1hr, 3hr preferred; 8hr for sleep Hz
- **Do NOT:** Use lullaby language, obvious white noise, baby/infant targeting
- **RPM profile:** ~$1.50-$3/1K views (music/meditation niche)

### SCL — Sleepy Cloud Lullabies
- **Core:** Sleep music for adults and children, lullabies, soft ambient soundscapes
- **Audience:** Parents (infant sleep), adults with insomnia, sleep hygiene seekers
- **Visual:** Soft pastels, clouds, moon, stars, gentle animations
- **Title formula:** "[Mood/feeling] [Sleep Music/Lullabies] — [Optional: duration or use case]"
- **Durations:** 30min, 1hr, 3hr, 8hr (all-night)
- **Do NOT:** Use Hz labels, binaural claims, loud/energetic audio
- **RPM profile:** ~$1-$2.50/1K views

### PS — Pure Static Noise
- **Core:** Brown noise, white noise, pink noise, rain, ASMR-adjacent ambient masking
- **Audience:** ADHD focus seekers, light sleepers, tinnitus sufferers, WFH workers
- **Visual:** Minimal, waveform visualizations, static textures, dark backgrounds
- **Title formula:** "[Color/Type] Noise — [Use Case] | [Duration]"
- **Durations:** 1hr, 3hr, 8hr, 10hr (all-night heavy)
- **Do NOT:** Hz/frequency claims, spiritual/healing language, lullaby aesthetics
- **RPM profile:** ~$1-$2/1K views (noise niche is competitive but high-volume)

## Execution Steps

1. **Identify the target channel** and load its niche rules above.
2. **Review any competitor gap data** provided. If none, note that `youtube-competitor-recon` should be run first for best results.
3. **Classify idea sources.** For each idea generated, tag its origin:
   - `search-demand` — targeting a specific keyword with known search intent
   - `gap-fill` — covering a topic competitors have validated but left uncovered
   - `format-experiment` — new duration/visual/structural approach for the channel
   - `seasonal` — tied to a time-sensitive event (exam season, holiday, Q4)
4. **Generate 10 ideas.** For each, apply the full brief template below.
5. **Score and rank** all 10 using the scoring rubric.
6. **Non-cannibalization check.** Before finalizing, verify no idea on the QF list could belong on SCL or PS (and vice versa). If overlap exists, assign it to the most natural channel and mark the other as "avoid."
7. **Flag production complexity.** Mark each idea as: Easy (existing audio pipeline handles it), Medium (needs parameter tuning or new style), Hard (new workflow required).

## Scoring Rubric

| Dimension | Weight | How to Assess |
|-----------|--------|---------------|
| Search demand | 30% | Is there a clear search keyword? Do competitors have 100K+ views on similar titles? |
| Channel fit | 25% | Does it strictly follow this channel's niche rules? |
| Production effort | 20% | Can existing Lyria/Vertex AI + thumbnail pipeline handle it? Easy = high score |
| Competitor gap | 15% | Is this underserved by competitors? |
| Revenue potential | 10% | Long video? Advertiser-friendly topic? (8hr+ sleep videos earn disproportionately via watch time) |

**Score = weighted average on 1-5 scale per dimension. Rank by total score.**

## Output Template

```markdown
## Content Idea Brief: [Channel Name] — [Date]

**Channel:** [QF / SCL / PS]
**Basis:** [Competitor gap data from [date] / Keyword research / Format experiment]

---

### Idea #[N] — Score: [X.X/5.0]

**Working Title (primary):** [Title following channel formula]
**Working Title (alt 1):** [Variant — different emotional hook or keyword placement]
**Working Title (alt 2):** [Variant — duration or use-case emphasis]

**Origin:** [search-demand / gap-fill / format-experiment / seasonal]
**Target duration:** [30min / 1hr / 3hr / 8hr / 10hr]
**Traffic strategy:** [Search-first / Browse-first / Shorts-first]

**Keyword rationale:**
- Primary keyword: [keyword] — [why: demand signal or competitor validation]
- Secondary keywords: [keyword 2], [keyword 3]

**Audio generation prompt (Lyria/Vertex AI):**
> [Specific prompt for the audio — include tempo, texture, frequency if binaural, mood descriptors. E.g.: "Generate 60-minute brown noise with gentle rain layered at -12dB, slight frequency drift between 250-350Hz, no music elements, suitable for ADHD focus"]

**Thumbnail concept:**
- Background: [color/texture description]
- Text overlay: [max 4 words — exact copy]
- Visual focal point: [abstract element, icon, or scene]
- Channel palette: [QF: dark purples/golds / SCL: soft blues/whites / PS: charcoal/waveform]

**Production complexity:** [Easy / Medium / Hard]
- If Medium/Hard: [specific blocker or new step required]

**Non-cannibalization note:** [Confirm this is clearly QF / SCL / PS and not ambiguous]

**Expected performance:**
- Views at 90 days (conservative): [X K]
- Primary traffic source: [Search / Browse / Suggested]

---

[Repeat for all 10 ideas]

---

### Ranked Summary

| Rank | Title | Score | Channel | Effort | Traffic |
|------|-------|-------|---------|--------|---------|
| 1 | [Working title] | X.X | QF | Easy | Search |
| ... | | | | | |

**Recommended production order:** [Top 3 by score, filtered for Easy effort first]

**Non-cannibalization conflicts:** [None / List any resolved conflicts]
```

## Common Pitfalls

1. **Ignoring duration as a signal.** For ambient channels, 8hr+ videos have dramatically higher watch time per view → higher RPM. Don't default to 1hr — explicitly consider 8hr all-night versions for SCL and PS sleep content.
2. **Hz value repetition.** If backlog already has 3× "432 Hz sleep" videos, a 4th is low ROI. Check `~/workspace/youtube_empire/` upload history before recommending more of the same Hz.
3. **Seasonal deadlines missed.** "Study music for finals" has a 6-week peak (April/May, Nov/Dec). If ideating in March, flag these as urgent.
4. **Lyria prompt too vague.** "Relaxing music" is not a Lyria prompt. Be specific about: texture type, frequency if binaural, BPM or absence of rhythm, layering instructions, duration hint. Load `vertex-ai-generative-media` skill before authoring audio prompts.
5. **Cross-channel contamination.** "Brown noise lullaby" — this is ambiguously both PS and SCL. Force a decision: pick the channel where the use-case (lullaby = SCL) dominates and exclude the other. Never schedule same concept on two channels.
6. **No search keyword for search-first ideas.** If an idea is tagged `search-demand`, it must have a concrete keyword phrase, not just a vague topic. "432 hz for studying concentration" is a keyword. "frequency music" is not.

## Verification Checklist

- [ ] All 10 ideas follow the target channel's niche rules (no contamination)
- [ ] Non-cannibalization check completed across all 3 channels
- [ ] Each idea has a specific Lyria/Vertex AI audio prompt
- [ ] Scored and ranked by the 5-dimension rubric
- [ ] Durations explicitly chosen (not left as "TBD")
- [ ] At least 1 format-experiment idea included (pushes the channel forward)
- [ ] Top 3 are Easy production effort (ready to queue immediately)
- [ ] Backlog checked to avoid repeating Hz values already in queue
