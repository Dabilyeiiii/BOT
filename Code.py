from aiogram import Dispatcher, Bot, types, executor
from Text import *
from Kb import *


bot = Bot(token='6645578412:AAGVgkJp0srxnj4r4VfFLVfXUm1BQUl2B4g')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def StartCmd(msg: types.Message):
    await msg.answer(text=START_TEXT, reply_markup=StartKb)


@dp.message_handler(commands='help')
async def HelpCmd(msg: types.Message):
    await msg.answer(text=HELP_TEXT)


@dp.message_handler(commands='info')
async def InfoCmd(msg: types.Message):
    await msg.answer(text=INFO_TEXT)


@dp.message_handler(commands='author')
async def AuthorCmd(msg: types.Message):
    await msg.answer(text=AUTHOR_TEXT)


@dp.message_handler(text='Консультация')
async def Consult1(msg: types.Message):
    await msg.answer(text='Какой в данный момент у вас цвет волос?', reply_markup=ColorHairKb)


@dp.message_handler(text= ['Блонд', 'Черный', 'Рыжий (натурал.)', 'Рыжий (ненатурал.)', 'Руссый'])
async def Consulr2(msg: types.Message):
    await msg.answer(text='Делали вы милирование, смывку, завивку ближайшие месяца?', reply_markup=EmKb)


@dp.message_handler(text=['Да, делал(а)', 'Нет, не делал(а)'])
async def Consult3(msg: types.Message):
    await msg.answer(text='Какова длина ваших волос?', reply_markup=LenKb)


@dp.message_handler(text=['До плеч', 'До лопаток', 'Ниже лопаток', 'До До талии'])
async def Consult4(msg: types.Message):
    await msg.answer(text=END_OF_CONSULT)


@dp.message_handler(text='Прайс-лист')
async def PriceList(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id, photo=types.InputFile(path_or_bytesio='PHOTO/ExBlack.jpg'))
    await bot.send_photo(chat_id=msg.from_user.id, photo=types.InputFile(path_or_bytesio='PHOTO/HOkrash.jpg'))
    await bot.send_photo(chat_id=msg.from_user.id, photo=types.InputFile(path_or_bytesio='PHOTO/Strishka.jpg'))
    await bot.send_photo(chat_id=msg.from_user.id, photo=types.InputFile(path_or_bytesio='PHOTO/Ton.jpg'))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)