import discord
import dotenv
import os
from playsound import playsound

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents = intents)

@bot.event
async def on_message(message):
    playsound("alert.mp3", False)
    print(message.author.name)
    print(message.content)
    print("\n")
    with open("log.txt", "a") as log:
        log.write(message.author.name)
        log.write("\n")
        log.write(message.content)
        log.write("\n\n")

@bot.event
async def on_ready():
    print(f"{bot.user} is online.")

bot.run(os.getenv('NOTIFY_TOKEN'))
