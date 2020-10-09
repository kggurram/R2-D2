#import libraries
import discord
from discord.ext import commands

#event listeners class
class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #bot is ready alert
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('X-Wing Simulator'))
        print("Beep, boop.")

    #command errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name + " was invoked incorrectly. Error:") #incorrect usage of command
        print(error) #print error

#required setup def
def setup(bot):
    bot.add_cog(CommandEvents(bot))