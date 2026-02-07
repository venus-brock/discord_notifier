from datetime import datetime
import discord
import dotenv
import os
from playsound import playsound
import re

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents = intents)

@bot.event
async def on_message(message):
    playsound("alert.mp3", False)
    output = message.author.name + "\n" + message.content
    ts = re.findall("<t:[0-9]+:.?>", message.content)
    for line in ts:
        output += "\n" + line
        num = re.sub("[^0-9]", "", line)
        output += " = " + datetime.utcfromtimestamp(int(num)).strftime("%Y-%m-%d %H:%M:%S")
    output += "\n"
    print(output)
    with open("log.txt", "a") as log:
        log.write(output)
        log.write("\n")

@bot.event
async def on_ready():
    print(f"{bot.user} is online.")

bot.run(os.getenv('NOTIFY_TOKEN'))
