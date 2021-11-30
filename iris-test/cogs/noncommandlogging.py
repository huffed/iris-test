import discord
from discord.ext import commands
import config
from datetime import date

class Logging(commands.Cog):

    def __init__(self, client):
        self.client = client

    # # Events
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        blacklist = [".reload", ".load", ".unload"]
        check = True
        for i in blacklist:
            if i in message.content:
                check = False
        if check == True and not message.content == "":
            channel = self.client.get_channel(config.messagedeletelogs)
            embed=discord.Embed(
                color=0xf52307,
                description=f"**Message sent by {message.author.mention} deleted in <#{message.channel.id}>**\n{message.content}"
            )
            embed.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar_url}")
            embed.set_footer(text=f"Author: {message.author.id} | Message ID: {message.id}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, b, a):
        if b.content != a.content:
            channel = self.client.get_channel(config.messageeditlogs)
            embed=discord.Embed(
                color=0x0066ff,
                description=f"**Message edited in** <#{b.channel.id}> [[Jump to Message]](https://discordapp.com/channels/{config.guild_id}/{a.channel.id}/{a.id})"
            )
            embed.add_field(name="Before:", value=f"{b.content}", inline=False)
            embed.add_field(name="After:", value=f"{a.content}")
            embed.set_author(name=f"{b.author}", icon_url=f"{b.author.avatar_url}")
            embed.set_footer(text=f"User ID: {b.author.id}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, b, a):
        channel = self.client.get_channel(config.voicechannellogs)
        if b.channel == None and a.channel != None:
            embed=discord.Embed(
                color=0x27c200,
                description=f"{member.mention}** joined voice channel** <#{a.channel.id}>"
            )
        elif b.channel != None and a.channel == None:
            embed=discord.Embed(
                color=0xde0000,
                description=f"{member.mention}** left voice channel** <#{b.channel.id}>"
            )
        elif b.channel != None and a.channel != None and b.channel != a.channel:
            embed=discord.Embed(
                color=0x0066ff,
                description=f"{member.mention}** moved voice channel** <#{b.channel.id}> ➜ <#{a.channel.id}>"
            )
        elif b.afk == False and a.afk == True:
            embed=discord.Embed(
                color=0x0066ff,
                description=f"{member.mention}** was moved to** <#{config.afkvc}>"
            )
        elif b.deaf == False and a.deaf == True:
            embed=discord.Embed(
                color=0xde0000,
                description=f"{member.mention}** was server deafened in** <#{b.channel.id}>"
            )
        elif b.deaf == True and a.deaf == False:
            embed=discord.Embed(
                color=0x27c200,
                description=f"{member.mention}** was un server deafened in** <#{b.channel.id}>"
            )
        elif b.self_deaf == False and a.self_deaf == True:
            embed=discord.Embed(
                color=0xde0000,
                description=f"{member.mention}** deafened themselves in** <#{b.channel.id}>"
            )
        elif b.self_deaf == True and a.self_deaf == False:
            embed=discord.Embed(
                color=0x27c200,
                description=f"{member.mention}** undeafened themselves in** <#{b.channel.id}>"
            )
        elif b.mute == False and a.mute == True:
            embed=discord.Embed(
                color=0xde0000,
                description=f"{member.mention}** was server muted in** <#{b.channel.id}>"
            )
        elif b.mute == True and a.mute == False:
            embed=discord.Embed(
                color=0x27c200,
                description=f"{member.mention}** was un server muted in** <#{b.channel.id}>"
            )
        elif b.self_mute == False and a.self_mute == True:
            embed=discord.Embed(
                color=0xde0000,
                description=f"{member.mention}** muted themselves in** <#{b.channel.id}>"
            )
        elif b.self_mute == True and a.self_mute == False:
            embed=discord.Embed(
                color=0x27c200,
                description=f"{member.mention}** unmuted themselves in** <#{b.channel.id}>"
            )
        elif b.self_stream == False and a.self_stream == True:
            embed=discord.Embed(
                color=0x27c200,
                description=f"{member.mention}** started streaming in** <#{b.channel.id}>"
            )
        elif b.self_stream == True and a.self_stream == False:
            embed=discord.Embed(
                color=0xde0000,
                description=f"{member.mention}** stopped streaming in** <#{b.channel.id}>"
            )
        elif b.self_video == False and a.self_video == True:
            embed=discord.Embed(
                color=0x27c200,
                description=f"{member.mention}** started their camera sharing in** <#{b.channel.id}>"
            )
        elif b.self_video == True and a.self_video == False:
            embed=discord.Embed(
                color=0xde0000,
                description=f"{member.mention}** stopped their camera sharing in** <#{b.channel.id}>"
            )
        embed.set_author(name=f"{member}", icon_url=f"{member.avatar_url}")
        embed.set_footer(text=f"ID: {member.id}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, _, user):
        guild = self.client.get_guild(config.guild_id)
        async for entry in guild.audit_logs(limit=2):
            if str(entry.action) == str("AuditLogAction.ban"):
                reason = str(entry.reason)
                break
        channel = self.client.get_channel(config.banlogs)
        if reason == "None":
            embed=discord.Embed(
                color=0xde0000,
                description=f"{user.mention} {user}\n\n Reason: No reason provided"
            )
            embed.set_author(name="Member Banned", icon_url=f"{user.avatar_url}")
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.set_footer(text=f"ID: {user.id}")
            await channel.send(embed=embed)
        else:
            embed=discord.Embed(
                color=0xde0000,
                description=f"{user.mention} {user}\n\n Reason: none given"
            )
            embed.set_author(name="Member Banned", icon_url=f"{user.avatar_url}")
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.set_footer(text=f"ID: {user.id}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, _, user):
        print()
        channel = self.client.get_channel(config.unbanlogs)
        embed=discord.Embed(
            color=0x27c200,
            description=f"{user.mention} {user}"
        )
        embed.set_author(name="Member Unbanned", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url=f"{user.avatar_url}")
        embed.set_footer(text=f"ID: {user.id}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        today = date.today()
        year = today.year
        month = today.month
        day = today.day
        accountAgeYears = year - member.created_at.year
        accountAgeMonths = month - member.created_at.month
        accountAgeDays = day - member.created_at.day
        yearoryears = ""
        monthormonths = ""
        dayordays = ""
        if accountAgeYears == 1:
            yearoryears = "year"
        else:
            yearoryears = "years"
        if accountAgeMonths == 1:
            monthormonths = "month"
        else:
            monthormonths = "months"
        if accountAgeDays == 1:
            dayordays = "day"
        else:
            dayordays = "days"
        accountAge = f"{accountAgeYears} {yearoryears}, {accountAgeMonths} {monthormonths}, {accountAgeDays} {dayordays}"
        channel = self.client.get_channel(config.joinlogs)
        embed=discord.Embed(
            color=0x27c200,
            description=f"{member.mention} {member}"
        )
        embed.add_field(name="Account Age", value=f"{accountAge}")
        embed.set_author(name="Member Joined", icon_url=f"{member.avatar_url}")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.set_footer(text=f"ID: {member.id}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(config.leavelogs)
        embed=discord.Embed(
            color=0xde0000,
            description=f"{member.mention} {member}"
        )
        embed.set_author(name="Member Left", icon_url=f"{member.avatar_url}")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.set_footer(text=f"ID: {member.id}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        guild = self.client.get_guild(config.guild_id)
        embedchannel = self.client.get_channel(config.channellogs)
        embed=discord.Embed(
            color=0x27c200,
            description=f"**Channel created: #{channel}**"
        )
        embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
        embed.set_footer(text=f"ID: {channel.id}")
        await embedchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        guild = self.client.get_guild(config.guild_id)
        embedchannel = self.client.get_channel(config.channellogs)
        embed=discord.Embed(
            color=0xde0000,
            description=f"**Channel deleted:** #{channel}"
        )
        embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
        embed.set_footer(text=f"ID: {channel.id}")
        await embedchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, b, a):
        guild = self.client.get_guild(config.guild_id)
        # if not amessage.author.bot:
        channel = self.client.get_channel(config.channellogs)
        if str(b.type) == "text":
            embed=discord.Embed(
                color=0x0066ff,
                description=f"**<#{b.id}> text channel updated**"
            )
            embed.add_field(name="Before:", value=f"**Category:** {b.category}\n**Name:** {b.name}\n**Position:** {b.position}\n**Permissions synced:** {b.permissions_synced}\n**Is NSFW:** {b.is_nsfw()}\n**Is News:** {b.is_news()}", inline=False)
            embed.add_field(name="After:", value=f"**Category:** {a.category}\n**Name:** {a.name}\n**Position:** {a.position}\n**Permissions synced:** {a.permissions_synced}\n**Is NSFW:** {a.is_nsfw()}\n**Is News:** {a.is_news()}")
            embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
            embed.set_footer(text=f"ID: {b.id}")
            await channel.send(embed=embed)
        elif str(b.type) == "voice":
            embed=discord.Embed(
                color=0x0066ff,
                description=f"**<#{b.id}> voice channel updated**"
            )
            embed.add_field(name="Before:", value=f"**Category:** {b.category}\n**Name:** {b.name}\n**Position:** {b.position}\n**Permissions synced:** {b.permissions_synced}", inline=False)
            embed.add_field(name="After:", value=f"**Category:** {a.category}\n**Name:** {a.name}\n**Position:** {a.position}\n**Permissions synced:** {a.permissions_synced}")
            embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
            embed.set_footer(text=f"ID: {b.id}")
            await channel.send(embed=embed)
        elif str(b.type) == "stage_voice":
            embed=discord.Embed(
                color=0x0066ff,
                description=f"**<#{b.id}> stage channel updated**"
            )
            embed.add_field(name="Before:", value=f"**Category:** {b.category}\n**Name:** {b.name}\n**Position:** {b.position}\n**Permissions synced:** {b.permissions_synced}", inline=False)
            embed.add_field(name="After:", value=f"**Category:** {a.category}\n**Name:** {a.name}\n**Position:** {a.position}\n**Permissions synced:** {a.permissions_synced}")
            embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
            embed.set_footer(text=f"ID: {b.id}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        guild = self.client.get_guild(config.guild_id)
        embedchannel = self.client.get_channel(config.rolelogs)
        embed=discord.Embed(
            color=0x27c200,
            description=f"**Role created: @{role}**"
        )
        embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
        embed.set_footer(text=f"ID: {role.id}")
        await embedchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        guild = self.client.get_guild(config.guild_id)
        embedchannel = self.client.get_channel(config.rolelogs)
        embed=discord.Embed(
            color=0xde0000,
            description=f"**Role deleted:** @{role}"
        )
        embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
        embed.set_footer(text=f"ID: {role.id}")
        await embedchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_update(self, b, a):
        # print(f"{dir(b)}\n\n{dir(a)}")
        guild = self.client.get_guild(config.guild_id)
        channel = self.client.get_channel(config.rolelogs)
        if not b.name == a.name and b.color == a.color and b.position == a.position and b.tags == a.tags and b.is_bot_managed() == a.is_bot_managed() and b.mentionable == a.mentionable:
            embed=discord.Embed(
                color=0x0066ff,
                description=f"**<@&{b.id}> role updated**"
            )
            embed.add_field(name="Before:", value=f"**Name:** {b.name}\n**Color:** {b.color}\n**Position:** {b.position}\n**Tags:** {b.tags}\n**Is bot managed:** {b.is_bot_managed()}\n**Mentionable:** {b.mentionable}", inline=False)
            embed.add_field(name="After:", value=f"**Name:** {a.name}\n**Color:** {a.color}\n**Position:** {a.position}\n**Tags:** {a.tags}\n**Is bot managed:** {a.is_bot_managed()}\n**Mentionable:** {a.mentionable}")
            embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
            embed.set_footer(text=f"ID: {b.id}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_update(self, b, a):
        bbanned_members = await b.bans()
        abanned_members = await a.bans()
        guild = self.client.get_guild(config.guild_id)
        channel = self.client.get_channel(config.guildlogs)
        if not b.name == a.name and b.owner_id == a.owner_id and b.rules_channel.id == a.rules_channel.id and b.afk_channel.id == a.afk_channel.id and b.afk_timeout == a.afk_timeout and b.icon_url == a.icon_url and b.banner_url == a.banner_url and len(b.categories) == len(a.categories) and len(b.channels) == len(a.channels) and len(b.text_channels) == len(a.text_channels) and len(b.voice_channels) == len(a.voice_channels) and len(b.stage_channels) == len(a.stage_channels) and len(b.roles) == len(a.roles) and len(b.emojis) == len(a.emojis) and int(len(bbanned_members)) == int(len(abanned_members)):
            embed=discord.Embed(
                color=0x0066ff,
                description=f"**{a.name} information updated**"
            )
            embed.add_field(name="Before:", value=f"**Name:** {b.name}\n**Owner:** <@{b.owner_id}>\n**Rules Channel:** <#{b.rules_channel.id}>\n**AFK Channel:** <#{b.afk_channel.id}>\n**AFK Timeout:** {b.afk_timeout/60}\n**Server Icon:** [[Server Icon Link]]({b.icon_url})\n**Banner:** [[Banner Link]]({b.banner_url})\n**Categories:** {len(b.categories)}\n**Channels:** {len(b.channels)}\n**Text Channels:** {len(b.text_channels)}\n**Voice Channels:** {len(b.voice_channels)}\n**Stage Channels:** {len(b.stage_channels)}\n**Roles:** {len(b.roles)}\n**Emojis:** {len(b.emojis)}\n**Banned Members:** {int(len(bbanned_members))}", inline=False)
            embed.add_field(name="After:", value=f"**Name:** {a.name}\n**Owner:** <@{a.owner_id}>\n**Rules Channel:** <#{a.rules_channel.id}>\n**AFK Channel:** <#{a.afk_channel.id}>\n**AFK Timeout:** {a.afk_timeout/60}\n**Server Icon:** [[Server Icon Link]]({a.icon_url})\n**Banner:** [[Banner Link]]({a.banner_url})\n**Categories:** {len(a.categories)}\n**Channels:** {len(a.channels)}\n**Text Channels:** {len(a.text_channels)}\n**Voice Channels:** {len(a.voice_channels)}\n**Stage Channels:** {len(a.stage_channels)}\n**Roles:** {len(a.roles)}\n**Emojis:** {len(a.emojis)}\n**Banned Members:** {int(len(abanned_members))}")
            embed.set_author(name=f"{guild}", icon_url=f"{guild.icon_url}")
            embed.set_footer(text=f"ID: {b.id}")
            await channel.send(embed=embed)

def setup(client):
  client.add_cog(Logging(client))
