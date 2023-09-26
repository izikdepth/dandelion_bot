import discord
from discord.ext import commands, tasks
import requests

intents = discord.Intents(guilds=True)
client = discord.Client(intents=intents)
 

class serverStats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 1156007756898246737
        self.bot.ready = False
        self.update_btc_price.start() 

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.ready = True
            print(f'Bot is ready. Channel ID: {self.channel_id}')
    
    @tasks.loop(minutes=1)  # Update every minute
    async def update_btc_price(self):
        if not self.bot.ready or self.channel_id is None:  # Don't do anything if the bot isn't ready or the channel hasn't been set
            return

        channel = self.bot.get_channel(int(self.channel_id))  # Make sure to convert the channel ID to an integer

        if channel is None:
            print(f'Could not find channel with ID {self.channel_id}')
            return

        # Fetch Bitcoin price
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        data = response.json()

        # Extract the price
        price = data['bitcoin']['usd']

        # Update the channel's name with the price
        await channel.edit(name=f"BTC : ${price}")

        # Set the bot's status
        await self.bot.change_presence(activity=discord.Game(name=f"BTC Price: ${price}"))

        
"""
set up bot and register the cog to the bot
"""
def setup(bot):
    bot.add_cog(serverStats(bot))
