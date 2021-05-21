from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv

############

############
class clear(commands.Cog):
    def __int__(self, bot):
        self.bot = bot
    @commands.command(aliase=['مسح'])
    @commands.has_role(support_role)
    async def clear(self, ctx , num : int = 10):
        if num > 500 or num < 0:
            await ctx.send(f"**❌ Invalid Amount Maximum 500**")
        await ctx.channel.purge(limit = num)
        await ctx.send(f"**Sucsses Delete `{num}` message**")

def setup(bot):
    bot.add_cog(clear(bot))
