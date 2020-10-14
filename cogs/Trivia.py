from discord.ext import commands
import discord

#Star Wars Trivia Class
class Trivia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #All of the Trivia Questions in the form of Question, 4 Options, Answer

    q1 = ("Which Star Wars movie was filmed entirely in the studio?", 
          "A. Star Wars",
          "B. Attack of the Clones",
          "C. Revenge of the Sith",
          "D. Return of the Jedi",
          "C"
          )

    q2 = ("'The Star Wars Holiday Special' marked the first appearance of which Star Wars character?",
          "A. Bobba Fett",
          "B. Jar Jar Binks",
          "C. Jabba the Hutt",
          "D. Lando Calrissian",
          "A"
          )


    @commands.command()
    async def trivia(self, ctx):
        await ctx.send("Welcome to Star Wars Trivia! Answer by entering the letter answer below! Let's Begin.")


#required setup def
def setup(bot):
    bot.add_cog(Trivia(bot))