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
        """You must enter a guide from the list"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_guides.command(pass_context=True, no_pm=True)
    async def calus(self, ctx):
        """Calus Guide"""
        await self.bot.say('Here is the guide for Calus:')
        await self.bot.say('https://youtu.be/aeKeJ6x_Zi8')

    @_guides.command(pass_context=True, no_pm=True)
    async def gauntlet(self, ctx):
        """Gauntlent Guide"""
        await self.bot.say('Here is the guide for the Gauntlet:')
        await self.bot.say('https://youtu.be/T0DbeXjkKRs')

    @_guides.command(pass_context=True, no_pm=True)
    async def baths(self, ctx):
        """Guide for the Baths and Enterance"""
        await self.bot.say('Here is the guide for the Enterancee and Baths:')
        await self.bot.say('https://youtu.be/FVAvumqd2Yw')

    @_guides.command(pass_context=True, no_pm=True)
    async def gardens(self, ctx):
        """Guide for the Pleasure Gardens"""
        await self.bot.say('Here is the guide for the Pleasure Gardens:')
        await self.bot.say('https://youtu.be/pPg7rxKxf8o')

    @_guides.command(pass_context=True, no_pm=True)
    async def spawns(self, ctx):
        """Some good info on spawns in the Throneroom"""
        await self.bot.say('Spawn pattern of ads in throne room:')
        await self.bot.say('https://redd.it/79gpxc')


def setup(bot):
    n = Guides(bot)
    bot.add_cog(n)
