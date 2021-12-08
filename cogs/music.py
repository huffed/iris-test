import discord
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL
import re
import config

class Music(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  def findurl(self, string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    return [x[0] for x in url]
  
  # # Events
  # @commands.Cog.listener()

  # Commands
  @commands.command()
  async def join(self, ctx):
    if ctx.author.voice is None:
      embed=discord.Embed(
        color=0x0066ff,
        description=f"{ctx.message.author.mention} You must join a voice channel.")
      embed.set_footer(text=f"{config.default_footer}")
      await ctx.send(embed=embed)
      voice_channel = ctx.author.voice.Channel
      voice = get(client.voice_clients, guild=ctx.guild)
      if voice and voice.is_connected():
        await voice.move_to(voice_channel)
      else:
        voice = await voice_channel.connect()

  @commands.command()
  async def disconnect(self,ctx):
    embed=discord.Embed(
      color=0x0066ff,
      description=f"Disconnected from {ctx.author.voice.Channel}.")
    embed.set_footer(text=f"{config.default_footer}")
    await ctx.send(embed=embed)
    await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self, ctx):
    string = "My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/"
    print("hello")
    print(findurl(string))
    print("hello")
    if ck_url(ctx.content) == True:
      YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      voice = get(client.voice_clients, guild = ctx.guild)

      if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPMCAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        print(info)
    else:
      print("PLACEHOLDER")

def setup(client):
  client.add_cog(Music(client))