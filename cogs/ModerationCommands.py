import discord
from discord.ext import commands

class ModerationCommands(commands.Cog):

  def __init__(self, client):
    self.client = client

  # # Events
  # @commands.Cog.listener()

  # Commands
  # @commands.command()
  # async def mute():
  #   print('')

def setup(client):
  client.add_cog(ModerationCommands(client))
