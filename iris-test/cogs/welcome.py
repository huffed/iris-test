import discord
from discord.ext import commands
import config
import asyncio

class Example(commands.Cog):

  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_member_join(self, member):
    if member.id != 618845089208467466:
        print(f"Member \"{member}\" joined")
        channel = self.client.get_channel(config.welcomeChannel)
        embed=discord.Embed(
          color=0x0066ff,
          description=f"Hello {member.mention}, welcome to DreamCity RolePlay!\nIn order to get verified, follow these steps:\n• Read and understand the <#{config.rulesChannel}>\n• Follow the instructions in <#{config.verifyChannel}>")
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_footer(text=config.default_footer)
        await channel.send(embed=embed)

  # @commands.Cog.listener()
  # async def on_raw_reaction_add(payload):
  #   if payload.message_id == 733759031138582538:
  #       if payload.emoji == "white_check_mark":
  #           member = discord.utils.find(payload.user_id)
  #           await member.add_roles("Guild Member")
  #           await member.remove_roles("Rules Pending")

def setup(client):
  client.add_cog(Example(client))
