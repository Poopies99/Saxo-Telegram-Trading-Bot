from re import M
from subprocess import call
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

def menu_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("View My Positions", callback_data="Positions"),
               InlineKeyboardButton("Create An Order", callback_data="CreateOrder"),
               InlineKeyboardButton("View My Balance", callback_data="ViewBalance"),
            #    InlineKeyboardButton("Create Price Alert", callback_data="CreateAlert"),
               InlineKeyboardButton("View My Price Alerts", callback_data="ViewAlert"))
    return markup

def select_instrument_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("EUR/USD", callback_data="21"),
                InlineKeyboardButton("GBP/USD", callback_data="31"),
                InlineKeyboardButton("USD/CHF", callback_data="39"),
                InlineKeyboardButton("USD/JPY", callback_data="42"),
                InlineKeyboardButton("AUD/USD", callback_data="4"),
                InlineKeyboardButton("NZD/USD", callback_data="37"),
                InlineKeyboardButton("USD/CAD", callback_data="38"))
    return markup

def select_amount():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("100,000", callback_data="100000"),
                InlineKeyboardButton("90,000", callback_data="90000"),
                InlineKeyboardButton("80,000", callback_data="80000"),         
                InlineKeyboardButton("70,000", callback_data="70000"), 
                InlineKeyboardButton("60,000", callback_data="60000"), 
                InlineKeyboardButton("50,000", callback_data="50000"), 
                InlineKeyboardButton("40,000", callback_data="40000"), 
                InlineKeyboardButton("30,000", callback_data="30000"), 
                InlineKeyboardButton("20,000", callback_data="20000"), 
                InlineKeyboardButton("10,000", callback_data="10000"))
    return markup

def select_asset_type():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("FxSpot", callback_data="FxSpot"))
    return markup

def select_buy_sell():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Buy", callback_data="Buy"),
                InlineKeyboardButton("Sell", callback_data="Sell"))
    return markup

def select_order_type():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Market", callback_data="Market"))
    return markup

# def menu_keyboard_markup():
#     markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     markup.add(KeyboardButton(text="View My Positions",),
#                KeyboardButton(text="Create An Order"),
#                KeyboardButton(text="View my Orders"),
#                KeyboardButton(text="Create Price Alert"),
#                KeyboardButton(text="View My Price Alerts"))
#     return markup

# Currency Pair 
"""
1. EUR/USD (Euro Dollar): 21
2. GBP/USD (Pound Dollar): 31
3. USD/CHF (Dollar Swissy): 39
4. USD/JPY (Dollar Yen): 42
5. AUD/USD (Aussie Dollar): 4
6. NZD/USD (Kiwi Dollar): 37
7. USD/CAD (Dollar Loonie): 38
"""