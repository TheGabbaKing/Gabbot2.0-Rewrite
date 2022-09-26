import discord
import os
import asyncio
from discord import app_commands
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Commands Cog is ready')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"Synced {len(fmt)} commands to {ctx.guild.name}.")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("This command is a test")


async def setup(bot):
    await bot.add_cog(Commands(bot), guilds=[discord.Object(id=524776650945200138)])