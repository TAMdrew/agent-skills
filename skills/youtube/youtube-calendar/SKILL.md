---
name: youtube-calendar
description: Use when building a monthly content calendar for the 3-channel ambient music empire (QuantumFrequencies777, Sleepy Cloud Lullabies, Pure Static Noise). Distributes ideas across upload slots, balances content pillars, assigns Shorts derivatives, flags CPM-critical timing windows, and generates a ready-to-execute schedule that integrates with the existing daily_content_orchestrator.py pipeline.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [youtube, calendar, content-planning, ambient, empire, scheduling, cpm, pillars]
    related_skills: [youtube-ideate, youtube-strategy, youtube-empire-daily-content-pipeline, yt-empire-audit-gate-workflow]
---

# YouTube Content Calendar — Ambient Music Empire

## Overview

Builds a concrete monthly (or bi-weekly) upload schedule for one or all 3 empire channels. Input: idea list (from `youtube-ideate` or ad-hoc) + current backlog status. Output: day-by-day upload plan per channel with pillar balance checks, Shorts derivatives assigned, CPM windows flagged, and a JSON-ready schedule block for `daily_content_orchestrator.py`.

**This skill coordinates the empire, not a single channel.** It ensures uploads are staggered across channels and not competing with each other on the same day for the same keywords.

## When to Use

- Monthly planning session (first week of each month)
- Backlog is depleted for one or more channels (< 7 days of content queued)
- A big CPM window is approaching (Q4, exam season, New Year) — plan 2-3 weeks in advance
- Adding a new pillar or format and need to slot it without disrupting cadence
- User asks "what do we upload this week?" or "build the schedule"

**Don't use for:** individual video production decisions (use `youtube-ideate`), audit/quality gate (use `yt-empire-audit-gate-workflow`).

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| Target month | Yes | Month and year (e.g. "June 2026") |
| Idea list | Yes | Video concepts to schedule — can be raw list or `youtube-ideate` output |
| Channels to schedule | Yes | "All 3" or specific channel(s) |
| Target cadence per channel | No | Videos/week per channel (defaults from `youtube-strategy`) |
| Shorts plan | No | Include Shorts derivatives? (default: Yes, 2 per long-form per week) |
| Backlog count | No | How many videos already in ready_to_upload per channel |

## Execution Steps

1. **Inventory the idea list.** Categorize each idea by: channel (QF/SCL/PS), pillar, duration tier, production effort (Easy/Medium/Hard). Hard items must be scheduled earlier to allow render time.

2. **Map the month.** Count publishing weeks. Identify:
   - **Q4 premium window** (Oct-Dec): CPM +30-50% — schedule highest-RPM content (long-form sleep/focus with ads enabled)
   - **January slump** (Jan 1-15): CPM drops ~25% — schedule experimental content here, not premium
   - **Exam season peaks** (Apr-May, Nov-Dec): Study music demand spikes → prioritize QF gamma/focus and PS focus noise
   - **Holiday adjacency** (Dec 20-31): Sleep and relaxation demand peaks — prioritize SCL and PS all-night formats

