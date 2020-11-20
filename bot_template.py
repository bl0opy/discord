
import discord
import os
import random
import nest_asyncio
nest_asyncio.apply()



bot_name = 'COOL NAME'

token = 'WRITE TOKEN HERE' 

client = discord.Client()

print(" ")
print(f"<{bot_name}>")
print(" ")
print("activating bot..\nestablishing socket connection\nentering discord..\n")

@client.event
async def on_ready():
    print('-> logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$ testing'):
        await message.channel.send("Yes, i'm working just fine")
    
    # Add other message stuff here


# more event types
        

client.run(token)







