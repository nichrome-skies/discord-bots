# ALL BOT TOKENS HAVE BEEN REMOVED FROM FILES
# YOU WILL NEED TO ADD YOUR OWN FOR THE CODE TO RUN ON YOUR BOT
# FOR BOT TOKENS, VISIT THE DISCORD DEVELOPER'S PORTAL

import discord
from discord.ext import commands

bot = commands.Bot (command_prefix = "+")

@bot.event
async def on_ready () :
    print ('online')

@bot.command ()
async def meep (ctx) :
    await ctx.send ("meep")

bot.run('BOT TOKEN')
