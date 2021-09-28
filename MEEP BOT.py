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
