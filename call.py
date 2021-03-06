import discord, asyncio, aiohttp, json
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

with open("config.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]), case_insensitive=True)

@bot.event
async def on_ready():
    print("=========\nReady for use!\n=========\nBot created by TnyavnTo")

@commands.cooldown(1, int(config["callCoolDown"]), BucketType.user)
@bot.command()
async def call(ctx, *, message):
    if len(message) <= 300:
        report = {}
        report["value1"] = f"New message. {message}"
        report["value2"] = f". Sent by {ctx.author.name} on the server {ctx.guild.name}."
        async with aiohttp.ClientSession() as session:
            await session.post(f"https://maker.ifttt.com/trigger/{config['eventName']}/with/key/{config['IFTTTkey']}", data=report)
        await ctx.send("**Data posted! Calling the bot owner now.**")
        print("Data recieved!")
    else:
        await ctx.send(f"**{ctx.author.mention} You can't send messages over 300 chars long. :no_entry:**")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"**:no_entry: {error}**")

if __name__ == '__main__':
    bot.run(config["discordToken"])
