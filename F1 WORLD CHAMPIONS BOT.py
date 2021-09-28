# the F1 World Champions database needs to be downloaded with this file for the bot to run

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
