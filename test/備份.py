import discord
import json
import requests
from discord.ext import commands

# Discord Bot Token
DISCORD_BOT_TOKEN = ""

# Twitch API 認證資訊
TWITCH_CLIENT_ID = ""
TWITCH_OAUTH_TOKEN = ""
TWITCH_API_URL = "https://api.twitch.tv/helix/streams?user_login="

# 讀取channels.json


def load_channels():
    with open("channels.json", "r", encoding="utf-8") as file:
        return json.load(file)

# check直播狀態


def check_twitch_stream(user_login):
    url = f"{TWITCH_API_URL}{user_login}"
    HEADERS = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_OAUTH_TOKEN}"
    }
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            stream_info = data["data"][0]
            return f"🎥 **{stream_info['user_name']}** 目前正在直播！🔥\n🎮 遊戲: {stream_info.get('game_name', '未知')}\n📌 標題: {stream_info['title']}\n👀 觀看人數: {stream_info['viewer_count']}\n🔗 直播網址: https://www.twitch.tv/{user_login}"
        else:
            return None
    else:
        return f"❌ API 請求失敗，錯誤碼: {response.status_code}"


# 設定 Discord Bot 指令前綴
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot 啟動時執行


@bot.event
async def on_ready():
    print(f"✅ Discord Bot 已啟動，登入身份：{bot.user}")

# 指令: 查詢所有主播的直播狀態


@bot.command()
async def 開台(ctx):
    channels = load_channels()
    messages = []
    for name, user_login in channels.items():
        result = check_twitch_stream(user_login)
        if result:
            messages.append(result)

    if messages:
        await ctx.send("\n\n".join(messages))
    else:
        await ctx.send("📢 目前沒有人開台！")

# 不需要使用! 前綴的指令


@bot.event
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == bot.user:
        return
    # 新訊息包含Hello，回覆Hello, world!
    if message.content == "Hello":
        await message.channel.send("Hello, world!")
    await bot.process_commands(message)

# 關閉機器人指令


@bot.command()
async def 關閉(ctx):
    if ctx.author.id == 579274467029680129:  # 限制只有你能關閉機器人
        await ctx.send("機器人即將關閉...")
        await bot.close()
    else:
        await ctx.send("你沒有權限關閉機器人！")
# 啟動 Bot
bot.run(DISCORD_BOT_TOKEN)
