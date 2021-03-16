#import libraries
import discord
from discord.ext import commands
from collections import deque
from tempfile import TemporaryFile
from gtts import  gTTS
import urllib.parse, urllib.request, re
from asyncio import sleep

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

    #join call command
    @commands.command()
    async def join(self, ctx):
        try:
            channel = ctx.message.author.voice.channel
            await channel.connect()
            return
        except(TypeError, AttributeError):
            await ctx.send("Either you are not in a voice channel, or I can't see the channel!")
            return

    #leave call command
    @commands.command()
    async def leave(self, ctx):
        try:
            await ctx.voice_client.disconnect(force=True)
            return
        except(TypeError, AttributeError):
            await ctx.send("Can't disconnect from a voice channel when I'm not in one!")
            return

    #text to speech command
    @commands.command(aliases=["texttospeech", "tts", "speak"])
    async def say(self, ctx):
        message_queue = deque([])
        message = ctx.message.content[5:]
        user = ctx.message.author.display_name
        message = user + " says " + message
        try:
            vc = ctx.message.guild.voice_client
            if not vc.is_playing():
                tts = gTTS(message)
                f = TemporaryFile()
                tts.write_to_fp(f)
                f.seek(0)
                vc.play(discord.FFmpegPCMAudio(f, pipe=True))
                while vc.is_playing():
                    await sleep(3)
                await vc.disconnect()
            else:
                message_queue.append(message)
                while vc.is_playing():
                    await asyncio.sleep(0.1)
                tts = gTTS(message_queue.popleft())
                f = TemporaryFile()
                tts.write_to_fp(f)
                f.seek(0)
                vc.play(discord.FFmpegPCMAudio(f, pipe=True))
                while vc.is_playing():
                    await sleep(3)
                await vc.disconnect()
        except(TypeError, AttributeError):
            try:
                tts = gTTS(message)
                f = TemporaryFile()
                tts.write_to_fp(f)
                f.seek(0)
                channel = ctx.message.author.voice.channel
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio(f, pipe=True))
                while vc.is_playing():
                    await sleep(3)
                await vc.disconnect()
            except(AttributeError, TypeError):
                await ctx.send("I'm not in a voice channel and neither are you!")
            return
        f.close()
        

#required setup def
def setup(bot):
    bot.add_cog(AV(bot))    