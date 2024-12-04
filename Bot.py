#SWATMod by ~ Gytis5089

import discord
import asyncio
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '*')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"*help"))
    print('://SWATMod now online.')
    print(f'We are running with {round(client.latency * 100)}ms ping.')

def is_gytis(ctx):
    return ctx.author.id in [301014178703998987]

def is_hicom(ctx):
    return ctx.author.id in [301014178703998987, 731930235951513651]

@client.command(aliases=['purge', 'wipe'])
@commands.check(is_hicom)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title = 'Wipe',
        colour = 0x000000,
        description = f'{ctx.author.mention} has wiped {amount} messages.'
    )
    embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
    message = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    await message.delete()

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, arg):
    embed = discord.Embed(
        title = 'Kick',
        colour = 0x000000,
        description = f'{ctx.author.mention} has kicked <@{member.id}> for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title = 'Kick',
        colour = 0x000000,
        description = f'{ctx.author.mention} has kicked you for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
    await member.send(embed=embed)
    await member.kick(reason=arg)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, arg):
    embed = discord.Embed(
        title = 'Ban',
        colour = 0x000000,
        description = f'{ctx.author.mention} has banned <@{member.id}> for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title = 'Ban',
        colour = 0x000000,
        description = f'{ctx.author.mention} has banned you for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
    await member.send(embed=embed)
    await member.ban(reason=arg)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	embed = discord.Embed(
		title = 'Unban',
        colour = 0x000000,
        description = f'{ctx.author.mention} has unbanned <@{member.id}>'
    )
	embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
	await ctx.send(embed=embed)
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			embed = discord.Embed(
				title = 'Unban',
                colour = 0x000000,
        		description = f'{ctx.author.mention} has unbanned you'
    		)
			embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
			await user.send(embed=embed)

@client.command(aliases=['guilds', 'guild', 'server'])
@commands.check(is_gytis)
async def servers(ctx):
    embed = discord.Embed(
        title='Servers',
        colour=0x000000
    )
    for guild in client.guilds:
       embed.add_field(name=guild.name, value=f'`ID:`{guild.id}\n`Members:`{guild.member_count}\n`Owner:`{guild.owner}', inline=False)
    embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
    await ctx.author.send(embed=embed)
    await ctx.send('Sent.')

@client.command(aliases=['dm', 'pm', 'msg'])
@commands.check(is_gytis)
async def message(ctx, member : discord.Member = None, *, arg):
    embed = discord.Embed(
        title=f'Message',
        colour=0x000000,
        description=f'**This is from:** <@{ctx.author.id}>\n\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
    await member.send(embed=embed)
    await ctx.send('Sent.')

@client.command()
@commands.check(is_hicom)
async def announce(ctx, *, arg):
    channel = discord.utils.get(ctx.guild.text_channels, name='announcements')
    await channel.send(f'{arg}\n\nThis was announced by {ctx.author.mention}\n||@everyone||')

@client.command()
@commands.check(is_hicom)
async def event(ctx, *, arg):
    channel = discord.utils.get(ctx.guild.text_channels, name='events')
    await channel.send(f'{arg}\n\nThis was shouted by {ctx.author.mention}\n||@everyone||')

@client.command()
@commands.check(is_hicom)
async def tryout(ctx, *, arg):
    channel = discord.utils.get(ctx.guild.text_channels, name='tryouts')
    await channel.send(f'{arg}\n\nThis was shouted by {ctx.author.mention}\n||@everyone||')

@client.command()
@commands.check(is_gytis)
async def say(ctx, *, arg):
    await ctx.send(arg)

@client.command(aliases=['created'])
async def create(ctx, member : discord.Member = None):
	embed = discord.Embed(
		title = 'Create',
        colour = 0x000000,
        description = f'{member.name} created their account on {str(member.created_at)[0:10]}'
    )
	embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
	await ctx.send(embed=embed)

@client.command()
@commands.check(is_hicom)
async def p1(ctx, member : discord.Member = None):
    role1 = discord.utils.get(member.guild.roles, name='Permitted')
    await member.add_roles(role1)
    await ctx.send('Added.')

@client.command()
@commands.check(is_hicom)
async def p2(ctx, member : discord.Member = None):
    role1 = discord.utils.get(member.guild.roles, name='Permitted')
    role2 = discord.utils.get(member.guild.roles, name='Access')
    role3 = discord.utils.get(member.guild.roles, name='://SWAT')
    await member.remove_roles(role1)
    await member.add_roles(role2)
    await member.add_roles(role3)
    await ctx.send('Added & Removed.')

@client.command()
async def help(ctx):
    embed = discord.Embed(
		title = 'Help',
        colour = 0x000000,
        description = '**Moderation**\n`*clear` - Used to clear the specified amount of messages (+1 when using.)\n`*kick` - Used to kick the specified member (reason required.)\n`*ban` - Used to ban the specified member (reason required.)\n`*unban` - Used to unban the specified member.\n\n**Shouts** __(Keep in mind pings are done automatically)__\n`*announce` - Used to shout <#822587079853998080>\n`*event` - Used to shout <#822587053211516949>\n`*tryout` - Used to shout <#822585893583323217>\n\n**Extra** (Restricted access.)\n`*servers` - Shows guilds the bot is currently in.\n`*message` - Allows those permitted to directly message users via the bot.\n`*say` - Makes the bot say what you say after the command.'
    )
    embed.set_thumbnail(url="https://i.ibb.co/Z1XsKYq/FBI-Seal.png")
    await ctx.send(embed=embed)

client.run('ODIyNTg5NDY2MTgyMTU2Mjk4.YFUeIw.JNBCjz75cyGC53q9JtbJZU9Lzow')