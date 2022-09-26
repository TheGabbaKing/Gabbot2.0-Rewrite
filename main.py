import discord
import config
import asyncio
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="g.", intents=intents)


@bot.event
async def on_ready():
    print("Gabbot is Online")

@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if ctx[1] == '.':
        return
    if ctx.author.id == bot.user.id:
        return
    await ctx.channel.send("What up bitch")

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())
