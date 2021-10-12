import discord
from discord.ext import commands
from config import settings
import req

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def салам(ctx):
    author = ctx.message.author
    await ctx.send(f'Салам алейкум, {author.mention}!')


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')


@bot.command()
async def правила(ctx):
    await ctx.send(f'1.Не спамить')
    await ctx.send(f'2.Не бунтовать')
    await ctx.send(f'3.Не оскорблять админов и других участников')
    await ctx.send(f'4.Быть вежливым')
    await ctx.send(f'5.Не менять название сервера без разришения верховного админа')
    await ctx.send(f'6.Не банить участников без ведома верховного админа')
    await ctx.send(f'7.Не устраивать революции')


@bot.command()
async def rules(ctx):
    await ctx.send(f'1.Не спамить')
    await ctx.send(f'2.Не бунтовать')
    await ctx.send(f'3.Не оскорблять админов и других участников')
    await ctx.send(f'4.Быть вежливым')
    await ctx.send(f'5.Не менять название сервера без разришения верховного админа')
    await ctx.send(f'6.Не банить участников без ведома верховного админа')
    await ctx.send(f'7.Не устраивать революции')


# Raw feature
@bot.command()
async def куадмины(ctx: commands.Context):
    # Получаем роль
    role = ctx.guild.get_role(role_id=752070970054803520)
    # Отправляем сообщение
    await ctx.send(f"Роль: {role.mention}")

# Raw feature
@bot.command()
async def pingadmins(ctx: commands.Context):
    # Получаем роль
    role = ctx.guild.get_role(role_id=752070970054803520)
    # Отправляем сообщение
    await ctx.send(f"Role: {role.mention}")


@bot.command()
async def префикс(ctx):
    await ctx.send(settings['prefix'])


@bot.command()
async def prefix(ctx):
    await ctx.send(settings['prefix'])


@bot.command()
async def помощь(ctx):
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
                    '   |    Reminds the rules.\n'

bot.run(settings['token'])
