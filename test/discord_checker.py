# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    channel = bot.get_channel(頻道id)  # 請替換為你的頻道 ID
    if channel:
        await channel.send("Hello, world!")

@bot.command()
# %Hello
async def Hello(ctx):
    # 回覆Hello, world!
    await ctx.send("Hello, world!")


@bot.command()
# %shutdown
async def shutdown(ctx):
    if ctx.author.id == 你的id:  # 限制只有你能關閉機器人
        await ctx.send("機器人即將關閉...")
        await bot.close()
    else:
        await ctx.send("你沒有權限關閉機器人！")

bot.run("bot token")
