import discord
from discord.ext import commands

bot = commands.Bot (command_prefix = "!run_")

@bot.event
async def on_ready () :
    print ('online')

@bot.command ()
async def rpa (ctx , * , message) :

    numbers = message.split ()

    lh = []
    rh = []
    total = 0

    a = numbers [0]
    b = numbers [1]

    while a >= 1 :
        lh.append (a)
        rh.append (b)
        a = int (a / 2)
        b = b * 2

    await ctx.send (lh)
    await ctx.send (rh)

    for i in range (len (lh)) :
        if lh [i] % 2 == 0 :
            rh [i] = 0

    await ctx.send (rh)

    for x in rh :
        total = total + x

    await ctx.send (total)

bot.run('BOT TOKEN')
