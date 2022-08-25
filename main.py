import emoji
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import Dispatcher

btn1 = KeyboardButton(emoji.emojize('Map of event :world_map:'))
btn2 = KeyboardButton(emoji.emojize('Choose a rat :rat:'))
btn3 = KeyboardButton(emoji.emojize('Programm :page_facing_up:'))
btn4 = KeyboardButton(emoji.emojize('Information :speaking_head:'))
navbtn = KeyboardButton(emoji.emojize('Navigation :compass:'))
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1,btn2,btn3,btn4,navbtn)

btn5 = KeyboardButton(emoji.emojize(':red_heart:'))
btn6 = KeyboardButton(emoji.emojize(':person_gesturing_NO:'))
secMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn5,btn6)

btn7 = KeyboardButton(emoji.emojize(':check_mark_button:'))
btn8 = KeyboardButton(emoji.emojize(':stop_sign:'))
trdMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn7,btn8)

MMbtn = KeyboardButton(emoji.emojize('To main menu :up_arrow:'))
ToMMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(MMbtn)