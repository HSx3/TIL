from flask import Flask, render_template, request
import os
import datetime
import requests
from bs4 import BeautifulSoup
import csv
# import redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello there!'

# 5월 20일부터 d-day 카운트 출력
@app.route('/dday')
def dday():
    now = datetime.datetime.now()
    vacation = datetime.datetime(2019, 5, 20)
    return f'{(vacation - now).days}일 남았습니다.'
    
# variable routing
@app.route('/hi/<string:name>')
def greeting(name):
    # return f'안녕, {name}'
    # greeting.html로 위처럼 안녕 누구누구를 출력해주세요.
    return render_template('greeting.html', html_name=name)




    
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다.'
    
# 반복문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)

# fake google
@app.route('/google')
def google():
    return render_template('google.html')

# ping-pong
@app.route('/ping')
def ping():
    return render_template('ping.html')
    
@app.route('/pong')
def pong():
    pongname = request.args.get('pingname')
    # pongname = request.args['pingname'] : 에러를 출력하기때문에 사용하지 않음.
    msg = request.args.get('msg')
    return render_template('pong.html', html_name=pongname, msg=msg)
    
    
@app.route("/ping_new")
def ping_new():
    return render_template('ping_new.html')
    
@app.route("/pong_new", methods=['POST'])
def pong_new():
    name = request.form.get('name')
    msg = request.form.get('msg')
    return render_template('pong_new.html', name=name, msg=msg)
    
    
# opgg
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')
    
@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    return render_template('opgg_result.html', username=username, wins=wins.text, loses=loses.text)
    

# CSV
@app.route('/timeline')
def timeline():
    # 1. username / message
    # 2. 지금까지 기록되어있는 방명록들을 보여주자!
    timeline = []
    with open('timeline.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            timeline.append(row)
    return render_template('timeline.html', timeline=timeline)
    # return redirect('/timeline')
    
    
    
    # with open('timeline.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     dic = {}
    #     for row in reader:
    #         dic.update({row['username'] : row['message']})
    # return render_template('timeline.html', dic=dic)

@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    with open('timeline.csv', 'a', newline='', encoding='UTF-8') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writer = csv.DictWriter(f, fieldnames=['username', 'message'])
        writer.writerow({'username': username, 'message': message})
    return render_template('timeline_create.html', username=username, message=message)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
