from tg_API.core import TGCoreIntarface

start = TGCoreIntarface.get_start()


# from settings import TGSettings
# import telebot
#
# tg = TGSettings()
#
# bot = telebot.TeleBot(tg.tg_api_key.get_secret_value())
#
#
# @bot.message_handler(commands=['hello-world'])
# def start(message):
#     bot.send_message(message.chat.id, 'Hello Hello!!!')
#
#
# @bot.message_handler(content_types=['text'])
# def greetings(message):
#     if message.chat.type == 'private':
#         if message.text == 'Привет':
#             bot.send_message(message.chat.id, 'Привет Привет!!!')
#
#
# bot.polling(none_stop=True)

# from binance.spot import Spot
#
# client = Spot()
#
# # Get server timestamp
# print(client.time())
# # Get klines of DOGEUSDT at 1m interval
# print(client.klines("DOGEUSDT", "1m"))
# # Get last 10 klines of BNBUSDT at 1h interval
# print(client.klines("BNBUSDT", "1h", limit=10))
#
# # API key/secret are required for user data endpoints
# client = Spot(api_key='<api_key>', api_secret='<api_secret>')
#
# # Get account and balance information
# print(client.account())
#
# # Post a new order
# params = {
#     'symbol': 'BTCUSDT',
#     'side': 'SELL',
#     'type': 'LIMIT',
#     'timeInForce': 'GTC',
#     'quantity': 0.002,
#     'price': 9500
# }
#
# response = client.new_order(**params)
# print(response)