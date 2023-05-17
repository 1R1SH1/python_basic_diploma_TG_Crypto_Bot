from settings import TGSettings
from site_API.utils.site_api_hendler import SiteApiInterface
from site_API.core import method, url, headers
from aiogram import Bot, Dispatcher, executor, types
from tg_API.keyboard.keyboard_core import KeyboardInterface

tg = TGSettings()

boty = Bot(tg.tg_api_key.get_secret_value())

bot = Dispatcher(boty)

keyboard_high = KeyboardInterface.keyboarding_high()
keyboard_low = KeyboardInterface.keyboarding_low()
keyboard_custom = KeyboardInterface.keyboarding_custom()


@bot.message_handler(commands=['high'])
async def _higher(message: types.Message):
    await message.answer('Выберите криптовалюту, пожалуйста:', reply_markup=keyboard_high)

    @bot.callback_query_handler(text=['high_bitcoin', 'high_etherium', 'high_litecoin', 'high_dogecoin'])
    async def _high(call: types.CallbackQuery):
        if call.data == 'high_bitcoin':
            cal = 'Qwsogvtv82FCd'
        if call.data == 'high_etherium':
            cal = 'razxDUgYGNAdQ'
        if call.data == 'high_litecoin':
            cal = 'D7B1x_ks7WhV5'
        if call.data == 'high_dogecoin':
            cal = 'a91GCGd_u96cF'

        coins = SiteApiInterface.get_coin()
        response = coins(method, url, headers, cal, 3)
        response = response.json()
        result = max(response['data']['history'], key=lambda feature: feature['price'])
        answer = result['price']
        await call.message.answer(f'Наибольшая цена за сегодня: {answer} $')


@bot.message_handler(commands=['low'])
async def _lower(message: types.Message):
    await message.answer('Выберите криптовалюту, пожалуйста:', reply_markup=keyboard_low)

    @bot.callback_query_handler(text=['low_bitcoin', 'low_etherium', 'low_litecoin', 'low_dogecoin'])
    async def _low(call: types.CallbackQuery):
        if call.data == 'low_bitcoin':
            cal = 'Qwsogvtv82FCd'
        if call.data == 'low_etherium':
            cal = 'razxDUgYGNAdQ'
        if call.data == 'low_litecoin':
            cal = 'D7B1x_ks7WhV5'
        if call.data == 'low_dogecoin':
            cal = 'a91GCGd_u96cF'

        coins = SiteApiInterface.get_coin()
        response = coins(method, url, headers, cal, 3)
        response = response.json()
        result = min(response['data']['history'], key=lambda feature: feature['price'])
        answer = result['price']
        await call.message.answer(f'Наименьшая цена за сегодня: {answer} $')


@bot.message_handler(commands=['custom'])
async def _custom(message: types.Message):
    await message.answer('Выберите криптовалюту, пожалуйста:', reply_markup=keyboard_custom)

    @bot.callback_query_handler(text=['avr_bitcoin', 'avr_etherium', 'avr_litecoin', 'avr_dogecoin'])
    async def _avr(call: types.CallbackQuery):
        if call.data == 'avr_bitcoin':
            cal = 'Qwsogvtv82FCd'
        if call.data == 'avr_etherium':
            cal = 'razxDUgYGNAdQ'
        if call.data == 'avr_litecoin':
            cal = 'D7B1x_ks7WhV5'
        if call.data == 'avr_dogecoin':
            cal = 'a91GCGd_u96cF'

        coins = SiteApiInterface.get_coin()
        response = coins(method, url, headers, cal, 3)
        response = response.json()
        result_min = min(response['data']['history'], key=lambda feature: feature['price'])
        result_max = max(response['data']['history'], key=lambda feature: feature['price'])
        price_min = result_min['price']
        price_max = result_max['price']
        to_float_min = float(price_min)
        to_float_max = float(price_max)
        prices = [to_float_min, to_float_max]
        avr = sum(prices) / 2
        await call.message.answer(f'Средняя цена за сегодня: {avr} $')


@bot.message_handler(commands=['hello-world'])
async def _start(message: types.Message):
    await message.answer('Hello Hello!!!')


@bot.message_handler(content_types=['text'])
async def _greetings(message: types.Message):
    if message.text == 'Привет' or message.text == 'привет':
        await message.answer('Привет Привет!!!')


class TGCoreInterface():

    @staticmethod
    def lower():
        return _lower

    @staticmethod
    def higher():
        return _higher

    @staticmethod
    def custom():
        return _custom

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
    _lower()
    _higher()
    _custom

    TGCoreInterface()