from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv

############
############
class setnick(commands.Cog):
    def __int__(self, bot):
        self.bot = bot
    @commands.command(aliase=['سمي'])
    @commands.has_role(support_role)
    async def setnick(self, ctx, member : discord.Member = None , *, nick = "by kmcodes"):
        if member == None:
            await ctx.send("**❌ You Must Mention Member First**")
        else:
            await member.edit(nick=nick)
            await ctx.send(f"✅ i change {member.name} nick to {nick}")


def setup(bot):
    bot.add_cog(setnick(bot))
