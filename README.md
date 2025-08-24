# Virtual Influencer YouTube Bot 🤖

This project is a fully automated, easily re-themable virtual influencer that fetches the latest news in a specific niche, generates a narrated video, and uploads it to YouTube.

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
- Use `crontab` or a Python scheduler to run the bot twice a week as desired.


## Who Created This Digital Influencer Electron App?

**Pierre-Henry Soria**. A **super passionate engineer** who loves automating content creation efficiently!

Enthusiast of YouTube, AI, learning, and—of course—writing! Find me at [pH7.me](https://ph7.me)

Enjoying this project? **[Buy me a coffee](https://ko-fi.com/phenry)** (spoiler: I love almond extra-hot flat white coffees).

[![Pierre-Henry Soria](https://s.gravatar.com/avatar/a210fe61253c43c869d71eaed0e90149?s=200)](https://ph7.me "Pierre-Henry Soria’s personal website")

[![@phenrysay][x-icon]](https://x.com/phenrysay "Follow Me on X")  [![YouTube Tech Videos][youtube-icon]](https://www.youtube.com/@pH7Programming "My YouTube Tech Channel")  [![pH-7][github-icon]](https://github.com/pH-7 "Follow Me on GitHub")  [![BlueSky][bsky-icon]](https://bsky.app/profile/ph7s.bsky.social "Follow Me on BlueSky")


---

**Enjoy your automated virtual influencer!** 



<!-- GitHub's Markdown reference links -->
[x-icon]: https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x
[bsky-icon]: https://img.shields.io/badge/BlueSky-00A8E8?style=for-the-badge&logo=bluesky&logoColor=white
[github-icon]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[youtube-icon]: https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white
