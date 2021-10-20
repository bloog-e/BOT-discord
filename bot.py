# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    for server in bot.guilds:
        if server.name == GUILD:
            break
    bot_des = str(bot.user.discriminator)
    bot_id = str(bot.user.id)
    bot_name = str(bot.user.name)
    print(
        f'{bot.user} is connected to the following guild:\n',
        f'{bot.user} id : {bot_id}\n',
        f'{server.name}  (id: {server.id})\n'
        f'avatar url : {str(bot.user.avatar_url)}'
    )
    
    members = '\n - '.join([member.name for member in server.members])
    print(f'Server Members:\n - {members}')

bot.run(TOKEN)