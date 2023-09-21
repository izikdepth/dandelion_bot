import discord
from discord.ext import commands
import logging





class Faq(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
        
    @discord.slash_command()
    async def whitepaper(self, ctx):
        message = "[Read our whitepaper](https://dandelionnet.io/wp-content/uploads/2022/09/dandelion_whitepaper.pdf)"
        await ctx.respond(message)
        
    @discord.slash_command()
    async def website(self, ctx):
        message = "[Website](https://dandelionnet.io/)"
        await ctx.respond(message)
    
    @discord.slash_command()
    async def community(self, ctx):
        message = ("[Reddit](https://www.reddit.com/user/Dandelion_Networks/)\n"
                   "[Telegram](https://t.me/+laYlUWRjDks1MWYx)\n"
                   "[Tiktok](https://www.tiktok.com/@ddln_networks)\n"
                   "[Linkedin](https://www.linkedin.com/company/dandelionnetworks/)\n"
                   "[Twitter](https://twitter.com/ddln_networks)\n"
                   "[Medium](https://dandelionnetworks.medium.com/)\n"
                   "[Youtube](https://www.youtube.com/channel/UCzS_dKW5Z0xJOnAGmA_2oXQ)"
                   )
        await ctx.respond(message)
    
    @discord.slash_command()
    async def node(self, ctx):
        message = "[#node-setup](https://discord.com/channels/1027371612875542588/1107803939283406878)"
        await ctx.respond(message)


    @discord.slash_command()
    async def exchanges(self, ctx):
        message = "[#exchanges](https://discord.com/channels/1027371612875542588/1108085988384841808)"
        await ctx.respond(message)
        
    @discord.slash_command()
    async def roadmap(self, ctx):
        message = ("Estimates:\n\n"
                   "Q3-Q4 2023 test nodes.\n"
                   "Q4 2023-Q1 2024 public nodes.\n"
                   "2024-2025 exchanges - tentatively txbit, tradeogre, mexc or kucoin \n"
                   "[more](https://discord.com/channels/1027371612875542588/1108085988384841808/1108086095528333383)")
        await ctx.respond(message)
        
    @discord.slash_command()
    async def help(self, ctx):
        message = ("Use the /help command to view all commands\n\n"
                   "1. /whitepaper - to view the whitepaper\n"
                   "2. /website - to view website\n"
                   "3. /community - for community links\n"
                   "4. /node - how to set up a node\n"
                   "5. /exchanges - centralized exchanges\n"
                   "6. /roadmap - to view the roadmap")
        await ctx.respond(message)
        
  

"""
set up bot and register the cog to the bot
"""
def setup(bot):
    bot.add_cog(Faq(bot))