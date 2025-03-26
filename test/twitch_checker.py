import requests

# 請填入你的 Twitch Client ID 和 OAuth Token
TWITCH_CLIENT_ID = "id"
TWITCH_OAUTH_TOKEN = "token"
TWITCH_CHANNEL = "name"  # 你要查詢的 Twitch 直播主名稱

# Twitch API 端點
TWITCH_API_URL = f"https://api.twitch.tv/helix/streams?user_login={TWITCH_CHANNEL}"

# 設定請求標頭
HEADERS = {
    "Client-ID": TWITCH_CLIENT_ID,
    "Authorization": f"Bearer {TWITCH_OAUTH_TOKEN}"
}

def check_twitch_stream():
    response = requests.get(TWITCH_API_URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            stream_info = data["data"][0]
            print(f"{TWITCH_CHANNEL} 目前正在直播！")
            print(f"標題: {stream_info['title']}")
            print(f"觀看人數: {stream_info['viewer_count']}")
            print(f"遊戲: {stream_info['game_name']}")
            print(f"直播網址: https://www.twitch.tv/{TWITCH_CHANNEL}")
        else:
            print(f"{TWITCH_CHANNEL} 目前沒有開台。")
    else:
        print(f"API 請求失敗，錯誤碼: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    check_twitch_stream()
