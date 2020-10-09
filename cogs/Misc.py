#import libraries
from discord.ext import commands
import random

#Miscellaneous commands class
class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #ping pong, space robot edition
    @commands.command()
    async def beep(self, ctx):
        await ctx.send("Boop!")
    
    #latency command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Beep zzt boop: {round(self.bot.latency * 1000)} ms") #return bot latency

    #purge messages command
    @commands.command(aliases=["purge", "decimate", "destroy"])
    async def clear(self, ctx, amount = 5): #default magnitude of 5
        await ctx.channel.purge(limit=amount) #clear messages

    #8 ball command
    @commands.command(aliases=['8ball', 'lucky?', 'luck', 'lucky'])
    async def eightball(self, ctx, *, question): #requires a question
        responses = [ "Beep boop.", #list of R2-D2 responses
                      "Boop!",
                      "Zzzt...",
                      "Zzt boop!",
                      "Boop? Zzt.",
                      "Beep.",
                      "Boop, beep zzt.",
                      "BEEEP!!!"]

        await ctx.send(f"{random.choice(responses)}") #return a random response from list

#required setup def
def setup(bot):
    bot.add_cog(Misc(bot))