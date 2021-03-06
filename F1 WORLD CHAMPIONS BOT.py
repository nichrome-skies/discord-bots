# ALL BOT TOKENS HAVE BEEN REMOVED FROM FILES
# YOU WILL NEED TO ADD YOUR OWN FOR THE CODE TO RUN ON YOUR BOT
# FOR BOT TOKENS, VISIT THE DISCORD DEVELOPER'S PORTAL

# THE F1 WORLD CHAMPIONS DATABASE FILE MUST BE DOWNLOADED WITH THIS FILE
# AND THE FILE MUST BE DOWNLOADED INTO THE SAME FOLDER OTHERWISE THE BOT WON'T RUN

import discord
from discord.ext import commands
import sqlite3

bot = commands.Bot (command_prefix = "!f1c ")

myDb = sqlite3.connect ('F1 WORLD CHAMPIONS.db')
cursor = myDb.cursor ()

@bot.event
async def on_ready () :
    print ('online')

@bot.command ()
async def on_message (message) :

    def findRacing (command) :

        cursor.execute (command)

        rows = cursor.fetchall ()
        myDb.commit ()
        outputData = '```'

        for i in rows :
            for x in range (len(rows[0])) :
                outputData = outputData + str(i[x]) + ':'
            outputData = outputData + '\n'
        outputData = outputData + '```'
        return (outputData)

    if message.author == client.user :
        return
    if message.content.startswith ('!find ') :
        mCommand = message.content[6 :]
        await message.channel.send (findRacing(mCommand))

client.run ('BOT TOKEN')
myDb.close ()
