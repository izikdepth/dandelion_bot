import discord
from discord.ext import commands, tasks
import requests
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    update_btc_price.start()  # Start the task as soon as the bot is ready

@tasks.loop(seconds=5)  # Update every 5 seconds
async def update_btc_price():
    channel_id = "Your channel id here"  # Replace with your channel ID
    channel = bot.get_channel(int(channel_id))  # Get the channel

    # Fetch Bitcoin price
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    data = response.json()

    # Extract the price
    price = data['bitcoin']['usd']

    # Update the channel's name or topic with the price
    await channel.edit(name=f"BTC Price: ${price}")
    
    # Set the bot's status
    await bot.change_presence(activity=discord.Game(name=f"BTC Price: ${price}"))



bot.run(os.getenv("FEDORABOT_TOKEN"))  # Replace with your bot token
