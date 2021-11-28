import json
import os
import io
import re
import contextlib
import platform
import random
import sys
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext

clear = lambda: os.system('clear')

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = discord.Intents.default()

bot = Bot(command_prefix=config["bot_prefix"], intents=intents, status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name="Christmas Movies!"))
slash = SlashCommand(bot)

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))


@bot.event
async def on_ready():
    clear()
    prGreen(f"Logged in as {bot.user.name} ✅")
    prCyan(f"Discord.py API version: {discord.__version__} 📘")
    prYellow(f"Python version: {platform.python_version()} 🟡")
    prPurple(f"Running on: {platform.system()} {platform.release()} ({os.name}) 💻")
    print(" ")
    

bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")



@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return
    with open("blacklist.json") as file:
        blacklist = json.load(file)
    if message.author.id in blacklist["ids"]:
        return
    await bot.process_commands(message)


@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    prGreen(
        f"Executed {executedCommand} command in {ctx.guild.name} by {ctx.message.author} ✅")


@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24
        embed = discord.Embed(
            title="Hey, please slow down!",
            description=f"You can use this command again in {f'{round(hours)} hours' if round(hours) > 0 else ''} {f'{round(minutes)} minutes' if round(minutes) > 0 else ''} {f'{round(seconds)} seconds' if round(seconds) > 0 else ''}.",
            color=0xff0000
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Error!",
            description="You are missing the permission `" + ", ".join(
                error.missing_perms) + "` to execute this command!",
            color=0xff0000
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Error!",
            description=str(error).capitalize(),
            color=0xff0000
        )
        await context.send(embed=embed)
    raise error
    
@bot.command()
async def weather(ctx, *, message): 
    embed = discord.Embed(color=0x1eff00,
                          title=f"Weather in {message}")
    embed.set_image(
        url=
        f"https://api.cool-img-api.ml/weather-card?location={message}&background=https://pbs.twimg.com/media/EnLHDYBVgAQNLAt.jpg"
    )
    embed.set_footer(text="Brought to you by Klopez", icon_url='https://cdn.discordapp.com/attachments/866421856957235200/913499699586162708/invert.png')
    embed.set_author(name="Klopez Utils", icon_url="https://cdn.discordapp.com/attachments/866421856957235200/913499699586162708/invert.png")
    await ctx.send(embed=embed)

@bot.command()
async def errorcat(ctx, *, message): 
    embed = discord.Embed(color=0xff0000, title=f"Showing You Error{message}")
    embed.set_image(url= f"https://http.cat/{message}")
    embed.set_footer(text="Brought to you by Klopez", icon_url='https://cdn.discordapp.com/attachments/866421856957235200/913499699586162708/invert.png')
    embed.set_author(name="Klopez Utils", icon_url="https://cdn.discordapp.com/attachments/866421856957235200/913499699586162708/invert.png")
    await ctx.send(embed=embed)

@bot.command()
async def errordog(ctx, *, message): 
    embed = discord.Embed(color=0xff0000, title=f"Showing You Error{message}")
    embed.set_image(url= f"https://httpstatusdogs.com/{message}")
    embed.set_footer(text="Brought to you by Klopez", icon_url='https://cdn.discordapp.com/attachments/866421856957235200/913499699586162708/invert.png')
    embed.set_author(name="Klopez Utils", icon_url="https://cdn.discordapp.com/attachments/866421856957235200/913499699586162708/invert.png")
    await ctx.send(embed=embed)

@bot.command()
async def lofi(ctx):
    embed = discord.Embed(title="Lofis Test thingy yeah", description="Poopshit", color=0x1eff00,)
    embed.set_footer(text="Yo this is so easy to make omfg", icon_url="https://cdn.discordapp.com/attachments/866421856957235200/913499699586162708/invert.png")    
    await ctx.send(embed=embed)

bot.run(config["token"])
