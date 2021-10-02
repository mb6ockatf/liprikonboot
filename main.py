import discord
from discord.ext import commands
from config import settings

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


bot.run(settings['token'])
