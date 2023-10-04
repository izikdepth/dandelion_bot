import discord
from discord.ext import commands, tasks
import sqlite3
import asyncio
import time
import os
from dotenv import load_dotenv
import re
# import csv
import yagmail
from keyrings.alt.file import EncryptedKeyring

load_dotenv()

# Get email address and password from environment variables
email_address = os.getenv('GMAIL_ADDRESS')
"""
Note that the password is not your normal google password. he's a link to a video on how to get this password.
https://youtu.be/nuD6qNAurVM?si=BXpO8w50PcxM6Gn3 (video is in hindi, fairly easy to understand what he's doing in the video, its the only 
tutorial i could find. i had to use subtitles kek)
"""
email_password = os.getenv('GMAIL_PASSWORD') 

# Create an instance of EncryptedKeyring
keyring = EncryptedKeyring()

# Set the password
service_id = 'google'
user_id = email_address
password =  email_password

# Ensure the password is a string ie convert to string if password is not a string
if isinstance(password, bytes):
    password = password.decode('utf-8')


keyring.set_password(service_id, user_id, password)
email_password = keyring.get_password(service_id, user_id)

# Register your email
yagmail.register(email_address, email_password)
yag = yagmail.SMTP(email_address, email_password)

# Set database & ddln stands for dandelion so ddln database
ddln = sqlite3.connect("dandelion.db")

# Execute statements and fetch results
cur = ddln.cursor()

# Create table for data
cur.execute("CREATE TABLE IF NOT EXISTS Users(user INTEGER, email TEXT, last_notified INTEGER, help_dms_enabled INTEGER DEFAULT 1)")

# Add email_sent column if it doesn't exist
cur.execute("PRAGMA table_info(Users)")
columns = cur.fetchall()
if not any(column[1] == 'email_sent' for column in columns):
    cur.execute("ALTER TABLE Users ADD COLUMN email_sent INTEGER DEFAULT 0")

# Commit the changes
ddln.commit()

class EmailCollectorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.send_collected_emails.start()

        # Fetch all emails from the Users table that haven't been sent yet
        self.rows = cur.execute("SELECT email FROM Users WHERE email_sent = 0").fetchall()

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
                # error_channel = self.bot.get_channel(1158037278929723493)  # Replace with the ID of the channel that'll alert users here
                # await error_channel.send(f"Cannot send DM to {member.name}. Kindly dm the bot with your email address to stay updated. You can ignore if you do not wish to submit your email.")
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
                    await member.send("The email address you've entered is invalid. Please enter a valid email address:")
                except discord.HTTPException as e:
                    if e.code == 50007:  # Cannot send messages to this user
                        break

        if email:
            try:
                await member.send("Thank you! Your email has been saved in our database")
            except discord.HTTPException as e:
                if e.code == 50007:  # Cannot send messages to this user
                    pass

            # Insert the user's username and email into the Users table
            try:
                cur.execute("INSERT INTO Users (user, email, last_notified, email_sent) VALUES (?, ?, ?, 0)", (member.id, email, 0))
                ddln.commit()
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return

            admin = self.bot.get_user(1108444934110978220)  # Replace with dandelion admin's user ID 1108444934110978220
            await admin.send(f'Member: {member.name}, Email: {email}')

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

    async def notify_admin(self, error):
        admin_id = 692834498102165594 # Replace with the actual admin's user ID that'll receive the error messages
        admin = self.bot.get_user(admin_id)
        if admin:
            await admin.send(f"An error occurred: {error}")
        else:
            print(f"Admin not found: {admin_id}")

    @tasks.loop(hours=24)  # Update every day
    async def send_collected_emails(self):
        # print("Debug: send_collected_emails started")  # Debug print to indicate the start of the task

        # Fetch all emails from the Users table that haven't been sent yet
        rows = cur.execute("SELECT email FROM Users WHERE email_sent = 0").fetchall()

        # print("Debug: Fetched rows from the database")  # Debug print to indicate the database fetch

        # If no emails were collected, skip this iteration
        if not rows:
            # print("Debug: No emails to send, skipping")  # Debug print for the no-email case
            return

        # Convert the data to a list of email addresses
        email_list = [row[0] for row in rows]
        email_list_str = ', '.join(email_list)

        receiving_emails = ["community@dandelionnet.com","irene@dandelionnet.io","kassiedwarika@gmail.com",
                            "jason.xu@dandelionnet.com", "paul.chafe@dandelionnet.com"]

        # print(f"Debug: Email addresses to send: {email_list_str}")  # Debug print to show the email addresses

        try:
            # Email server setup
            # print("Debug: Setting up email server")  # Debug print for email server setup
            yag = yagmail.SMTP(email_address, email_password)

            # Send email with the list of collected emails
            # print("Debug: Sending email")  # Debug print to indicate email sending
            yag.send(
                to=receiving_emails, #email addresses that'll be receiving collected mails .email or whatever
                subject='Collected Emails From Dandelion Bot',
                contents=f'NEW EMAILS COLLECTED ALERT: {email_list_str}'
            )
            # print("Debug: Email sent!")

            # Update the email_sent column for the users whose emails have been sent
            # print("Debug: Updating database for sent emails")  # Debug print for database update
            for email in email_list:
                cur.execute("UPDATE Users SET email_sent = 1 WHERE email = ?", (email,))
            ddln.commit()

        except Exception as e:
            print(f"Error: {e}")
            # Log the error
            with open('error_log.txt', 'a') as f:
                f.write(f"General Error at {time.ctime()}: {e}\n")
            # Notify the admin about the error
            await self.notify_admin(e)


        # except yagmail.SMTPAuthenticationError as e:
        #     print(f"SMTP Authentication Error: {e}")
        #     # Log the error
        #     with open('error_log.txt', 'a') as f:
        #         f.write(f"SMTP Authentication Error at {time.ctime()}: {e}\n")
        #     #to notify the admin about the errors that occured
        #     await self.notify_admin(e)

        # except Exception as e:
        #     print(f"Error: {e}")
        #     # Log the error
        #     with open('error_log.txt', 'a') as f:
        #         f.write(f"General Error at {time.ctime()}: {e}\n")
        #     #to notify the admin about the errors
        #     await self.notify_admin(e)

        # print("Debug: send_collected_emails completed")  # Debug print to indicate the end of the task


            
def setup(bot):
    bot.add_cog(EmailCollectorCog(bot))
