# ALL BOT TOKENS HAVE BEEN REMOVED FROM FILES
# YOU WILL NEED TO ADD YOUR OWN FOR THE CODE TO RUN ON YOUR BOT
# FOR BOT TOKENS, VISIT THE DISCORD DEVELOPER'S PORTAL

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

bot = commands.Bot (command_prefix = ".q")

@bot.event
async def on_ready () :
    print ('online')

@bot.command ()
async def aa (ctx, *, message) :
    embed = discord.Embed (title = 'meep' , description = 'i am a plant' , colour = 0xDBE7F5)
    embed.add_field (name = "meep2" , value = message , inline = False)
    await ctx.send (embed = embed)
#    await ctx.message.delete ()

@aa.error
async def aa_error (ctx , error) :
    if isinstance (error , commands.MissingRequiredArgument) :
        embed = discord.Embed (title = 'ERROR' , description = 'Missing Arguement' , colour = 0x960000)
        await ctx.send (embed = embed)

@bot.event
async def on_command_error (ctx , error) :
    if isinstance (error , CommandNotFound) :
        embed = discord.Embed (title = 'ERROR' , description = 'Command Error' , colour = 0x960000)
        await ctx.send (embed = embed)

bot.run ('BOT TOKEN')
