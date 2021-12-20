import discord
from discord import embeds
from discord.ext import commands
#import json
import aiohttp
#import io
from discord.ext.commands.errors import NSFWChannelRequired
from botconfig.definitions import * #cwd, f_get_prefix, f_dump_prefix, update_url, url_encode#, bot
import random
#from hash import url_encode

"""url_encode = {
    " " : "%20",
    "#" : "%23",
    "$" : "%24",
    "%" : "%25",
    "&" : "%26",
    "\'" : "%27",
    "+" : "%2B",
    "," : "%2C",
    "/" : "%2F",
    ":" : "%3A",
    ";" : "%3B",
    "=" : "%3D",
    "?" : "%3F",
    "@" : "%40",
    "[" : "%5B",
    "\\" : "%5C",
    "]" : "%5D",
    "^" : "%5E",
    "`" : "%60",
    "{" : "%7B",
    "|" : "%7C",
    "}" : "%7D"
}"""

# Commands cog
class Groups(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()            # logs success message to console
    async def on_ready(self):
        print("-----\nCommands Cog has been loaded")
        
    @commands.command(brief='Pulls and sends a NSFW image/GIF of a boob.', description='Queries reddit under the search term \"boob\" and posts a random image result.')
    @commands.is_nsfw()
    async def boob(self, ctx):
        embed = discord.Embed(title='Scraping result:', description='Query: \"boob\"')
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.reddit.com/search.json?q=boobs%20nsfw%3A1%20self%3A0&include_over_18=1") as resp:
                #buffer = io.BytesIO(await resp.read())
                res = await resp.json()
                num=random.sample(range(100), 1)
                #num=random.randint(0,25)
                print(num)
                addr=res['data']['children'][num]['data']['url']
                if ".jpg" in addr or ".png" in addr:
                    embed.set_image(url=addr)
                    print(f'image addr:{addr}')
                    await ctx.send(embed=embed)
                    #await ctx.send(addr)
                    #await print('not image')
                else:
                    print(f'not image {addr}')
                    await ctx.send(addr)
                    #await ctx.send(embed=embed)
                    #await print('image')

                print(num)      # For debugging/logging
                print(addr)

        #await ctx.send_file(channel, fp=buffer, filename="shekx")

    # Throws an error if the command is called in a channel not flagged as NSFW
    @boob.error
    async def boob_error(self, ctx, error):
        if isinstance(error, NSFWChannelRequired):
            await ctx.send(file=discord.File('/home/shagger/Pictures/memes/downbad.jpg'))
            await ctx.send('Channel not marked as NSFW ;)')

    @commands.group(brief='Pulls an image/GIF result relevant to the provided search term', description='Queries reddit under the given search term and posts a random image result')
    async def img(self, ctx, arg1):
        if ctx.invoked_subcommand is None:
            arg1 = update_url(arg1)    # Fetches string updated with urlcodes for special characters should they be input through arg1
            embed = discord.Embed(title='Scraping result:', description=f'Query: \"{arg1}\"')
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://www.reddit.com/search.json?q={arg1}&sort=relevance") as resp:
                    res = await resp.json()
                    num=random.randint(0,25)
                    addr=res['data']['children'][num]['data']['url']
                    embed.set_image(url=addr)
                    if not "gif" in addr:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send(addr)
                    
                    print(num)   # for debugging x2
                    print(addr)

    @commands.command()
    async def greet(self, ctx):
        await ctx.send("shtup")

    @commands.command()
    async def ly(self, ctx):
        await ctx.send("ok we will have se\nx")

    @commands.group(brief='Displays the current command prefix.', description='Displays current command prefix. Can be chained with subcommands to perform various prefix-related functions.')
    async def prefix(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f'Current command prefix is {f_get_prefix(self, ctx)}')

    @prefix.command(brief='Changes the command prefix. Changes to default prefix with no args.', description='Changes the command prefix to whatever comes after it. To use prefixes with whitespaces, enclose the string with double quotes \(\" \"\). If no arguments are provided, the default prefix is loaded.')
    async def ch(self, ctx, arg1=None):
        f_dump_prefix(self, ctx, arg1)
        if arg1 is None:
            await ctx.send(f'Command prefix changed to default prefix, \"{f_get_prefix(self, ctx)}\".')
        else:
            await ctx.send(f'Command prefix changed to \"{f_get_prefix(self, ctx)}\".')

def setup(bot):
    bot.add_cog(Groups(bot))