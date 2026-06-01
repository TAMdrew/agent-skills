---
name: youtube-competitor-recon
description: Use when conducting competitor analysis for any of the 3 ambient music channels (QuantumFrequencies777, Sleepy Cloud Lullabies, Pure Static Noise). Spawns parallel analysis agents to map top-video patterns, keyword gaps, format gaps, and audience unmet needs in the ambient/sleep/noise/binaural vertical. Produces ranked content opportunities with keyword demand signals.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [youtube, competitor, ambient, music, recon, keyword-gap, content-strategy]
    related_skills: [youtube-analytics-feedback-loop, youtube-seo-2026-best-practices, youtube-empire-daily-content-pipeline]
---

# YouTube Competitor Recon — Ambient Music Vertical

## Overview

Performs multi-dimensional competitor gap analysis for ambient/sleep/noise YouTube channels, spawning 4 parallel agents covering top-video patterns, keyword gaps, format gaps, and audience unmet needs. Output is a ranked list of content opportunities the empire can exploit.

**This skill is scoped to the ambient music vertical.** Competitors are channels like:
- Sleep/relaxation: `Jason Stephenson`, `Meditative Mind`, `Greenred Productions`, `Soothing Relaxation`
- Binaural/frequency: `PowerThoughts Meditation Club`, `Magnetic Minds`, `Brainwave Power Music`
- White/brown/pink noise: `TMSOFT`, `Relaxing White Noise`, `Nature Relaxation Films`

## When to Use

- Planning a new content push for QF, SCL, or PS
- CTR or views have plateaued — need to identify uncovered demand
- New sub-niche spotted (e.g. "432 Hz for studying") — validate competitor presence before committing
- Monthly content ideation round (run before `youtube-ideate`)
- Investigating whether a competitor is cannibalizing a specific keyword cluster

**Don't use for:** auditing your own channel health (use `youtube-analytics-feedback-loop`), checking upload quality (use `yt-empire-audit-gate-workflow`).

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| Competitor channels | Yes | 2-3 channel names/URLs to analyze |
| Target channel | Yes | Which empire channel: QF / SCL / PS |
| Keyword focus | No | Optional seed topics (e.g. "sleep music", "binaural beats", "432 hz") |
| Time window | No | How far back to look (default: top videos all-time + last 90 days) |

## Parallel Agent Architecture

Spawn all 4 agents simultaneously. Each investigates one competitive dimension.

### Agent A: Top Video Pattern Analysis
**Scope:** Each competitor's top 20 videos by all-time view count

**Analyze:**
- Title patterns: keyword placement, length (char count), number usage, emotional triggers
- Frequency/Hz claims in titles (e.g. "432 Hz", "528 Hz", "40 Hz") — which Hz values dominate
- Duration distribution: which lengths (1hr, 2hr, 8hr, 10hr) have highest views
- Sleep vs study vs meditation vs focus segmentation
- Thumbnail style: dark vs light, text-heavy vs minimal, abstract vs nature imagery
- Upload age vs view velocity (old evergreens vs recent viral)

**Output:** Top 5 title formulas, dominant duration patterns, thumbnail style breakdown, top Hz/frequency claims by view count

### Agent B: Keyword Gap Analysis
**Scope:** Competitor video titles, descriptions (first 200 chars), tags (if visible)

**Analyze:**
- Extract keywords from top 30 competitor videos
- Cross-reference against the target channel's recent 60 uploads
- Identify keyword clusters competitors rank for that target channel has NOT covered
- Classify gaps by: [High-demand: obvious search intent] vs [Niche-demand: specific Hz/mood combos] vs [Format-gap: duration/style not attempted]
- For ambient channels, check these specific gap types:
  - Hz frequency combinations (e.g. "285 Hz + 432 Hz combined")
  - Temporal variants (e.g. "12 hour", "all night", "30 min power nap")
  - Use-case variants (e.g. "for dogs", "ADHD focus", "dark academia study")
  - Seasonal/situational (e.g. "rain sounds for sleeping", "winter lo-fi", "thunderstorm sleep")

**Output:** Top 10 keyword gaps ranked by estimated opportunity, with rationale for each

### Agent C: Format Gap Analysis
**Scope:** Content format and production style differences

**Analyze:**
- Video length distribution for competitors vs target channel
- Visual format: static image / slow zoom / AI video / nature footage / abstract visualization / screen saver style
- Chapter/timestamp usage (does competitor use chapters for long ambient videos?)
- Shorts integration: do competitors post Shorts clips from long-form ambient content?
- Playlist structure: do competitors organize by Hz, mood, use-case, duration?
- Upload cadence: daily / 3x week / weekly — compare to target channel's current cadence

