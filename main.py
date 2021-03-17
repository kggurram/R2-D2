# import libraries
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from itertools import cycle 

#status list - need to add more
status = cycle(['X-Wing Simulator',
                'Death Star Decimator',
                'Rebel Anthem',
                'Battlefront II (2005)',
                "with Leia's heart",
                'Saving Luke',
                'the Skywalker Theme',
                'Saving Anakin',
                'Saving the Galaxy'
                ])

#load .env file and aquire token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#set command prefix
r2d2 = commands.Bot(command_prefix = '>')

#list of cog files
extensions = ['cogs.Administrator', 'cogs.CommandEvents', 'cogs.Misc', 'cogs.AV', 'cogs.Trivia']

#load cog files
if __name__ == "__main__":
    for ext in extensions:
        r2d2.load_extension(ext)

#bot is ready alert
@r2d2.event
async def on_ready():
    change_status.start() #starts status activity loop
    print("Beep, boop.")

#changes status of the bot every 60 seconds
@tasks.loop(seconds=60)
async def change_status():
    await r2d2.change_presence(activity=discord.Game(next(status))) #switched to next status

#run bot
r2d2.run(TOKEN)