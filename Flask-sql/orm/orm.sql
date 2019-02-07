python
from app import *

-- CREATE

-- SQL의 INSERT문과 같다.
-- INSERT INTO users(username, email)
-- VALUES ('babo', 'example@gmail.com')
user = User(username='babo', email='example@gmail.com')

db.session.add(user)
db.session.commit()
user.username -- username 확인
user.email  -- email 확인

-- READ

-- SELECT * FROM users;
users = User.query.all()
users -- users 확인

-- SELECT * FROM users WHERE username='babo';
users = User.query.filter_by(username='babo').all()

-- SELECT * FROM users WHERE username='babo' LIMIT 1;
users = User.query.filter_by(username='babo').first()

-- 값이 없으면 None
miss = User.query.filter_by(username='ssafy').first()
type(miss) -- None 확인

-- Get one by id:
-- PRIMARY KEY만 get으로 가져올 수 있음.
-- SELECT * FROM users WHERE id=1;
user = User.query.get(1)

-- LIKE
users = User.query.filter(User.email.like('%exam%')).all()
users = User.query.limit(1).offset(2).all()

-- UPDATE
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit() -- UPDATE에서는 add 생략
user.username -- UPDATE 확인

-- DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()