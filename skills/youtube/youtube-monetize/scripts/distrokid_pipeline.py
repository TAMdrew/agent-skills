import asyncio
import os
import subprocess
from pathlib import Path
from playwright.async_api import async_playwright, expect

# --- CONFIGURATION ---
DISTROKID_EMAIL = os.environ.get("DISTROKID_EMAIL", "your_email@example.com")
DISTROKID_PASSWORD = os.environ.get("DISTROKID_PASSWORD", "your_password")
STATE_DIR = Path.home() / "workspace" / "youtube_empire" / "state" / "browser_state"
WORKSPACE = Path.home() / "workspace" / "youtube_empire"

async def extract_audio_for_streaming(video_path: Path, output_dir: Path) -> Path:
    """
    Extracts high-fidelity audio from an MP4 and formats it as a 16-bit 44.1kHz WAV
    (the optimal format for DistroKid/Apple Music/Spotify delivery).
    """
    print(f"[*] Extracting audio from {video_path.name}...")
    output_dir.mkdir(parents=True, exist_ok=True)
    wav_path = output_dir / f"{video_path.stem}_master.wav"
    
    # FFmpeg command: extract audio, convert to 44.1kHz, 16-bit WAV (CD quality standard)
    cmd = [
        "ffmpeg", "-y", "-i", str(video_path),
        "-vn", # Disable video
        "-acodec", "pcm_s16le", # 16-bit PCM
        "-ar", "44100", # 44.1 kHz sample rate
        "-ac", "2", # Stereo
        str(wav_path)
    ]
    
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"[+] Audio extracted successfully: {wav_path.name}")
    return wav_path

async def distrokid_upload_single(
    playwright, 
    artist_name: str, 
    track_title: str, 
    audio_path: Path, 
    artwork_path: Path, 
    genre: str = "Electronic", 
    secondary_genre: str = "Fitness & Workout" # Often used for ambient/focus
):
    """
    Automates the DistroKid single-track upload form.
    Uses persistent context to bypass 2FA after the first manual login.
    """
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    
    # Launch browser with persistent state (saves cookies/session)
    browser = await playwright.chromium.launch_persistent_context(
        user_data_dir=STATE_DIR,
        headless=False, # Run headed first time to pass 2FA if needed
        args=["--disable-blink-features=AutomationControlled"]
    )
    
    page = browser.pages[0]
    
    print("[*] Navigating to DistroKid...")
    await page.goto("https://distrokid.com/new")
    
    # 1. Login if not authenticated
    if "/signin" in page.url:
        print("[!] Not logged in. Automating login...")
        await page.fill("input[name='email']", DISTROKID_EMAIL)
        await page.fill("input[name='password']", DISTROKID_PASSWORD)
        await page.click("button:has-text('Sign In')")
        
        # Wait for potential 2FA prompt
        print("[!] Waiting for login success (handle 2FA manually if prompted)...")
        await page.wait_for_url("**/new**", timeout=60000)
    
    print(f"[*] Beginning upload for: {artist_name} - {track_title}")
    
    # 2. Select Stores (Default is all, usually fine, but you can uncheck specific ones if needed)
    
    # 3. Number of songs: 1 (Single)
    await page.locator("input[name='songCount']").first.click() # Defaults to 1 usually
    
    # 4. Previously released? No
    await page.locator("input[name='previouslyReleased'][value='no']").click()
    
    # 5. Artist/Band Name
    await page.fill("input[name='bandName']", artist_name)
    
    # 6. Release Date (leave default for 'as soon as possible')
    
    # 7. Upload Artwork (Must be exactly 3000x3000px JPG/PNG)
    print(f"[*] Uploading artwork: {artwork_path.name}")
    await page.set_input_files("input[type='file'][accept*='image']", str(artwork_path))
    
    # 8. Primary & Secondary Genre
    await page.select_option("select[name='primaryGenre']", label=genre)
    await page.select_option("select[name='secondaryGenre']", label=secondary_genre)
    
    # 9. Track Title
    await page.fill("input[name='trackName']", track_title)
    
    # 10. Upload Audio File (WAV)
    print(f"[*] Uploading audio: {audio_path.name}")
    await page.set_input_files("input[type='file'][accept*='audio']", str(audio_path))
    
    # 11. Songwriter / Original details
    await page.locator("input[name='isOriginal'][value='yes']").click()
    
    # DistroKid asks for real songwriter names. Put your actual name or LLC info.
    await page.fill("input[name='writerFirstName']", "Andrew")
    await page.fill("input[name='writerLastName']", "Anolasco")
    
    # 12. Explicit Lyrics? No
    await page.locator("input[name='explicit'][value='no']").click()
    
    # 13. Instrumental? Yes (for ambient)
    await page.locator("input[name='instrumental'][value='yes']").click()
    
    # 14. Check all mandatory agreement boxes at the bottom
    print("[*] Checking agreement boxes...")
    checkboxes = await page.locator("input[type='checkbox']").all()
    for box in checkboxes:
        if await box.is_visible() and not await box.is_checked():
            try:
                await box.check(force=True)
            except Exception:
                pass
                
    print("[+] Form filled successfully.")
    
    # 15. SUBMIT (Commented out by default for safety during testing)
    # print("[*] Clicking Submit...")
    # await page.click("button:has-text('DONE')")
    # print("[+] Upload dispatched to stores!")
    # await page.wait_for_url("**/successful**", timeout=120000)
    
    print("[!] TEST MODE: Closing without submitting. Uncomment the Submit block in the code to go live.")
    await browser.close()

async def main():
    print("==================================================")
    print("  DISTROKID AUTOMATED PUBLISHING PIPELINE (v1.0)")
    print("==================================================")
    
    # Example Target: Let's extract audio from a recent Pure Static video
    channel = "pure_static"
    # Provide the path to a finished video and your 3000x3000 album art
    test_video = WORKSPACE / "channels" / channel / "published" / "example_video.mp4" 
    test_art = WORKSPACE / "channels" / channel / "assets" / "album_art_3000x3000.jpg"
    
    # We will output the streaming-ready WAV to a new 'streaming_masters' folder
    output_dir = WORKSPACE / "channels" / channel / "streaming_masters"
    
    # 1. Extract and Format Audio
    if test_video.exists():
        wav_path = await extract_audio_for_streaming(test_video, output_dir)
    else:
        print(f"[!] Test video not found at {test_video}. Please update the path.")
        return

    if not test_art.exists():
        print(f"[!] Album artwork not found at {test_art}. DistroKid requires exactly 3000x3000 px.")
        return

    # 2. Automate DistroKid Upload via Playwright
    async with async_playwright() as p:
        await distrokid_upload_single(
            playwright=p,
            artist_name="Pure Static Noise",
            track_title="Deep Brown Noise (Focus & Sleep)",
            audio_path=wav_path,
            artwork_path=test_art,
            genre="Electronic", 
            secondary_genre="Fitness & Workout"
        )

if __name__ == "__main__":
    asyncio.run(main())