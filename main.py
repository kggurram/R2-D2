# import libraries
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#load .env file and aquire token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#set command prefix
r2d2 = commands.Bot(command_prefix = '?')

#list of cog files
extensions = ['cogs.Administrator', 'cogs.CommandEvents', 'cogs.Misc', 'cogs.AV']

#load cog files
if __name__ == "__main__":
    for ext in extensions:
        r2d2.load_extension(ext)

#run bot
r2d2.run(TOKEN)