import discord
import destiny_api_queries

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content == "$item":
        item = destiny_api_queries.get_random_item()
        await message.channel.send(item)

client.run("")