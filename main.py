import os
import disnake
from disnake.ext import commands
from datetime import datetime


intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# for cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print("Bot ready!")

# Logging joint on server
@bot.event
async def on_member_join(member):
    chnljoin = bot.get_channel(1370428575722897419)
    await chnljoin.send(f"{member.mention} присоеденился на сервер! \nЭто уже {member.guild.member_count} участник.")

# Logging exit from server
@bot.event
async def on_member_remove(member):
    chnlExit = bot.get_channel(1383224073345171476)
    await chnlExit.send(f"{member.mention} покинул наш сервер! \nЭто был {member.guild.member_count} участник.")

#token
bot.run("token")
