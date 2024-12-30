import discord

TOKEN = ""

intents = discord.Intents.defaut()
intents.members = True
intents.message_content = True

activity = discord.CustomActivity(
    "Your custom Message. (line 10, main.py)"
)

bot = discord.Bot(
    intents=intents,
    activity=activity,
    debug_guilds=None
)

async def setup():
    bot.load_extension("cogs.")

@bot.event
async def on_ready():
    print("The bot is running!")
    setup()


if TOKEN == "":
    bot.run(TOKEN)
else:
    print("Please enter a valid Token! Line 3, main.py")