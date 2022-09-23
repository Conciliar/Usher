import discord
import sys
import os
from dataclass import dataclass
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_connect():
    print("Python version: ")
    print(sys.version)
    print(sys.version_info)
    print("Connected to the server!")

class QuotesException(Exception):
    pass

@dataclass
class Poll:
    poll_question: str
    poll_choices: List[str]

    @classmethod
    def input_message(cls, poll_message):
        #Ideally we need a pair of quotes for every poll choice.
        #So we make sure that the number of quotes is even.
        #If it's not, we throw an exception.
        quotes_count = poll_message.count('"')
        if quotes_count == 0 or quotes_count % 2 != 0:
            raise QuotesException("Make sure you use a pair of quotes for each choice!")

load_dotenv()
token = os.getenv("TOKEN")
client.run(token)
