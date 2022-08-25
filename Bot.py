from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import main
import emoji

TOKEN = "5555612366:AAEjBJAX_m7R24tHdlMD_omHp2UBB0WHp1Q"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async  def start(message : types.Message):
    await bot.send_message(message.from_user.id, emoji.emojize('Welcome to our rats show. We hope you will pleasure our animals!') , reply_markup=main.mainMenu)

@dp.message_handler()
async def send_message(message : types.Message):
    if message.text==emoji.emojize('Map of event :world_map:'):
        await message.answer_photo(photo=open('stadiumv2.0.jpg', 'rb'))
    if message.text==emoji.emojize('Choose a rat :rat:'):
        await bot.send_message(message.from_user.id, 'Do you like rats?', reply_markup=main.secMenu)
    if message.text==emoji.emojize('Programm :page_facing_up:'):
        await bot.send_message(message.from_user.id, emoji.emojize(':memo: 10:00-12:00 - you get a regastration form, fill it in and enter to the show\n\n:hot_beverage: 12:00-12:30 - coffiebreak\n\n:mouse: 12:30-14:00 - lessons on rats presenteg at the exhibitoin\n\n:meat_on_bone: 14:00-15:00 - lunch\n\n:partying_face: 15:00-16:00 -the show\n\n:man_cartwheeling: 16:00-18:00 - free time\n\n:teacher: 18:00-19:00 - lesson on rat food\n\n:star-struck: 19:00-20:00 - FEDUK\n\n:waving_hand: Further the end of the event and sayng goodbye to each other'))
    if message.text==emoji.emojize('Information :speaking_head:'):
        await bot.send_message(message.from_user.id, 'You shoul write him\nhttps://vk.com/tivaliyspb')
    if message.text==emoji.emojize('To main menu :up_arrow:'):
        await bot.send_message(message.from_user.id, 'To main menu', reply_markup=main.mainMenu)
    if message.text == emoji.emojize(':red_heart:'):
        await bot.send_message(message.from_user.id, emoji.emojize('Cool! Do you like tails? :upside-down_face:'), reply_markup=main.trdMenu)
    if message.text == emoji.emojize(':person_gesturing_NO:'):
        await bot.send_message(message.from_user.id, 'Cant you like these pretty creations?', reply_markup=main.mainMenu)
        await message.answer_photo(photo=open('hairless_rat.jpg', 'rb'))
    if message.text == emoji.emojize(':check_mark_button:'):
        await bot.send_message(message.from_user.id, 'Oooo! You are a lover of standard rats', reply_markup=main.mainMenu)
        await message.answer_photo(photo=open('standart_rat.jpeg', 'rb'))
    if message.text == emoji.emojize(':stop_sign:'):
        await bot.send_message(message.from_user.id, 'Get your tailes rat', reply_markup=main.mainMenu)
        await message.answer_photo(photo=open('tailes_rat.jpg', 'rb'))
    if message.text == emoji.emojize('Navigation :compass:'):
        await bot.send_message(message.from_user.id, 'Stadium "Zenit", Football al., 1, St.Petersburg\n\nYou can get to the event from 3 metro stations:\n1)Zenit\n2)Krestovskit island\n3)Begovaya')
        await message.answer_photo(photo=open('zenit.jpg', 'rb'))
executor.start_polling(dp, skip_updates=True)
