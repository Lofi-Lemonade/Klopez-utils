import json
import os
import platform
import random
import sys

import aiohttp
import discord
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class Seasonal(commands.Cog, name="seasonal 🎄"):
    def __init__(self, bot):
        self.bot = bot

@commands.command(name ="present")
async def  present(self, ctx):
        """
        pls just work istg
        """
        answers = ["When you open your present you find COAL! ❌", "When you open your present you find the toy you had on your wishlist! 🧸", "You open up your present suprised to find a YOGABALL! 🟢",
        "When you open your present you find some clothes 👚"]
        embed=discord.Embed(
            title="Presents",
            description=random.choice(answers),
            color=0xff0000
        )
        embed.set_footer(text="Command Suggested By @Kylе#6536", icon_url="https://cdn.discordapp.com/avatars/781211271009140746/c42213cf58f8cf94e94ee8d744b9e321.png?size=128")
        await ctx.send(embed=embed)

@commands.command(name="christmas")
async def  christmas(self, ctx):
        """
        Merry Christmas Everybody!
        """
        embed = discord.Embed(title="Merry Christmas Everyone!", description="Have a great christmas this year!", color=0xf0000)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Seasonal(bot))