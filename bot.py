from telebot import TeleBot

bot = TeleBot(token='5456469961:AAHRLzVTU-S4Roe2tKCY3Qd7J7uGm_DHiGo')

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Greetings!")

@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")

bot.polling()