import discord
from discord.ext import commands
import config


class BotDevCommands(commands.Cog):

  def __init__(self, client):
    self.client = client

  # # Events
  # @commands.Cog.listener()

  # Commands
  @commands.command()
  @commands.has_any_role(config.leadbotdev)
  async def send100(self, ctx, *args):
    if len(args) >= 2:
      embed=discord.Embed(
      color=0xde0000,
      description="Too many arguments given."
      )
      embed.set_author(name="Error", icon_url=config.error)
      embed.set_footer(text=config.default_footer)
      message = await ctx.channel.send(embed=embed)
      await asyncio.sleep(3)
      await msg.delete()
      await ctx.message.delete()
    else:
      if len(args) == 0:
        embed=discord.Embed(
          color=0xde0000,
          description="You must give an argument."
        )
        embed.set_author(name="Error", icon_url=config.error)
        embed.set_footer(text=config.default_footer)
        message = await ctx.channel.send(embed=embed)
        await asyncio.sleep(3)
        await msg.delete()
        await ctx.message.delete()
      else:
        embed=discord.Embed(
          color=0x0066ff,
          description="**Are you sure you want to send 100 messages, this will take some time**"
        )
        embed.set_author(name="", icon_url=config.question)
        embed.set_footer(text=config.default_footer)
        clientmsg = await ctx.channel.send(embed=embed)
        yes = ["y","yes"]
        no = ["n", "no"]
        def check(msg):
          return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in yes or msg.content.lower() in no
        msg = await self.client.wait_for("message", check=check)
        if msg.content.lower() in yes:
          for i in range(1, 100):
            await ctx.channel.send(args[0])
        else:
          pass

def setup(client):
  client.add_cog(BotDevCommands(client))