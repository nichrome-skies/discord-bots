import discord
import sqlite3

client = discord.Client ()

myDb = sqlite3.connect ('F1 2019 CHAMPIONSHIP STANDINGS.db')
cursor = myDb.cursor ()

def findRacing () :

    cursor.execute ("SELECT * FROM Drivers , Points WHERE Drivers.driverTeam LIKE '%Racing%' AND Drivers.driverNumber = Points.driverNumber ORDER BY driverPosition ASC ;")

    rows = cursor.fetchall ()
    myDb.commit ()
    driverData = '```'

    for i in rows :
        for x in range (len(rows[0])) :
            driverData = driverData + str(i[x]) + ':'
        driverData = driverData + '\n'
    driverData = driverData + '```'
    return (driverData)

@client.event
async def on_ready () :
    print ('online')

@client.event
async def on_message (message) :
    if message.author == client.user :
        return
    if message.content.startswith ('named racing teams') :
        await message.channel.send (findRacing())

client.run ('BOT TOKEN')
myDb.close ()
