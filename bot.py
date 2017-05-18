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
    if ("hello" in message.content or "hi" in message.content or "hey" in message.content or "hola" in message.content):
        yield from myBot.send_message(message.channel, "Hello, Hello?")
    yield from myBot.process_commands(message)

@myBot.command()
@asyncio.coroutine
def hello(*args):
    yield from myBot.say("Hello, world!")

@myBot.command()
@asyncio.coroutine
def notOntoKennen(*args):
    yield from myBot.say("You're not onto Kennen :)")

myBot.run("MzE0NTI0NTk0MjA1NjIyMjc0.C_5eKQ.bt2Tqhs_1sGSroG8zHTI2TfT-ko")
