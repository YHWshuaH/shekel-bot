from pathlib import Path
import json

cwd = Path(__file__).parents[1]
cwd = str(cwd)

v_default_prefix="shekel"

pd = Path('/home/shagger/Pictures/meme')
pd = str(pd)

url_encode = {
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
}

# Homemade "endwith" function
def f_endswith(string):
    strlength=len(string)
    strlength = strlength-1
    array = [None]
    for i in string:
        array.append(i)
    array.pop(0)
    return array[strlength]

# Fetches prefixes for the guild the bot was run in
def f_get_prefix(bot, message):
    with open(cwd + "/botconfig/metadata.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

# dumps prefixes for use with the change prefix command
def f_dump_prefix(bot, message, arg1=None):
    with open(cwd + "/botconfig/metadata.json", "r") as f:
        prefixes = json.load(f)
        if not arg1==None:
            prefixes[str(message.guild.id)] = arg1
        else:
            prefixes[str(message.guild.id)] = v_default_prefix + " "
    with open(cwd + "/botconfig/metadata.json", "w") as f:
        json.dump(prefixes, f)

async def update_url(arg1):        # func for updating the search term with suitable urlcode for special characters
    for i in url_encode:
        #print(url_encode[i])
        if i in arg1:
            l = url_encode[i]
            break
        else:
            l = i
    arg1 = arg1.replace(i, l)
    return arg1
#result = update_url("funky")
#print(result)