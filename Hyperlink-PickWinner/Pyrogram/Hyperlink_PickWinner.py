# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/O_okarma
# PROVIDED BY https://t.me/ProjectCodeX
# ➥ /pickwinner <participant1> <participant2> ... : Picks a random winner from the provided list of participants.
# ➥ /hyperlink <text> <link> : Creates a markdown hyperlink with the provided text and link.


import random
import re

from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import CallbackQuery

from REPO import app


# Define the command handler for the "/pickwinner" command
@app.on_message(filters.command("pickwinner"))
async def pick_winner(_, message):
    # Get the list of participants
    participants = message.text.split()[1:]

    if participants:
        # Select a random winner
        winner = random.choice(participants)

        # Send the winner as a reply
        await message.reply_text(f"🎉 The winner is: {winner}")
    else:
        # If no participants are provided
        await message.reply_text("Please provide a list of participants.")


@app.on_message(filters.command("hyperlink"))
async def hyperlink_command(client, message):
    """Process the /hyperlink command."""
    args = message.text.split()[1:]
    if len(args) >= 2:
        text = " ".join(args[:-1])
        link = args[-1]
        hyperlink = f"[{text}]({link})"
        await client.send_message(
            chat_id=message.chat.id,
            text=hyperlink,
            disable_web_page_preview=True,
            parse_mode=ParseMode.MARKDOWN,
        )
    else:
        match = re.search(r"/hyperlink ([^\s]+) (.+)", message.text)
        if match:
            text = match.group(1)
            link = match.group(2)
            hyperlink = f"[{text}]({link})"
            await client.send_message(
                chat_id=message.chat.id,
                text=hyperlink,
                disable_web_page_preview=True,
                parse_mode=ParseMode.MARKDOWN,
            )
        else:
            await client.send_message(
                chat_id=message.chat.id,
                text="❌ Invalid format! Please use the format: /hyperlink <text> <link>.",
            )