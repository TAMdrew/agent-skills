---
name: youtube-strategy
description: Use when building or refreshing a 90-day content strategy for any of the 3 ambient music channels (QuantumFrequencies777, Sleepy Cloud Lullabies, Pure Static Noise). Covers channel positioning, content pillar framework, upload cadence optimization, milestone planning, and cross-channel differentiation. Adapted to algorithmic ambient music channels running Vertex AI / Lyria pipelines.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [youtube, strategy, ambient, music, content-pillars, positioning, 90-day, empire]
    related_skills: [youtube-ideate, youtube-competitor-recon, youtube-analytics-feedback-loop, youtube-empire-daily-content-pipeline]
---

# YouTube Channel Strategy — Ambient Music Empire

## Overview

Builds a concrete 90-day channel strategy for one or more of the empire's 3 channels. Covers: channel positioning review, content pillar framework (4-6 pillars per channel), upload cadence recommendation, milestone plan, and cross-channel differentiation rules. Output is an actionable roadmap, not a vague "grow your audience" deck.

**This skill is empire-aware.** It accounts for the 3-channel structure and enforces non-cannibalization as a first-class constraint.

## When to Use

- Quarterly planning reset (run every 90 days)
- A channel's growth has stalled for 3+ weeks (zero CTR improvement, flat subs)
- Adding a new content pillar or sub-niche to a channel
- Before spinning up a new channel to ensure it doesn't cannibalize QF/SCL/PS
- Channel has drifted off-niche (e.g., PS posted sleep lullabies that belong on SCL)

**Don't use for:** video-level metadata optimization (use `youtube-seo-2026-best-practices`), individual idea generation (use `youtube-ideate`), audit gate (use `yt-empire-audit-gate-workflow`).

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| Target channel(s) | Yes | QF, SCL, PS — or "all 3" |
| Current state | Yes | Sub count, monthly views, upload frequency, avg CTR/AVD if known |
| Primary goal | Yes | Growth / Monetization / Both |
| Time horizon | No | 30 / 60 / 90 days (default: 90) |
| Competitor gap data | No | Feed output from `youtube-competitor-recon` if available |
| Known constraints | No | API quota limits, audio render capacity, team size |

## Execution Steps

1. **Load channel state.** Retrieve or confirm: subscriber count, monthly views, last 30-day CTR, AVD, primary traffic source (Browse/Search/Suggested split), upload cadence (videos/week).

2. **Diagnose current positioning.** For each channel, answer:
   - Is the channel clearly differentiated from the other two? (If not, identify the overlap and resolve it)
   - What's the primary traffic source? If Search > 60%, the channel is keyword-dependent and fragile — strategy should add pillar content optimized for Browse/Suggested
   - What's the current content pillar distribution? Is any pillar over-concentrated?

3. **Define/refresh content pillars.** Each channel should have 4-6 pillars. Use the defaults below as starting points, then adjust based on performance data.

4. **Set upload cadence.** Use the tier-matched recommendation table. For ambient/music channels, consistency beats volume — irregular uploads hurt subscriber notification CTR.

5. **Build 90-day milestone plan.** Break into 3 monthly phases with specific, measurable targets.

6. **Cross-channel differentiation audit.** Run the non-cannibalization check across all 3 channels. Resolve any pillar overlaps.

7. **Output the strategy document** using the template below.

## Default Content Pillars by Channel

### QF — QuantumFrequencies777 (Binaural / Solfeggio)
| Pillar | Description | Target Share |
|--------|-------------|-------------|
| Core Hz library | Standard solfeggio frequencies (432, 528, 639, 741, 852, 963 Hz) | 35% |
| Gamma focus | 40 Hz gamma for study/focus/cognitive performance | 20% |
| Healing frequencies | Tissue/emotional healing claims (285 Hz, 174 Hz) | 15% |
| Schumann resonance | 7.83 Hz Earth frequency, grounding | 10% |
| Hz combinations | Multi-frequency blends (e.g., 528+432, DNA repair stacks) | 12% |
| Chakra | Chakra-aligned frequencies (root 396 Hz → crown 963 Hz) | 8% |

