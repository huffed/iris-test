import asyncio
import discord
from discord.ext import commands

# def read_banner():
#     with open("/home/server1/discord/faye/banner/banner.txt", "r") as f:
#         lines = f.readlines()
#         return lines[0].strip()

# banner = read_banner()

# variable options

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx):
      embed1=discord.Embed(color=0x00ffaa, description="Miscellaneous / Setup Commands **|** **:exclamation:Help page navigation expires after 70 seconds**")
#        embed1.add_field(name=":desktop: ip", value="`displays FiveM server IP and PORT`", inline=True)
      embed1.add_field(name=":question: help", value="`shows this help page. Use the arrows at the bottom to switch pages`", inline=True)
      embed1.add_field(name=":frame_photo: avatar <@user>", value="`displays avatar of a user as a image`", inline=True)
      embed1.add_field(name=":man_detective: userinfo <@user>", value="`shows info about a user`", inline=True)
      embed1.add_field(name=":globe_with_meridians: guildinfo", value="`shows information about the guild`", inline=True)
      embed1.add_field(name=":signal_strength: ping", value="`checks latency of {}`".format(self.client.user.name), inline=True)
      embed1.add_field(name=":coin: coin", value="`flips a coin. Heads or Tails`", inline=True)
      embed1.add_field(name=":rock: :newspaper: :scissors: rps", value="`plays rock paper scissors`", inline=True)
      embed1.add_field(name=":brain: guess", value="`plays guess a number between 0 - 30`", inline=True)
      embed1.add_field(name=":robot: bot", value="`shows very limited information about {}`".format(self.client.user.name), inline=True)
      embed1.add_field(name=":white_sun_rain_cloud: weather <city-name>", value="`shows current weather in specified city`", inline=True)
      embed1.add_field(name=":chart_with_upwards_trend: math <value>", value="`Calculates your math needs. Type: '.math help' for a detailed help page`")
      embed1.add_field(name=":desktop: serverinfo", value="`Shows information about {}'s server`".format(self.client.user.name))
#        embed1.add_field(name=":earth_africa: aop", value="`Shows the current in game AOP`")
      embed1.add_field(name=":m: meme", value="`Sends a meme from the Meme database`")
      embed1.add_field(name=":gemini: zodiac <zodiacsign>", value="`Shows information about a specified zodiac sign. Type .zodiac help for a more detailed help page`")
      embed1.add_field(name=":warning: setup{}".format(self.client.user.name), value="`sets up {}'s roles. Use this after inviting {}, or when the roles are messed up`".format(self.client.user.name, self.client.user.name))
