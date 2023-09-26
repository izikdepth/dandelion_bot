# dandelion_bot
To run the bot, for the repo and put the bot token , admin id and channel id (for alerting members whose dm are closed) after that run ```python3 DDLN.py``` on linux or ```python DDLN.py``` on windows  to start the bot.
This bot is an faq bot that also receives emails from members of a discord and sends those emails to the dm of the admin of the project.
It checks every two weeks for members who haven't given their emails to the bot and ask them for it.
Members can use command "/stop" to stop receiving notifications to send emails.

##serverstats_example.py
the serverstats_example code is an example of how you can display the price of a coin/token over a discord channel.

##serverstats.py
is the code you'll use in a Cog to display the price/marketcap/hashrate of a coin /token over a  discord channel

##how to do?
To display the price of a token over a  channel in discord:
1. Add the bot to your discord server 
2. create a  discord voice channel and name it whatever you want
3. click on the channel's settings then click permission
4. in permissions, Allow memebers to "view channel", "send messages", and "read message history". feel free to not allow the rest of the permissions or ignore
5. Save changes
6. Right click on the channel you just created and copy channel id
7.  paste the channel id in self.channel_id = " your channel id". you can do this with as many channels as you want.
8. Done. test code
