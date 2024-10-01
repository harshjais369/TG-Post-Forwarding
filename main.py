import asyncio
from telethon import TelegramClient, events

# Replace with your own values
API_ID = 0
API_HASH = ''
TARGET_CHATS = []
MY_CHATS = []

bot = TelegramClient('anon', API_ID, API_HASH)

@bot.on(events.NewMessage(incoming=True, chats=TARGET_CHATS))
async def handler(event):
    msg = event.message
    for c in MY_CHATS:
        await asyncio.sleep(0.5)
        await bot.send_message(int(c), msg.message, formatting_entities=msg.entities)

with bot:
    bot.run_until_disconnected()
