# Upload video to YouTube using YouTube Data API
# Uses real upload if GOOGLE_APPLICATION_CREDENTIALS is set, else simulates upload

import os
from config import YOUTUBE_CHANNEL_ID, GOOGLE_APPLICATION_CREDENTIALS

def upload_video(video_path: str, script_text: str):
    if GOOGLE_APPLICATION_CREDENTIALS and os.path.exists(GOOGLE_APPLICATION_CREDENTIALS):
        # Real upload using YouTube Data API
        import google_auth_oauthlib.flow
        import googleapiclient.discovery
        import googleapiclient.errors
        import googleapiclient.http
        import httplib2
        import json

        scopes = ["https://www.googleapis.com/auth/youtube.upload"]
        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = GOOGLE_APPLICATION_CREDENTIALS

        # OAuth flow
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_local_server(port=0)
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        # Prepare video metadata
        body = {
            "snippet": {
                "title": script_text.split("\n")[0][:80],  # Use first line as title
                "description": script_text[:500],
                "tags": ["Australia", "Immigration", "Visa", "News"],
                "categoryId": "25"  # News & Politics
            },
            "status": {
                "privacyStatus": "public"
            }
        }
        # Upload video
        try:
            request = youtube.videos().insert(
                part=",".join(body.keys()),
                body=body,
                media_body=googleapiclient.http.MediaFileUpload(video_path, resumable=True)
            )
            response = request.execute()
            print(f"Video uploaded: https://www.youtube.com/watch?v={response['id']}")
            return True
        except Exception as e:
            print(f"YouTube upload error: {e}")
            return False
    else:
        # Simulate upload
        print(f"Uploading {video_path} to YouTube with description: {script_text[:60]}...")
        print("(Simulated upload: Set up GOOGLE_APPLICATION_CREDENTIALS for real upload)")
        return True
