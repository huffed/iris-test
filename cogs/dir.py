import discord
from discord.ext import commands

class Dir(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  # # Events
  # @commands.Cog.listener()

  # Commands
  @commands.command()
  async def dir(self, ctx, arg):
    print(arg)
    await ctx.send(f"```{dir(arg)}```")
    print()

def setup(client):
  client.add_cog(Dir(client))