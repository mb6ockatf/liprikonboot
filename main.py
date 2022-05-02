import discord
from discord.ext import commands
from sys import argv
from subprocess import check_output
from datetime import datetime as dt

start = dt.now()
prefix = '/'
TOKEN = argv[1]
client = discord.Client(max_messages=10)


@client.event
async def on_message(message):
    author, content = message.author, message.content
    if author == client.user:
        return
    if author.id == 725303688192720977:
        if content == 'ping':
            await message.channel.send('pong')
        elif content == 'uptime':
            await message.channel.send(dt.now() - start)
        elif content.startswith('execute'):
            await message.channel.send(check_output(content[7:], universal_newlines=True))


client.run(TOKEN)
