from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv

class ban(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(aliases=['بند'])
  @commands.has_any_role(admine_role)
  async def ban(self, ctx, member : discord.Member = None, *, reason=None):
    if member == None:
      await ctx.send("**❌ You Must Mention User First**")
    if reason == None:
      reason = "بدون سبب"
    if black_list_role in [role.id for role in ctx.author.roles] or ctx.author.top_role <= member.top_role:
      await ctx.send("** ❌ You Cant Ban This User**")
    else:
      banlog = self.bot.get_channel(banlogchannel)
      embed=discord.Embed(title="Ban LOG", description="تم تبنيد شخص من السيرفر", color=0x0467da)
      embed.set_author(name="</>KMCodes")
      embed.add_field(name="اسم الاداري", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="اي دي الاداري", value=f"{ctx.author.id}", inline=True)
      embed.add_field(name="اسم العضو", value=f"{member.mention}", inline=True)
      embed.add_field(name="اي دي العضو", value=f"{member.id}", inline=True)
      embed.add_field(name="السبب", value=f"{reason}", inline=True)
      embed.set_footer(text="</> KMCodes & KINGMAN")
      await ctx.send(f"**✅ [{member.name}] Hass Been Baned From The Server**")
      await member.ban(reason=reason)
      await banlog.send(embed=embed)











    @commands.command(aliases=['فك بان'])
    @commands.has_any_role(admine_role)
    async def unban(self, ctx, id: int = None, *, reason=None):
      if id == None:
        await ctx.send("حدد شخص لكي اقوم بفك البان عنه")
      if reason == None:
        reason = "بدون سبب"
      if black_list_role in [role.id for role in ctx.author.roles]:
        await ctx.send(cant_ban_member_up_role)
      else:
        banlog = self.bot.get_channel(banlogchannel)
        embed=discord.Embed(title="UNBAN LOG", description="تم فك بان شخص من السيرفر", color=0x0467da)
        embed.set_author(name="</>KMCodes")
        embed.add_field(name="اسم الاداري", value=f"{ctx.author.mention}", inline=True)
        embed.add_field(name="اي دي الاداري", value=f"{ctx.author.id}", inline=True)
        embed.add_field(name="اي دي العضو", value=f"{id}", inline=True)
        embed.add_field(name="السبب", value=f"{reason}", inline=True)
        embed.set_footer(text="</>KMCodes KINGMAN")
        if len(str(id)) == 18:
          user = await self.bot.fetch_user(id)
          await ctx.guild.unban(user)
          await ctx.send("تم فك البان عن الشخص المحدد")
          await banlog.send(embed=embed)



def setup(bot):
    bot.add_cog(ban(bot))
