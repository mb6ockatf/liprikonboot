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

@bot.command()
async def pingadmins(ctx: commands.Context):
    # Получаем роль
    role = ctx.guild.get_role(role_id=752070970054803520)
    # Отправляем сообщение
    await ctx.send(f"Роль: {role.mention}")

@bot.command()
async def prefix(ctx):
    await ctx.send(settings['prefix'])

@bot.command()
async def bothelp(ctx):
    await ctx.send(f'Все комманды должны использоваться с префиксом бота :robot: .'
                    'Вот текущий список комманд:'
                    '\n\n• Помощь :hammer: (help):\n'
                    '   |----"bothelp"\n'
                    '   |    Отправляет вот это сообщение.\n'
                    '   |----"prefix"\n'
                    '   |    Выдаёт текущий префикс.\n'
                    '\n• Приветствия :handshake: (ping):\n'
                    '   |----"hello"\n'
                    '   |    Для проверки онлайна бота (пинга), т.к. зелёная точка не всегда показывает правду.\n'
                    '   |----"салам"\n'
                    '   |    То же самое.\n'
                    '\n• Правила :closed_book: (moder):\n'
                    '   |----"rules"\n'
                    '   |    Напоминает правила.\n'
                    '   |----"правила"\n'
                    '   |    То же самое.\n')


bot.run(settings['token'])
