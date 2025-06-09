# Virtual Influencer YouTube Bot

This project is a fully automated, easily re-themable virtual influencer that fetches the latest news in a specific niche (default: Australian immigration), generates a narrated video, and uploads it to YouTube.

## Features
- Fetches real news using NewsAPI (free tier)
- Summarizes news using OpenAI GPT (optional, free tier)
- Generates video using gTTS (free) and moviepy (free)
- Uploads to YouTube (requires free OAuth setup)
- Easily change the niche/topic in `.env`

## Setup

### 1. Clone the repo and install dependencies
```sh
pip install -r requirements.txt
```

### 2. Create a `.env` file with the following variables:
```
NEWS_API_KEY=your_newsapi_key
YOUTUBE_API_KEY=your_youtube_api_key  # (not used, but reserved)
VIDEO_GEN_API_KEY=your_video_gen_api_key  # (not used, but reserved)
GOOGLE_APPLICATION_CREDENTIALS=client_secret.json  # Path to your YouTube OAuth credentials
YOUTUBE_CHANNEL_ID=your_channel_id
NARRATOR_VOICE=default
NICHE="Australian immigration news"
POST_SCHEDULE="0 9 * * 1,4"
OPENAI_API_KEY=your_openai_api_key  # Optional, for better summarization
```

- Get a free NewsAPI key at https://newsapi.org/
- (Optional) Get a free OpenAI key at https://platform.openai.com/
- For YouTube upload, create OAuth credentials in Google Cloud Console and download `client_secret.json`.

### 3. Run the bot
```sh
python main.py
```

- The script will fetch news, generate a summary, create a video, and upload (or simulate upload) to YouTube.
- The output video will be `output_video.mp4`.

## Changing the Niche/Theme
- Edit the `NICHE` variable in `.env` to any topic (e.g., "crypto news", "AI breakthroughs", etc.).
- The bot will fetch and summarize news for the new topic automatically.

## Scheduling (Optional)
- Use `cron` or a Python scheduler to run the bot twice a week as desired.

## All services used are free (NewsAPI, gTTS, moviepy, OpenAI free tier, YouTube Data API).

---

**Enjoy your automated virtual influencer!** 