#        embed1.add_field(name=":musical_note: Music Commands", value=":arrow_down:", inline=False)
#        embed1.add_field(name=":ballot_box_with_check: summon", value="`Summons Faye to your current Voice Channel`", inline=True)
#        embed1.add_field(name=":play_pause: play <song>", value="`Plays song from either Youtube or Soundcloud`", inline=True)
#        embed1.add_field(name=":pause_button: pause", value="`Pauses currently playing song`", inline=True)
#        embed1.add_field(name=":play_pause: resume", value="`Resumes currently paused song`", inline=True)
#        embed1.add_field(name=":wave: leave", value="`Disconnects Faye from currently playing voice channel`", inline=True)
#        embed1.add_field(name=":loud_sound: volume <0-100>", value="`Set volume of music playing from Faye`", inline=True)
#        embed1.add_field(name=":newspaper: queue", value="`Diplays songs currently queued songs`", inline=True)
#        embed1.add_field(name=":wastebasket: clear", value="`Clears the song queue`", inline=True)
#        embed1.add_field(name=":mag: search <song>", value="`Searches for songs matching your input`", inline=True)
#        embed1.add_field(name=":musical_note: np", value="`Displays song that is currently playing`", inline=True)
#        embed1.add_field(name=":notepad_spiral: perms", value="`Shows what you can do with your current roles`", inline=True)
#        embed1.add_field(name=":wastebasket: clean", value="`Clears all sent music embed's`", inline=True)
      embed1.set_author(name=f"{self.client.user.name} | Commands | Page 1/4", icon_url="https://media.discordapp.net/attachments/894002414569553970/901440818676633630/unknown.png")
      embed1.set_footer(text="[React to the arrow under this message to change pages]\n©{} Commands".format(self.client.user.name))


      embed2=discord.Embed(color=0xeeff00, description="Staff Commands **|** **:exclamation:Help page navigation expires after 70 seconds**")
      embed2.add_field(name=":judge: kick <@user> <reason>", value="`kicks user`", inline=True)
      embed2.add_field(name=":judge: ban <@user> <reason>", value="`bans user`", inline=True)
      embed2.add_field(name=":crossed_swords: battle <@user> <reason>", value="`bans member a little, well..... Aggresively`", inline=True)
      embed2.add_field(name=":judge: strike <@user> <reason>", value="`strikes specified member`", inline=True)
      embed2.add_field(name=":wastebasket: purge <10>", value="`bulk deletes 10 messages. Number is a variable`", inline=True)
      embed2.add_field(name=":mute: mute <@user timeramount reason>", value="`mutes user until timer exceeds | be aware, timeramount is in minutes`", inline=True)
      embed2.add_field(name=":loud_sound: unmute <@user>", value="`unmutes user`", inline=True)
      embed2.add_field(name=":lock: lock ", value="`locks the current channel`", inline=True)
      embed2.add_field(name=":unlock: unlock", value="`unlock the current channel`", inline=True)
      embed2.add_field(name=":mega: announce <message-to-announce>", value="`announces message`", inline=True)
      embed2.add_field(name=":e_mail: edit <messageID message-to-edit-to>", value="`edit's any embedded messages by {}`".format(self.client.user.name), inline=True)
      embed2.add_field(name=":mailbox_with_mail: tt <message-to-send>", value="`sends message in current channel`", inline=True)
      embed2.add_field(name=":mailbox_with_mail: ttc #channel <message-to-send>", value="`sends message to specified channel`", inline=True)
      embed2.add_field(name=":newspaper: massadd <@role>", value="`Adds specified role to everyone in the guild`", inline=True)
      embed2.add_field(name=":newspaper: massdel <@role>", value="`Removes specified role from everyone in the guild`", inline=True)
      embed2.add_field(name=":tools: suggestion <accept - deny - reject>", value="`Accepts or denies bot-suggestions`", inline=True)
      embed2.add_field(name=":mega: massannounce <message-to-announce>", value="`sends mass dm to all users in guild`", inline=True)
      embed2.add_field(name=":notepad_spiral: suggestion <msgID> <accept, reject / deny>", value="`let's the suggesting member know if their suggestion was either accepted or rejected`", inline=True)
      embed2.add_field(name=":passport_control: giverole <@role> <@Member>", value="`Lets department heads/command add roles to members without needing discord permissions`", inline=True)
      embed2.set_author(name="{} | Commands | Page 2/4".format(self.client.user.name), icon_url=banner)
      embed2.set_footer(text=f"©{self.client.user.name} Commands")

      embed3=discord.Embed(color=0xae00ff, description="Ticket Commands / Bot Moderation**|** **:exclamation:Help page navigation expires after 70 seconds**")
