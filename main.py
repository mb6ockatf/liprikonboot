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
import request
import roles
from forbidden_words import swearing
import os
import asyncio

settings = {
    'bot': 'LiprikonBoot',
    'prefix': '/',
    'TOKEN': os.environ['discord_token'],
    # TODO: Check syntax around there
    # TODO: Install TODO extension
    'id': os.environ['discord_id']
    }


client = discord.Client()

bot = discord.Client()
bot = commands.Bot(command_prefix = settings['prefix'])


class System:

    @bot.command(pass_context=True)
    async def ping(self, ctx):
        """
        Make the server not sleep, because Heroku is known to
        stop the code if it does nothing for some time
        """
        while True:
            await ctx.send("ping")
            await asyncio.sleep(5)
            await ctx.message.delete()
            await asyncio.sleep(1800)


    @bot.command(pass_context=True)
    async def clear(self, amount=None):
        '''
        Only for admins
        Deletes the quantity of messages which is mentioned after the command,
        or deletes *all messages*
        For an instance,
        <prefix here>clear 12
        - deletes 12 last messages,
        and
         <prefix here>clear
        - deletes all messages
        '''
        is_admin = False
        for role in discord.Member.roles:
            if role.name == roles.admins_role_id:
                is_admin = True
                break
        if is_admin:
            await ctx.channel.purge(limit=int(amount))
            await ctx.channel.send(':: Sucessfully deleted.')
        else:
            await ctx.send("Not enough rights to run this :-< \n  Just contact admins")


    @bot.command(pass_context = True)
    async def очистить(self, amount=None):
        """
        Только для админов
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


class Ping:
    """
    Commands to get some reply from the bot to check online
    """
    @bot.command(pass_context=True)
    async def салам(self, ctx):
        '''
        Проверяем, онлайн ли бот
        '''
        author = ctx.message.author
        await ctx.send(f'Салам алейкум, {author.mention}!')
        await asyncio.sleep(5)
        await ctx.message.delete()


    @bot.command(pass_context=True)
    async def hello(self, ctx):
        '''
        Check if the bot is online
        '''
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')
        await asyncio.sleep(5)
        await ctx.message.delete()


class Information:
    @bot.command(pass_context=True)
    async def правила(self, ctx):
        '''
        Правила
        '''
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


    @bot.command(pass_context=True)
    async def rules(self, ctx):
        '''
        Shows the rules
        '''
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


    @bot.command(pass_context=True)
    async def префикс(self, ctx):
        '''
        Текущий префикс
        '''
        await ctx.send(settings['prefix'])
        await asyncio.sleep(5)
        await ctx.message.delete()


    @bot.command(pass_context=True)
    async def prefix(self, ctx):
        '''
        Current prefix
        '''
        await ctx.send(settings['prefix'])
        await asyncio.sleep(5)
        await ctx.message.delete()

 
class Mention:
    @bot.command(pass_context=True)
    async def куадмины(self, message):
        """
        Упоминание админов
        """
        admins = ctx.guild.get_role(roles.admins_role_id)
        # Отправляем сообщение
        await message.reply(f"Ахтунг! {admins.mention} были \
        упомянуты {ctx.message.author.mention}", mention_author = True)


    @bot.command(pass_context=True)
    async def pingadmins(self, message):
        """
        Pings admin's role
        """
        admins = ctx.guild.get_role(roles.admins_role_id)
        # Отправляем сообщение
        await message.reply(f"Achtung! {admins.mention} were menrioned by\
            {ctx.message.author.mention}", mention_author = True)


    @bot.command(pass_context=True)
    async def куадмины(self, message):
        """
        Упоминание модераторов (админы + владелец)
        Используйте команду pigadmins, если
        упоминать владельца ненужно
        """
        a = []
        for j in roles.moder_role_id:
            a.append(ctx.guild.get_role(j))
        # Отправляем сообщение
        await message.reply(f"Ахтунг! {j.mention for j in a} были \
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
@bot.command()
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

# Adding all cathegories
bot.add_cog(System())
bot.add_cog(Ping())
bot.add_cog(Information())
bot.add_cog(Mention())

bot.run(settings['TOKEN'])
