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
    @commands.command(aliase=['فعل'])
    @commands.has_role(support_role)
    async def active(self, ctx, member: discord.Member):
        active = ctx.guild.get_role(member_role_id)
        if active in member.roles:
            await ctx.send("**❌ This Member Already Activated**")

        else:
            await member.add_roles(active)
            await ctx.send(f"**✅: [{member.mention}] has been activated**")
    @commands.command(aliase=['ازلة التفعيل'])
    @commands.has_role(support_role)
    async def unactive(self, ctx, member: discord.Member):
        active = ctx.guild.get_role(member_role_id)
        if active in member.roles:
            await member.remove_roles(active)
            await ctx.send(f"**✅ : [{member.mention}] has been unactivated**")
        else:
            await ctx.send("**❌ This Member Already UNactivated**")

def setup(bot):
    bot.add_cog(active(bot))
