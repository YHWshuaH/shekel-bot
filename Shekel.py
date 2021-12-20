import discord
#import logging
import json
import os
#from discord import message
from cogs.commands import *
from botconfig.definitions import *

# Printing path to working directory
print(f"{cwd} is the current working directory")
#print(f"\n-----\n{pd} is the media directory")

# Local variable declarations
bot = commands.Bot(command_prefix = f_get_prefix, case_insensitive = True)
secret_file = json.load(open(cwd + '/secrets.json'))
bot.config_token = secret_file["token"]
#logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f"-----\nLogged in as {bot.user}")
    await bot.change_presence(activity=discord.Game("Ping me to find my prefix!"))

@bot.event
async def on_guild_join(guild):
    with open(cwd + "/botconfig/metadata.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = v_default_prefix + " "
    
    with open(cwd + "/botconfig/metadata.json", "w") as f:
        json.dump(prefixes,f)

@bot.event
async def on_guild_leave(guild):
    with open(cwd + "/botconfig/metadata.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open(cwd + "/botconfig/metadata.json", "w") as f:
        json.dump(prefixes[str(guild.id)])

# Loading cog files
if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")
    bot.run(bot.config_token)