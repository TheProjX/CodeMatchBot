from aiogram import Bot, Dispatcher, executor, types
from config import *
from loguru import logger

# Инициализация бота и диспетчера
bot = Bot(token=token)
dp = Dispatcher(bot)


# /start & /help & Вызов главного меню
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Профиль")],
        [types.KeyboardButton(text="Заказать разработку")],
        [types.KeyboardButton(text="FAQ")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Меню")
    await message.answer("Тыры-пыры | туда-сюда -> Какая-то инфа", reply_markup=keyboard)


# Обработка профиля
@dp.message_handler(lambda message: message.text == "Профиль")
async def with_puree(message: types.Message):
    kb = [
        types.InlineKeyboardButton(
            text='Пополнить баланс',
            callback_data='balance_replenish'
        ),
        types.InlineKeyboardButton(
            text='Активные заказы',
            callback_data='active_orders'
        ),
        types.InlineKeyboardButton(
            text='Завершенные заказы',
            callback_data='finished_orders'
        ),
    ]

    try:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*kb)
        await message.answer(f"Ваш профиль: \n\nВаш баланс: 0₽", reply_markup=keyboard)
    except Exception as e:
        logger.error(f"Ошибка получения профиля -----> {e}")
        await message.reply(f"Ошибка получения профиля")


# Обработка FAQ
@dp.message_handler(lambda message: message.text == "FAQ")
async def without_puree(message: types.Message):
    kb = [
        types.InlineKeyboardButton(
            text='Разработчики',
            callback_data='choice'
        ),
        types.InlineKeyboardButton(
            text='Администрация',
            callback_data='choice'
        ),
        types.InlineKeyboardButton(
            text='Баланс',
            callback_data='choice'
        ),
    ]

    try:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        keyboard.add(*kb)
        await message.answer(f"FAQ: \n\n", reply_markup=keyboard)
    except Exception as e:
        logger.error(f"Ошибка получения FAQ -----> {e}")
        await message.reply(f"Ошибка получения FAQ")


# Создание нового заказа
@dp.message_handler(lambda message: message.text == "Заказать разработку")
async def with_puree(message: types.Message):
    kb = [
        types.InlineKeyboardButton(
            text='Бот',
            callback_data='cat_bot'
        ),
        types.InlineKeyboardButton(
            text='Скрипт',
            callback_data='cat_script'
        ),
        types.InlineKeyboardButton(
            text='Чекер',
            callback_data='cat_checker'
        ),
        types.InlineKeyboardButton(
            text='Регер',
            callback_data='cat_reger'
        ),
        types.InlineKeyboardButton(
            text='Сайт',
            callback_data='cat_site'
        ),
        types.InlineKeyboardButton(
            text='Парсер',
            callback_data='cat_parser'
        ),
    ]

    try:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        keyboard.add(*kb)
        await message.answer(f"Выберите категорию: \n\n", reply_markup=keyboard)
    except Exception as e:
        logger.error(f"Ошибка создания заказа -----> {e}")
        await message.reply(f"Ошибка создания заказа")

if __name__ == '__main__':
    try:
        logger.info("Проект запущен!")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота ------> {e}")
