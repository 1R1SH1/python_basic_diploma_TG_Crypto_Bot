from site_API.utils.site_api_hendler import SiteApiInterface
from site_API.core import method, url, headers
import json


def _get_coins():
    coins = SiteApiInterface.get_coin()
    response = coins(method, url, headers, 'razxDUgYGNAdQ', 4)
    response = response.json()
    print(response)


class TGApiInterface():

    @staticmethod
    def get_coins():
        return _get_coins()


if __name__ == '__main__':
    _get_coins()

    TGApiInterface()