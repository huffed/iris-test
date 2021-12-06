import discord
from discord.ext import commands

class ctxDIR(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  # # Events
  # @commands.Cog.listener()

  # Commands
  @commands.command()
  async def ctxDIR(self, ctx):
    await ctx.send(f"```{dir(ctx.message.author)}```")

def setup(client):
  client.add_cog(ctxDIR(client))