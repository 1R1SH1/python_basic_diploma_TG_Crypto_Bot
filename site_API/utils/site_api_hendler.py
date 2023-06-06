from typing import Dict
import requests


def _make_response(method: str, url: str, headers: Dict, timeout: int, success=200):
    response = requests.request(
        method,
        url,
        headers=headers,
        timeout=timeout
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


def _get_coin(method: str, url: str, headers: Dict, coin: str, timeout: int, func=_make_response):

    url = '{}/{}/{}/history'.format(url, 'coin', coin)

    response = func(method, url, headers=headers, timeout=timeout)

    return response


class SiteApiInterface():

    @staticmethod
    def get_coin():
        return _get_coin


if __name__ == '__main__':
    _make_response()
    _get_coin()

    SiteApiInterface()