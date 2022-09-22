import discord
import sys
import os
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_connect():
    print("Python version: ")
    print(sys.version)
    print(sys.version_info)
    print("Connected to the server!")

load_dotenv()
token = os.getenv("TOKEN")
client.run(token)
