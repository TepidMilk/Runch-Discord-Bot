import discord
from discord.ext import commands
from graph import HomiePointsGraph
import os
from dotenv import load_dotenv
from storage import load_graph, save_graph

load_dotenv(".env")
TOKEN: str = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True # Enable member intents to access user information

bot = commands.Bot(command_prefix="!", intents=intents)
homie_points = load_graph()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'Members Intent: {intents.members}')
    print(f'Message Content Intent: {intents.message_content}')

@bot.command(name="add_debt")
async def add_debt(ctx, from_user: discord.Member, to_user: discord.Member, points: int):
    """Add debt from one user to another."""
    homie_points.add_debt(from_user.id, to_user.id, points)
    await ctx.send(f"{from_user.mention} now owes {to_user.mention} {points} homie points.")
    save_graph(homie_points)

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

@bot.command(name="settle_debt")
async def settle_debt(ctx, from_user: discord.Member, to_user:discord.Member):
    homie_points.settle_debt(from_user.id, to_user.id, points=0)
    message = await ctx.send(f"{from_user.mention} has settled their debt with {to_user.mention}.")
    shake = "🤝"
    await message.add_reaction(shake)
    save_graph(homie_points)


@bot.command(name="show_all")
async def show_all(ctx):
    """Show all debts in the system."""
    await ctx.send(str(homie_points))

@bot.event
async def on_disconnect():
    save_graph(homie_points)
    print("Graph saved.")

# Replace 'YOUR_BOT_TOKEN' with your bot's token
bot.run(TOKEN)