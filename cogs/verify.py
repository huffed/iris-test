import discord
from discord.ext import commands
import config
import asyncio
from discord.utils import get
import random

class Verify(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.channel.id == config.verifyChannel and not message.content.startswith(".verify "):
        if message.author == self.client.user:
            pass
        else:
            await message.delete()

  @commands.command()
  async def verify(self, ctx, *args):
    if args == () and ctx.channel.id == config.verifyChannel:
      msg = await ctx.send("Missing arguments")
      await asyncio.sleep(2)
      await msg.delete()
      await ctx.message.delete()
    elif ctx.channel.id != config.verifyChannel or args == ():
      msg = await ctx.send("This command can't be used in this channel.")
      await asyncio.sleep(2)
      await msg.delete()
      await ctx.message.delete()
    elif ctx.channel.id == config.verifyChannel and args[0] != config.verifycode:
      msg = await ctx.send("Incorrect code.")
      await asyncio.sleep(2)
      await msg.delete()
      await ctx.message.delete()
    else:
      if ctx.channel.id == config.verifyChannel and args[0] == config.verifycode:
        await ctx.message.delete()
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, id=config.verifyrole)
        await member.add_roles(role)
        channel = self.client.get_channel(config.verifylogs)
        embed=discord.Embed(
            color=0x0066ff,
            description=f"**{member}** verified and got **{role}** role")
        embed.set_footer(text=f"User ID: {ctx.message.author.id}")
        await channel.send(embed=embed)

  @commands.command()
  async def verifymessage(self, ctx):
    channel = self.client.get_channel(config.verifyChannel)
    embed=discord.Embed(
      title="Verification:",
      color=0x0066ff,
      )
    embed.add_field(name="To confirm that you are not a bot, please enter:", value=f"`.verify {config.verifycode}`")
    embed.set_footer(text=config.default_footer)
    await channel.send(embed=embed)

  @verify.error
  async def verify_error(self, ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
      await ctx.send("Missing required arguments.")
      await ctx.message.delete()
    else:
      print(error)

def setup(client):
  client.add_cog(Verify(client))
