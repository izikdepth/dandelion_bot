import discord
from discord.ext import commands, tasks
import requests

intents = discord.Intents(guilds=True)
client = discord.Client(intents=intents)
intents.members = True
 

class serverStats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.channel_id =  #price feed channel
        self.member_countChannel = #members count channel
        self.bot.ready = False
        self.update_btc_price.start() 
        self.update_memberCount.start()

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
        # await self.bot.change_presence(activity=discord.Game(name=f"BTC Price: ${price}"))
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"BTC Price: ${price}"))
        
    @tasks.loop(seconds=30) # Update every 30 seconds
    async def update_memberCount(self):
        if not self.bot.ready or self.member_countChannel is None:
            return

        channel = self.bot.get_channel(int(self.member_countChannel))

        if channel is None:
            print(f'Could not find channel with ID {self.member_countChannel}')
            return

        guild = self.bot.guilds[0]
        member_count = guild.member_count

        await channel.edit(name=f"Members: {member_count}")





        
"""
set up bot and register the cog to the bot
"""
def setup(bot):
    bot.add_cog(serverStats(bot))
    
    
"""
NOTES  

1. replace the variable "response" with the api you're going to use to fetch the price of $DDLN coin.
2. you can copy the same code and reuse it to view & display the market cap of the coin but don't use the code that show's the status "#set bot status"
3. if you're going to use multiple channels, then name channel_id as 1, 2, 3 etc
4. you need the on_ready code to allow the  bot to load permissions in the channel first before it's able to edit the channel with price else it'll return None type
5. you need to ```self."function".start() to start the function immediately bot is activated eg to start the update price function etc


"""
