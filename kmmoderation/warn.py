from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv

class warn(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['تحذير'])
  @commands.has_any_role(support_role)
  async def warn(self, ctx, player : discord.Member, *, reason="اسال مين اعطاك الوارن."):

    embed=discord.Embed(title=f"** لقد تم تحذيرك **", url="https://github.com/KINGMAN1996", description="لقد تم تحذيرك", color=0xfe3f00)

    embed.add_field(name="** اسم السيرفر **", value=f"`{player.guild.name}`", inline=False)
    embed.add_field(name="** السبب **", value=f"`{reason}`", inline=False)
    embed.add_field(name="**  اسم الاداري **", value=f"{ctx.message.author.mention}", inline=True)
    embed.set_footer(text="</> KMCodes Warn System")
    
    try:

      await player.send(embed=embed)
      embed=discord.Embed(title="Warning Log", url="https://github.com/KINGMAN1996", description="تم تحذير شخص", color=0x0467da)
      embed.set_author(name="</>KMCodes", url="https://github.com/KINGMAN1996")
      embed.add_field(name="اسم الاداري", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="اي دي الاداري", value=f"{ctx.author.id}", inline=True)
      embed.add_field(name="اسم العضو", value=f"{player.mention}", inline=True)
      embed.add_field(name="اي دي العضو", value=f"{player.id}", inline=True)
      embed.add_field(name="السبب", value=f"{reason}", inline=True)
      embed.set_footer(text="</>KMCodes KINGMAN")
      warnlog = self.bot.get_channel(warnlogchannelid)
      await warnlog.send(embed=embed)
      await ctx.send(f"تم تحذير {player.mention}")
    except:

      embed=discord.Embed(title="Warning Log", description="تم تحذير شخص", color=0x0467da)
      embed.set_author(name="</>KMCodes")
      embed.add_field(name="اسم الاداري", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="اي دي الاداري", value=f"{ctx.author.id}", inline=True)
      embed.add_field(name="اسم العضو", value=f"{player.mention}", inline=True)
      embed.add_field(name="اي دي العضو", value=f"{player.id}", inline=True)
      embed.add_field(name="السبب", value=f"{reason}", inline=True)
      embed.set_footer(text="</>KMCodes KINGMAN")
      warnlog = self.bot.get_channel(warnlogchannelid)
      await warnlog.send(embed=embed)
      await ctx.send(player.mention + "لم تصل الرسالة الى الخاص لكن لم تتم تسجيلها" +  ctx.message.author.mention + "!")



def setup(bot):
  bot.add_cog(warn(bot))