import discord
from discord.ext import commands
import banned_words
import linkblacklist
import whitelistedlinks
import config
import asyncio
import re
import os

class Automod(commands.Cog):

  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_message(self, ctx):
    if ctx.author.bot == True:
      pass
    else:
      guild = self.client.get_guild(config.guild_id)
      blacklist = [897965307388383332, 897965405673496606, 900504453285814293, 901229355953438800, 897965827528228885, 900893222052692008]
      authormemberobj = guild.get_member(int(ctx.author.id))
      authorroles = authormemberobj.roles
      sendMessage = []
      for i in authorroles:
        if i.id in blacklist:
          sendMessage.append(False)
      if False not in sendMessage:
        if i.id not in blacklist:
          ctx.content = re.sub(r"\s+", "", ctx.content.lower(), flags=re.UNICODE)
          ctx.content = ctx.content.replace(",", "")
          if any(banned_word in ctx.content for banned_word in banned_words.list):
              await ctx.delete()
              message = await ctx.channel.send(f"{ctx.author.mention} Watch your language.")
              await asyncio.sleep(5)
              await message.delete()
      capitalletters = []
      for word in ctx.content:
        if word.isupper():
          capitalletters.append(word)
      if False not in sendMessage:
        if i.id not in blacklist:
          if len(capitalletters) > 10:
            await ctx.delete()
            message = await ctx.channel.send(f"{ctx.author.mention} Too many caps.")
            await asyncio.sleep(5)
            await message.delete()
      if False not in sendMessage:
        if i.id not in blacklist:
          if not any(allowed_links.lower() in ctx.content.lower() for allowed_links in linkblacklist.list):
            if ".gg" in ctx.content.lower():
              await ctx.delete()
              message = await ctx.channel.send(f"{ctx.author.mention} That invite is not allowed in this server.")
              await asyncio.sleep(5)
              await message.delete()
            for filename in os.listdir('./cogs'):
              if filename.endswith('.py'):
                if f".{filename[:-3]}" not in ctx.content.lower() and "." in ctx.content.lower():
                    if not any(allowedweb.lower() in ctx.content.lower() for allowedweb in whitelistedlinks.list):
                      await ctx.delete()
                      message = await ctx.channel.send(f"{ctx.author.mention} That link is not allowed in this server.")
                      await asyncio.sleep(5)
                      await message.delete()

  # # Commands
  # @commands.command()

def setup(client):
  client.add_cog(Automod(client))
