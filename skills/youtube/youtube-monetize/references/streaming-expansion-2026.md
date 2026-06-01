# Ambient Revenue Expansion: Streaming Platforms (2026)

YouTube AdSense for ambient channels is capped at ~$1.75 RPM, requiring ~55M views/mo to hit $100k. Streaming platforms offer blended RPMs of ~$6.60 and capture passive 8-hour loops.

## Platform Intelligence
1. **Amazon Music:** Massive passive volume via Alexa ("Alexa, play brown noise"). Streams while users sleep count as paid streams.
2. **Apple Music:** Pays 2-3x more than Spotify ($0.007-$0.010). Offers a **10% royalty bonus** for Spatial Audio/Dolby Atmos. (Binaural beats map perfectly to this bonus).
3. **Spotify:** Lowest RPM ($0.003-$0.005) and destroys binaural beats via aggressive audio compression (collapsing stereo fields). Best for melodic ambient (Sleepy Cloud Lullabies) and Noise (Pure Static), but **avoid for frequency-specific binaural content (QF777)**.

## Distribution Automation (DistroKid)
- **The API Gap:** DistroKid remains the best for high-volume ($39/yr Musician Plus for 2 artists). However, they strictly block official API access. The iOS wrapper `distrogo` is deprecated and requires risky token sniffing.
- **The Playbook:** Use headless browser automation (Playwright/Puppeteer) with persistent contexts (to bypass 2FA) to automate DistroKid web uploads.
- **PRO Registration:** B2B licensing requires ASCAP/BMI registration for the LLC to collect performance royalties.