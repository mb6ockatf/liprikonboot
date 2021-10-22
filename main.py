"""
Setup:
- 2 vitally important environment variables before running this code:
  ds_server_token = <your token here>
  ds_server_id = <your id here>

- A few environment variables with some roles' ids:
  ds_admins = <role id>

  ds_members = <role id>
  (all verified members)

  ds_hoster = <role id>
  (server's owner role)


"""


import discord
from discord.ext import commands
from forbidden_words import swearing
import asyncio
from bot_config import *


client = discord.Client()
bot = discord.Client()
bot = commands.Bot(command_prefix = ds_bot_prefix)


class System(commands.Cog):

    @commands.command(pass_context=True)
    async def clear(self, ctx,  amount=1):
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
        is_admin = False
        for role in discord.Member.roles:
            if role.id == ds_server_admins:
                is_admin = True
                break
        if is_admin:
            await ctx.channel.purge(limit=amount)
            await ctx.send(':: Successfully deleted.')
        else:
            await ctx.send("Not enough rights to run this.")


    @commands.command(pass_context = True)
    async def очистить(self, ctx, amount=1):
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
        is_admin = False
        for role in discord.Member.roles:
            if role.id == ds_server_admins:
                is_admin = True
                break
        if is_admin:
            await ctx.channel.purge(limit=amount)
            await ctx.send(':: Сообщения успешно удалены')
        else:
            await ctx.send("Недостаточно прав.")


class Ping(commands.Cog):
    @commands.command(pass_context=True)
    async def салам(self, ctx):
        """RU: Проверка, онлайн ли бот"""
        author = ctx.message.author
        await ctx.send(f'Салам алейкум, {author.mention}!')
        await asyncio.sleep(5)
        # TODO: Need normal delete func there
        await ctx.message.delete()


    @commands.command(pass_context=True)
    async def hello(self, ctx):
        """Check if the bot is online"""
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')
        await asyncio.sleep(5)
        await ctx.message.delete()


class Information(commands.Cog):
    @commands.command(pass_context=True)
    async def правила(self, ctx):
        """RU: Правила"""
        await ctx.send(f'1.Не спамить\n'
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
        await ctx.send(f'1.Do not spam\n'
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
        await ctx.send(settings['prefix'])
        await asyncio.sleep(5)
        await ctx.message.delete()


    @commands.command(pass_context=True)
    async def prefix(self, ctx, amount=1):
        """Current prefix"""
        await ctx.send(settings['prefix'])
        await asyncio.sleep(5)
        await ctx.message.delete()

 
class Mention(commands.Cog):
    @commands.command(pass_context=True)
    async def pingadmins(self, ctx,  message):
        """Pings admin role"""
        role = discord.utils.get(guild.roles, id=ds_server_admins)
        role.mention
        await message.reply("Achtung!", role.mention, f"were mentioned by \
            {ctx.message.author.mention}", mention_author = True)


    @commands.command(pass_context=True)
    async def куадмины(self, ctx):
        """RU: Упоминание модераторов"""
        role = discord.utils.get(guild.roles, id=ds_server_admins)
        await ctx.message.reply("Ахтунг!", role.mention, f"были упомянуты \
            {ctx.message.author.mention}", mention_author = True)



@bot.event
async def on_message(message):
    # React when message contains swearing
    for j in swearing:
        if j in message.content:
            await message.reply('pong', mention_author=True)
    await bot.process_commands(message)

bot.add_cog(System())
bot.add_cog(Ping())
bot.add_cog(Information())
bot.add_cog(Mention())

bot.run(ds_server_token)