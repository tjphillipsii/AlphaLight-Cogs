import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os


class AlphaFun:

    """ A few fun things for Alpha Light"""

    def __init__(self, bot):
        self.bot = bot
        self.quotes = fileIO("data/alphafun/quotes.json", "load")

    @commands.command()
    async def getsum(self):
        """Return a random Shaxx quote"""
        await self.bot.say(randchoice(self.quotes))

    @commands.command()
    async def kenny(self, ctx):
        """T I dougle Grrr POTATO!"""
        await self.bot.say('Ummm... POTATO')
        await self.bot.send_file(ctx.message.channel, 'data/alphafun/kennythetiger.jpg')


def setup(bot):
    n = AlphaFun(bot)
    bot.add_cog(n)
