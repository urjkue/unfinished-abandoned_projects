import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

@bot.command()
async def dm(ctx, *, message):
    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(message)
                print(f"DM sent to {member.name}")
            except discord.Forbidden:
                print(f"Unable to send DM to {member.name}")
    await ctx.send("Mass DM sent to all members.")

@bot.command()
async def hi(ctx):
    await ctx.send("Hi!")




bot.run('NzMyOTY5MzM0MjA4NTkzOTMz.Gzf1zH.WmsSLJ_2l3Cf09yt4dKQTqLjqPQOkS3Myp_ATc')
