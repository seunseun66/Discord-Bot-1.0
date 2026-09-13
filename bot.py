import os
import discord
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise ValueError('DISCORD_TOKEN not found. Check your .env file.')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme', timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get('url')
    except requests.RequestException as e:
        print(f'Error fetching meme: {e}')
        return None


@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

    if message.content.startswith('$meme'):
        meme_url = get_meme()
        if meme_url:
            await message.channel.send(meme_url)
        else:
            await message.channel.send("Couldn't fetch a meme right now, try again later.")


client.run(TOKEN)
