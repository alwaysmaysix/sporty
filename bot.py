#!/usr/bin/env python
import config
import telebot
import traceback
from telebot import types
from datetime import date
from flask import Flask, request, jsonify

# new bot instance
bot = telebot.TeleBot(config.api_key)

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello, I am Sporty the Soccer Bot! 🤖⚽'

def bot_polling():
    try:
        print("Starting bot polling now. New bot instance started!")
        bot.polling(none_stop=True, interval=config.bot_interval, timeout=config.bot_timeout)
    except Exception as ex:
        print("Bot polling failed, restarting. Error:\n{}".format(ex))
        bot.stop_polling()
        traceback.print_exc()
        sleep(config.bot_timeout)
        bot_polling()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚽ Soccer', 'Help')
    msg = 'Hello, I\'m Sporty 🤖! Use me to get the latest soccer information.'
    bot.send_message(message.chat.id, msg, reply_markup=user_markup)

@bot.message_handler(regexp="Help")
def command_help(message):
    help_text = "Send my creator a message if you need help with anything."
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(regexp="⚽ Soccer")
def send_soccer(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row('🏴 England', '🇫🇷 France')
    user_markup.row('🇩🇪 Germany', '🇮🇹 Italy')
    user_markup.row('🇪🇸 Spain', '🇺🇸 United States')
    bot.send_message(message.chat.id, 'Choose a league:', reply_markup=user_markup)

# Define each country's league section with scores and tables
# Example for England
@bot.message_handler(regexp="🏴 England")
def send_england(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row('EPL Scores', 'EPL Table')
    bot.send_message(message.chat.id, 'English Premier League scores and table:', reply_markup=user_markup)

@bot.message_handler(regexp="EPL Scores")
def send_eplscores(message):
    d = date.today()
    # Assuming you have a function to fetch EPL scores
    epl_scores = "Mock data for EPL scores on " + str(d)
    bot.reply_to(message, epl_scores)

@bot.message_handler(regexp="EPL Table")
def send_epltable(message):
    # Assuming you have a function to fetch EPL table
    epl_table = "Mock data for EPL table"
    bot.reply_to(message, epl_table)

# Handler for France - Ligue 1
@bot.message_handler(regexp="🇫🇷 France")
def send_france(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Ligue 1 Scores', 'Ligue 1 Table')
    bot.send_message(message.chat.id, 'French Ligue 1 scores and table:', reply_markup=user_markup)

@bot.message_handler(regexp="Ligue 1 Scores")
def send_ligue1_scores(message):
    d = date.today()
    # Replace the following with actual data fetching logic
    ligue1_scores = "Mock data for Ligue 1 scores on " + str(d)
    bot.reply_to(message, ligue1_scores)

@bot.message_handler(regexp="Ligue 1 Table")
def send_ligue1_table(message):
    # Replace the following with actual data fetching logic
    ligue1_table = "Mock data for Ligue 1 table"
    bot.reply_to(message, ligue1_table)

# Handler for Germany - Bundesliga
@bot.message_handler(regexp="🇩🇪 Germany")
def send_germany(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Bundesliga Scores', 'Bundesliga Table')
    bot.send_message(message.chat.id, 'German Bundesliga scores and table:', reply_markup=user_markup)

@bot.message_handler(regexp="Bundesliga Scores")
def send_bundesliga_scores(message):
    d = date.today()
    bundesliga_scores = "Mock data for Bundesliga scores on " + str(d)
    bot.reply_to(message, bundesliga_scores)

@bot.message_handler(regexp="Bundesliga Table")
def send_bundesliga_table(message):
    bundesliga_table = "Mock data for Bundesliga table"
    bot.reply_to(message, bundesliga_table)

# Handler for Italy - Serie A
@bot.message_handler(regexp="🇮🇹 Italy")
def send_italy(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Serie A Scores', 'Serie A Table')
    bot.send_message(message.chat.id, 'Italian Serie A scores and table:', reply_markup=user_markup)

@bot.message_handler(regexp="Serie A Scores")
def send_serie_a_scores(message):
    d = date.today()
    serie_a_scores = "Mock data for Serie A scores on " + str(d)
    bot.reply_to(message, serie_a_scores)

@bot.message_handler(regexp="Serie A Table")
def send_serie_a_table(message):
    serie_a_table = "Mock data for Serie A table"
    bot.reply_to(message, serie_a_table)

# Handler for Spain - La Liga
@bot.message_handler(regexp="🇪🇸 Spain")
def send_spain(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row('La Liga Scores', 'La Liga Table')
    bot.send_message(message.chat.id, 'Spanish La Liga scores and table:', reply_markup=user_markup)

@bot.message_handler(regexp="La Liga Scores")
def send_la_liga_scores(message):
    d = date.today()
    la_liga_scores = "Mock data for La Liga scores on " + str(d)
    bot.reply_to(message, la_liga_scores)

@bot.message_handler(regexp="La Liga Table")
def send_la_liga_table(message):
    la_liga_table = "Mock data for La Liga table"
    bot.reply_to(message, la_liga_table)

# Handler for the United States - Major League Soccer (MLS)
@bot.message_handler(regexp="🇺🇸 United States")
def send_unitedstates(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.row('MLS Scores', 'MLS Table')
    bot.send_message(message.chat.id, 'MLS scores and table:', reply_markup=user_markup)

@bot.message_handler(regexp="MLS Scores")
def send_mls_scores(message):
    d = date.today()
    mls_scores = "Mock data for MLS scores on " + str(d)
    bot.reply_to(message, mls_scores)

@bot.message_handler(regexp="MLS Table")
def send_mls_table(message):
    mls_table = "Mock data for MLS table"
    bot.reply_to(message, mls_table)

if __name__ == "__main__":
    bot.polling()
