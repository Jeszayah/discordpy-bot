# This example requires the 'message_content' privileged intents
import os
import discord
from discord.ext import commands

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='!', 
    intents=intents, 
    status=discord.Status.idle, 
    activity=discord.CustomActivity(name="with xen")
)










@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")


bot.run(os.environ["DISCORD_TOKEN"])
