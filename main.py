"""
Setup:
- 2 vitally important environment variables before running this code:
  discord_token = <your token here>
  discord_id = <your id here>

- A few environment variables with some roles' ids:
  discord_admins = <role id>

  discord_members = <role id>
  (all verified members)

  discord_owner = <role id>
  (server's owner role)


"""


import discord
from discord.ext import commands
import roles
from forbidden_words import swearing
import os
import asyncio
settings = {
    'bot': 'LiprikonBoot',
    'prefix': '/',
    'TOKEN': os.environ['discord_token'],
    'id': os.environ['discord_id']
    }
client = discord.Client()
bot = discord.Client()
bot = commands.Bot(command_prefix = settings['prefix'])


class System(commands.Cog):
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """
        Make the server not sleep.
        Because Heroku is known to stop the code if it does nothing for some
        time (or not?).
        """
        while True:
            await ctx.send("ping")
            await asyncio.sleep(5)
            await ctx.message.delete()
            await asyncio.sleep(1800)


    @commands.command(pass_context=True)
    async def пинг(self, ctx):
        """
        RU: Делает так, чтобы ссервер не спал.
        Потому что хостинг Heroku останавливает
        сервер если он ничего не делает в течение
        некоторого времени (а может и нет).
        """
        while True:
            await ctx.send("пинг")
            await asyncio.sleep(5)
            await ctx.message.delete()
            await asyncio.sleep(1800)


    @commands.command(pass_context=True)
    async def clear(self, ctx,  amount=None):
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
            if role.name == roles.admins_role_id:
                is_admin = True
                break
        if is_admin:
            await ctx.channel.purge(limit=int(amount))
            await ctx.channel.send(':: Successfully deleted.')
        else:
            await ctx.send("Not enough rights to run this :-< \n  Just contact admins")


    @commands.command(pass_context = True)
    async def очистить(self, ctx, amount=None):
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
            if role.name ==roles.admins_role_id:
                is_admin = True
                break
        if is_admin:
            await ctx.channel.purge(limit=int(amount))
            await ctx.channel.send(':: Сообщения успешно удалены')
        else:
            await ctx.send("Недостаточно прав :-< Смирись\n"
                           " или напиши администраторам.")


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
        asyncio.sleep(5)
        await ctx.message.delete()


    @commands.command(pass_context=True)
    async def префикс(self, ctx):
        """RU: Текущий префикс"""
        await ctx.send(settings['prefix'])
        await asyncio.sleep(5)
        # TODO: make normal message delete
        await ctx.message.delete()


    @commands.command(pass_context=True)
    async def prefix(self, ctx):
        """Current prefix"""
        await ctx.send(settings['prefix'])
        await asyncio.sleep(5)
        # TODO: make normal message delete
        await ctx.message.delete()

 
class Mention(commands.Cog):
    @commands.command(pass_context=True)
    async def pingadmins(self, ctx,  message):
        """Pings admin role"""
        # TODO: Bug there
        admins = ctx.guild.get_role(roles.admins_role_id)
        await message.reply(f"Achtung! {admins.mention} were mentioned by\
            {ctx.message.author.mention}", mention_author = True)


    @commands.command(pass_context=True)
    async def куадмины(self, ctx):
        """RU: Упоминание модераторов (админы + владелец).
        Используйте команду pigadmins, если
        упоминать владельца не нужно."""
        a = []
        # TODO: Bug there
        for j in roles.moder_role_id:
            a.append(ctx.guild.get_role(j))
        await ctx.message.reply(f"Ахтунг! {j.mention for j in a} были \
         упомянуты {ctx.message.author.mention}", mention_author = True)



@bot.event
async def on_message(message):
    # React when message contains swearing
    for j in swearing:
        if j in message.content:
            await message.reply('pong', mention_author=True)
    await bot.process_commands(message)


'''
# TODO: Do I need a customized 'help' output command?
@commands.command()
async def помощь(ctx):
    Отправляет значение всех комманд

    await ctx.send(f'Все комманды должны \
    использоваться с префиксом бота :robot: .'
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
                    '    |    То же самое.\n')


@commands.command()
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

bot.add_cog(System())
bot.add_cog(Ping())
bot.add_cog(Information())
bot.add_cog(Mention())

bot.run(settings['TOKEN'])