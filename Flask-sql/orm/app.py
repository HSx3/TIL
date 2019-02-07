import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy # 모델과 분리하는 경우 주석처리
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)

# flask app에 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'    # db_flask는 생성될 파일명
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ['SQLALCHEMY_TRACK_MODIFICATIONS'] = True sqlalchemy 데이터베이스 객체 수정 및 신호 방출 등을 추적합니다. 과도한 메모리를 사용하기 때문에 False.

# sqlalchemy 초기화
# db = SQLAlchemy(app)  # 모델과 분리하는 경우 주석처리
db.init_app(app)    

migrate = Migrate(app, db)

@app.route('/')
# 뷰 함수
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/create')
# orm 동작시켜주는 페이지
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)
    
@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    
    user.username = username
    user.email = email
    db.session.commit()
    
    return redirect(url_for('index'))

'''
# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User '{self.username}'>"
'''




if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)