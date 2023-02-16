from telegram import Bot
import os

# Get environment variables
TOKEN = os.environ.get('TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

async def enviar_mensagem(msg:str):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=msg)