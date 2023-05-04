from settings import TGSettings
from tg_API.utils.tg_api_hendler import TGApiInterface
import telebot

tg = TGSettings()

bot = telebot.TeleBot(tg.tg_api_key.get_secret_value())

# tg_api = TGApiInterface()
#
# if __name__=='__main__':
#     tg_api()

@bot.message_handler(commands=['hello-world'])
def _start(message):
    bot.send_message(message.chat.id, 'Hello Hello!!!')


@bot.message_handler(content_types=['text'])
def _greetings(message):
    if message.chat.type == 'private':
        if message.text == 'Привет':
            bot.send_message(message.chat.id, 'Привет Привет!!!')

class TGCoreIntarface():
    @staticmethod
    def get_start():
        return _start

    @staticmethod
    def get_greetings():
        return _greetings

    bot.polling(none_stop=True)

if __name__=='__main__':
    _start()
    _greetings()

    TGCoreIntarface()