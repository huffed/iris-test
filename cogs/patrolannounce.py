import discord
from discord.ext import commands,tasks
import asyncio
import config

class PatrolAnnouncement(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @tasks.loop(hours=24)
  async def patrolannounceuk(self):
    guild = self.client.get_guild(config.guild_id)
    channelToSendTo = guild.get_channel(898234664509136997)
    try:
      await channelToSendTo.send("**UK Patrol Notification** - <@&898231182502817792>")
    except Exception as error:
      print(' cannot be loaded. [{}]'.format(error))

  @tasks.loop(hours=24)
  async def patrolannounceus(self):
    guild = self.client.get_guild(config.guild_id)
    channelToSendTo = guild.get_channel(898234664509136997)
    try:
      await channelToSendTo.send("**US Patrol Notification** - <@&898231182502817792>")
    except Exception as error:
      print(' cannot be loaded. [{}]'.format(error))

  @commands.command()
  async def startuk(self, ctx):
    print("uk patrol noti loop started")
    self.patrolannounceuk.start()
  @commands.command()
  async def stopuk(self, ctx):
    print("uk patrol noti loop stopped")
    self.patrolannounceuk.stop()
  @commands.command()
  async def startus(self, ctx):
    print("us patrol noti loop started")
    self.patrolannounceus.start()
  @commands.command()
  async def stopus(self, ctx):
    print("us patrol noti loop stopped")
    self.patrolannounceus.stop()

def setup(client):
  client.add_cog(PatrolAnnouncement(client))