from botconfig.definitions import *
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.bot = client
        print('Events Cog has been loaded')
    
    @commands.Cog.listener()
    async def on_message(self,ctx):
        if self.bot.user.mentioned_in(ctx)and len(ctx.content.split(' ')) == 1 and ctx.content[-1] == '>' and ctx.content[0] == '<':
            await ctx.channel.send(f'Current command prefix is \"{f_get_prefix(self, ctx)}\".')

def setup(bot):
    bot.add_cog(Events(bot))