**Output:** Top 3 format opportunities the target channel has NOT exploited

### Agent D: Audience Unmet Needs
**Scope:** Comment sections of competitor's top 10 recent videos (last 90 days)

**Analyze:**
- Recurring requests ("can you make one for X")
- Complaints about missing variants ("I wish this was longer / had rain sounds / had no binaural")
- Testimonials revealing specific use cases (medical insomnia, PTSD, tinnitus masking, infant sleep)
- Timestamp requests (if video lacks chapters)
- Language/region requests (non-English comments = geo opportunity)

**Output:** Top 5 explicit audience requests competitors are NOT fulfilling; 3 emerging use-case angles

## Execution Steps

1. **Identify competitors** from the inputs or default list above. Pick 2-3 most relevant to the target channel's niche (QF → binaural/frequency; SCL → sleep/lullaby; PS → noise/ASMR).
2. **Spawn all 4 agents simultaneously.**
3. **Retrieve data** using available tools: YouTube Data API v3 via `execution/fetch_channel_data.py` (if available), YouTube web search, or direct channel inspection.
4. **Synthesize findings** after all 4 agents complete. Do NOT synthesize until all 4 have returned.
5. **Build opportunity ranking.** Score each opportunity on:
   - Search demand (High/Medium/Low)
   - Competitor coverage (None/Weak/Strong — lower is better for us)
   - Production effort (Easy/Medium/Hard — for ambient, Easy = static image + AI audio)
   - Channel fit (does it match QF/SCL/PS niche rules?)
6. **Output the ranked opportunity list** with production notes per item.

## Output Template

```markdown
## Competitor Recon Report: [Target Channel] — [Date]

**Competitors analyzed:** [Channel A], [Channel B], [Channel C]
**Data window:** [Top all-time + last 90 days]

---

### Agent A: Top Video Patterns

**Top title formulas (by view count):**
1. "[Hz value] Hz — [Use Case] | [Duration]" — avg Xm views
2. ...

**Dominant durations:** [e.g., 3hr (40%), 1hr (30%), 8hr (20%), other (10%)]

**Thumbnail style:** [e.g., 80% dark/cosmic abstract, 15% nature, 5% text-only]

**Top performing Hz claims:** 432 Hz > 528 Hz > 963 Hz (by aggregate views)

---

### Agent B: Keyword Gaps

| # | Keyword Gap | Estimated Demand | Competitor Coverage | Channel Fit |
|---|-------------|-----------------|---------------------|-------------|
| 1 | "432 Hz for dogs sleep" | Medium | None found | PS/SCL |
| ... | | | | |

---

### Agent C: Format Gaps

1. **[Format opportunity]:** [Description + why it's an opportunity]
2. ...

---

### Agent D: Audience Unmet Needs

**Explicit requests not being met:**
1. "[Quote from comment or paraphrase]" — seen X times across Y videos
2. ...

**Emerging use-case angles:**
1. [Use case] — [evidence]
2. ...

---

### Ranked Opportunity List

| Rank | Opportunity | Demand | Coverage | Effort | Channel |
|------|-------------|--------|----------|--------|---------|
| 1 | [Title concept] | High | None | Easy | QF |
| ... | | | | | |

**Recommended next step:** Feed top 3 opportunities into `youtube-ideate` for full production briefs.
```

## Ambient-Specific Pitfalls

1. **Hz claim fatigue:** 432 Hz and 528 Hz are over-saturated. Check actual search volume before committing — niche combos (e.g. "285 Hz + 528 Hz immune system") often have less competition.
2. **Duration trap:** Competitors with 10hr+ videos dominate search for sleep terms. For PS/SCL, competing on duration directly is hard — instead target use-case + duration combos they haven't covered.
3. **Cannibalizing your own channels:** Before recommending an opportunity to QF, verify it doesn't conflict with SCL or PS niches. Run through the non-cannibalization check in `youtube-empire-daily-content-pipeline`.
4. **Comment data quality:** Ambient channels get spam/bot comments. Filter for comments >10 words with specific requests — short "❤️" comments are noise.
5. **DataForSEO not required:** This skill works without DataForSEO. YouTube web search + channel inspection is sufficient for ambient niche recon where competition is lower than general YouTube.

## Verification Checklist

- [ ] Analyzed at least 2 competitors relevant to the target channel's niche
- [ ] All 4 agents ran in parallel (not sequentially)
- [ ] Keyword gaps cross-referenced against target channel's actual recent uploads
- [ ] Opportunity list checked against non-cannibalization rules (QF vs SCL vs PS)
- [ ] Output includes at least 5 ranked opportunities with effort/demand/coverage scores
- [ ] Findings fed forward to `youtube-ideate` or content calendar
