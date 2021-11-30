import discord
from discord.ext import commands
import config
import asyncio
from discord.utils import get

class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # # Events
    # @commands.Cog.listener()

    # Commands
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        guild = self.client.get_guild(config.guild_id)
        logchannel = self.client.get_channel(config.kicklogs)
        if reason == None:
            embed=discord.Embed(
                color=0xde0000,
                description=f":white_check_mark: ***{user} was kicked*** | No reason given."
            )
            log=discord.Embed(
                color=0xde0000,
                description=f"{user.mention} {user}\n\n Reason: No reason given."
            )
            log.set_author(name="Member Kicked", icon_url=f"{user.avatar_url}")
            log.set_thumbnail(url=f"{user.avatar_url}")
            log.set_footer(text=f"ID: {user.id}")
            await logchannel.send(embed=log)
        else:
            embed=discord.Embed(
                color=0xde0000,
                description=f":white_check_mark: ***{user} was kicked*** | {reason}"
            )
            log=discord.Embed(
                color=0xde0000,
                description=f"{user.mention} {user}\n\n Reason: {reason}"
            )
            log.set_author(name="Member Kicked", icon_url=f"{user.avatar_url}")
            log.set_thumbnail(url=f"{user.avatar_url}")
            log.set_footer(text=f"ID: {user.id}")
            await logchannel.send(embed=log)
        dm=discord.Embed(
            color=0xde0000,
            description=f"You were kicked from {guild}"
        )
        dmchannel = await user.create_dm()
        embed.set_footer(text=f"{config.default_footer}")
        await ctx.send(embed=embed)
        await dmchannel.send(embed=dm)
        await user.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        guild = self.client.get_guild(config.guild_id)
        print(guild)
        if reason == None:
            embed=discord.Embed(
                color=0xde0000,
                description=f":white_check_mark: ***{user} was banned*** | No reason given."
            )
        else:
            embed=discord.Embed(
                color=0xde0000,
                description=f":white_check_mark: ***{user} was banned*** | {reason}"
            )
        dm=discord.Embed(
            color=0xde0000,
            description=f"You were banned from {guild}"
        )
        dm.set_footer(text=f"{config.default_footer}")
        dmchannel = await user.create_dm()
        embed.set_footer(text=f"{config.default_footer}")
        await ctx.send(embed=embed)
        await dmchannel.send(embed=dm)
        await user.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, user: discord.Member):
        guild = self.client.get_guild(config.guild_id)
        role = discord.utils.get(guild.roles, name='Muted')
        print(guild)
        if reason == None:
            embed=discord.Embed(
                color=0xde0000,
                description=f":white_check_mark: ***{user} was muted*** | No reason given."
            )
        else:
            embed=discord.Embed(
                color=0xde0000,
                description=f":white_check_mark: ***{user} was muted*** | {reason}."
            )
        embed.set_footer(text=f"{config.default_footer}")
        await ctx.send(embed=embed)
        await member.remove_roles("DCRP | Member")
        await member.add_roles("MUTED")
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
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
        elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed=discord.Embed(
                    color=0xde0000,
                    description="Missing arguments."
            )
            embed.set_author(name="Error", icon_url=config.error)
            embed.set_footer(text=config.default_footer)
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(3)
            await msg.delete()
            await ctx.message.delete()
            print(error)
        elif isinstance(error, discord.ext.commands.errors.BadArgument):
            embed=discord.Embed(
                    color=0xde0000,
                    description="That user doesn't exist."
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
                    description="Error detected in `kick`."
            )
            embed.set_author(name="Error", icon_url=config.error)
            embed.set_footer(text=config.default_footer)
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(3)
            await msg.delete()
            await ctx.message.delete()
            print(error)

    @ban.error
    async def ban_error(self, ctx, error):
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
        elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed=discord.Embed(
                    color=0xde0000,
                    description="Missing arguments."
            )
            embed.set_author(name="Error", icon_url=config.error)
            embed.set_footer(text=config.default_footer)
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(3)
            await msg.delete()
            await ctx.message.delete()
            print(error)
        elif isinstance(error, discord.ext.commands.errors.BadArgument):
            embed=discord.Embed(
                    color=0xde0000,
                    description="That user doesn't exist."
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
                    description="Error detected in `kick`."
            )
            embed.set_author(name="Error", icon_url=config.error)
            embed.set_footer(text=config.default_footer)
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(3)
            await msg.delete()
            await ctx.message.delete()
            print(error)

    @commands.command()
    @commands.has_any_role("DCRP | Administrator", "DCRP | Bot Developer")
    async def status(self, ctx, *args):
        try:
            try:
                self.client.unload_extension('cogs.statusLoop')
                print('Status Loop Toggled: Off')
                await ctx.send("Status Loop Toggled: Off")
            except:
                pass
            statusMessage = args[1:]
            statusMessage = " ".join(statusMessage)
            await ctx.send(f'{self.client.user.name}\'s activity changed to "{args[0]} {statusMessage}"')
            if args[0].lower() == "playing":
                await self.client.change_presence(activity=discord.Game(name=statusMessage))
            elif args[0].lower() == "streaming":
                await self.client.change_presence(activity=discord.Streaming(name=statusMessage))
            elif args[0].lower() == "listening":
                await self.client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.listening, name=statusMessage))
            elif args[0].lower() == "watching":
                await self.client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.watching, name=statusMessage))
        except Exception as error:
            print(' cannot be loaded. [{}]'.format(error))

    @commands.command()
    @commands.has_any_role("DCRP | Administrator", "DCRP | Bot Developer")
    async def toggle(self, ctx, arg1):
        if arg1 == "statusloop":
            try:
                self.client.load_extension('cogs.statusLoop')
                print('Status Loop Toggled: On')
                embed=discord.Embed(
                  color=0x0066ff,
                  description="Status Loop Toggled: On"
                  )
                embed.set_footer(text=config.default_footer)
                message = await ctx.channel.send(embed=embed)
                await asyncio.sleep(4)
                await message.delete()
                await ctx.message.delete()
            except discord.ext.commands.errors.ExtensionAlreadyLoaded:
                self.client.unload_extension('cogs.statusLoop')
                print('Status Loop Toggled: Off')
                embed=discord.Embed(
                  color=0x0066ff,
                  description="Status Loop Toggled: Off"
                  )
                embed.set_footer(text=config.default_footer)
                message = await ctx.channel.send(embed=embed)
                await asyncio.sleep(4)
                await message.delete()
                await ctx.message.delete()
            except Exception as error:
                print(' cannot be loaded. [{}]'.format(error))
        else:
            await ctx.send("Invalid arguments.")


def setup(client):
    client.add_cog(AdminCommands(client))
