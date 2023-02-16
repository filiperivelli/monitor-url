from telegram import Bot

TOKEN = '6211504952:AAF8iflnUWQOXHPpDTTu9BFOCbAxeQxuR00'
CHAT_ID = '-1001868103348'

async def enviar_mensagem(msg:str):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=msg)