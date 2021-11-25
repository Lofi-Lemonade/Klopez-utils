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

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = discord.Intents.default()

bot = Bot(command_prefix=config["bot_prefix"], intents=intents)
slash = SlashCommand(bot)


# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    status_task.start()


# Setup the game status task of the bot
@tasks.loop(minutes=1.0)
async def status_task():
    statuses = ["In the Christmas Cabin", "With Kyle", f"{config['bot_prefix']}help"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))


# Removes the default help command of discord.py to be able to create our custom help command.
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


# The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself
    if message.author == bot.user or message.author.bot:
        return
    # Ignores if a command is being executed by a blacklisted user
    with open("blacklist.json") as file:
        blacklist = json.load(file)
    if message.author.id in blacklist["ids"]:
        return
    await bot.process_commands(message)


# The code in this event is executed every time a command has been *successfully* executed
@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})")


# The code in this event is executed every time a valid commands catches an error
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
            # We need to capitalize because the command arguments have no capital letter in the code.
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
    embed.set_footer(text="Brought to you by Klopez", icon_url='https://cdn.discordapp.com/icons/838607169074888744/6032690c7a3c80143d17836c6f6aa506.png?size=4096')
    embed.set_author(name="Klopez Utils", icon_url="https://cdn.discordapp.com/icons/838607169074888744/6032690c7a3c80143d17836c6f6aa506.png?size=4096")
    await ctx.send(embed=embed)

@bot.command()
async def lofi(ctx):
    embed = discord.Embed(title="Lofis Test thingy yeah", description="Poopshit", color=0x1eff00,)
    embed.set_footer(text="Yo this is so easy to make omfg", icon_url="https://cdn.discordapp.com/icons/838607169074888744/6032690c7a3c80143d17836c6f6aa506.png?size=4096")    
    await ctx.send(embed=embed)


    
# Run the bot with the token
bot.run(config["token"])
