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
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content.startswith("https://www.instagram.com") or ctx.content.startswith("https://twitter.com"):
            url = ctx.content.split("?") #splits URL into parts
            if ctx.author.id == self.bot.user.id or ctx.author.id != 487110546223661076: #checks if the user who sent it was the bot or NOT me
                return
            elif ctx.content.startswith("https://twitter.com"):
                cutURL = url[0]
                if ctx.content.endswith("no"):
                    noURL = cutURL[:-2]
                    await ctx.channel.send(f"{noURL}")
                else:
                    newURL = cutURL[:8] + "fx" + cutURL[8:]
                    await ctx.channel.send(f"{newURL}")
            else:
                await ctx.channel.send(f"{url[0]}")
            await ctx.delete()

async def setup(bot):
    await bot.add_cog(Commands(bot), guilds=[discord.Object(id=524776650945200138)])