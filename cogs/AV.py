#import libraries
import discord
from discord.ext import commands
from collections import deque
from tempfile import TemporaryFile
from gtts import  gTTS
import urllib.parse, urllib.request, re
from asyncio import sleep, queues
import shutil
import os
import sys
import asyncio
from googlesearch import search
from google_images_search import GoogleImagesSearch
from bs4 import BeautifulSoup
from discord.utils import get
import youtube_dl
# from main import r2d2

#google project API
apikey = os.environ.get('API_KEY')

#google search engine token
cx = os.environ.get('CX')
gis = GoogleImagesSearch(apikey, cx)

#Audio/Visual commands class
class AV(commands.Cog):
    def __init__(self, r2d2):
        self.r2d2 = r2d2

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
            await ctx.send("Either you are not in a voice channel, or I can't see the channel...")
            return

    #leave call command
    @commands.command()
    async def leave(self, ctx):
        try:
            await ctx.voice_client.disconnect(force=True)
            return
        except(TypeError, AttributeError):
            await ctx.send("Not possible...")
            return

    #text to speech command
    @commands.command(aliases=["texttospeech", "tts", "speak"])
    async def say(self, ctx):
        message_queue = deque([])
        message = ctx.message.content[5:]
        user = ctx.message.author.display_name
        # message = user + " says " + message
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
                await ctx.send("I'm not in a voice channel and neither are you...")
            return
        f.close()
  
    ###################################################################################

    @commands.command(aliases=["p"])
    async def play(self, ctx, *url: str):
        print("accepted play command")
        channel = ctx.message.author.voice.channel
        voice1 = get(ctx.voice_client, guild=ctx.guild)

        if voice1 is not None:
            await voice1.move_to(channel)

        try:
            await channel.connect()
        except:
            print("already in voice channel")

        def checkqueue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                    print("first file =" + first_file)
                except:
                    print("No more queued songs")
                    queues.clear()
                    return
                main_location = os.path.dirname(
                    os.path.realpath("./Queue"))
                print("main location = " + main_location)
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                print("song path = " + song_path)
                if length != 0:
                    print("Song done, playing next queued song\n")
                    print(f"Songs still in queue: {still_q}")
                    song_exists = os.path.isfile("song.mp3")
                    if song_exists:
                        os.remove("song.mp3")
                    shutil.move(song_path, main_location)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, 'song.mp3')
                    voicenew.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: checkqueue())
                    voicenew.source = discord.PCMVolumeTransformer(voicenew.source)
                    voicenew.source.volume = 0.15
                else:
                    queues.clear()
                    return
            else:
                queues.clear()
                print("No songs were queued before the ending of the last song")

        song_exists = os.path.isfile("song.mp3")
        try:
            if song_exists:
                os.remove('song.mp3')
                queues.clear()
                print("removed existing song")
        except PermissionError:
            await ctx.send("Another song is already playing")
            print("exception error")
            return

        Queue_infile = os.path.isdir("./Queue")
        try:
            Queue_folder = "./Queue"
            if Queue_infile is True:
                print("Removed old Queue Folder")
                shutil.rmtree(Queue_folder)
        except:
            print("No old queue folder")

        await ctx.send("Hold on, getting everything ready (this clears the queue as well)")

        voicenew = get(ctx.voice_client, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': './song.mp3',
            'postprocessors': [{
                'key': "FFmpegExtractAudio",
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        song_search = " ".join(url)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("downloading audio now...\n")
            ydl.download([f"ytsearch1:{song_search}"])

        voicenew.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: checkqueue())
        voicenew.source = discord.PCMVolumeTransformer(voicenew.source)
        voicenew.source.volume = 0.15

        print("playing song successfully")
        await ctx.send(f"Playing song")

    @commands.command()
    async def pause(self, ctx):
        voice2 = get(ctx.voice_client, guild=ctx.guild)

        if voice2 and voice2.is_playing():
            voice2.pause()
            await ctx.send("Music is paused")
        elif voice2.is_paused():
            voice2.resume()
            await ctx.send("Resuming music")
        else:
            await ctx.send("Music isn't playing")

    @commands.command()
    async def skip(self, ctx):
        voice3 = get(ctx.voice_client, guild=ctx.guild)
        queues.clear()
        if voice3 and voice3.is_playing():
            voice3.stop()
            await ctx.send("Song skipped")
        else:
            await ctx.send("Music is not playing")

    global queues
    queues = {}

    @commands.command(aliases=["q", "qu", "que"])
    async def queue(self, ctx, *url: str):
        queue_infile = os.path.isdir("./Queue")
        if queue_infile is False:
            os.mkdir("./Queue")
        DIR = os.path.abspath(os.path.realpath("Queue"))
        qlength = len(os.listdir(DIR))
        qlength += 1
        add_queue = True
        while add_queue:
            if qlength in queues:
                qlength += 1
            else:
                add_queue = False
                queues[qlength] = qlength
        queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{qlength}.%(ext)s")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': queue_path,
            'postprocessors': [{
                'key': "FFmpegExtractAudio",
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        song_search = " ".join(url)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("downloading queue audio now...\n")
            ydl.download([f"ytsearch1:{song_search}"])
        await ctx.send("Adding song " + str(qlength) + " to the queue")


    #################################################################################


    #google image search command
    @commands.command(aliases=["gi","googleimages","googlei","gimage","gimages"])
    async def googleimage(self, ctx,*imaged):
        Images_infile = os.path.isdir("E:\Projects\GitHub\R2-D2\Images")
        await ctx.send("Beep, boop...")
        try:
            Images_folder = "E:\Projects\GitHub\R2-D2\Images"
            if Images_infile is True:
                shutil.rmtree(Images_folder)
                print("Removed old Images folder")
                os.mkdir("E:\Projects\GitHub\R2-D2\Images")
                print("Made new Images folder")
            else:
                os.mkdir("E:\Projects\GitHub\R2-D2\Images")
                print("images_infile was false, making images folder")
        except:
            print("No old images folder")
            os.mkdir("E:\Projects\GitHub\R2-D2\Images")
            print("Made new images folder")
        Images_infile2 = os.path.isdir("E:\Projects\GitHub\R2-D2\Images")
        if Images_infile2 is False:
            return await ctx.send("Brrp-bloop :(")
        q = " ".join(imaged)
        start = 1
        _search_params = {
            'q': q,
            'searchType': 'image',
            'start': start,
            'safe': 'medium',
            'fileType': 'jpg',
            'imgType': None,
            'imgSize': None,
            'imgDominantColor': None
        }
        gis.search(search_params=_search_params, path_to_dir='E:\Projects\GitHub\R2-D2\Images')
        count = 1
        dirrr = "E:\Projects\GitHub\R2-D2\Images"
        for file in os.listdir(dirrr):
            if file.endswith(".jpg"):
                os.rename(f"E:\Projects\GitHub\R2-D2\Images\{file}",
                          f"E:\Projects\GitHub\R2-D2\Images\image{count}.jpg")
                count += 1
        for image in os.listdir('E:\Projects\GitHub\R2-D2\Images'):
            if image.startswith("image"):
                await ctx.send(file=discord.File(f'E:\Projects\GitHub\R2-D2\Images\{image}'))

#required setup def
def setup(r2d2):
    r2d2.add_cog(AV(r2d2))    