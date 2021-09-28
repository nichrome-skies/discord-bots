import discord
import sqlite3

client = discord.Client ()

myDb = sqlite3.connect ('F1 WORLD CHAMPIONS.db')
cursor = myDb.cursor ()

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

@client.event
async def on_ready () :
    print ('online')

@client.event
async def on_message (message) :
    if message.author == client.user :
        return
    if message.content.startswith ('!find ') :
        mCommand = message.content[6 :]
        await message.channel.send (findRacing(mCommand))

client.run ('BOT TOKEN')
myDb.close ()
