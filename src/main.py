# main app features go here
import discord
import os
from dotenv import load_dotenv
# import local functions
import core as C
# load env credentials
load_dotenv()

# quotes stuff
quotes = C.reader('./replies/phrases.txt')
# C.get_random(quotes)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.endswith('Hamid says:'):
        # call the function here to post a message into the server
        await message.channel.send(quotes[C.get_random(quotes)])

client.run(os.getenv('TOKEN'))
