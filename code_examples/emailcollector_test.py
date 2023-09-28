import discord
from discord.ext import commands
import sqlite3
import asyncio
import time
import os
from dotenv import load_dotenv
import re
import csv
import yagmail



load_dotenv()

# Get email address and password from environment variables
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('SOFTWARE_PASSWORD')

#register your email 
yagmail.register(email_address, email_password)
yag = yagmail.SMTP(email_address, email_password)


# Set database & ddln stands for dandelion so ddln database
ddln = sqlite3.connect("dandelion.db")

# Execute statements and fetch results
cur = ddln.cursor()

# Create table for data
cur.execute("CREATE TABLE IF NOT EXISTS Users(user INTEGER, email TEXT, last_notified INTEGER, help_dms_enabled INTEGER DEFAULT 1)")

class EmailCollectorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.check_email_notifications())
        self.bot.loop.create_task(self.check_email_notifications())
        self.bot.loop.create_task(self.send_collected_emails())

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.collect_email(member)

    @commands.command(name='stop', description="To disable notifications from this bot.")
    async def stop(self, ctx):
        cur.execute("UPDATE Users SET last_notified=-1 WHERE user=?", (ctx.author.id,))
        ddln.commit()

    async def is_valid_email(self, email):
        email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        return bool(re.search(email_regex, email))

    async def collect_email(self, member):
        def check(m):
            return m.author == member and isinstance(m.channel, discord.DMChannel)

        try:
            await member.send('Hey! Welcome to Dandelion! If you wish, you can enter your email to stay updated:')
        except discord.HTTPException as e:
            if e.code == 50007:  # Cannot send messages to this user
                cur.execute("UPDATE Users SET help_dms_enabled = 0 WHERE user = ?", (member.id,))
                ddln.commit()

                # Notify in a different channel or log the error
                error_channel = self.bot.get_channel('channel id')  # Replace with the ID of the channel you'll like to log errors in
                await error_channel.send(f"Cannot send DM to {member.name}. Kindly dm the bot with your email address to stay updated. You can ignore if you do not wish to submit your email.")
        else:
            pass

        while True:
            msg = await self.bot.wait_for('message', check=check)
            email = msg.content

        # Check if the email address is valid
            if not email or await self.is_valid_email(email):
                break
            else:
                try:
                    await member.send("The email address you've entered is invalid. Please enter a valid email address.")
                except discord.HTTPException as e:
                    if e.code == 50007:  # Cannot send messages to this user
                        break

        if email:
            try:
                await member.send("Thank you! Your email has been saved in our database")
            except discord.HTTPException as e:
                if e.code == 50007:  # Cannot send messages to this user
                    pass

    #         # Insert the user's username and email into the Users table
            # try:
            #     cur.execute("INSERT INTO Users (user, email, last_notified) VALUES (?, ?, ?)", (member.id, email, 0))
            #     ddln.commit()
            # except sqlite3.Error as e:
            #     print(f"Database error: {e}")
            #     return

            admin = self.bot.get_user('admin discord')  
            await admin.send(f'Member: {member.name}, Email: {email}')
        
            # print(f"Data stored successfully: Member: {member.name}, Email: {email}")
    



    async def check_email_notifications(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            for guild in self.bot.guilds:
                for member in guild.members:
                    row = cur.execute("SELECT * FROM Users WHERE user=?", (member.id,)).fetchone()
                    if row is None:
                        await self.collect_email(member)
                    elif row[2] == -1:
                        continue
            await asyncio.sleep(1209600)  # Check every two weeks


    async def send_collected_emails():
        while True:
            # Fetch all emails from the Users table
            rows = cur.execute("SELECT email FROM Users").fetchall()

            # If no emails were collected, skip this iteration
            if not rows:
                await asyncio.sleep(60)  # Wait for 1 minute before checking again
                continue

            # Convert the data to a list of email addresses
            email_list = [row[0] for row in rows]
            email_list_str = ', '.join(email_list)

            try:
                # Email server setup
                yag = yagmail.SMTP(email_address, email_password)

                # Send email with the list of collected emails
                yag.send(
                    to='receiving-email@gmail.com',
                    subject='Discord Bot Email - Collected Emails',
                    contents=f'NEW EMAILS COLLECTED ALERT: {email_list_str}'
                )
                print("Email sent!")

            except yagmail.SMTPException as e:
                print(f"SMTP Exception: {e}")
            except yagmail.SMTPAuthenticationError as e:
                print(f"SMTP Authentication Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

            await asyncio.sleep(60)  # Wait for 1 minute before sending the next email

    asyncio.run(send_collected_emails())


            
def setup(bot):
    bot.add_cog(EmailCollectorCog(bot))
