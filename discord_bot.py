from dotenv import load_dotenv
load_dotenv()

import discord
import os

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    # when the bot is ready, this message will send
    print("We have logged in as {0.user}".format(client))
    
    channel = client.get_channel(1055981827338293302)
    await channel.send('Take Your Creatine!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return    
    
    if message.author.id == 196331016225292289:
        await message.channel.send("Hello")
        


client.run(os.getenv("TOKEN"))



