# YouTube Shorts Subtitle Mechanics: ASS over Drawtext

When programmatically generating YouTube Shorts (9:16 vertical aspect ratio), adding an on-screen text "hook" is critical to breaking the swipe-reflex. However, the default FFmpeg `drawtext` filter is famously rigid: it doesn't wrap long text properly, has archaic border styling, and can drift off-center.

**The Solution:** Use **ASS (Advanced SubStation Alpha)** subtitles injected via FFmpeg's `subtitles` filter instead of `drawtext`.

## Why ASS is superior for 2026 Shorts Automation
1. **Perfect Centering & Margins:** ASS maps text to a strict coordinate system (e.g., `PlayResX: 1080`, `PlayResY: 1920`). By setting `Alignment: 5` (true center-center) and defining side margins (e.g., `MarginL: 80`, `MarginR: 80`), the text auto-wraps elegantly and never bleeds off the phone screen.
2. **Premium Typography:** Drop the 2012 meme-style black borders. ASS supports sophisticated typography, soft translucent drop-shadows (e.g., `&H88000000`), and elegant serif fonts (like Georgia) that look cinematic against ambient visuals (like Veo 3.1 aurora renders).

## Code Recipe

Generate the `.ass` file programmatically, replacing standard newlines with `\N`:

```python
ass_text = text.replace('\\n', '\\N').replace('\n', '\\N')

ass_content = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Georgia,75,&H00FFFFFF,&H00FFFFFF,&H00000000,&H88000000,-1,0,0,0,100,100,1,0,1,0,4,5,80,80,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:07.00,Default,,0,0,0,,{ass_text}
"""
ass_path.write_text(ass_content)
```

Then burn it into the final mux using `[0:v]subtitles=your_file.ass[v]`:

```python
cmd = [
    "ffmpeg", "-y",
    "-i", str(video),
    "-i", str(audio),
    "-filter_complex", f"[0:v]subtitles={str(ass_path)}[v]",
    "-map", "[v]", "-map", "1:a",
    "-c:v", "libx264", "-preset", "fast", "-crf", "20",
    str(out_path)
]
subprocess.run(cmd, check=True)
```

Use this technique whenever generating or upgrading programmatic Shorts to match 2026 premium aesthetics.