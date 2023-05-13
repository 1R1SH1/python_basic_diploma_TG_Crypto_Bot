# from database.core import crud
# from site_API.core import method, url, headers
from tg_API.core import TGCoreInterface
import json

results = TGCoreInterface.choose_coin()
result = TGCoreInterface.coin_lower_price()

# tg_bitcoin = TGApiInterface.get_bitcoin()
# tg_ethereum = TGApiInterface.get_ethereum()
# tg_dogecoin = TGApiInterface.get_dogecoin()
# tg_litecoin = TGApiInterface.get_litecoin()

# print(tg_bitcoin)
# print(tg_ethereum)
# print(tg_dogecoin)
# print(tg_litecoin)
# print(city_founding())
# db_write = crud.create()
# db_read = crud.retrieve()

