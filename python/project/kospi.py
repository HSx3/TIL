import requests
from bs4 import BeautifulSoup
# req = requests.get("https://www.google.com/") #.text
# print(req)
# print(req.text)
# print(req.status_code)

# soup = BeautifulSoup.(req, 'html.parser')    # bs가 읽을 수 있게 꾸며줌
# kospi = soup.select_one('경로')
# print(kospi.text)


url = 'https://finance.naver.com/sise/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('#KOSPI_now')

print('현재 코스피 지수는 ' kospi.text)