import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types

#объект бота
bot = Bot(token="5580797422:AAGRo_rzDDxcdEVb2AQkLzqWcWDhmOpj4qQ")
#Диспетчер бота
dp = Dispatcher(bot)
#Включение логирования, чтобы не пропустить важные сообщения?
logging.basicConfig(level=logging.INFO)

#Хэндлер на команду /test1

@dp.message_handler(commands = "start")
async def test1(message: types.Message):
    await message.reply("кто прочитал тот умер")

@dp.message_handler(commands='help')
async def test2(message: types.Message):
    await message.reply('кто прочитал тот воскрес')

if __name__ == "__main__":
        #запуск бота
    executor.start_polling(dp, skip_updates=True)


