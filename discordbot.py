#   Jay Patel

from __future__ import print_function
import discord
from discord.ext import commands
import asyncio
import mlbgame #api for game data
import datetime
import os

bot = commands.Bot(command_prefix='!', description='description here')
client = discord.Client()

@bot.command()
async def say(*,something):
    """ !say something, to echo something 
    """
    em = discord.Embed(title="!say",description=something, colour=discord.Colour(0xFFFFFF))
    await bot.say(embed=em)

@bot.group(pass_context=True)
async def scores(ctx): # working
    """ !scores or !scores team_name, for daily scores
    """
    if ctx.invoked_subcommand is None:
        today = datetime.datetime.now()
        games = mlbgame.day(today.year, today.month, today.day, home=None, away=None)
        #games = mlbgame.day(2018, 4, 4, home=None, away=None)    #used for testing specific date
        if not games:
            await bot.say("No games today")
        for game in games:
            await bot.say(game)

@scores.command(name="team") 
async def scores_team(*,team): # working
    team = team.title()
    today = datetime.datetime.now()
    games = mlbgame.day(today.year, today.month, today.day, home=team, away=team)
    #games = mlbgame.day(2018, 2, 23, home=team, away=team)    #used for testing
    if not games:
        await bot.say("No games today")
    for game in games:
        await bot.say(game)

@bot.command()
async def standings():   # not working
    """ !standings, not working atm 
    """
    today=datetime.datetime(2018, 2, 23, 0, 59, 6, 838799)
    #today = datetime.datetime.now()
    standings = standings(today)
    await bot.say(standings)


bot.run(os.getenv('TOKEN'))

# !scores
# !scores team *team name*
