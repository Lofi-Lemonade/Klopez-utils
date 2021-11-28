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


class Ball(commands.Cog, name="Balls 🔴🟢🔵"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="yogaball")
    async def yogaball(self, ctx):
        """
        A Command Suggested By @Qüīêt#6066!
        """
        if ctx.invoked_subcommand is None:
                embed = discord.Embed(title="Yogaball Colors", description="", color=0xff0000)
                embed.add_field(name="Red 🔴", value="`-yogaball Red`", inline=False)
                embed.add_field(name="Green 🟢", value="`-yogaball Green`", inline=False)
                embed.add_field(name="Blue 🔵", value="`-yogaball Blue`", inline=False)
                embed.set_footer(text="Command Suggested By @Qüīêt#6066 ", icon_url="https://cdn.discordapp.com/avatars/574107787416567820/2d05f621420afa168149d82c0d4bec76.png?size=128")
                embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/574107787416567820/2d05f621420afa168149d82c0d4bec76.png?size=128")
                await ctx.send(embed=embed)

    @yogaball.command(name="red")
    async def yogaball_red(self, ctx):
                """
                Red Yoga Ball
                """
                embed=discord.Embed(title="Red  Yoga Ball", description="Heres A Red Yoga Ball! 🔴", color=0xff0000)
                embed.set_image(url="https://m.media-amazon.com/images/I/91zAh1eHixL._AC_SL1500_.jpg")
                embed.set_footer(text="Command Suggested By Qüīêt#6066", icon_url="https://cdn.discordapp.com/icons/838607169074888744/b89f584442452692fde640b68852c365.png?size=4096")
                await ctx.send(embed=embed)

    @yogaball.command(name="green")
    async def yogaball_green(self, ctx):
                """
                Green Yoga Ball
                """
                embed=discord.Embed(title="Green Yoga Ball", description="Heres A Green Yoga Ball! 🟢", color=0x1eff00)
                embed.set_image(url="https://cdn.discordapp.com/attachments/859251551586615356/914335475056128080/IMG_0483.png")
                embed.set_footer(text="Command Suggested By Qüīêt#6066", icon_url="https://cdn.discordapp.com/icons/838607169074888744/b89f584442452692fde640b68852c365.png?size=4096")
                await ctx.send(embed=embed)

    @yogaball.command(name="blue")
    async def yogaball_blue(self, ctx):
                """
                Blue Yoga Ball
                """
                embed=discord.Embed(title="Blue Yoga Ball", description="Heres A Blue Yoga Ball! 🔵", color=0x34aeeb)
                embed.set_image(url="https://cdn.discordapp.com/attachments/859251551586615356/914377817163202580/4826ec85-d0e6-4321-87d6-4f88646e016a_1.11bae0d81525f9ea43c28e87762534aa.jpeg")
                embed.set_footer(text="Command Suggested By Qüīêt#6066", icon_url="https://cdn.discordapp.com/icons/838607169074888744/b89f584442452692fde640b68852c365.png?size=4096")
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ball(bot))