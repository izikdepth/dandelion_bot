import discord
from discord.ext import commands 
import os
from dotenv import load_dotenv
import logging

load_dotenv()

#intents
intents = discord.Intents.default()
intents.members = True



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

bot.run(os.getenv('DDLN_BOT')) 

