import telebot
import os

tgbot = telebot.TeleBot(os.environ["TG_API_KEY"]);

from bot.command_handler import *
