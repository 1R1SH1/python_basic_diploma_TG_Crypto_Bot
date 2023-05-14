from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

button1 = InlineKeyboardButton(text='Bitcoin', callback_data='Qwsogvtv82FCd')
button2 = InlineKeyboardButton(text='Ethereum', callback_data='razxDUgYGNAdQ')
button3 = InlineKeyboardButton(text='Litecoin', callback_data='D7B1x_ks7WhV5')
button4 = InlineKeyboardButton(text='Dogecoin', callback_data='a91GCGd_u96cF')


def _keyboarding():
    keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4)

    return keyboard_inline


class KeyboardInterface():

    @staticmethod
    def keyboarding():
        return _keyboarding()


if __name__ == '__main__':
    _keyboarding()

    KeyboardInterface()