3. **Assign videos to slots.** Follow these rules:
   - No two channels upload on the same day to the same keyword cluster (e.g., don't post "sleep music" on both SCL and PS the same day)
   - Rotate pillars within each channel — never 3 consecutive uploads from the same pillar
   - Shorts should lag 24-48h behind the parent long-form (gives long-form a head start on initial distribution)
   - Schedule Hard-effort items in week 1-2; Easy items can fill week 3-4 as buffer
   - Leave at least 1 "emergency slot" per channel per week for trend-responsive content

4. **Balance check.** Run the pillar distribution check per channel. If any pillar exceeds 50% of the month's uploads, redistribute.

5. **Generate Shorts derivatives.** For each long-form video scheduled, identify the optimal Shorts clip:
   - QF: The first 30-60 seconds of audio with a looping visual — title: "[Hz value] Hz #shorts"
   - SCL: The most melodically distinct section — title: "[Mood] Sleep Music #shorts"
   - PS: A 15-30 sec texture preview — title: "[Noise type] for [use case] #shorts"
   - Post Shorts 24-48h after parent long-form.

6. **Write the schedule** in both human-readable table format and orchestrator-ready JSON.

7. **Stagger timing across channels.** Suggested default:
   - QF: Tues/Thurs/Sat + Shorts Mon/Fri
   - SCL: Mon/Wed/Fri + Shorts Sun/Tue
   - PS: Mon/Wed/Sat + Shorts Thu/Sat
   - *Adjust based on Analytics → Reports → Audience → "When your viewers are on YouTube"*

## CPM Calendar (Ambient Niche)

| Period | CPM Direction | Action |
|--------|--------------|--------|
| Q4 (Oct 1 – Dec 31) | +30-50% | Schedule premium long-form (2hr+ with mid-rolls enabled) |
| Jan 1-15 | -25% | Slot experiments, new formats, risky ideas |
| Jan 16-31 | Recovery | Resume standard cadence |
| Feb-Mar | Stable | Standard cadence |
| Apr-May | +15% (exam peak) | Prioritize QF focus/gamma + PS brown noise |
| Jun-Aug | Summer stable | Standard cadence; test Shorts aggressive cadence |
| Sep | Back-to-school bump | +10% for study/focus content |
| Nov-Dec | Peak again | Ramp to maximum cadence, all-night formats |

## Output Template

```markdown
## Content Calendar: [Month Year]

**Channels:** QF / SCL / PS
**Total videos scheduled:** [N long-form] + [N Shorts]
**CPM window:** [Q4 premium / Exam peak / Standard / January slump]

---

### QF — QuantumFrequencies777

| Date | Day | Title | Pillar | Duration | Effort | Shorts? |
|------|-----|-------|--------|----------|--------|---------|
| Jun 3 | Tue | 432 Hz Deep Sleep — 8 Hours | Core Hz | 8hr | Easy | Jun 4 |
| Jun 5 | Thu | 40 Hz Gamma Focus Study Music | Gamma | 3hr | Easy | Jun 6 |
| Jun 7 | Sat | 528 Hz DNA Repair Healing | Healing | 1hr | Easy | — |
| Jun 10 | Tue | 963 Hz Pineal Activation — 1 Hour | Core Hz | 1hr | Med | Jun 11 |
| ... | | | | | | |

**Pillar balance check:**
- Core Hz: [N]% | Gamma: [N]% | Healing: [N]% | Schumann: [N]% | Combos: [N]% | Chakra: [N]%
- Status: [Balanced / Warning: [pillar] over-concentrated at [N]%]

---

### SCL — Sleepy Cloud Lullabies

[Same table format]

---

### PS — Pure Static Noise

[Same table format]

---

### Empire-Level Stagger Check

| Date | QF | SCL | PS |
|------|----|----|-----|
| Jun 1 | — | SCL: [Title] | — |
| Jun 2 | — | — | PS: [Title] |
| Jun 3 | QF: [Title] | — | — |
| ... | | | |

**Keyword collision check:** [None found / Warning: [QF + PS both posting sleep content Jun 5 — resolved by moving PS to Jun 6]]

---

### Orchestrator JSON Block

```json
{
  "schedule": {
    "2026-06-03": {
      "QF": {
        "title": "432 Hz Deep Sleep — 8 Hours",
        "pillar": "core_hz",
        "duration_hr": 8,
        "effort": "easy",
        "shorts_date": "2026-06-04"
      }
    },
    "2026-06-04": {
      "QF_shorts": {
        "parent": "432 Hz Deep Sleep — 8 Hours",
        "title": "432 Hz Deep Sleep #shorts",
        "clip_range_sec": [0, 45]
      }
    }
  }
}
```

**Integration note:** Paste the JSON block into `~/workspace/youtube_empire/config/content_schedule.json`. The `daily_content_orchestrator.py` reads this at 6am cron to determine what to render and queue.
```

## Common Pitfalls

1. **Scheduling without knowing backlog.** If 14 videos are already queued for PS and you schedule 20 more, the renders overlap and the orchestrator queue deadlocks. Always check `ls ~/workspace/youtube_empire/*/ready_to_upload/` before building the calendar.
2. **Same-day cross-channel collision.** QF and SCL posting "sleep music" content on the same day splits Browse impressions. Use the stagger table and run the keyword collision check.
3. **Forgetting Shorts lag timing.** Posting a Short before the parent long-form goes live trains the algorithm on the wrong audience. Always lag Shorts by 24-48h minimum.
4. **Over-scheduling Hard-effort items in Week 4.** If render or QA fails, you have no buffer. Hard items must be in week 1-2 with week 3-4 as fallback easy slots.
5. **Ignoring the January CPM cliff.** Every January, the ambitious planner front-loads the best content. Don't — use January for experiments that you'd be OK with underperforming.
6. **Shorts without parent context.** Every Shorts derivative needs a parent video to link back to via pinned comment. Never schedule orphan Shorts.

## Verification Checklist

- [ ] Backlog count confirmed per channel before scheduling
- [ ] No two channels posting to same keyword cluster on same day
- [ ] Pillar distribution check run — no pillar exceeds 50% per channel per month
- [ ] CPM window flagged and premium content assigned to it
- [ ] Shorts scheduled 24-48h after each parent long-form
- [ ] Hard-effort items scheduled in weeks 1-2
- [ ] Orchestrator JSON block generated and ready to paste into config
- [ ] Emergency slots (1/channel/week) kept open
