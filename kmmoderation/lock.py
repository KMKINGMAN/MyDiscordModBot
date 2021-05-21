from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv

class lock(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(aliases=['قفل'])
  @commands.has_any_role(support_role)
  async def lock(self, ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('**تم قفل الشات**')
  @commands.command(aliases=['افتح'])
  @commands.has_any_role(support_role)
  async def unlock(self, ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = None
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('**تم فتح الشات**')




def setup(bot):
  bot.add_cog(lock(bot))