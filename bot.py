from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

from api_client import get_world_cup_matches
from leaderboard import build_leaderboard, format_leaderboard

load_dotenv()

bot_token = os.getenv("DISCORD_BOT_TOKEN")
football_token = os.getenv("FOOTBALL_DATA_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', intents=intents)

@bot.command()
async def lb(ctx):
    data = get_world_cup_matches(football_token)
    final_leaderboard = build_leaderboard(data["matches"])
    message = format_leaderboard(final_leaderboard)
    embed = discord.Embed(title="🏆  Leaderboard", description=message,colour=discord.Colour.gold())
    await ctx.send(embed=embed)

bot.run(bot_token)