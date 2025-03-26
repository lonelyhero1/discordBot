import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# 讀取 .env 檔案
load_dotenv()

# 讀取環境變數
TOKEN = os.getenv("DISCORD_TOKEN")
# 啟用機器人
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    channel = bot.get_channel(1353871024206381076)  # 請替換為你的頻道 ID
    if channel:
        await channel.send("Hello, world!123")
        
    # 加載擴展模組
    for ext in ['commands.basic', 'commands.twitch']:
        try:
            await bot.load_extension(ext)  
            print(f"✅ 已載入模組: {ext}")
        except Exception as e:
            print(f"❌ 加載模組 {ext} 時發生錯誤: {e}")

# 啟動機器人
bot.run(TOKEN)
