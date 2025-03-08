import discord
from discord.ext import commands
from graph import HomiePointsGraph
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Enable member intents to access user information

bot = commands.Bot(command_prefix="!", intents=intents)
homie_points = HomiePointsGraph()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name="add_debt")
async def add_debt(ctx, from_user: discord.Member, to_user: discord.Member, points: int):
    """Add debt from one user to another."""
    homie_points.add_debt(from_user.id, to_user.id, points)
    await ctx.send(f"{from_user.mention} now owes {to_user.mention} {points} homie points.")

@bot.command(name="get_debt")
async def get_debt(ctx, from_user: discord.Member, to_user: discord.Member):
    """Check how much one user owes another."""
    debt = homie_points.get_debt(from_user.id, to_user.id)
    await ctx.send(f"{from_user.mention} owes {to_user.mention} {debt} homie points.")

@bot.command(name="total_debt")
async def total_debt(ctx, user: discord.Member):
    """Check how much a user owes in total."""
    total = homie_points.get_total_debt(user.id)
    await ctx.send(f"{user.mention} owes a total of {total} homie points.")

@bot.command(name="total_owed")
async def total_owed(ctx, user: discord.Member):
    """Check how much a user is owed in total."""
    total = homie_points.get_total_owed(user.id)
    await ctx.send(f"{user.mention} is owed a total of {total} homie points.")

@bot.command(name="show_all")
async def show_all(ctx):
    """Show all debts in the system."""
    await ctx.send(str(homie_points))

# Replace 'YOUR_BOT_TOKEN' with your bot's token
bot.run(TOKEN)