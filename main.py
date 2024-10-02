import asyncio
from telethon import TelegramClient, events

# Replace with your own values
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'
TARGET_CHATS = []
MY_CHATS = []

bot = TelegramClient('anon', int(API_ID), API_HASH)

@bot.on(events.NewMessage(incoming=True, chats=TARGET_CHATS))
async def handler(event):
    msg = event.message
    for c in MY_CHATS:
        await asyncio.sleep(0.5)
        # Uncomment this line to send first line of text only
        # msg.message = msg.message.split('\n')[0]
        await bot.send_message(int(c), msg.message, formatting_entities=msg.entities)

with bot:
    print('\n• Bot has started!\n(Press Ctrl + C to stop.)')
    bot.run_until_disconnected()
