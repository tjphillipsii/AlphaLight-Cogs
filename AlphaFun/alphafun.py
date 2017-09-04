from random import choice
from discord.ext import commands

quotes = {
    "That Hunter's got a big mouth. Guess he can back it up though.",
    "Would love to get Zavala back in the Crucible. Teach the new breed how it's done.",
    "Warlocks might be thinkers, but most I know can hold their own.",
    "The Darkness might as well come right in and take the place if that's all we've got.",
    "You think you can fight Fallen without training? They'll put your head on the spike.",
    "Something bad's going down on the Moon.",
    "You want to take on the Cabal? You've got to train, or they'll stomp you flat.",
    "New Monarchy will have to wait.",
    "Future War Cult's getting antsy. They must be preparing for something.",
    "Ikora's gift from the Light is like few I've ever seen.",
    "Dead Orbit's not in charge of the Crucible. I am.",
    "You want the Crucible? I am the Crucible.",
    "Cayde ran through the Crucible like as if it was a game...Sly bastard.",
    "Let them burn in your Light",
    "I abhor sitting here while others fight my battles. But I wouldn't have missed that match for anything.",
    "Your strategy is working, keep it up",
    "I would tear out a Vex heart with my teeth, I would sear the Cabal with my burning light, challenge the Kells to personal combat and scatter them. I'd... I've been watching too many Crucible matches.",
    "Your spirit is unrivaled. Show me more!",
    "Enough! This battle was one-sided! You've obliterated them! Love it!",
    "Do you like it better when Lord Saladin oversees these matches? Do I look like I care? Get back in there!",
    "Your legend grows.",
    "This is amazing!",
    "Fight forever Guardian!",
    "Get back out there.",
    "Wipe. Them. Out.",
    "Look at them fall!",
    "I can't believe what I'm seeing!",
    "I'm not gonna tell you how I lost the horn; you couldn't handle it.",
    "I will tell you how I lost my horn, but it doesn't live up to slaying Oryx.",
    "Securing the Crest is vital. Good work.",
    "Heh. You're crushing them. Send them home crying.",
    "I say take the Crest; you take all the Crests."
}

class AlphaFun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getsum(self):
        """Return a random Shaxx quote"""
        await bot.say(choice(quotes))


    @commands.command()
    async def kenny(self):
        """T I dougle Grrr POTATO!"""
        await self.bot.say('Ummm... POTATO')
        await self.bot.send_file(ctx.message.channel, 'kennythetiger.jpg')

def setup(bot):
    n = AlphaFun(bot)
    bot.add_cog(n)

