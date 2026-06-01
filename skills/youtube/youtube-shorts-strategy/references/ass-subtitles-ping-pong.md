# FFmpeg Ping-Pong Looping & ASS Subtitle Generation

Captured 2026-05-24 during YouTube Shorts pipeline automation.

## 1. Seamless Ping-Pong Loops
When generating 8-second or 30-second clips from generative video models (like Veo 3.1), they often need to be extended into 30s-60s Shorts for higher Average View Duration (AVD).
The most effective way to loop generative ambient scenes without a jarring jump-cut is a ping-pong loop (forward, reverse, forward, reverse).

```bash
# Example: Looping an 8s raw video to 32s (4 iterations)
ffmpeg -y -i input_8s.mp4 \
  -filter_complex "[0:v]reverse[r];[0:v][r][0:v][r]concat=n=4:v=1:a=0[v]" \
  -map "[v]" \
  -c:v libx264 -preset fast -crf 20 \
  output_32s.mp4
```

## 2. ASS Subtitles vs. drawtext
The default FFmpeg `drawtext` filter is rigid—it doesn't wrap long text properly, alignment is flaky depending on text bounding boxes, and it produces an outdated aesthetic. 
For a 2026 premium aesthetic, inject ASS (Advanced SubStation Alpha) subtitles. 
ASS provides perfect coordinate centering, text wrapping, and elegant soft drop-shadows.

### Example ASS Template (`.ass`)
```ini
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Georgia,75,&H00FFFFFF,&H00FFFFFF,&H00000000,&H88000000,-1,0,0,0,100,100,1,0,1,0,4,5,80,80,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:07.00,Default,,0,0,0,,Listen to this 432 Hz frequency\Nfor just 10 seconds\Nto clear your anxiety.
```
*Note: Use `\N` for manual newlines.*
*PlayRes is explicitly set to the 9:16 Shorts resolution (1080x1920) so `Alignment 5` (Center-Center) and the 80px side margins map correctly.*

### Muxing ASS in FFmpeg
```bash
ffmpeg -y -i video.mp4 -i audio.wav \
  -filter_complex "[0:v]subtitles=template.ass[v]" \
  -map "[v]" -map 1:a \
  -c:v libx264 -preset fast -crf 20 \
  -c:a aac -b:a 192k \
  output_final.mp4
```