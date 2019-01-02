import requests
import random
from bs4 import BeautifulSoup


numbers = random.sample(range(800, 838), 8)
for num in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    lucky = soup.select(".ball_645")
    print(f'{num} 회차 당첨번호')

    for i in lucky:
        print(i.text, end=" ")
        count += 1
        if count == 6:
            print("+", end=" ")
    print()

        # numwin = tag.select_one('.win').text
    
       
        # numbonus = tag.select_one('.bonus').text
        # # print(numwin)
        # print(f"{numwin} + {numbonus}")
        
    # lucky = soup.select_one("#article > div:nth-child(2) > div > div.win_result").text
# print(req)

# print(lucky)

# 100 회차 당첨번호
# 1 2 3 4 5 6 + 7



# # 스크래핑
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.naver.com"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')

# for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
#     rank = tag.select_one('.ah_r').text
#     name = tag.select_one('.ah_k').text
#     print(f'{rank}는 {name}입니다.')




# for
# url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=837"
# requests
# BeautifulSoup
# select
# print 몇회차 당첨번호




