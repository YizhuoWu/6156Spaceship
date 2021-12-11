
import requests


API_KEY = 'a7ba9dae22dd4951b49770d53ffb61de'
NEWS_URL_PREFIX = 'https://newsapi.org/v2/everything'

# 'https://newsapi.org/v2/everything?q={}&apiKey={API_KEY}'

query = 'twitter'
NEWS_URL = '{}?q={}&apiKey={}'.format(NEWS_URL_PREFIX, query, API_KEY)
response = requests.get(NEWS_URL)

res = response.json()

print(type(res))
print(res['articles'][0])

