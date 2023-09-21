import discord
from discord.ext import commands
import sqlite3
import asyncio
import time

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

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.collect_email(member)

    @commands.command(name='stop', description="To disable notifications from this bot.")
    async def stop(self, ctx):
        cur.execute("UPDATE Users SET last_notified=-1 WHERE user=?", (ctx.author.id,))
        ddln.commit()

    async def collect_email(self, member):
        def check(m):
            return m.author == member and isinstance(m.channel, discord.DMChannel)

        # Assign the restricted access role
        role = discord.utils.get(member.guild.roles, name="Restricted")
        if role is None:
            print("Role not found")
            return

        try:
            await member.add_roles(role)
        except (discord.NotFound, discord.Forbidden) as e:
            print(f"Error adding role: {e}")
            return

        try:
            await member.send('Hey! welcome to Dandelion! Kindly enter your email to stay updated:')
        except discord.HTTPException as e:
            if e.code == 50007:  # Cannot send messages to this user
            # Update a flag in the database or store it in memory
            # For our dandelion db
                cur.execute("UPDATE Users SET help_dms_enabled = 0 WHERE user = ?", (member.id,))
                ddln.commit()
            
            # Notify in a different channel or log the error
            error_channel = self.bot.get_channel(1066107466510774362)  # Replace with the ID of the channel 1034328239138689045 (#random ) on ddln
            await error_channel.send(f"Cannot send DM to {member.name}. Kindly dm the bot with your email address to stay updated. You can ignore if you do not wish to submit your email.")
        else:
            pass
            
            # return

        msg = await self.bot.wait_for('message', check=check)
        email = msg.content
        await member.send("Thank you! You're now allowed in the server.")
        
        # Insert the user's username and email into the Users table
        try:
            cur.execute("INSERT INTO Users (user, email, last_notified) VALUES (?, ?, ?)", (member.id, email, 0))
            ddln.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return

        # Assign the full access role and remove the restricted access role
        full_access_role = discord.utils.get(member.guild.roles, name="champion")
        if full_access_role is not None:
            try:
                await member.add_roles(full_access_role)
                await member.remove_roles(role)
            except (discord.NotFound, discord.Forbidden) as e:
                print(f"Error changing roles: {e}")
                return

        admin = self.bot.get_user(692834498102165594)  # Replace with dandelion admin's user ID 1108444934110978220
        await admin.send(f'Member: {member.name}, Email: {email}')
        
        print(f"Data stored successfully: Member: {member.name}, Email: {email}")

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

def setup(bot):
    bot.add_cog(EmailCollectorCog(bot))
