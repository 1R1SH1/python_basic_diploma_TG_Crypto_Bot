from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

button_low_1 = InlineKeyboardButton(text='Bitcoin', callback_data='low_bitcoin')
button_low_2 = InlineKeyboardButton(text='Ethereum', callback_data='low_etherium')
button_low_3 = InlineKeyboardButton(text='Litecoin', callback_data='low_litecoin')
button_low_4 = InlineKeyboardButton(text='Dogecoin', callback_data='low_dogecoin')

button_high_1 = InlineKeyboardButton(text='Bitcoin', callback_data='high_bitcoin')
button_high_2 = InlineKeyboardButton(text='Ethereum', callback_data='high_etherium')
button_high_3 = InlineKeyboardButton(text='Litecoin', callback_data='high_litecoin')
button_high_4 = InlineKeyboardButton(text='Dogecoin', callback_data='high_dogecoin')

button_custom_1 = InlineKeyboardButton(text='Bitcoin', callback_data='avr_bitcoin')
button_custom_2 = InlineKeyboardButton(text='Ethereum', callback_data='avr_etherium')
button_custom_3 = InlineKeyboardButton(text='Litecoin', callback_data='avr_litecoin')
button_custom_4 = InlineKeyboardButton(text='Dogecoin', callback_data='avr_dogecoin')


def _keyboarding_low():
    keyboard_inline_low = InlineKeyboardMarkup().add(button_low_1, button_low_2, button_low_3, button_low_4)

    return keyboard_inline_low


def _keyboarding_high():
    keyboard_inline_high = InlineKeyboardMarkup().add(button_high_1, button_high_2, button_high_3, button_high_4)

    return keyboard_inline_high


def _keyboarding_custom():
    keyboard_inline_custom = InlineKeyboardMarkup().add(button_custom_1, button_custom_2, button_custom_3,
                                                        button_custom_4)

    return keyboard_inline_custom


class KeyboardInterface():

    @staticmethod
    def keyboarding_low():
        return _keyboarding_low()

    @staticmethod
    def keyboarding_high():
        return _keyboarding_high()

    @staticmethod
    def keyboarding_custom():
        return _keyboarding_custom()


if __name__ == '__main__':
    _keyboarding_low()
    _keyboarding_high()
    _keyboarding_custom()

    KeyboardInterface()