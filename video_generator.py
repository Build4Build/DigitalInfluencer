# Generate a video from script text using free tools (gTTS + moviepy)
# In production, use TTS (gTTS) and moviepy, or a virtual influencer API

from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
import os
from config import VIDEO_TITLE


def generate_video(script_text: str) -> str:
    if not script_text or not script_text.strip():
        raise ValueError("Script text cannot be empty")

    audio_path = "output_audio.mp3"
    img_path = "background.png"
    video_path = "output_video.mp4"

    try:
        # Generate TTS audio from script
        tts = gTTS(text=script_text, lang='en')
        tts.save(audio_path)

        # Create a solid color background image (1280x720)
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (1280, 720), color=(
            30, 144, 255))  # Dodger blue
        d = ImageDraw.Draw(img)
        # Add title text (optional, short)
        title = VIDEO_TITLE
        try:
            # Try different font paths for cross-platform compatibility
            font_paths = [
                "arial.ttf",  # Windows
                "/System/Library/Fonts/Arial.ttf",  # macOS
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Linux
            ]
            font = None
            for font_path in font_paths:
                try:
                    font = ImageFont.truetype(font_path, 60)
                    break
                except (OSError, IOError):
                    continue
            if font is None:
                font = ImageFont.load_default()
        except Exception:
            font = ImageFont.load_default()
        d.text((50, 50), title, fill=(255, 255, 255), font=font)
        img.save(img_path)

        # Create video clip from image
        audio_clip = None
        image_clip = None
        try:
            audio_clip = AudioFileClip(audio_path)
            duration = audio_clip.duration
            image_clip = ImageClip(img_path).set_duration(duration)
            image_clip = image_clip.set_audio(audio_clip)

            # Generate video
            image_clip.write_videofile(
                video_path, fps=24, codec="libx264", audio_codec="aac")
        finally:
            # Properly close clips to free memory
            if audio_clip:
                audio_clip.close()
            if image_clip:
                image_clip.close()

    finally:
        # Clean up temp files (always executed)
        for temp_file in [audio_path, img_path]:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except OSError:
                    pass  # Ignore cleanup errors

    return video_path
