import discord
from discord.ext import commands
import os
from cogs.utils import checks
from __main__ import send_cmd_help


class Guides:
    """Guides

    Guide Videos Provided by ShadowsGirl4Life"""

    def __init__(self, bot):
        self.bot = bot


    @commands.group(name="guides", pass_context=True)
    async def _guides(self, ctx):
        """You must enter a guide from the list

        Example: !guides <name>"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_guides.command(pass_context=True)
    async def calus(self, ctx):
        """Calus Guide"""
        await self.bot.say('Here is the guide for Calus:')
        await self.bot.say('https://youtu.be/aeKeJ6x_Zi8')

    @_guides.command(pass_context=True)
    async def gauntlet(self, ctx):
        """Gauntlet Guide"""
        await self.bot.say('Here is the guide for the Gauntlet:')
        await self.bot.say('https://youtu.be/T0DbeXjkKRs')

    @_guides.command(pass_context=True)
    async def baths(self, ctx):
        """Baths and Entrance Guide"""
        await self.bot.say('Here is the guide for the Entrance and Baths:')
        await self.bot.say('https://youtu.be/FVAvumqd2Yw')

    @_guides.command(pass_context=True)
    async def gardens(self, ctx):
        """Pleasure Gardens Guide"""
        await self.bot.say('Here is the guide for the Pleasure Gardens:')
        await self.bot.say('https://youtu.be/pPg7rxKxf8o')

    @_guides.command(pass_context=True)
    async def spawns(self, ctx):
        """Some good info on spawns in the Throneroom"""
        await self.bot.say('Spawn pattern of ads in throne room:')
        await self.bot.say('https://redd.it/79gpxc')

    @commands.group(name="challenge", pass_context=True)
    async def _challenge(self, ctx):
        """Commands for showing the challenge modes

        Example: !challenge <name>"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_challenge.command(pass_context=True)
    async def rb(self, ctx):
        """Royal Bath Challenge"""
        await self.bot.say("Royal Baths Challenge mode")
        await self.bot.say("https://youtu.be/rwBH07GZfZU")

    @_challenge.command(pass_context=True)
    async def pg(self, ctx):
        """Pleasure Gardens Challenge"""
        await self.bot.say("Pleasure Gardens Challenge Mode")
        await self.bot.say("https://youtu.be/n9w38R-4xzg")

    @_challenge.command(pass_context=True)
    async def gaunt(self, ctx):
        """Gauntlet Challenge"""
        await self.bot.say("Gauntlet Challenge Mode")
        await self.bot.say("https://youtu.be/HB3cBq0VU-8")

    @_challenge.command(pass_context=True)
    async def cal(self, ctx):
        """Calus Challenge"""
        await self.bot.say("Calus Challenge Mode")
        await self.bot.say("https://youtu.be/5lP700fFgfo")


def setup(bot):
    n = Guides(bot)
    bot.add_cog(n)
