from config import NICHE
from news_fetcher import fetch_latest_news
from summarizer import summarize_news
from video_generator import generate_video
from youtube_uploader import upload_video

# Main orchestrator for the virtual influencer
if __name__ == "__main__":
    # 1. Fetch latest news in the configured niche
    news_items = fetch_latest_news(NICHE)
    if not news_items:
        print("No news found for the current niche.")
        exit(0)

    # 2. Summarize or script the news for narration
    script_text = summarize_news(news_items)

    # 3. Generate a video with virtual influencer
    video_path = generate_video(script_text)

    # 4. Upload the video to YouTube
    upload_video(video_path, script_text)

    print("Video published successfully!") 