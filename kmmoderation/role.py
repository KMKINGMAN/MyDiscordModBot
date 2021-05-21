from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv



class addrole(commands.Cog):
  def __init__(self, bot):
    self.bot = bot



  @commands.command()
  @commands.has_any_role(admine_role)

  async def addrole(self, ctx, user: discord.Member = None, role: discord.Role = None):
    if user == None:
     await ctx.send("**❌ You Must Mention User First**")
    if role == None:
     await ctx.send("**❌ You Must Mention Role First**")

    if black_list_role in [role.id for role in ctx.author.roles]:
      await ctx.send("لايمكن اضافة رول")
    else:
      embed=discord.Embed(title="Roles Log", url="https://github.com/KINGMAN1996", description="تم اعطاء رول", color=0x0467da)
      embed.set_author(name="</>KMCodes", url="https://github.com/KINGMAN1996")
      embed.add_field(name="اسم الاداري", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="اي دي الاداري", value=f"{ctx.author.id}", inline=True)
      embed.add_field(name="اسم العضو", value=f"{user.mention}", inline=True)
      embed.add_field(name="اي دي العضو", value=f"{user.id}", inline=True)
      embed.add_field(name="الرول", value=f"{role.mention}", inline=True)
      embed.set_footer(text="Power By </>KMCodes & MeCodes")
      rolelog = self.bot.get_channel(rolelogchannel)

      await user.add_roles(role)
      await ctx.send(f"تم اضافة رول {role.mention} بواسطة {ctx.author.mention}")
      await rolelog.send(embed=embed)
  @commands.command()
  @commands.has_any_role(admine_role)
  async def removerole(self, ctx, user: discord.Member = None, role: discord.Role = None):
    if user == None:
     await ctx.send("**❌ You Must Mention User First**")
    if role == None:
     await ctx.send("**❌ You Must Mention Role First**")

    if black_list_role in [role.id for role in ctx.author.roles] or ctx.author.top_role <= user.top_role:
      await ctx.send("لايمكن اضافة رول")
    else:
      embed=discord.Embed(title="Roles Log", url="https://github.com/KINGMAN1996", description="تم ازالة رول", color=0x0467da)
      embed.set_author(name="</>KMCodes", url="https://github.com/KINGMAN1996")
      embed.add_field(name="اسم الاداري", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="اي دي الاداري", value=f"{ctx.author.id}", inline=True)
      embed.add_field(name="اسم العضو", value=f"{user.mention}", inline=True)
      embed.add_field(name="اي دي العضو", value=f"{user.id}", inline=True)
      embed.add_field(name="الرول", value=f"{role.mention}", inline=True)
      embed.set_footer(text="</>KMCodes KINGMAN")
      rolelog = self.bot.get_channel(rolelogchannel)     #role.mention

      await user.remove_roles(role)
      await ctx.send(f"تم ازالة رول {role.mention} بواسطة {ctx.author.mention}")
      await rolelog.send(embed=embed)


def setup(bot):
  bot.add_cog(addrole(bot))
