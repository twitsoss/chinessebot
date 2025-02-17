import logging
import time

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from db import init_db, get_user_role, add_user_to_db

logging.basicConfig(level=logging.INFO)

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = 'YOUR TOKEN HERE'

# init bot
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
init_db()

# Keyboard create
def create_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="AL工具箱"),
        types.KeyboardButton(text="购买卡密")
    )
    builder.row(
        types.KeyboardButton(text="激活卡密"),
        types.KeyboardButton(text="获取帮助？")
    )
    builder.row(
        types.KeyboardButton(text="公告新闻"),
        types.KeyboardButton(text="赞助合作")
    )
    builder.row(
        types.KeyboardButton(text="会员中心")
    )
    return builder.as_markup(resize_keyboard=True)

# command /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Отправляем приветственное сообщение с клавиатурой
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    created_time = int(time.time())



    role = get_user_role(telegram_id)
    if role is None:
        add_user_to_db(telegram_id,username,first_name,last_name,created_time,created_time,created_time,'your method for inv link,','default','default',0,0,'0',0,0,0,0,0)
    await message.answer(f'Твоя роль - {role}')
    await message.answer("Привет! Выберите действие:", reply_markup=create_keyboard())

# Обработчик для кнопки "AL工具箱"
@dp.message(lambda message: message.text == "AL工具箱")
async def handle_al_toolbox(message: types.Message):
    await message.answer("Вы нажали кнопку 'AL工具箱'. Это заглушка.")

# Обработчик для кнопки "购买卡密"
@dp.message(lambda message: message.text == "购买卡密")
async def handle_buy_key(message: types.Message):
    await message.answer("Вы нажали кнопку '购买卡密'. Это заглушка.")

# Обработчик для кнопки "激活卡密"
@dp.message(lambda message: message.text == "激活卡密")
async def handle_activate_key(message: types.Message):
    await message.answer("Вы нажали кнопку '激活卡密'. Это заглушка.")

# Обработчик для кнопки "获取帮助？"
@dp.message(lambda message: message.text == "获取帮助？")
async def handle_get_help(message: types.Message):
    await message.answer("Вы нажали кнопку '获取帮助？'. Это заглушка.")

# Обработчик для кнопки "公告新闻"
@dp.message(lambda message: message.text == "公告新闻")
async def handle_news(message: types.Message):
    await message.answer("Вы нажали кнопку '公告新闻'. Это заглушка.")

# Обработчик для кнопки "赞助合作"
@dp.message(lambda message: message.text == "赞助合作")
async def handle_sponsor(message: types.Message):
    await message.answer("Вы нажали кнопку '赞助合作'. Это заглушка.")

# Обработчик для кнопки "会员中心"
@dp.message(lambda message: message.text == "会员中心")
async def handle_member_center(message: types.Message):
    await message.answer("Вы нажали кнопку '会员中心'. Это заглушка.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())