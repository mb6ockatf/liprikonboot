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
    author, content = message.author, message.content.split()
    command = content[0]
    if author == client.user:
        return
    if author.id == 725303688192720977:
        if command == 'ping':
            await message.channel.send('pong')
        elif command == 'uptime':
            await message.channel.send(dt.now() - start)
        elif command == 'log':
            b = '\n'
            system(f'echo {" ".join(content[1:]) + b} >> ../logging.txt')
        elif command == 'system':
            await message.channel.send(system(" ".join(content[1:])))


client.run(TOKEN)
