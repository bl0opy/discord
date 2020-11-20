
import discord
import os
import random
import requests
import json
import nest_asyncio
nest_asyncio.apply()




def KtoF(K):
    G = float(K)
    F = (G-273.15)*(9/5)+32
    return str(round(float(F), 2))


def getWeather(city):
    
    API_ID = "YOUR OWM API ID"
    link = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_ID
    
    response = requests.get(link)
    x = response.json()
    
    if x["cod"] != "404": 
        
        y = x["main"]
        
        temp = y['temp']
        feel = y['feels_like']
        min = y['temp_min']
        max = y['temp_max']
        
        z = x['weather']
        des = z[0]["description"] 
        
        
        return [city,str(des),KtoF(temp),KtoF(feel),KtoF(min),KtoF(max)]
    
    else: 
        print(" City Not Found ") 




token = 'WRITE DISCORD TOKEN HERE'


client = discord.Client()

print(" ")
print("<WEATHER_BOT>")
print(" ")
print("activating bot..\nestablishing socket connection\nentering discord..\n")

@client.event
async def on_ready():
    print('-> logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$ testing'):
        await message.channel.send("Yes, a am active and working!")
    if message.content.startswith('$ weather '):
        print('weather')
        vals = message.content.split(' ')
        city = vals[2]
        data = getWeather(city)
        # print(data)
        await message.channel.send("Weather in " + str(data[0]))
        await message.channel.send("--------------------------")
        await message.channel.send("~ " + str(data[1]) + " ~")
        await message.channel.send("Temp: " + str(data[2]) + "˚F")
        await message.channel.send("Feels like " + str(data[3]) + "˚F")
        await message.channel.send("MIN - " + str(data[4]))
        await message.channel.send("MAX - " + str(data[5]))
        await message.channel.send("--------------------------")
    
    # Add other message stuff here


# more event types idk
        

client.run(token)