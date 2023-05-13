from settings import SiteSettings
from site_API.utils.site_api_hendler import SiteApiInterface

site = SiteSettings()

url = 'https://api.coinranking.com/v2/'

headers = {
	'x-access-token': site.api_key.get_secret_value()
}

site_api = SiteApiInterface()

method = 'GET'


if __name__ == '__main__':
	site_api()