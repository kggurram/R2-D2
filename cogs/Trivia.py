from discord.ext import commands
import discord

#Star Wars Trivia Class
class Trivia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command
async def trivia(self, ctx):
    await ctx.send("Welcome to Star Wars Trivia! Answer by entering the letter answer below! Let's Begin.")

    pass

#required setup def
def setup(bot):
    bot.add_cog(Trivia(bot))