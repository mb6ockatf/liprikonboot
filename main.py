import discord
from discord.ext import commands
from sys import argv
from os import system
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
    elif content == 'ping':
        await message.channel.send('pong')
    elif content == 'uptime':
        await message.channel.send(dt.now() - start)
    elif content.startswith('execute'):
        system(content[7:])


client.run(TOKEN)
