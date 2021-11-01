import discord
from discord.ext import commands
from forbidden_words import swearing
import asyncio
from bot_config import (ds_app_token, ds_server_admins,
                        ds_prefix, myserver)

client = discord.Client()
bot = commands.Bot(command_prefix=ds_prefix)

def right_server(ctx=ctx):
    if ctx.message.guild.id == myserver:
        return True
    else:
        return False

def is_admin(ctx=ctx):
    role = ctx.guild.get_role(role_id=ds_server_admins)
    if role in ctx.message.author.roles:
        return True
    else:
        return False


class System(commands.Cog):
    @commands.command()
    async def clear(self, ctx, amount=2):
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
        - deletes all messages
        """
        if right_server():
            if is_admin():
                await ctx.channel.purge(limit=amount)
                await ctx.send(':white_check_mark: Successfully deleted.')
            else:
                await ctx.reply(':red_circle: Not enough rights.')


    @commands.command()
    async def очистить(self, ctx, amount=2):
        """
        RU: Очистка чата.
        Только для админов!
        Удаляет то количество сообщений, которое
        введено после команды,
        либо очищает *весь чат*.
        Например,
        <сдесь префикс>очистить 12
        - удалит 12 последних сообщений, a
        <сдесь префикс>очистить
        - удалит все сообщения
        """
        if right_server():
            if is_admin(ctx):
                await ctx.channel.purge(limit=amount)
                await ctx.send(':white_check_mark: Сообщения успешно удалены.')
            else:
                await ctx.reply(':red_circle: Недостаточно прав.')


class Ping(commands.Cog):
    @commands.command()
    async def салам(self, ctx):
        """RU: Проверка, онлайн ли бот"""
        if right_server():
            author = ctx.message.author
            await ctx.send(f'Салам алейкум, {author.mention}!')
            await asyncio.sleep(5)
            await ctx.message.delete()

    @commands.command()
    async def hello(self, ctx):
        """Check if the bot is online"""
        if right_server():
            author = ctx.message.author
            await ctx.send(f'Hello, {author.mention}!')
            await asyncio.sleep(5)
            await ctx.message.delete()


class Information(commands.Cog):
    @commands.command(pass_context=True)
    async def правила(self, ctx):
        """RU: Правила"""
        # TODO: it must send a message which id is defined in env vars
        if right_server():
            await ctx.send('1.Не спамить\n'
                           '2.Не бунтовать\n'
                           '3.Не оскорблять админов и других \
                            участников\n'
                           '4.Быть вежливым\n'
                           '5.Не менять название сервера без\
                             разрешения верховного админа\n'
                           '6.Не банить участников без ведома \
                            верховного админа\n'
                           '7.Не устраивать революции\n'
                           '    © @liprikon2020')
            await asyncio.sleep(5)
            await ctx.message.delete()

    @commands.command(pass_context=True)
    async def rules(self, ctx):
        """Shows the rules"""
        # TODO: it must send a message which id is defined in env vars
        if right_server():
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

    @commands.command(pass_context=True)
    async def префикс(self, ctx):
        """RU: Текущий префикс"""
        if right_server():
            await ctx.send(ds_prefix)
            await asyncio.sleep(5)
            await ctx.message.delete()

    @commands.command(pass_context=True)
    async def prefix(self, ctx, amount=1):
        """Current prefix"""
        if right_server():
            await ctx.send(ds_prefix)
            await asyncio.sleep(5)
            await ctx.message.delete()


class Mention(commands.Cog):
    @commands.command()
    async def pingadmins(self, ctx: commands.Context):
        """Pings admin role"""
        if right_server():
            role = ctx.guild.get_role(role_id=ds_server_admins)
            await ctx.message.reply("Achtung!" + f"{role.mention}" + f"were mentioned")

    @commands.command()
    async def куадмины(self, ctx: commands.Context):
        """RU: Упоминание модераторов"""
        if right_server():
            role = ctx.guild.get_role(role_id=ds_server_admins)
            await ctx.message.reply("Ахтунг!" + f"{role.mention}" + "были упомянуты")


@bot.event
async def on_message(message):
    # React when message contains swearing
    if right_server():
        for j in swearing:
            if j in message.content:
                await message.reply('pong', mention_author=True)
        await bot.process_commands(message)


bot.add_cog(System())
bot.add_cog(Ping())
bot.add_cog(Information())
bot.add_cog(Mention())
bot.run(ds_app_token)
