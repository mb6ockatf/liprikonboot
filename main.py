import discord
from discord.ext import commands
from config import settings
import request
from forbidden_words import swearing

client = discord.Client()

bot = discord.Client()
bot = commands.Bot(command_prefix = settings['prefix'])



@bot.command()
async def салам(ctx):
    '''Пинаем бота'''
    author = ctx.message.author
    await ctx.send(f'Салам алейкум, {author.mention}!')


@bot.command()
async def hello(ctx):
    '''
    Ping the bot
    '''
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')


@bot.command()
async def правила(ctx):
    '''
    Правила
    '''
    await ctx.send(f'1.Не спамить\n'
                    '2.Не бунтовать\n'
                    '3.Не оскорблять админов и других участников\n'
                    '4.Быть вежливым\n'
                    '5.Не менять название сервера без разришения верховного админа\n'
                    '6.Не банить участников без ведома верховного админа\n'
                    '7.Не устраивать революции\n')


@bot.command()
async def rules(ctx):
    '''
    Shows the rules
    '''
    await ctx.send(f'1.Do not spam\n'
                    '2.Do not rebel\n'
                    '3.Do not offend admins & other members\n'
                    '4.Be polite\n'
                    "5.Do not change the server's name with no permission of the Head Admin\n"
                    '6.Do not ban other members with no permission of the Head Admin\n'
                    '7.Revolutions are forbidden\n')


# Raw feature
@bot.command()
async def куадмины(ctx: commands.Context):
    '''
    Упоминаем младшего админа
    '''
    # Получаем роль
    role = ctx.guild.get_role(role_id=752070970054803520)
    # Отправляем сообщение
    await ctx.send(f"Роль: {role.mention}")

'''
@bot.command()
async def enemy():
'''



@bot.event
async def on_message(message):
    for j in swearing:
        if j in message.content:
            await message.reply('pong', mention_author=True)
    await bot.process_commands(message)



# Raw feature
@bot.command()
async def pingadmins(ctx: commands.Context):
    '''
    Pings Junior Admin's role
    '''
    # Получаем роль
    role = ctx.guild.get_role(role_id=752070970054803520)
    # Отправляем сообщение
    await ctx.send(f"Role: {role.mention}")


@bot.command()
async def префикс(ctx):
    '''
    Текущий префикс
    '''
    await ctx.send(settings['prefix'])


@bot.command()
async def prefix(ctx):
    '''
    Current prefix
    '''
    await ctx.send(settings['prefix'])

'''
@bot.command()
async def помощь(ctx):
    Отправляет значение всех комманд

    await ctx.send(f'Все комманды должны использоваться с префиксом бота :robot: .'
                    'Вот текущий список комманд:'
                    '\n\n• Помощь :hammer: (help):\n'
                    '   |----"помощь"\n'
                    '   |    Отправляет вот это сообщение.\n'
                    '   |----"префикс"\n'
                    '   |    Выдаёт текущий префикс.\n'
                    '\n• Приветствия :handshake: (ping):\n'
                    '   |----"салам"\n'
                    '   |    Для проверки онлайна бота (пинга), т.к. зелёная точка не всегда показывает правду.\n'
                    '\n• Правила :closed_book: (moder):\n'
                    '   |----"правила"\n'
                    '   |    То же самое.\n')


@bot.command()
async def bothelp(ctx):

    Sends the meaning of all commands

    await ctx.send(f"All commands can be used only if the bot's :robot: prefix is typed right before the command."
                    'Current list of commands:'
                    '\n\n• Help :hammer: (help):\n'
                    '   |----"bothelp"\n'
                    '   |    Sends this message.\n'
                    '   |----"prefix"\n'
                    "   |    Sends the bot's prefix.\n"
                    '\n• Greetings :handshake: (ping):\n'
                    '   |----"hello"\n'
                    "   |    It's to check if the bot is online because this green dot isn't always showing the truth.\n"
                    '\n• Rules :closed_book: (moder):\n'
                    '   |----"rules"\n'
                    '   |    Reminds the rules.\n')
'''

bot.run(settings['token'])
