import discord
from discord.ext import commands
from discord.utils import get
import config
import asyncio

class Announce(commands.Cog):

  def __init__(self, client):
    self.client = client

  # # Events
  # @commands.Cog.listener()

  # Commands
  @commands.command()
  @commands.has_any_role(897965307388383332, 897965405673496606, 900504453285814293, 901229355953438800, 897965827528228885, 900893222052692008)
  async def announce(self, ctx, *args):
      print(args)
      guild = self.client.get_guild(config.guild_id)
      text_channel_list=[]
      for channel in guild.text_channels:
          text_channel_list.append(f"<#{channel.id}>")
      if args == ():
          embed=discord.Embed(
            color=0x0066ff,
            title=f"Command: {config.prefix}announce",
            description=f"**Description: ** Send an announcement using the bot.\n**Sub Commands:**\n{config.prefix}announce everyone - Send an announcement with @everyone.\n{config.prefix}announce here - Send an announcement with @here.\n{config.prefix}announce role - Send an announcement with a role mention.\n**Usage:**\n{config.prefix}announce [channel] [message]\n{config.prefix}announce everyone [channel] [message]\n{config.prefix}announce here [channel] [message]\n{config.prefix}announce role [role] [channel] [message]\n**Example:**\n{config.prefix}announce #updates Some nice announcement!\n{config.prefix}announce everyone #updates A big announcement! :tada:\n{config.prefix}announce here #updates A somewhat big announcement!\n{config.prefix}announce role @Updates #announcements Some new stuff happened!"
          )
          embed.set_footer(text=f"{config.default_footer}")
          await ctx.send(embed=embed)
      elif args[0] == "everyone" and len(args) >= 2:
          if "<#" in args[1]:
              channelStripped = args[1].lstrip("<#").rstrip(">")
              channelToSendTo = guild.get_channel(int(channelStripped))
          messageToSend = " ".join(args[2:])
          if args[1] in text_channel_list:
              logchannel = self.client.get_channel(config.announcementlogs)
              embed=discord.Embed(
                color=0x0066ff
              )
              embed.add_field(name="Announcement:", value=f"{messageToSend}")
              embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"{config.default_footer}")
              embed2=discord.Embed(
                color=0x0066ff,
                description=f"**Announcement sent to <#{channelToSendTo.id}>**"
              )
              embed2.add_field(name="Message:", value=f"@everyone\n{messageToSend}")
              embed2.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"{config.default_footer}")
              log=discord.Embed(
                color=0x0066ff,
                description=f"**Announcement sent to <#{channelToSendTo.id}>**"
              )
              log.add_field(name="Sent by:",value=f"{ctx.author}", inline=False)
              log.add_field(name="Message:", value=f"@everyone\n{messageToSend}")
              log.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              log.set_footer(text=f"{config.default_footer}")
              msg = await channelToSendTo.send("@everyone")
              msg2 = await channelToSendTo.send(embed=embed)
              msg3 = await ctx.send(embed=embed2)
              log = await logchannel.send(embed=log)
              await ctx.message.delete()
          elif args[1] not in text_channel_list:
              embed=discord.Embed(
                color=0xde0000,
                description="Invalid channel."
              )
              embed.set_author(name="Error", icon_url=config.error)
              embed.set_footer(text=config.default_footer)
              msg = await ctx.channel.send(embed=embed)
              await asyncio.sleep(3)
              await msg.delete()
              await ctx.message.delete()
      elif args[0] == "here" and len(args) >= 2:
          if "<#" in args[1]:
              channelStripped = args[1].lstrip("<#").rstrip(">")
              channelToSendTo = guild.get_channel(int(channelStripped))
          messageToSend = " ".join(args[2:])
          if args[1] in text_channel_list:
              logchannel = self.client.get_channel(config.announcementlogs)
              embed=discord.Embed(
                color=0x0066ff
              )
              embed.add_field(name="Announcement:", value=f"{messageToSend}")
              embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"{config.default_footer}")
              embed2=discord.Embed(
                color=0x0066ff,
                description=f"**Announcement sent to <#{channelToSendTo.id}>**"
              )
              embed2.add_field(name="Message:", value=f"@here\n{messageToSend}")
              embed2.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"{config.default_footer}")
              log=discord.Embed(
                color=0x0066ff,
                description=f"**Announcement sent to <#{channelToSendTo.id}>**"
              )
              log.add_field(name="Sent by:",value=f"{ctx.author}", inline=False)
              log.add_field(name="Message:", value=f"@here\n{messageToSend}")
              log.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              log.set_footer(text=f"{config.default_footer}")
              msg = await channelToSendTo.send("@here")
              msg2 = await channelToSendTo.send(embed=embed)
              msg3 = await ctx.send(embed=embed2)
              log = await logchannel.send(embed=log)
              await ctx.message.delete()
          elif args[1] not in text_channel_list:
              embed=discord.Embed(
                color=0xde0000,
                description="Invalid channel."
              )
              embed.set_author(name="Error", icon_url=config.error)
              embed.set_footer(text=config.default_footer)
              msg = await ctx.channel.send(embed=embed)
              await asyncio.sleep(3)
              await msg.delete()
              await ctx.message.delete()
      elif args[0] == "role" and len(args) >= 3:
          if "<#" in args[2]:
              channelStripped = args[2].lstrip("<#").rstrip(">")
              channelToSendTo = guild.get_channel(int(channelStripped))
          if "<@&" in args[1]:
              roleStripped = args[1].lstrip("<@&").rstrip(">")
          messageToSend = " ".join(args[3:])
          role_list=[]
          for role in guild.roles:
              role_list.append(f"<@&{role.id}>")
          if args[2] in text_channel_list:
              if args[1] in role_list:
                  role = get(guild.roles, id=int(roleStripped))
                  logchannel = self.client.get_channel(config.announcementlogs)
                  embed=discord.Embed(
                    color=0x0066ff
                  )
                  embed.add_field(name="Announcement:", value=f"{messageToSend}")
                  embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
                  embed.set_footer(text=f"{config.default_footer}")
                  embed2=discord.Embed(
                    color=0x0066ff,
                    description=f"**Announcement sent to <#{channelToSendTo.id}>**"
                  )
                  embed2.add_field(name="Message:", value=f"\n{role.mention}\n{messageToSend}")
                  embed2.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
                  embed.set_footer(text=f"{config.default_footer}")
                  log=discord.Embed(
                    color=0x0066ff,
                    description=f"**Announcement sent to <#{channelToSendTo.id}>**"
                  )
                  log.add_field(name="Sent by:",value=f"{ctx.author}", inline=False)
                  log.add_field(name="Message:", value=f"{role.mention}\n{messageToSend}")
                  log.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
                  log.set_footer(text=f"{config.default_footer}")
                  msg = await channelToSendTo.send(f"{role.mention}")
                  msg2 = await channelToSendTo.send(embed=embed)
                  msg3 = await ctx.send(embed=embed2)
                  log = await logchannel.send(embed=log)
                  await ctx.message.delete()
          if args[2] not in text_channel_list:
              embed=discord.Embed(
                color=0xde0000,
                description="Invalid channel."
              )
              embed.set_author(name="Error", icon_url=config.error)
              embed.set_footer(text=config.default_footer)
              msg = await ctx.channel.send(embed=embed)
              await asyncio.sleep(3)
              await msg.delete()
              await ctx.message.delete()
          if args[1] not in role_list:
              embed=discord.Embed(
                color=0xde0000,
                description="Invalid role."
              )
              embed.set_author(name="Error", icon_url=config.error)
              embed.set_footer(text=config.default_footer)
              msg = await ctx.channel.send(embed=embed)
              await asyncio.sleep(3)
              await msg.delete()
              await ctx.message.delete()
      elif args[0] in text_channel_list and len(args) >= 2:
          if "<#" in args[0]:
              channelStripped = args[0].lstrip("<#").rstrip(">")
              channelToSendTo = guild.get_channel(int(channelStripped))
          messageToSend = " ".join(args[1:])
          if args[0] in text_channel_list:
              logchannel = self.client.get_channel(config.announcementlogs)
              embed=discord.Embed(
                color=0x0066ff
              )
              embed.add_field(name="Announcement:", value=f"{messageToSend}")
              embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"{config.default_footer}")
              embed2=discord.Embed(
                color=0x0066ff,
                description=f"**Announcement sent to <#{channelToSendTo.id}>**"
              )
              embed2.add_field(name="Message:", value=f"{messageToSend}")
              embed2.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"{config.default_footer}")
              log=discord.Embed(
                color=0x0066ff,
                description=f"**Announcement sent to <#{channelToSendTo.id}>**"
              )
              log.add_field(name="Sent by:",value=f"{ctx.author}", inline=False)
              log.add_field(name="Message:", value=f"{messageToSend}")
              log.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              log.set_footer(text=f"@here\n{config.default_footer}")
              msg2 = await channelToSendTo.send(embed=embed)
              msg3 = await ctx.send(embed=embed2)
              log = await logchannel.send(embed=log)
              await ctx.message.delete()
          elif args[0] not in text_channel_list:
              print(text_channel_list)
              embed=discord.Embed(
                color=0xde0000,
                description="Invalid channel."
              )
              embed.set_author(name="Error", icon_url=config.error)
              embed.set_footer(text=config.default_footer)
              msg = await ctx.channel.send(embed=embed)
              await asyncio.sleep(3)
              await msg.delete()
              await ctx.message.delete()
      else:
          embed=discord.Embed(
            color=0xde0000,
            description="Invalid syntax."
          )
          embed.add_field(name="Usage:", value=f"{config.prefix}announce [channel] [message]\n{config.prefix}announce everyone [channel] [message]\n{config.prefix}announce here [channel] [message]\n{config.prefix}announce role [role] [channel] [message]")
          embed.set_author(name="Error", icon_url=config.error)
          embed.set_footer(text=config.default_footer)
          msg = await ctx.channel.send(embed=embed)
          await ctx.message.delete()
          await asyncio.sleep(20)
          await msg.delete()

def setup(client):
  client.add_cog(Announce(client))
