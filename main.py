#KMCODES SYSTEM ----------- DEV:MUHAMMAD KR
#GITHUB : KINGMAN1996
from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def main():
  return "KMCODES/KINGMAN4HACK"
def run():
  app.run(host="0.0.0.0", port=8080)
def keep_alive():
  server = Thread(target=run)
  server.start()
keep_alive()
"""
*        Power By KMCODES
*        DEVLOPER KINGMMAN4HACLK
*        Phone Number +962792914245 
*        RealName: Muhammad Rafat Kurakar
*        PY/CSS/JS/PHP/HTML/CSS/C++/C#/RUBY
"""
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv
import os
from random import randrange
load_dotenv()
prefix = "."
km = commands.Bot(command_prefix=prefix , case_insensitive=True , owner_id=1)

TOKEN = os.getenv('TOKEN')
ssupport_role = os.getenv('SUPPORT_ROLE')
smember_role_id = os.getenv('MEMBER_ROLE')
sadmine_role = os.getenv('ADMINE_ROLE')
sbanlogchannel = os.getenv('BAN_LOG')
sblacklistmanager = os.getenv('BLACK_LIST_MANAGER')
sblack_list_role = os.getenv('BLACK_LIST_ROLE')
sblackllog = os.getenv('BLACK_LIST_LOG')
skikelogchannel = os.getenv('KICK_LOG')
smute = os.getenv('MUTE_ROLE')
srolelogchannel = os.getenv('ADD_REMOVE_ROLES_LOG')
swarnlogchannelid = os.getenv('WARN_LOG')
#########
km.remove_command('help')
game = "BOT STATUS"

kmbanner = """
KMCODES
"""
@km.event
async def on_ready():
    await km.change_presence(activity=discord.Streaming(name=f"{game}", url = "https://www.twitch.tv/kingman4hack"))
    print("KM SYSTEM log in as ")
    print(km.user.name)
    print(km.user.id)
    print(discord.__version__)
    print("---------")
    print(kmbanner)
    print("Server Connect to")
    for guild in km.guilds:
        print(guild.name)
        print(guild.id)
        print("----------")


@km.command()
async def help(ctx):
    embed=discord.Embed(title="HELP", url="https://github.com/KINGMAN1996", description=f"<@&{admine_role}>\n `{prefix}ban` : ban members \n `{prefix}kick` : kick members \n `{prefix}addrole` : addrole to members \n `{prefix}removerole ` : remove role from members\n  <@&{support_role}> \n `{prefix}active` : active members\n`{prefix}unactive` : unactive members\n`{prefix}clear `: clear chat\n`{prefix}lock` : lock channels\n`{prefix}unlock `: unlock channels\n`{prefix}mute` : mute members\n`{prefix}setnick` : setnick name\n`{prefix}warn` : warn members \n\n <@&{blacklistmanager}>\n `{prefix}blacklist` \n {prefix}unblacklist", color=0x237bf5)
    embed.set_author(name="</> KM SYSTEM", url="https://github.com/KINGMAN1996")
    embed.set_footer(text="</> Power By KMCodes")
    await ctx.send(embed=embed)
@km.command()
async def embedm(ctx, *, msg ):
    embed=discord.Embed(description=f"{msg}")
    await ctx.send(embed=embed)
@km.command()
async def say(ctx , *, msg):
    await ctx.send(msg)

@km.command()
async def lover(ctx, member: discord.Member = None):
    if member == None:
        await ctx.send()
    x = randrange(100)
    if x > 50:
        embed=discord.Embed(title="**نسبة الحب**", url="https://github.com/KINGMAN1996", description=f"**[{ctx.author.mention}] __love__ [{member.mention}] [{str(x)}%]**", color=0xff0000)
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.set_footer(text="Dev KMCODES&KINGMAN")
        embed.set_image(url="https://2.bp.blogspot.com/-M1OUfMPOVVc/WoR7I-6FGlI/AAAAAAAAHPA/SHsGZG3fQpAcUFtWNSPkektTV2kqC9CPwCLcBGAs/s1600/SmartSelectImage_%25D9%25A2%25D9%25A0%25D9%25A1%25D9%25A8-%25D9%25A0%25D9%25A2-%25D9%25A1%25D9%25A4-%25D9%25A2%25D9%25A0-%25D9%25A1%25D9%25A9-%25D9%25A3%25D9%25A4.png")
        await ctx.send(embed=embed)
    elif x < 50:
        embed=discord.Embed(title="**نسبة الحب**", url="https://github.com/KINGMAN1996", description=f"**[{ctx.author.mention}] __love__ [{member.mention}] [{str(x)}%]**", color=0xff0000)
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.set_footer(text="Dev KMCODES&KINGMAN")
        embed.set_image(url="https://d3b4rd8qvu76va.cloudfront.net/d96/9becf/1b38/40f0/9f3a/c8751fb5c946/large/1960104.jpg")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="**نسبة الحب**", url="https://github.com/KINGMAN1996", description=f"**[{ctx.author.mention}] __love__ [{member.mention}] [{str(x)}%]**", color=0xff0000)
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.set_footer(text="Dev KMCODES&KINGMAN")
        embed.set_image(url="https://www.freevector.com/uploads/vector/preview/2672/FreeVector-Broken-Heart-Cartoon.jpg")
        await ctx.send(embed=embed)


# [**{ctx.author.mention} __love__ {member.mention} []**]
#
#set_image(url="")

###
#print(randrange(10))
###
km.load_extension("kmmoderation.active")
km.load_extension("kmmoderation.ban")
km.load_extension("kmmoderation.blacklist")
km.load_extension("kmmoderation.clear")
km.load_extension("kmmoderation.kick")
km.load_extension("kmmoderation.lock")
km.load_extension("kmmoderation.mute")
km.load_extension("kmmoderation.role")
km.load_extension("kmmoderation.setnick")
km.load_extension("kmmoderation.warn")
km.load_extension("kmmoderation.error")


km.run(TOKEN)
