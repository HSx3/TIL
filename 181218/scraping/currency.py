# import requests
# from bs4 import BeautifulSoup
# import bs4.BeautifulSoup
# from bs4 import BeautifulSoup as bus

# print(requests.get("https://www.naver.com").text)
# print(requests.get("https://www.naver.com").status_code)

# req = requests.get("https://www.naver.com").text
# print(req)

# req = requests.get("https://finance.naver.com/sise/").text
# soup = BeautifulSoup(req,'html.parser')
# kospi = soup.select_one("#KOSPI_now")
# print(kospi.text)


# req = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94").text
# soup = BeautifulSoup(req,'html.parser')
# movie = soup.select_one("#main_pack > div.movie_run.section > div.tab_tx > ul > li.on > a")
# print(movie.text)


# 스크래핑
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank}는 {name}입니다.')