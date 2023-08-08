# 웹사이트 크롤링해서 맛집리스트 만들기

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://www.chicagomag.com/chicago-magazine/january-2023/our-30-favorite-things-to-eat-right-now/'

hdr = {'User-Agent':'Mozilla/5.0'}
req = Request(url, headers=hdr)
page = urlopen(req)
soup = bs(page, 'html.parser')

food_list = []
for item in tmp.find_all('h2'):
    food_list.append(item.text)

restaurant_list = []
for item in tmp.find_all('h3'):
    restaurant_list.append(item.text[3:])

money_list = []
address_list = []
for item in tmp.find_all('p'):
    sample_text = item.get_text()
    idx_of_dollar = sample_text.index('$')
    money = sample_text[idx_of_dollar:].split(' ')[0].strip('.')
    dummy_address = sample_text[idx_of_dollar+len(money)+1:]
    if dummy_address.split(' ')[0] == 'for':
        dummy_address = dummy_address[dummy_address.index('. ')+2:]
    money_list.append(money)
    address_list.append(dummy_address.strip())

df = pd.DataFrame({'food': food_list, 'restaurant': restaurant_list, 'price': money_list, 'address': address_list})


# 테스트
df
