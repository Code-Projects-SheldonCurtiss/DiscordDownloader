
import discord
import difflib
import yaml
from discord.ext import commands
import re
import random
import time
import os
import hashlib
import asyncio
import requests

# This is ghetto but before I started using that config module and I'm lazy, ensure your token is on the first line.
dirpath = os.getcwd()
tokenfile = open(dirpath + '\\code\\token.txt', 'r')
tokens = tokenfile.readlines()
token = tokens[0]
token = token.replace('\n', '')

master = discord.Client(fetch_offline_users=False)

loop = asyncio.new_event_loop()

print('Connecting to discord')
master = discord.Client(loop=loop)

@master.event
async def on_connect():
    print('\nConnected\n')
    while 1 == 1:
        print('\nPlease input the Channel ID you want to save from\n')
        selection = input('')
        try:
            selection = int(selection)
        except:
            print('Should be a number!')

        for each in master.guilds:
            for channel in each.channels:
                if channel.id == selection:


                    print('\nSaving!\n')
                    amount = 0
                    async for message in channel.history(limit=None):
                        try:
                            os.mkdir('./' + str(channel.id))
                        except:
                            fug = 1


                        for attachment in message.attachments:
                            await attachment.save(dirpath + '\\' + str(channel.id) + '\\' + attachment.filename)
                            amount = amount + 1
                            print('Saving ' + str(amount))

                    print('Done!')

master.run(token, bot=False)