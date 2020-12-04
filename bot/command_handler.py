from bot import tgbot

@tgbot.message_handler()
def echo(msg):
    tgbot.send_message(msg.from_user.id, msg.text)
