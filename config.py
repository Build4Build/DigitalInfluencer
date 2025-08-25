import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Niche/topic for the virtual influencer (easily changeable)
NICHE = os.getenv("NICHE", "Australian immigration news")

# Video configuration
VIDEO_TITLE = os.getenv("VIDEO_TITLE", "Australian Immigration News")

# API keys and credentials
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
VIDEO_GEN_API_KEY = os.getenv("VIDEO_GEN_API_KEY")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")
NARRATOR_VOICE = os.getenv("NARRATOR_VOICE", "default")
POST_SCHEDULE = os.getenv("POST_SCHEDULE", "0 9 * * 1,4")  # Default: 9am Mon & Thu

# Add more config as needed 