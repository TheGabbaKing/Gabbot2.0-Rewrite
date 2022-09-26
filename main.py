import discord
import config
import asyncio
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="g.", intents=intents, application_id="1020217647973027870")


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

@bot.command()
@commands.is_owner()
async def reload(ctx):
    async with ctx.typing():
        print("trying to reload")
        for ext in os.listdir("./cogs/"):
            if ext.endswith(".py") and not ext.startswith("_"):
                try:
                    print("found extensions")
                    await bot.reload_extension(f"cogs.{ext[:-3]}")
                    await ctx.send(f"{ext[:-3]} Cog Reloaded")
                except Exception as e:
                    print("didn't find anything")
                    await ctx.send(f"No cogs were reloaded")
                await asyncio.sleep(0.5)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())
