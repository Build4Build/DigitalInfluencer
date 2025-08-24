# Generate a video from script text using free tools (gTTS + moviepy)
# In production, use TTS (gTTS) and moviepy, or a virtual influencer API

from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
import os

def generate_video(script_text: str) -> str:
    # Generate TTS audio from script
    tts = gTTS(text=script_text, lang='en')
    audio_path = "output_audio.mp3"
    tts.save(audio_path)

    # Create a solid color background image (1280x720)
    from PIL import Image, ImageDraw, ImageFont
    img_path = "background.png"
    img = Image.new('RGB', (1280, 720), color=(30, 144, 255))  # Dodger blue
    d = ImageDraw.Draw(img)
    # Add title text (optional, short)
    title = "Australian Immigration News"
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
    d.text((50, 50), title, fill=(255,255,255), font=font)
    img.save(img_path)

    # Create video clip from image
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    image_clip = ImageClip(img_path).set_duration(duration)
    image_clip = image_clip.set_audio(audio_clip)

    # Optionally, add fade-in/out or text overlays here
    video_path = "output_video.mp4"
    image_clip.write_videofile(video_path, fps=24, codec="libx264", audio_codec="aac")

    # Clean up temp files
    os.remove(audio_path)
    os.remove(img_path)

    return video_path 