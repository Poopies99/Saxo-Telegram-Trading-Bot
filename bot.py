from ctypes import resize
from email import message
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import portfolio
import notification
import os

def runBot():
    bot = TeleBot(token=os.getenv('TelegramBot'))

    @bot.message_handler(commands=['Greet'])
    def greet(message):
        bot.send_message(message.chat.id, "Greetings!")
        print(message.chat.id)

    @bot.message_handler(commands=['Hello'])
    def hello(message):
        bot.send_message(message.chat.id, "Hello!")
        print(message.chat.id)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "One":
            bot.answer_callback_query(call.id, "Viewing Positions")
            bot.send_message(os.getenv('ChatID'), "This Works!")
        elif call.data == "Two":
            bot.answer_callback_query(call.id, "Creating Order")
        elif call.data == "Three":
            bot.answer_callback_query(call.id, "Viewing Orders")
        elif call.data == "Four":
            bot.answer_callback_query(call.id, "Creating a Price Alert")
        elif call.data == "Five":
            bot.answer_callback_query(call.id, "Viewing Price Alerts")
        else:
            bot.add_callback_query_handler(call.id, "Invalid Choice")

    @bot.message_handler(func=lambda message: True)
    def message_handler(message):
        bot.send_message(message.chat.id, "How Can I Help You?", reply_markup=menu_markup())

    bot.infinity_polling()


def menu_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("View My Positions", callback_data="One"),
               InlineKeyboardButton("Create An Order", callback_data="Two"),
               InlineKeyboardButton("View My Orders", callback_data="Three"),
               InlineKeyboardButton("Create Price Alert",
                                    callback_data="Four"),
               InlineKeyboardButton("View My Price Alerts", callback_data="Five"))
    return markup


def menu_keyboard_markup():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(KeyboardButton(text="View My Positions"),
               KeyboardButton(text="Create An Order"),
               KeyboardButton(text="View my Orders"),
               KeyboardButton(text="Create Price Alert"),
               KeyboardButton(text="View My Price Alerts"))
    return markup


def test(bot, message):
    @bot.message_handler(commands=["Hello"])
    def hello(message):
        bot.send_message(message.chat.id, "Hello!")
