#   Jay Patel

import os
from __future__ import print_function
import discord
from discord.ext import commands
import asyncio
import mlbgame #api for game data
import datetime

bot = commands.Bot(command_prefix='!', description='description here')
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@bot.command()
async def say(*,something):
    em = discord.Embed(title=None,description=something)
    await bot.say(embed=em)

@bot.group(pass_context=True)
async def scores(ctx): # working
    if ctx.invoked_subcommand is None:
        today = datetime.datetime.now()
        games = mlbgame.day(today.year, today.month, today.day, home=None, away=None)
        #games = mlbgame.day(2018, 4, 4, home=None, away=None)    #used for testing specific date
        for game in games:
            await bot.say(game)

@scores.command(name="team") 
async def scores_team(*,team): # working
    team = team.title()
    today = datetime.datetime.now()
    #games = mlbgame.day(today.year, today.month, today.day, home=None, away=None)
    games = mlbgame.day(2018, 4, 4, home=team, away=team)    #used for testing 
    for game in games:
        await bot.say(game)

@bot.command()
async def standings():   # not working
    today=datetime.datetime(2017, 10, 6, 0, 59, 6, 838799)
    #today = datetime.datetime.now()
    standings = standings(today)
    await bot.say(standings)


bot.run(os.getenv('TOKEN'))

# !scores
# !scores team *team name*