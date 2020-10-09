import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import urllib.parse, urllib.request, re
import datetime
# from discord import Reaction

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

r2d2 = commands.Bot(command_prefix = '?')

@r2d2.event
async def on_ready():
    print("Beep, boop.")

@r2d2.command()
async def beep(ctx):
    await ctx.send("Boop!")
    
@r2d2.command()
async def ping(ctx):
    await ctx.send(f"Beep zzt boop: {round(r2d2.latency * 1000)} ms")
    
@r2d2.command(aliases=['8ball', 'lucky?', 'luck', 'lucky'])
async def eightball(ctx, *, question):
    responses = [ "Beep boop.",
                  "Boop!",
                  "Zzzt...",
                  "Zzt boop!",
                  "Boop? Zzt.",
                  "Beep.",
                  "Boop, beep zzt.",
                  "BEEEP!!!"]

    await ctx.send(f"{random.choice(responses)}")

@r2d2.command(aliases=["purge", "decimate", "destroy"])
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

@r2d2.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    
@r2d2.command()
@commands.has_any_role("Administrator, Bot")
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention}, twee-vwoop ZZT! >:(")

@r2d2.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention}, zzt beep :/")
            return

@r2d2.command(aliases=["yt", "youtube"])
async def yTube(ctx, *, search):
    query_string = urllib.parse.urlencode({'search_query': search})
    html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@r2d2.event
async def on_command_error(ctx, error):
    print(ctx.command.name + "was invoked incorrectly.")
    print(error)

r2d2.run(TOKEN)