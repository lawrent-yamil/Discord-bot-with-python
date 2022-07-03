#Import libraries
import os
from discord.ext import commands
from dotenv import load_dotenv
import random

# Import Jokes
from jokes import JOKES_XD

load_dotenv()

#Token
TOKEN = os.getenv('DISCORD_TOkEN')

bot = commands.Bot(command_prefix='!') #Bot prefix

#add numbers
@bot.command(name='add', help='add two numbers')
async def sumar(ctx, num1: int, num2: int):
    try:
        await ctx.send(num1 + num2)
    except Exception:
        await ctx.send("cannot be added")

#Tell a random joke from the array CHISTES
@bot.command(name='joke', help='tell a random joke')
async def chiste(ctx):
    try:
        await ctx.send(random.choice(JOKES_XD))
    except IndexError:
        await ctx.send("No jokes")


#Run
bot.run(TOKEN)