### SCL — Sleepy Cloud Lullabies (Sleep / Lullaby)
| Pillar | Description | Target Share |
|--------|-------------|-------------|
| Baby/infant sleep | Lullabies and soft music for infant sleep | 30% |
| Adult insomnia | Long-form sleep music (3hr, 8hr) for adult listeners | 25% |
| Nature + sleep | Rain, ocean, forest soundscapes blended with soft music | 20% |
| Nap/power rest | 20-30 min focused rest music, non-sleep depth | 12% |
| Relaxation | Daytime de-stress / anxiety relief ambient | 13% |

### PS — Pure Static Noise (Noise / Masking)
| Pillar | Description | Target Share |
|--------|-------------|-------------|
| Brown noise | Primary pillar — deepest masking, ADHD focus + sleep | 35% |
| White noise | Classic sleep noise, infant sleep crossover | 20% |
| Pink noise | Memory/sleep cycle optimization | 15% |
| Rain/storm | Nature-derived masking (heavy rain, thunder, mixed) | 15% |
| Fan/mechanical | Fan hum, AC, ambient mechanical for focus | 10% |
| ASMR-adjacent | Soft textured sounds (pages turning, fire crackling) | 5% |

## Upload Cadence Recommendations

| Monthly Views | Recommended Cadence | Notes |
|---------------|---------------------|-------|
| < 50K/mo | 3-4 videos/week | Maximize catalog coverage — more evergreen titles = more search surface |
| 50K-200K/mo | 4-5 videos/week | Scale with consistent pillar rotation |
| 200K-500K/mo | 5-7 videos/week | Daily if pipeline can sustain it without quality drop |
| 500K+/mo | 7+ videos/week | Daily + Shorts supplementary feed |

**For ambient channels specifically:** Uploading at consistent times (same day/time each week per channel) increases subscriber notification open rate. The 6am/7am slot performs well for sleep content (users checking their morning routine).

**Shorts cadence:** 2-3 Shorts/week per channel is the minimum to maintain Shorts feed presence. See `youtube-shorts-strategy` for ambient Shorts production.

## Milestone Framework (90-Day)

### Month 1: Foundation Audit + Pillar Stabilization
- Audit current pillar distribution against targets above
- Fill any pillar with < 3 videos (thin pillars hurt playlist SEO)
- Ensure all published videos have correct chapters + timestamps
- Set up playlist pages per pillar (one playlist per pillar minimum)
- **Measurable target:** All pillars at ≥ 3 videos; playlist pages created

### Month 2: Gap Fill + Format Experiments
- Produce top 5 opportunities from `youtube-competitor-recon` output
- Test at least 1 new format (new duration tier, new visual style, or Shorts version)
- A/B test 2 thumbnail variants on lowest-CTR video
- **Measurable target:** 5 gap-fill videos live; 1 A/B thumbnail test run

### Month 3: Optimization + Momentum
- Analyze Month 2 performance — double down on what moved CTR/AVD
- Expand best-performing new format into a full content push
- Review monetization posture — see `youtube-monetize` skill if needed
- **Measurable target:** CTR improvement ≥ 0.5% on at least one pillar; 1 new pillar or sub-niche validated

## Cross-Channel Non-Cannibalization Rules

The 3 channels must remain distinctly positioned. Apply these hard rules:

| Content Type | Correct Channel | Never on |
|-------------|-----------------|----------|
| Binaural beats + Hz labels | QF | SCL, PS |
| Lullabies (baby/child focus) | SCL | QF, PS |
| White/brown/pink noise (pure) | PS | QF, SCL |
| Nature sounds + soft music | SCL (if sleepy) or PS (if masking) | QF |
| Meditation music (no Hz label) | QF or SCL — pick one, commit | Never both |
| Study focus music | PS (if noise-based) or QF (if Hz-based) | SCL |
| ASMR-style ambient | PS | QF, SCL |

**Resolve ambiguous content:** If a concept could fit two channels, assign it to the channel with the lower recent upload volume (underserved channel gets the boost).

## Output Template

