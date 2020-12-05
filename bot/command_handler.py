import telebot
from bot import tgbot

@tgbot.message_handler(commands=['ban'], func = lambda m: m.chat.type in ['group', 'supergroup' ] )
def ban(msg):
    if tgbot.get_chat_member(msg.chat.id, msg.from_user.id).status in ['creator', 'administrator']:
        if msg.reply_to_message:
            tgbot.kick_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, 0)
            tgbot.send_message(msg.chat.id, "banned")
        else:
            tgbot.send_message(msg.chat.id, "reply to message")
    else:
        tgbot.send_message(msg.chat.id, "you are not admin")

@tgbot.message_handler(commands=['mute'], func = lambda m: m.chat.type in ['group', 'supergroup' ])
def mute(msg):
    if tgbot.get_chat_member(msg.chat.id, msg.from_user.id).status in ['creator', 'administrator']:
        if msg.reply_to_message:
            permissions = telebot.types.ChatPermissions(can_send_messages=False)
            tgbot.restrict_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, permissions)
            tgbot.send_message(msg.chat.id, "muted")
        else:
            tgbot.send_message(msg.chat.id, "reply to message")
    else:
        tgbot.send_message(msg.chat.id, "you are not admin")

@tgbot.message_handler()
def echo(msg):
    print(msg)
