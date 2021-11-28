import json
import os
import sys

import discord
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class Help(commands.Cog, name="help 🧾"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, context):
        """
        List all commands from every Cog the bot has loaded.
        """
        prefix = config["bot_prefix"]
        if not isinstance(prefix, str):
            prefix = prefix[0]
        embed = discord.Embed(title="Help", description="Heres a list of all the commands on the bot! 📚", color=0xff0000)
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i)
            commands = cog.get_commands()
            command_list = [command.name for command in commands]
            command_description = [command.help for command in commands]
            help_text = '\n'.join(f'{prefix}{n} - {h}' for n, h in zip(command_list, command_description))
            embed.add_field(name=i.capitalize(), value=f'```{help_text}```', inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/838607169074888744/b89f584442452692fde640b68852c365.png?size=4096")
            embed.set_footer(text="Brought To You By Klopez", icon_url="https://cdn.discordapp.com/icons/838607169074888744/b89f584442452692fde640b68852c365.png?size=4096")
        await context.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
