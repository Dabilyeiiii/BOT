from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


StartKb = ReplyKeyboardMarkup(resize_keyboard=True)

StartKbB1 = KeyboardButton('Консультация')
StartKbB2 = KeyboardButton('Прайс-лист')

StartKb.add(StartKbB2, StartKbB1)


ColorHairKb = ReplyKeyboardMarkup(resize_keyboard=True)

ColorHairKbB1 = KeyboardButton('Блонд')
ColorHairKbB2 = KeyboardButton('Черный')
ColorHairKbB3 = KeyboardButton('Рыжий (натурал.)')
ColorHairKbB4 = KeyboardButton('Рыжий (ненатурал.)')
ColorHairKbB5 = KeyboardButton('Руссый')

ColorHairKb.row(ColorHairKbB1, ColorHairKbB2)
ColorHairKb.add(ColorHairKbB5)
ColorHairKb.row(ColorHairKbB3, ColorHairKbB4)


EmKb = ReplyKeyboardMarkup(resize_keyboard=True)

EmKbB1 = KeyboardButton('Да, делал(а)')
EmKbB2 = KeyboardButton('Нет, не делал(а)')

EmKb.add(EmKbB1, EmKbB2)


LenKb = ReplyKeyboardMarkup(resize_keyboard=True)

LenKbB1 = KeyboardButton('До плеч')
LenKbB2 = KeyboardButton('До лопаток')
LenKbB3 = KeyboardButton('Ниже лопаток')
LenKbB4 = KeyboardButton('До До талии')

LenKb.row(LenKbB1, LenKbB2)
LenKb.row(LenKbB3, LenKbB4)