import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import config
import asyncio

load_dotenv()
intents = discord.Intents.all()
client = commands.Bot(command_prefix = config.prefix, help_command=None, intents=intents)

@client.event
async def on_ready():
  loaded_cogs_list = []
  print(f'\nLogged in as {client.user}\n')

  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        # To blacklist cogs uncomment the three lines below and indent the two bottom lines of code
        if filename == "ctxDIR.py" or filename == "dir.py" or filename == "lockdown.py":
            pass
        else:
            client.load_extension(f'cogs.{filename[:-3]}')
            print('Loaded {}'.format(filename[:-3]))

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    print('{} used command "{}" - {}'.format(ctx.message.author.name, ctx.invoked_with, error))
    if ctx.channel != config.verifyChannel:
        embed=discord.Embed(
            color=0xde0000,
            description=f"{ctx.message.author.mention} - Command `{ctx.invoked_with}` not found. - [`{error}`]"
        )
        embed.set_author(name="Error", icon_url=config.error)
        embed.set_footer(text=config.default_footer)
        message = await ctx.send(embed=embed)
        await asyncio.sleep(10)
        await ctx.message.delete()
        await message.delete()

@client.command()
@commands.has_any_role("DCRP | Bot Developer")
async def load(ctx, extension):

  try:
    channel = client.get_channel(config.loadunloadreloadlogs)
    client.load_extension(f'cogs.{extension}')
    print('Loaded {}'.format(extension))
    embed=discord.Embed(
        color=0x0066ff,
        description=f"Loaded **{extension}**"
    )
    embed.set_footer(text=config.default_footer)
    embed2=discord.Embed(
        color=0x0066ff,
        description=f"{ctx.message.author.mention} loaded **{extension}**")
    embed2.set_footer(text=f"User ID: {ctx.message.author.id}")
    embed2.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.message.author.avatar_url}")
    await channel.send(embed=embed2)
    message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(2)
    await message.delete()
  except Exception as error:
      print('{} cannot be loaded. [{}]'.format(extension, error))
      embed=discord.Embed(
          color=0x0066ff,
          description=f"**{extension}** cannot be loaded. [**{error}**]"
      )
      embed.set_footer(text=config.default_footer)
      message = await ctx.send(embed=embed)
      await ctx.message.delete()
      await asyncio.sleep(20)
      await message.delete()

@client.command()
@commands.has_any_role("DCRP | Bot Developer")
async def unload(ctx, extension):
  try:
    channel = client.get_channel(config.loadunloadreloadlogs)
    client.unload_extension(f'cogs.{extension}')
    print('Unloaded {}'.format(extension))
    embed=discord.Embed(
        color=0x0066ff,
        description=f"Unloaded **{extension}**"
    )
    embed.set_footer(text=config.default_footer)
    embed2=discord.Embed(
        color=0x0066ff,
        description=f"{ctx.message.author.mention} unloaded **{extension}**")
    embed2.set_footer(text=f"User ID: {ctx.message.author.id}")
    embed2.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.message.author.avatar_url}")
    await channel.send(embed=embed2)
    message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(2)
    await message.delete()
  except Exception as error:
    print('{} cannot be unloaded. [{}]'.format(extension, error))
    embed=discord.Embed(
        color=0x0066ff,
        description=f"**{extension}** cannot be unloaded. [**{error}**]"
    )
    embed.set_footer(text=config.default_footer)
    message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(20)
    await message.delete()

@client.command()
@commands.has_any_role("DCRP | Bot Developer")
async def reload(ctx, extension):
  try:
    channel = client.get_channel(config.loadunloadreloadlogs)
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print('Reloaded {}'.format(extension))
    embed=discord.Embed(
        color=0x0066ff,
        description=f"Reloaded **{extension}**"
    )
    embed.set_footer(text=config.default_footer)
    embed2=discord.Embed(
        color=0x0066ff,
        description=f"{ctx.message.author.mention} reloaded **{extension}**")
    embed2.set_footer(text=f"User ID: {ctx.message.author.id}")
    embed2.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.message.author.avatar_url}")
    await channel.send(embed=embed2)
    message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(2)
    await message.delete()
  except Exception as error:
    print('{} cannot be reloaded. [{}]'.format(extension, error))
    embed=discord.Embed(
        color=0x0066ff,
        description=f"**{extension}** cannot be reloaded. [**{error}**]"
    )
    embed.set_footer(text=config.default_footer)
    message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(20)
    await message.delete()

client.run(os.getenv("TOKEN"))
