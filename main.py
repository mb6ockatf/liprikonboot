from discord import Client
from sys import argv
from os import system
from datetime import datetime as dt

client, start = Client(max_messages=10), dt.now()


@client.event
async def on_message(message):
    author, content = message.author, " ".join(message.content.split())
    command = content[0:content.find(' ')]
    if author in (client.user, 725303688192720977):
        return
    if command == '$ping':
        await message.channel.send('pong')
    elif command == '$uptime':
        await message.channel.send(dt.now() - start)
    else:
        line = " ".join(content[1:])
        if command == '$log':
            system('echo ' + line + '>> ../logging.txt')
        elif command == '$$':
            system(line + ' > temp.txt')
            with open('temp.txt', 'r') as file:
                await message.channel.send(file.read())


client.run(argv[1])
