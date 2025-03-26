import requests
import os
from dotenv import load_dotenv

# 讀取 .env 檔案
load_dotenv()

# 從環境變數讀取 Twitch API 金鑰
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_OAUTH_TOKEN = os.getenv("TWITCH_OAUTH_TOKEN")

HEADERS = {
    "Client-ID": TWITCH_CLIENT_ID,
    "Authorization": f"Bearer {TWITCH_OAUTH_TOKEN}"
}

def check_twitch_stream(channel_name):
    url = f"https://api.twitch.tv/helix/streams?user_login={channel_name}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            stream_info = data["data"][0]
            return {
                "live": True,
                "title": stream_info["title"],
                "viewers": stream_info["viewer_count"],
                "game": stream_info["game_name"],
                "url": f"https://www.twitch.tv/{channel_name}"
            }
        else:
            return {"live": False}
    else:
        return {"error": f"API 請求失敗，錯誤碼: {response.status_code}"}
