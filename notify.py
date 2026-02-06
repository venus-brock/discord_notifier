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
    ts = re.findall("<t:[0-9]+.?>", message.content)
    for line in ts:
        output += "\n" + line
        re.sub("[^0-9]", "", line)
        output += "\n" + datetime.utcfromtimestamp(int(line)).strftime("%Y-%m-%d %H:%M:%S")
    print(output)
    print("\n")
    with open("log.txt", "a") as log:
        log.write(output)
        log.write("\n\n")

@bot.event
async def on_ready():
    print(f"{bot.user} is online.")

bot.run(os.getenv('NOTIFY_TOKEN'))
