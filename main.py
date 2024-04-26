import os
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # Get your bot token from the .env file
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Get the channel ID from the .env file

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

async def send_message(channel, message):
    try:
        await channel.send(message)
        print("Message sent successfully!")
    except discord.errors.HTTPException as e:
        print(f"Failed to send message: {e}")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    print(f'Listening to messages in channel: {channel.name}')

    while True:
        try:
            message = await asyncio.get_event_loop().run_in_executor(None, input, "Enter your message: ")
            if message.lower() == 'exit':
                await client.close()
                break  # Exit the loop if the user wants to exit
            await send_message(channel, message)
        except Exception as e:
            print(f"An error occurred: {e}")

client.run(TOKEN)
