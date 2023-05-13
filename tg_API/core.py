from settings import TGSettings
from site_API.utils.site_api_hendler import SiteApiInterface
from site_API.core import method, url, headers
from aiogram import Bot, Dispatcher, executor, types
from tg_API.keyboard.keyboard_core import KeyboardInterface

tg = TGSettings()

boty = Bot(tg.tg_api_key.get_secret_value())

bot = Dispatcher(boty)

keyboard = KeyboardInterface.keyboarding()


@bot.message_handler(commands=['low'])
async def _choose_coin(message: types.Message):
    await message.answer('Уточните, пожалуйста:', reply_markup=keyboard)


@bot.callback_query_handler(text=['Qwsogvtv82FCd', 'razxDUgYGNAdQ', 'D7B1x_ks7WhV5', 'a91GCGd_u96cF'])
async def _coin_lower_price(call: types.CallbackQuery):
    if call.data == 'Qwsogvtv82FCd':
        await call.answer('Qwsogvtv82FCd')
    if call.data == 'razxDUgYGNAdQ':
        await call.answer('razxDUgYGNAdQ')
    if call.data == 'D7B1x_ks7WhV5':
        await call.answer('D7B1x_ks7WhV5')
    if call.data == 'a91GCGd_u96cF':
        await call.answer('a91GCGd_u96cF')

    coins = SiteApiInterface.get_coin()
    response = coins(method, url, headers, call.data, 3)
    response = response.json()

    result = min(response['data']['history'], key=lambda feature: feature['price'])
    answer = result['price']

    await call.message.answer(f'Наименьшая цена за сегодня: {answer} $')


@bot.message_handler(commands=['hello-world'])
async def _start(message: types.Message):
    await message.answer('Hello Hello!!!')


@bot.message_handler(content_types=['text'])
async def _greetings(message: types.Message):
    if message.text == 'Привет' or message.text == 'привет':
        await message.answer('Привет Привет!!!')


class TGCoreInterface():

    @staticmethod
    def coin_lower_price():
        return _coin_lower_price

    @staticmethod
    def choose_coin():
        return _choose_coin

    @staticmethod
    def get_start():
        return _start

    @staticmethod
    def get_greetings():
        return _greetings

    executor.start_polling(bot)


if __name__ == '__main__':
    _start()
    _greetings()
    _choose_coin()
    _coin_lower_price()

    TGCoreInterface()