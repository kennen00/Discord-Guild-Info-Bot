import discord
from discord.ext.commands import Bot

import aiohttp
import asyncio
import websockets

myBot = Bot(command_prefix="!")

@myBot.event
@asyncio.coroutine
def on_read():
    print("Client logged in")

@myBot.event
@asyncio.coroutine
def on_message(message):
    if (message.channel.id == "314867907739910165"):
        if ("hello" in message.content):
            yield from myBot.send_message(myBot.get_channel("314867907739910165"), "Hello, Hello?")
        elif ("purpose" in message.content):
            yield from myBot.send_message(myBot.get_channel("314867907739910165"), "Did you say Purpose? HA! I'd tell you what it is if it was in my database!!")
    yield from myBot.process_commands(message)

@myBot.command()
@asyncio.coroutine
def hello(*args):
    yield from myBot.say("Hello, world!")

myBot.run("MzE0NTI0NTk0MjA1NjIyMjc0.C_5eKQ.bt2Tqhs_1sGSroG8zHTI2TfT-ko")
