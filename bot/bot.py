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
        await message.channel.send(f'For you, {message.author}: {item}')

    if message.content == "$joke":
        item1 = destiny_api_queries.get_random_item()
        item2 = destiny_api_queries.get_random_item()
        item3 = destiny_api_queries.get_random_item()
        await message.channel.send(f'She {item1} on my {item2} till {message.author} {item3}')

client.run("")