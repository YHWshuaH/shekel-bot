from discord.ext.commands.errors import CommandInvokeError, MissingRequiredArgument
from cogs.commands import Groups
from discord.ext import commands
from Shekel import bot

group = Groups(bot)

class Errors(commands.Cog):
    @group.img.error
    async def img_error(self, ctx, error):
        options = {
            MissingRequiredArgument : "This command does not take zero args. Consult the help page (default \"shekel help img\")for command usage and syntax.",
            CommandInvokeError : "Error. List index out of range. Contact bot owner."}
        for i in range(3):
            if error in options:
                errorMessage = options[error]
            else:
                errorMessage = "Unknown error. Contact bot owner."
        await ctx.send(errorMessage)

def setup(bot):
    bot.add_cog(Errors(bot))