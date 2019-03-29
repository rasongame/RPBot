import logging 
from aiogram import Bot, Dispatcher, executor, types, utils
from aiogram.utils import exceptions
import config
import asyncio
logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
bot = Bot(token=config.API_TOKEN,loop=loop, proxy=config.PROXY_URL,proxy_auth=config.PROXY_AUTH)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start_Message(message: types.Message):
    await bot.send_message(message.from_user.id, "/me чищу стол \n /do На улице необычайно красиво \n Это примеры")
@dp.message_handler(commands=['me'])
async def me_Message(message: types.Message):
    await bot.send_message(message.chat.id,f"{message.from_user.first_name} {message.get_args()}")
    await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(commands=['do'])
async def do_Message(message: types.Message):
    try:
        await bot.send_message(message.chat.id,f"{message.get_args()}")
    except exceptions.MessageTextIsEmpty:
        print("crashing bu")

    
    await bot.delete_message(message.chat.id, message.message_id)
@dp.message_handler(commands=['f'])
async def f_Message(message: types.Message):
    await bot.send_message(message.chat.id, f"{message.from_user.first_name} pressed F to pay respect.")
    await bot.delete_message(message.chat.id,message.message_id)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)