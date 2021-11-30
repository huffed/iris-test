import discord
from discord.ext import commands

class BotDevCommands(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  # # Events
  # @commands.Cog.listener()

  # # Commands
  # @commands.command()

def setup(client):
  client.add_cog(BotDevCommands(client))