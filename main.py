import discord
from discord.ext import commands
import asyncio
import config
import datetime
import ban_words

ds_app_token, myserver, ds_server_admins, ds_server_host, \
ds_prefix, swearing, rules = config.ds_app_token, config.myserver, \
config.ds_server_admins, config.ds_server_host, config.ds_prefix, \
ban_words.swearing, config.rules

client = discord.Client()
bot = commands.Bot(command_prefix=ds_prefix)
time = datetime.datetime.now


def right_server(ctx):
    if ctx.guild.id == myserver:
        return True
    else:
        return False


def is_admin(ctx=discord.ext.commands.Context):
    role = ctx.guild.get_role(role_id=ds_server_admins)
    if role in ctx.message.author.roles:
        return True
    else:
        return False


class Hello(commands.Cog):
    @commands.command()
    async def hello(self, ctx):
        """Check if the bot is online"""
        if right_server(ctx):
            author = ctx.message.author
            await ctx.send(f'Hello, {author.mention}!')
            await asyncio.sleep(5)
            await ctx.message.delete()


class Admin(commands.Cog):
    @commands.command()
    async def purge(self, ctx, amount='2'):
        """
        Clear the chat.
        Only for admins!
        Deletes the quantity of messages which is mentioned after the command,
        or deletes *all messages*
        For an instance,
        <prefix here>clear 12
        - deletes 12 last messages,
        and
         <prefix here>clear
        - deletes 2 messages: 1 where the func was called and 1 previous
        """
        if right_server(ctx):
            if is_admin(ctx):
                if amount == 'all':
                    try:
                        while True:
                            await ctx.channel.purge()
                    except:
                        ctx.send(':ninja: Successfully deleted or some error appeared.')
                else:
                    await ctx.channel.purge(limit=int(amount))
                    await ctx.send(':white_check_mark: Successfully deleted.')
            else:
                await ctx.reply(':red_circle: Not enough rights.')


    @commands.command()
    async def rules(self, ctx):
        """Shows the rules"""
        if right_server(ctx):
            await ctx.send('1.Do not spam\n'
                           '2.Do not rebel\n'
                           '3.Do not offend admins & other members\n'
                           '4.Be polite\n'
                           "5.Do not change the server's name with no permission of the \
Head Admin\n"
                           '6.Do not ban other members with no permission of the Head \
Admin\n'
                           '7.Revolutions are forbidden\n'
                           '    © @liprikon2020')
            await asyncio.sleep(5)
            await ctx.message.delete()

    @commands.command()
    async def ban(self, ctx, member:discord.User=None, reason='for being a jerk'):
        """Ban!"""
        if right_server(ctx) and is_admin(ctx):
            if member.id == ctx.guild.id:
                await ctx.send(f":ninja: You can't ban yourself.\nIt's not my idea, it's just forbidden by Discord.")
            else:
                await ctx.guild.ban(member, reason=reason)
                await ctx.send(f':ninja:@{member} has been banned for {reason}.')

    @commands.command()
    async def kick(self, ctx, member:discord.User=None, reason='for being too bad'):
        """Permanent ban!"""
        if right_server(ctx) and is_admin(ctx):
            await ctx.guild.kick(member, reason=reason)
            if member.id == ctx.guild.id:
                await ctx.send(f":ninja: You can't ban yourself.\nIt's not my idea, it's just forbidden by Discord.")
            else:
                await ctx.guild.kick(member, reason=reason)
                await ctx.send(f':ninja:@{member} has been permanently banned for {reason}.\nI mean kicked.')

    @commands.command()
    async def prefix(self, ctx, amount=1):
        """Current prefix"""
        if right_server(ctx):
            await ctx.send(ds_prefix)
            await asyncio.sleep(5)
            await ctx.message.delete()


class Mention(commands.Cog):
    @commands.command()
    async def mod(self, ctx: commands.Context):
        """Pings moderators' role"""
        if right_server(ctx):
            role = ctx.guild.get_role(role_id=ds_server_admins)
            await ctx.message.reply("Achtung!" + f"{role.mention}" + f"were mentioned")


@bot.event
async def on_message(ctx):
    """React when message contains ban word"""
    if right_server(ctx):
        for j in swearing:
            if j in ctx.content:
                await ctx.reply('pong', mention_author=True)
        await bot.process_commands(ctx)

time = datetime.datetime.now
@bot.event
async def timer(ctx):
    if time.hour() == 7 and time.minute == 0:
        while True:
            await ctx.send('Доброе утро')
            await asyncio.sleep(86400)


bot.add_cog(Admin())
bot.add_cog(Mention())
bot.add_cog(Hello())
bot.run(ds_app_token)