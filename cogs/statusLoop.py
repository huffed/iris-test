from discord.ext import commands,tasks
import config
import asyncio
import discord

class StatusLoop(commands.Cog):

    def __init__(self, client):
        self.index = 0
        self.client = client
        self.statusLoop.start()

    def cog_unload(self):
        self.statusLoop.cancel()

#    @tasks.loop(seconds=3.0)
    @tasks.loop()
    async def statusLoop(self):
      try:
        memberCount = []
        for guild in self.client.guilds:
          guild = self.client.get_guild(config.guild_id)
        for member in guild.members:
          if member.bot == True:
            pass
          else:
            memberCount.append(member)

        await self.client.wait_until_ready()
        statuses = [
          f"{guild}",
          f"{len(memberCount)} Members",
          f"{config.prefix}help | {self.client.user.name}"
        ]
        while not self.client.is_closed():
          status = 0
          while True:
            if status == 3:
              status = 0
            if status == 0:
              if statuses[0] == "{ALPHA} Dream City Roleplay 2.0":
                await self.client.change_presence(activity=discord.Game(name="DreamCity RolePlay"))
            if status == 1:
              await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=statuses[1]))
            if status == 2:
              await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=statuses[2]))
            status += 1
            await asyncio.sleep(10)
      except Exception as error:
        print(' cannot be loaded. [{}]'.format(error))

    @statusLoop.before_loop
    async def before_status(self):
        await self.client.wait_until_ready()

def setup(client):
  client.add_cog(StatusLoop(client))
