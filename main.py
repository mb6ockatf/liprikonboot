import discord
from discord.ext import commands
import asyncio
import datetime
from ban_words import swearing
from argparse import ArgumentParser

parser = ArgumentParser(description='start 1 instance', prog='%(prog)', epilog='never share token')
waited_args = {'-token': 'app token', '-server': 'id of the server the bot is going to run on',
               '-admins': "id of the server admins role / account's id",
               '-host': "Server host's role / account's id", '-prefix': 'bot commands prefix',
               '-rules': "name of a *.txt file which contain a the rules"}
[parser.add_argument(arg, help=help_string) for arg, help_string in waited_args.items()]
args = parser.parse_args()
with open(args.rules, 'r') as file:
    args.rules = file.read()
client = discord.Client()
bot = commands.Bot(command_prefix=args.prefix)
time = datetime.datetime.now
messages = {'ban_yourself': ":ninja: You can't ban or kick yourself.\n\
It's not my idea, it's just forbidden by Discord."}


def right_server(ctx):
    return True if str(ctx.guild.id) == args.server else False


def is_admin(ctx):
    return True if ctx.guild.get_role(role_id=int(args.admins)) in ctx.message.author.roles else False


@bot.tree.command()
async def hello(ctx):
    """Get a greeting from bot"""
    if right_server(ctx):
        print(1)
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')
        await asyncio.sleep(5)
        await ctx.message.delete()


@bot.command()
async def purge(ctx, amount='2'):
    """Deletes the given number of messages"""
    if right_server(ctx):
        if is_admin(ctx):
            for _ in range(int(amount)):
                try:
                    await ctx.channel.purge()
                except BaseException as error:
                    await ctx.send(f':ninja: Successfully deleted or an error appeared: {error}')
            await ctx.channel.purge()
            await ctx.send(':white_check_mark: Successfully deleted.')
        else:
            await ctx.reply(':red_circle: Not enough rights.')


@bot.command()
async def rules(ctx):
    """Send the rules"""
    if right_server(ctx):
        await ctx.send(args.rules)


@bot.command()
async def ban(ctx, member: discord.User = None, reason='for being a jerk'):
    """Ban command"""
    if right_server(ctx) and is_admin(ctx):
        if member.id == ctx.guild.id:
            await ctx.send(messages['ban_yourself'])
        else:
            await ctx.guild.ban(member, reason=reason)
            await ctx.send(f':ninja:@{member} has been banned for {reason}.')


@bot.command()
async def kick(ctx, member: discord.User = None, reason='for being too bad'):
    """Kick command"""
    if right_server(ctx) and is_admin(ctx):
        if member.id == ctx.guild.id:
            await ctx.send(messages['ban_yourself'])
        else:
            await ctx.guild.kick(member, reason=reason)
            await ctx.guild.kick(member, reason=reason)
            await ctx.send(f':ninja:@{member} has been permanently kicked for {reason}')


@bot.command()
async def prefix(ctx):
    """Current prefix"""
    if right_server(ctx):
        await ctx.send(args.prefix)


@bot.command()
async def mod(ctx):
    """Pings admin role"""
    if right_server(ctx):
        role = ctx.guild.get_role(role_id=int(args.admins))
        await ctx.message.reply(role.mention + 'were mentioned')


@bot.event
async def on_message(ctx):
    """React when message contains ban word"""
    if right_server(ctx):
        for j in swearing:
            if j in ctx.content:
                await ctx.reply('pong', mention_author=True)
        await bot.process_commands(ctx)


@bot.event
async def morning(ctx):
    if datetime.datetime.now().hour == 7 and datetime.datetime.now().minute == 0:
        await ctx.send('Good morning! :grinning:\nWish this day will be nice to you')


bot.run(args.token)
