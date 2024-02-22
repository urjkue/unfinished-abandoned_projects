import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

@bot.command()
@commands.has_role('Dante')  # Only users with the 'admin' role can use this command
async def msdm(ctx, *, message):
    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(message)
                print(f"DM sent to {member.name}")
            except discord.Forbidden:
                print(f"Unable to send DM to {member.name}")
    await ctx.send("Mass DM sent to all members.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the necessary role to use this command.")

# Replace 'YOUR_BOT_TOKEN' with your own Discord bot token
bot.run("")
