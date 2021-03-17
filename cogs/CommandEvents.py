#import libraries
import discord
from discord.ext import commands

#event listeners class
class CommandEvents(commands.Cog):
    def __init__(self, r2d2):
        self.r2d2 = r2d2

    #command errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name + " was invoked incorrectly. Error:") #incorrect usage of command
        print(error) #print error

#required setup def
def setup(r2d2):
    r2d2.add_cog(CommandEvents(r2d2))