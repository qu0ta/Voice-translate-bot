from aiogram import Dispatcher, Bot, executor
from aiogram.types import Message
from dotenv import dotenv_values
from utils import get_file_name, get_mp3_file

config = dotenv_values('config.env')
token = config['TOKEN']
bot = Bot(token=token)
dp = Dispatcher(bot)


async def start(_):
	print('=== БОТ ЗАПУЩЕН ===')


@dp.message_handler(commands='start')
async def wait_for_message(msg: Message):
	await msg.answer('Отправь мне текст для перевода в аудио!')


@dp.message_handler()
async def take_text(msg: Message):
	text = msg.text
	language = 'RU'
	file_name = get_file_name()
	get_mp3_file(file_name, text, language)
	await bot.send_audio(msg.from_user.id, audio=open(file_name, 'rb'))


if __name__ == '__main__':
	executor.start_polling(dp, on_startup=start)
