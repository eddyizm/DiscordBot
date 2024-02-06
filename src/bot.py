import os
import discord

from dotenv import load_dotenv

import logging as log
from logging.handlers import RotatingFileHandler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
LOG_FILE = os.getenv('LOG_FILE')
LOG_LEVEL = os.getenv('LOG_LEVEL')

log_handler = RotatingFileHandler(LOG_FILE, mode='a',
                                  maxBytes=5 * 1024 * 1024,
                                  backupCount=5, encoding=None, delay=0)
handlers = [log_handler, log.StreamHandler()]
log.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', handlers=handlers, level=LOG_LEVEL)

_intents = discord.Intents.default()
client = discord.Client(intents=_intents)

@client.event
async def on_ready():
    log.info(f'{client.user.name} has successfully connected to discord.')

client.run(TOKEN)
