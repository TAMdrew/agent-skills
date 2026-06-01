# Veo 3.1 Native Audio + Ping-Pong Loops

When generating Shorts with Veo 3.1:
1. **Native Audio:** Set `"generateAudio": True` in the Veo API payload. Veo now generates excellent, highly-matching ambient audio alongside the video.
2. **Ping-Pong Loop:** Veo 3.1 outputs 8-second clips. Shorts perform best around 32 seconds. Use an `ffmpeg` ping-pong loop (forward-backward concatenation) to seamlessly extend the 8s clip into a 32s loop while preserving the native audio.
3. **Audio Mixing:** Mix the native Veo audio with a binaural frequency carrier (e.g., 10Hz alpha) and a TTS whisper hook.

Example FFmpeg filter complex for a 4-loop ping-pong that preserves audio:
`[0:v]reverse[rv];[0:a]areverse[ra];[0:v][0:a][rv][ra][0:v][0:a][rv][ra]concat=n=4:v=1:a=1[ov][oa]`