# ALL BOT TOKENS HAVE BEEN REMOVED FROM FILES
# YOU WILL NEED TO ADD YOUR OWN FOR THE CODE TO RUN ON YOUR BOT
# FOR BOT TOKENS, VISIT THE DISCORD DEVELOPER'S PORTAL

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

bot = commands.Bot (command_prefix = "!")

@bot.event
async def on_ready () :
    print ('online')

@bot.command ()
async def ping (ctx) :
    await ctx.send (f"pong {round (bot.latency * 1000)} ms")

@bot.command ()
async def say (ctx, *, message) :
    await ctx.send (message)
    await ctx.message.delete()

@say.error
async def say_error (ctx , error) :
    if isinstance (error , commands.MissingRequiredArgument) :
        await ctx.send ('idk mate')

@bot.event
async def on_command_error (ctx , error) :
    if isinstance (error , CommandNotFound) :
        await ctx.send ('bruh...')

bot.run ('BOT TOKEN')
