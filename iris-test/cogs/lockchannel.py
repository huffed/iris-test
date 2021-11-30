import discord
from discord.ext import commands
import config
import asyncio

class LockChannel(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  # # Events
  # @commands.Cog.listener()

  # Commands
  @commands.command()
  @commands.has_any_role(897976674921099284, 900893222052692008)
  async def lockchannel(self, ctx):
    guild = self.client.get_guild(config.guild_id)
    role = guild.get_role(config.verifyrole)
    overwrites = ctx.channel.overwrites_for(role)
    overwrites.send_messages=False
    await ctx.channel.set_permissions(role, overwrite=overwrites)
    embed=discord.Embed(
        color=0x0066ff,
        description=f":lock: Locked **{ctx.channel}**"
    )
    embed.set_footer(text=config.default_footer)
    message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(5)
    await message.delete()

  @commands.command()
  @commands.has_any_role(897976674921099284, 900893222052692008)
  async def unlockchannel(self, ctx):
    guild = self.client.get_guild(config.guild_id)
    role = guild.get_role(config.verifyrole)
    overwrites = ctx.channel.overwrites_for(role)
    overwrites.send_messages=True
    await ctx.channel.set_permissions(role, overwrite=overwrites)
    embed=discord.Embed(
        color=0x0066ff,
        description=f":closed_lock_with_key: Unlocked **{ctx.channel}**"
    )
    embed.set_footer(text=config.default_footer)
    message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(5)
    await message.delete()

  @lockchannel.error
  async def lockchannel_error(self, ctx, error):
    if isinstance(error, discord.ext.commands.MissingPermissions):
          embed=discord.Embed(
            color=0xde0000,
            description="Insufficient permissions."
          )
          embed.set_author(name="Error", icon_url=config.error)
          embed.set_footer(text=config.default_footer)
          msg = await ctx.channel.send(embed=embed)
          await asyncio.sleep(3)
          await msg.delete()
          await ctx.message.delete()
          print(error)
    else:
          embed=discord.Embed(
            color=0xde0000,
            description="Error detected in `lockchannel`."
          )
          embed.set_author(name="Error", icon_url=config.error)
          embed.set_footer(text=config.default_footer)
          msg = await ctx.channel.send(embed=embed)
          await asyncio.sleep(3)
          await msg.delete()
          await ctx.message.delete()
          print(error)

  @unlockchannel.error
  async def unlockchannel_error(self, ctx, error):
    if isinstance(error, discord.ext.commands.MissingPermissions):
          embed=discord.Embed(
            color=0xde0000,
            description="Insufficient permissions."
          )
          embed.set_author(name="Error", icon_url=config.error)
          embed.set_footer(text=config.default_footer)
          msg = await ctx.channel.send(embed=embed)
          await asyncio.sleep(3)
          await msg.delete()
          await ctx.message.delete()
          print(error)
    else:
          embed=discord.Embed(
            color=0xde0000,
            description="Error detected in `unlockchannel`."
          )
          embed.set_author(name="Error", icon_url=config.error)
          embed.set_footer(text=config.default_footer)
          msg = await ctx.channel.send(embed=embed)
          await asyncio.sleep(3)
          await msg.delete()
          await ctx.message.delete()
          print(error)

def setup(client):
  client.add_cog(LockChannel(client))