#import libraries
from discord.ext import commands
import urllib.parse, urllib.request, re

#Audio/Visual commands class
class AV(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #youtube search command
    @commands.command(aliases=["yt", "youtube"])
    async def yTube(self, ctx, *, search):
        query_string = urllib.parse.urlencode({'search_query': search}) #parse query
        html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string) #search and parse html content of search
        search_results = re.findall(r'/watch\?v=(.{11})', html_content.read().decode()) #refine to videos
        print(search_results) #print searches
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0]) #return first result

#required setup def
def setup(bot):
    bot.add_cog(AV(bot))    