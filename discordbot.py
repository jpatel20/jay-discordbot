#   Jay Patel

from __future__ import print_function
import discord
from discord.ext import commands
import asyncio
import mlbgame #api for game data
import datetime
import os
import re

bot = commands.Bot(command_prefix='!', description='description here')
client = discord.Client()

@bot.listen()
async def on_message(message):
    output = '<@'    
    if ":surspanka:" in message.content:
        output += os.getenv('HARSH_MENTION') '>'
        await bot.send_message(message.channel, output)        
    elif ":ivan:" in message.content:
        output += os.getenv('IVAN_MENTION') '>'
        await bot.send_message(message.channel, output)        
    elif ":sc4rface:" in message.content:
        output += os.getenv('BRANDON_MENTION') + '>'
        await bot.send_message(message.channel, output)

@bot.command()
async def say(*,something):
    """ !say something, to echo something 
    """
    em = discord.Embed(title="!say",description=something, colour=discord.Colour(0xFFFFFF))
    await bot.say(embed=em)

@bot.group(pass_context=True)
async def scores(ctx):
    """ !scores or !scores team_name, for daily scores
    """
    if ctx.invoked_subcommand is None:
        today = datetime.datetime.now()
        games = mlbgame.day(today.year, today.month, today.day, home=None, away=None)
        if not games:
            await bot.say("No games today")
        for game in games:
            await bot.say(game)

@scores.command(name="team") 
async def scores_team(*,team): 
    team = team.title()
    today = datetime.datetime.now()
    games = mlbgame.day(today.year, today.month, today.day, home=team, away=team)
    if not games:
        await bot.say("No games today")
    for game in games:
        await bot.say(game)

@bot.command()
async def emojify(*,something):
    """ !emojify something, to echo something with emoji letters/numbers
    """
    output = ""
    for i, c in enumerate(something):
        if c == "0":
            output += ":zero:"
        elif c == "1":
            output += ":one:"
        elif c == "2":
            output += ":two:"		
        elif c == "3":
            output += ":three:"
        elif c == "4":
            output += ":four:"
        elif c == "5":
            output += ":five:"
        elif c == "6":
            output += ":six:"
        elif c == "7":
            output += ":seven:"
        elif c == "8":
            output += ":eight:"
        elif c == "9":
            output += ":nine:"
        elif c == "?":
            output += ":grey_question:"
        elif c == "!":
            output += ":grey_exclamation:"
        elif c == " ":
            output += " "
        else:
            output +=":black_small_square:"
    await bot.say(output)

bot.run(os.getenv('TOKEN'))

# !scores
# !scores team *team name*
