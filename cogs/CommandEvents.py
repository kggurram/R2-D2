#import libraries
from discord.ext import commands

#event listeners class
class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #bot is ready alert
    @commands.Cog.listener()
    async def on_ready(self):
        print("Beep, boop.")

    #command errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name + " was invoked incorrectly. Error:") #incorrect usage of command
        print(error) #print error

#required setup def
def setup(bot):
    bot.add_cog(CommandEvents(bot))