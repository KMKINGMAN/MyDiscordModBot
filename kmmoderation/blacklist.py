from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv


class blacklist(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['حرمان'])
  @commands.has_any_role(blacklistmanager)
  async def blacklist(self, ctx, user: discord.Member):
      if ctx.message.author.id == user.id:
          await ctx.send(f"**❌ You Cant add blacklist to your self :)**")
          return


      bl = ctx.guild.get_role(black_list_role)
      #await ctx.user.send(f"**l{logemoji}l**You are Black Listed")
      await user.add_roles(bl)
      embed=discord.Embed(title="Blacklist System", description="تمت اضافة شخص لقائمة البلاك ليست و هو محروم من اوامر الادارة", color=0x0772f0)
      embed.set_author(name="</> KMCodes")
      embed.add_field(name="المحروم", value=f"{user.mention}", inline=False)
      embed.add_field(name="الاداري ", value=f"{ctx.author.mention}", inline=True)
      embed.set_footer(text="</>KMCodes KINGMAN")
      await ctx.send(f"**✅ {user.name} Hass Beeen added to BlackLists**")
      bllog = self.bot.get_channel(blackllog)
      await bllog.send(embed=embed)


      #log

  @commands.command(aliases=['سامحناك'])
  @commands.has_any_role(blacklistmanager)
  async def unblacklist(self, ctx, user: discord.Member):
      bl = ctx.guild.get_role(black_list_role)
      await user.remove_roles(bl)
      #await ctx.user.send(f"**l{logemoji}l**You are unBlack Listed")
      embed=discord.Embed(title="Blacklist System", url="https://github.com/KINGMAN1996", description="تمت ازالة شخص لقائمة البلاك ليست و هو محروم من اوامر الادارة", color=0x0772f0)
      embed.set_author(name="</> KMCodes", url="https://github.com/KINGMAN1996")
      embed.add_field(name="عاد من جديد", value=f"{user.mention}", inline=False)
      embed.add_field(name="الاداري ", value=f"{ctx.author.mention}", inline=True)
      embed.set_footer(text="</>KMCodes KINGMAN")
      await ctx.send(f"**✅ {user.name} Hass Beeen Removed from BlackLists**")
      bllog = self.bot.get_channel(blackllog)
      await bllog.send(embed=embed)



def setup(bot):
  bot.add_cog(blacklist(bot))
