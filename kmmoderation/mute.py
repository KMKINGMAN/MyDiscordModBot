from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv

############
############
class active(commands.Cog):
    def __int__(self, bot):
        self.bot = bot
    @commands.command(aliase=['ميوت'])
    @commands.has_role(support_role)
    async def mute(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.send("**❌ You Must Mention User First**")
        muters = ctx.guild.get_role(mute)
        if muters in member.roles:
            await ctx.send("**❌ This Member Already Muted**")

        else:
            await member.add_roles(muters)
            await ctx.send(f"**✅ [{member.name}] Hass Been Muted From The Server**")
    @commands.command(aliase=['فك الميوت'])
    @commands.has_role(support_role)
    async def unmute(self, ctx, member: discord.Member):
        muters = ctx.guild.get_role(mute)
        if muters in member.roles:
            await member.remove_roles(muters)
            await ctx.send(f"**✅ [{member.name}] Hass Been UNMuted From The Server**")
        else:
            await ctx.send("**❌ This Member NOT Muted !!!**")

def setup(bot):
    bot.add_cog(active(bot))