```markdown
## 90-Day Strategy: [Channel Name] — [Date]

**Current state:**
- Subscribers: [N]
- Monthly views: [N]
- CTR: [X%] | AVD: [Xmin Xs]
- Traffic mix: Browse [X%] / Search [X%] / Suggested [X%]
- Current cadence: [X videos/week]

**Primary goal:** [Growth / Monetization / Both]

---

### Positioning Statement
[One paragraph: what this channel is, who it serves, and why it's distinct from the other 2 empire channels]

### Content Pillar Plan

| Pillar | Current # | Target Share | Gap | Priority |
|--------|-----------|-------------|-----|----------|
| [Pillar 1] | [N] | [X%] | [+N needed] | [High/Med/Low] |
| ... | | | | |

### Upload Cadence
**Current:** [X/week] | **Recommended:** [X/week]
**Rationale:** [One sentence]
**Optimal publish times:** [Day + time, based on audience timezone data if available]

### 90-Day Milestone Plan

**Month 1 (Foundation):**
- [ ] [Specific task]
- Target: [Measurable metric]

**Month 2 (Gap Fill):**
- [ ] [Specific task]
- Target: [Measurable metric]

**Month 3 (Momentum):**
- [ ] [Specific task]
- Target: [Measurable metric]

### Cross-Channel Audit
**QF ↔ SCL overlap risk:** [None / [Specific overlap + resolution]]
**SCL ↔ PS overlap risk:** [None / [Specific overlap + resolution]]
**QF ↔ PS overlap risk:** [None / [Specific overlap + resolution]]

### Next Actions (This Week)
1. [Highest priority concrete action]
2. [Second action]
3. [Third action]
```

## Common Pitfalls

1. **Strategy without performance data.** Never write a strategy without knowing the current CTR, AVD, and traffic source split. If you don't have it, run `youtube-analytics-feedback-loop` first.
2. **KPI dumping instead of strategy.** When presenting strategy or analytics, DO NOT just dump basic KPIs or vanity metrics. The user is strictly focused on aggressive growth ("make this empire huge"). Lead with the most actionable, high-leverage insights (e.g., format pivots, breakable sub-niches, empirical PMF proof) and skip the technical/metric recaps. Adhere strictly to the user's verbosity intolerance rules (cut recaps, give bottom line).
3. **Setting unrealistic growth targets.** Ambient channels grow slower than viral/trend content. Month-over-month 5-10% view growth is excellent for a mature channel. Don't set targets that require trending behavior.
4. **Pillar imbalance causing keyword myopia.** If QF has 80% of videos in "432 Hz" and zero in Schumann/Gamma/Chakra, the channel is algorithmically fragile. Search volume drops → channel views collapse. Enforce pillar targets.
5. **Ignoring Shorts in cadence planning.** Shorts are the cheapest way to grow subscriber count for ambient channels. 15-30 second clips of existing audio with a looped visual are almost zero-effort. Build Shorts cadence into the plan.
5. **Cross-channel drift.** The biggest risk to the empire is two channels competing for the same keywords. Review the non-cannibalization table every 90 days and reassign any drifted content.
6. **The "Video Uploads per day" Quota Trap.** Google maintains two separate YouTube API quotas: the visible 10,000 Points (`Queries per day`), and a hidden anti-spam filter (`Video Uploads per day`). New channels are strictly limited to ~5-6 video uploads per day regardless of API points remaining. 
   * **Automation Pitfall:** When a batch upload script hits this 429 quota error, it MUST gracefully `break` the loop and exit cleanly. NEVER use `sys.exit(1)` on a quota limit—this kills the orchestrator and breaks downstream jobs. Other video-specific upload errors should `continue` to the next video.
   * **Solution:** Use drip-feed cron jobs (e.g., 5/day max) to slowly build algorithmic trust until the limit scales (usually 4-8 weeks).

## Verification Checklist

- [ ] Current channel state data confirmed (not estimated)
- [ ] All content pillars defined with target shares that sum to 100%
- [ ] Non-cannibalization check run across all 3 channels
- [ ] Upload cadence recommendation grounded in current view volume tier
- [ ] Each monthly milestone has a measurable target (not "improve CTR")
- [ ] Next 3 concrete actions identified (can begin this week)
- [ ] Strategy document saved to `~/workspace/youtube_empire/strategy/[channel]_90day_[date].md`
