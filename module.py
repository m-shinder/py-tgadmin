#!/usr/bin/env python3
from bot import tgbot

if __name__=="__main__":
    tgbot.polling(none_stop=True, interval=1)
