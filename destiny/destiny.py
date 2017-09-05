import os
import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from datetime import datetime
from collections import namedtuple, defaultdict, deque

#uses the base economy cog for the bones, very much a work in progress

class NoAccount(VerificationError):
    pass

class Verification():

    def __init__(self, bot, file_path):
        self.useraccounts = dataIO.load_json(file_path)
        self.bot

    def get_dest_account(self, user):
        acct = self._get_account(user)
        acct["id"] = user.id
        acct["server"] = user.server
        return self._create_dest_account_obj(acct)

    def _create_account_obj(self, account):
        account["member"] = account["server"].get_member(account["id"])
        account["created_at"] = datetime.strptime(account["created_at"],
                                                  "%Y-%m-%d %H:%M:%S")
        Account = namedtuple("Account", "id name balance "
                             "created_at server member")
        return Account(**account)

    def _get_account(self, user):
        server = user.server
        try:
            return deepcopy(self.accounts[server.id][user.id])
        except KeyError:
            raise NoAccount()


class Destiny():
    """Provide info and stats as it relates to Destiny.

    This will only provide stats for Destiny 2. All Destiny
    1 data is depreciated."""

    def __init__(self, bot):
        global default_settings
        self.bot = bot
        self.file_path = "data/destiny/settings.json"
        self.settings = dataIO.load_json(self.file_path)
        self.userinfo = dataIO.load_json(userinfo_path)
        self.settings = defaultdict(lambda: default_settings, self.settings)

    @commands.command():
    async def clanmembers(self):
        """List all of the current members of the clan.

        Will use to tie PSN to Discord name."""
        pass

    @commands.command(pass_context=True):
    async def verify(self):
        """Prompt user to change status to string

        Save information into the userinfo.json
        If status string == saved"""


def check_folders():
    if not os.path.exists("data/destiny"):
        print("Creating data/destiny folder...")
        os.makedirs("data/destiny")


def check_files():
    f = "data/destiny/settings.json"
    if not dataIO.is_valid_json(f):
        print("Creating default destiny settings.json...")
        dataIO.save_json(f, {})

    f = "data/destiny/userinfo.json"
    if not dataIO.is_valid_json(f):
        print("Creating default destiny userinfo.json...")
        dataIO.save_json(f, {})


def setup(bot):
    global logger
    check_folders()
    check_files()
    bot.add_cog(Destiny(bot))
