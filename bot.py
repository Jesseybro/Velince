import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='.hulp'))
    print ("lol folks")

@client.command(pass_context=True)
@commands.has_any_role("Staff")
async def warn(ctx, user: discord.Member, *, reason: str):
        await client.send_message(ctx.message.channel, ':warning: {} is gewaarschuwd voor: **{}**.'.format(user.mention, reason))
        await client.add_reaction(ctx.message, '\U000026a0')
        await client.send_message(ctx.message.author, ':thumbsup: Je hebt {} gewaarschuwt. Reden: `{}`'.format(user.mention, reason))

@client.command(pass_context = True)
@commands.has_any_role("*")
@commands.has_permissions(ban_members = True)
async def ban(ctx, userName: discord.User, *, reason: str):
        await client.ban(userName)
        await client.send_message(ctx.message.channel, ':thumbsup: Deze speler is gebanned met de reden: **{}**.'.format(reason))
        await client.add_reaction(ctx.message, '\U0001f528')

@client.command(pass_context=True)
@commands.has_any_role("Staff")
async def mute(ctx, user: discord.Member, reason: str):
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await client.add_roles(user, role)
    await client.send_message(ctx.message.channel, "{} is zojuist gemuted, voor: **{}**.".format(user.mention, reason))
    await client.send_message(ctx.message.author, ':thumbsup: Je hebt {} gemuted! Reden: **{}**.'.format(user.mention, reason))
    await client.add_reaction(ctx.message, '\U0001f507')

@client.command(pass_context=True)
@commands.has_any_role("*")
async def unmute(ctx, user: discord.Member):
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await client.remove_roles(user, role)
    await client.send_message(ctx.message.author, ':thumbsup: Je hebt {} geunmuted.'.format(user.mention))
    await client.add_reaction(ctx.message, '\U0001f508')


@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
        role = discord.utils.get(ctx.message.server.roles, name='*')
        if role in ctx.message.author.roles:
            await client.kick(userName)


@client.command(pass_context=True)
@commands.has_any_role("Owner")
async def announce(ctx, *, message:str):
  embed = discord.Embed(title="Velince", description="Information", color=0x00ff00)
  embed.add_field(name='Message', value="Information velince:\n\n**You need the 'Staff' Role for this:\n\n.warn <@player> <reason>\n\nYou need the * role for this:\n\n.unmute <@player>\n.ban <@player>\n.kick <@player>\n.clear <hoeveel berichten>\n\nThe bot developer is: Jessey.#0038", inline=False)
  general_channel = discord.utils.get(ctx.message.server.channels, name="information")
  await client.send_message(general_channel, message, embed=embed)

@client.command(pass_context=True)
async def hulp(ctx):
        embed = discord.Embed(title="Command", description="Help", color=0x00ff00)
        embed.add_field(name='Message', value="Velince is een Moderation bot. Op dit moment is het nog privé. Voor updates, join deze Discord: https://discord.gg/qY2tJ2 !", inline=False)
        await client.send_message(ctx.message.author, embed=embed)
        await client.send_message(ctx.message.channel, ":thumbsup: Bekijk mijn bericht in je privé berichten!")
        await client.add_reaction(ctx.message, '\U0001f4e5')

@client.event
async def on_member_join(member):
    if member.server.id == "456879670445604867":
        channel = client.get_channel("456882424824070157")
        await client.send_message(channel, "Welkom {} op onze **Discord Server** server. Ik hoop dat je het leuk gaat vinden!".format(member.mention))

@client.event
async def on_member_remove(member):
    if member.server.id == "45687967044560486":
        channel = client.get_channel("456882424824070157")
        await client.send_message(channel, "{} heeft de server verlaten. :(".format(member.name))

        
@client.command(pass_context=True)
@commands.has_any_role("*")
async def rules(ctx, user: discord.Member):
    role = discord.utils.get(ctx.message.server.roles, name="Kijk #rules")
    await client.add_roles(user, role)

@client.command()
async def say(*args):
    output = ''
    for word in args:
        output +=word
        output += ' '
        await client.say(output)

@client.command(pass_context=True)
@commands.has_any_role("Staff")
async def clear(ctx, amount=400):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount + 1)):
        messages.append(message)
    await client.delete_messages(messages)
    if amount == 1:
        await client.say('Berichten zijn verwijderd!')
    else:
        await client.say('Berichten zijn verwijderd!')

@client.command(pass_context = True)
@commands.has_any_role("*")
async def sendalts(ctx):
    await client.say("Spotify & Netflix: https://icutit.ca/GDrLrz\n**LETOP** Alle wachtwoorden zijn: jessey")
    client.remove_command(".sendalts")
    

        




client.run("NDU4MzIwMDgxMzYyMDkyMDUy.Dgl7Wg.pLUA7d6t23GxvpwCTHiqnZPKzcw")
