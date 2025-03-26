from discord.ext import commands

# 建立指令類別
class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        print("Hello!")
        await ctx.send("Hello, world!")

# 註冊 Cog
async def setup(bot): 
    await bot.add_cog(BasicCommands(bot))
