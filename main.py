import discord
 
 
client = discord.Client()
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('Привет'):
        await message.channel.send('Ага канешна') #ОТВЕТ
    if message.content.startswith('Пока'):
        await message.channel.send('Ага Нет')    
 
 

client.run('ODM4MDM0OTQ4NTkzMTU2MTU3.YI1O3Q.F86mj-dzN6vFNUb0-ytW1hg1TZo')
 