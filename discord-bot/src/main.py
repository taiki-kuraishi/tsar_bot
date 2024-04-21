"""
this is discord.py sample code
"""

import os

import discord
from discord.message import Message

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready() -> None:
        """
        This function is called when the bot is ready to start sending messages
        """
        print(f"We have logged in as {client.user}")

    @client.event
    async def on_message(message: Message) -> None:
        """
        This function is called when the bot receives a message
        """
        if message.author == client.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")

    token = os.environ["DISCORD_BOT_TOKEN"]
    client.run(token)
