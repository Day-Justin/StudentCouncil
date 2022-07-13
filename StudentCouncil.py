# A moderate moderation Bot

import discord
from discord.ext import commands
import os
import random
import logging
import json


with open(os.path.dirname(__file__) + '/../config.json') as f:
    data = json.load(f)
    token = data["StudentCouncil"]["TOKEN"]
    prefix = data["StudentCouncil"]["PREFIX"]


'''
intents = discord.Intents.all()

client = discord.Client(intents=intents)
'''

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)


# Start each command with the @bot.command decorater
@bot.command()
async def square(ctx, arg):  # The name of the function is the name of the command
    print(arg)  # this is the text that follows the command
    await ctx.send(int(arg) ** 2)  # ctx.send sends text in chat


bot.run(token)

