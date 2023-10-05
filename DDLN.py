import discord
from discord.ext import commands 
import os
from dotenv import load_dotenv
import logging

load_dotenv()

#intents
intents = discord.Intents.default()
intents.members = True


##setting up logging 
# logger = logging.getLogger('discord')
# handler = logging.FileHandler(filename='DDLN_logs.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

#set bot command prefix and initial bot
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")


Cogs_list = [
    "faq", 
    "emailcollector",
    "serverstats",
]

for Cog in Cogs_list:
    bot.load_extension(f'Cogs.{Cog}')

bot.run(os.getenv('Your bot token')) 

