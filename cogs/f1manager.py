import discord
from discord import app_commands
from discord.ext import commands

class F1Manager(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog is ready')

async def setup(bot):
    await bot.add_cog(F1Manager(bot), guilds=[discord.Object(id=524776650945200138)])