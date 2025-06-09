import os
import openai
from config import NICHE

# Summarize news items into a script for narration
# Uses OpenAI GPT if API key is set, else falls back to simple concatenation

def summarize_news(news_items):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        openai.api_key = openai_api_key
        # Compose prompt for GPT
        prompt = f"Summarize the following news items about {NICHE} in a friendly, engaging way for a YouTube video script:\n\n"
        for item in news_items:
            prompt += f"- {item['title']}: {item['content']}\n"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI error: {e}")
            # Fallback to simple concatenation
    # Fallback: simple concatenation
    script = "\n".join([f"{item['title']}: {item['content']}" for item in news_items])
    return script 