#        embed3.add_field(name=":white_check_mark: :x: app <accept or deny> <application or interview or training> <@user>", value="`marks specified stage as accepted if command in application channel`", inline=True)
#        embed3.add_field(name=":clock12: clock help", value="`shows commands for shift logs / clock in - clock out logs`", inline=True)
#        embed3.add_field(name=":notepad_spiral: loa <till-when> <reason>", value="`Marks you as LOA`", inline=True)
#        embed3.add_field(name=":notepad_spiral: clearloa", value="`Unmarks you as LOA`", inline=True)
      #embed3.add_field(name="Turbine Commands", value="⬇", inline=False)
      embed3.add_field(name=":ticket: close", value="`closes ticket if command was executed in a Ticket Channel`", inline=True)
      embed3.add_field(name=":ticket: ticketadd <@Member> OR <MemberID>", value="`Adds a member to an existing Ticket Channel`", inline=True)
      embed3.add_field(name=":ticket: ticketremove", value="`Removes a member from an existing Ticket Channel`", inline=True)
      embed3.add_field(name=":green_circle: online", value="`sets Faye's status to online`", inline=True)
      embed3.add_field(name=":red_circle: offline", value="`sets Faye's status to offline`", inline=True)
      embed3.add_field(name=":orange_circle: update ", value="`sets Faye's status to updating`", inline=True)
      embed3.add_field(name=":mega: bannounce <message-to-announce>", value="`announces bot message`", inline=True)
      embed3.set_author(name=f"{self.client.user.name} | Commands | Page 3/4", icon_url=banner)
      embed3.set_footer(text=f"©{self.client.user.name} Commands")

  #    embed4=discord.Embed(color=0xfbff00, description="Music Commands [Faye]")
  #    embed4.add_field(name=":musical_note: summon", value="`summon's faye to current joined channel`", inline=True)
  #    embed4.add_field(name=":arrow_forward: play <url>", value="`plays song`", inline=True)
  #    embed4.add_field(name=":pause_button: pause", value="`pauses currently playing song`", inline=True)
  #    embed4.add_field(name=":pause_button: resume", value="`resumed currently paused song`", inline=True)
  #    embed4.add_field(name=":twisted_rightwards_arrows: shuffle", value="`shuffles playlist`", inline=True)
  #    embed4.add_field(name=":track_next: skip", value="`skips current song`", inline=True)
  #    embed4.add_field(name=":arrow_down: queue", value="`shows queue songs`", inline=True)
  #    embed4.add_field(name=":loud_sound: volume <value>", value="`sets music volume`", inline=True)
  #    embed4.add_field(name=":wastebasket: remove <queue-number>", value="`removes specified song from the queue`", inline=True)
  #    embed4.add_field(name=":put_litter_in_its_place: clean", value="`cleans messages send by Faye's music module`", inline=True)
  #    embed4.add_field(name=":wastebasket: clear", value="`clears queue list`", inline=True)
  #    embed4.add_field(name=":wave: disconnect", value="`disconnect's Faye from current channel`", inline=True)
  #    embed4.set_author(name="Faye | Commands | Page 4/4", icon_url=banner)

      embed4=discord.Embed(color=0xff0000, description="Bot moderation / Networking commands **|** **:exclamation:Help page navigation expires after 70 seconds**")
      embed4.add_field(name=":mega: bannounce <message-to-announce>", value="`announces bot message`", inline=True)
      embed4.add_field(name=":beginner: modules", value="`shows {}'s modules`".format(self.client.user.name), inline=True)
      embed4.add_field(name=":green_circle: load <module>", value="`loads specified module`", inline=True)
      embed4.add_field(name=":orange_circle: reload <module>", value="`reloads specified module`", inline=True)
      embed4.add_field(name=":red_circle: unload <module>", value="`unloads specified module`", inline=True)
      embed4.add_field(name="__Networking / Open source intelligence Commands__", value=":arrow_down:", inline=False)
      embed4.add_field(name=":globe_with_meridians: geoip <IP-Address>", value = "`shows basic information about an IP, like geolocation, ISP etc`", inline=True)
      embed4.add_field(name=":globe_with_meridians: usernamebacktrace <username>", value="`crawls the internet and searches for usernames that match your input, and shows where they are registered`")
      embed4.add_field(name=":e_mail: emailvalidator <e-mail>", value="`checks if a email is valid or not`")
      embed4.set_author(name=f"{self.client.user.name} Commands | Page 4/4", icon_url=banner)
      embed4.set_footer(text=f"©{self.client.user.name} Commands")

      await ctx.send(embed=embed1)

def setup(client):
    client.add_cog(Help(client))
