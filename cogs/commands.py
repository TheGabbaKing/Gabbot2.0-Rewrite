import discord, requests, uuid, shutil
from discord import app_commands
from discord.ext import commands
from typing import Optional

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener() #INITIALISER
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog is ready')

    @commands.command() #SYNC SLASH COMMANDS
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"Synced {len(fmt)} commands to {ctx.guild.name}.")

    @commands.Cog.listener() #INSTAGRAM & TWITTER URL PARSER
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

    @commands.command() #WEBM CONVERTER
    async def save(self, ctx, arg1:Optional[str] = None):
        if arg1 == None and ctx.message.attachments and ctx.message.attachments[0].url.endswith("webm"):
            print("Attachment found")
            url = ctx.message.attachments[0].url
        elif arg1.startswith("https://cdn.discordapp.com") and arg1.endswith(".webm"):
            print("URL found")
            url = arg1
        else:
            await ctx.send("Sorry your file isn't supported yet. Only webm is supported right now.")
        r = requests.get(url, stream=True)
        fileName = f'files/{str(uuid.uuid4())}' + '.mp4'
        with open(fileName, 'wb') as outFile:
            async with ctx.typing():
                print("Saving file: " + fileName)
                shutil.copyfileobj(r.raw, outFile)
                await ctx.send(file=discord.File(f'{fileName}'))
            
async def setup(bot):
    await bot.add_cog(Commands(bot), guilds=[discord.Object(id=524776650945200138)])