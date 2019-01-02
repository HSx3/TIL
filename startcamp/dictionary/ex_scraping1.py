# 스크래핑
import requests
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/index.nhn"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

# for tag in soup.select('.intnl_major_item'):
for tag in soup.select('.item_lst'):
    rank = tag.select_one('.stock_item').text
    name = tag.select_one('.stock_price').text
    print(f'{rank}는 {name}입니다.')
    print(type(rank))
# print(tag)


