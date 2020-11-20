
import insult
import discord
import os
import random
import nest_asyncio
nest_asyncio.apply()



def generate_pic():
    path = 'PATH TO GIF FOLDER'
    files = os.listdir(path)
    d = random.choice(files)
    if d != '.DS_Store':
        return path + d
    else:
        generate_pic()


token = 'WRITE TOKEN HERE'

client = discord.Client()

print(" ")
print("<DISS_bot>")
print(" ")
print("activating bot..\nestablishing socket connection\nentering discord..\n")

@client.event
async def on_ready():
    print('-> logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$ testing'):
        await message.channel.send("Yes, i'm working just fine")
    elif message.content.startswith('$ insult'):
        vals = message.content.split(' ')
        name = vals[2].capitalize() + ", "
        roast = name + insult.generate_insult()
        gif = generate_pic()
        await message.channel.send(roast)
        print('diss ~ ' + gif)
        await message.channel.send(file=discord.File(gif))

    # Add other message stuff here


# more event types idk
        

client.run(token)


