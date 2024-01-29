import random
import telebot
from telebot.types import ReplyKeyboardMarkup, Message as m, InputMediaPhoto
import runes
import text

bot = telebot.TeleBot("Token")


def create_start_keyboard():
    keyboard = ReplyKeyboardMarkup(True, True)
    keyboard.row("Магический шар", "Хрустальный шар")
    keyboard.row("Книга «Гадаем на кофейной гуще»", "Руны")
    return keyboard


@bot.message_handler(['start'])
def bot_start(msg: m):
    bot.send_message(msg.chat.id, text.welcome_msg, reply_markup=create_start_keyboard())
    bot.register_next_step_handler(msg, start_handler)


def start_handler(msg: m):
    if msg.text == "Магический шар":
        magic_ball(msg)
    elif msg.text == "Хрустальный шар":
        bot.send_document(msg.chat.id, open("magicball.gif", 'rb'), caption="Купи хрустальный шар и всё узнаешь")
        bot_start(msg)
    elif msg.text == "Книга «Гадаем на кофейной гуще»":
        bot.send_document(msg.chat.id, open("book.gif", 'rb'), caption="Купи книгу и всё прочитаешь")
        bot_start(msg)
    elif msg.text == "Руны":
        runes_divination(msg)
    else:
        bot_start(msg)


def magic_ball(msg: m):
    keyboard = ReplyKeyboardMarkup(True, True)
    keyboard.row("Узнать ответ")
    keyboard.row("Вернуться назад")
    bot.send_message(msg.chat.id, "Задай свой вопрос!", reply_markup=keyboard)
    bot.register_next_step_handler(msg, magic_ball_handler)


def magic_ball_handler(msg: m):
    if msg.text == "Вернуться назад":
        bot_start(msg)
        return

    bot.send_message(msg.chat.id, text.get_magic_ball_phrase())
    magic_ball(msg)


def runes_divination(msg: m):
    runes_list = []
    for _ in range(3):
        runes_list.append(random.choice(tuple(runes.runes_files.items())))
    caption = ""
    for key in runes_list:
        caption += f"{key[0]} — {runes.runes[key[0]]}\n\n"
    media = []
    for n, rune in enumerate(runes_list):
        media.append(InputMediaPhoto(open(rune[1], 'rb'), caption if n == 0 else None))
    bot.send_media_group(msg.chat.id, media)
    bot_start(msg)


bot.infinity_polling()
