### django - models

`python manage.py makemigrations boards` : migrations를 만드는 명령어

`migrations 파일` : 아직 db에 반영되지않은 설계도

`python manage.py sqlmigrate boards 0001` : migrations 파일을 sql문으로 확인하는 명령어

`python manage.py migrate` : 설계도를 db에 반영

`sqlite3 db.sqlite3` : db로 들어가는 명령어

`.tables` : table 목록

`.schema 테이블명` : 테이블명의 schema 확인

------------------

#### django ORM

`python manage.py shell` : django의 shell 실행

`from boards.models import Board` : 

`Board.objects.all()` : SELECT와 같다

`board.full_clean()` : 한글로 에러 확인

* Create

  `board = Board()`

  `board.title = 'first'`

  `board.content = 'django!'`

  `board.save()` : 저장, commit과 같다.

  `Board.objects.all()` : table 내용 확인

  > 두 줄로 끝내기 : `board = Board(title='second', content='django!!')`, `board.save()`
  >
  > 한 줄로 끝내기 : `Board.objects.create(title='third', content='django!!!')`

* Read

  `Board.objects.filter(title='first').all()` : WHERE과 같다.

  `Board.objects.filter(title='missing').first()` : 없는 경우 리턴값은 `None`

  `board = Board.objects.get(pk=1)` : PRIMARY KEY 1을 가져옴, id를 가져오는 경우 filter대신 get을 사용!

  `boards = Board.objects.filter(title__contains='fi').all()` : WHERE + LIKE

  `boards = Board.objects.order_by('-title').all()` : 내림차순 정렬

* Update

  `board = Board.objects.get(pk=1)`

  `board.title = 'hello'`

  `board.save()`

  `board.title` : 수정 확인

* Delete

  `board.delete()`

---------------------------

#### django extension

1. `pip install django-extensions` : extensions 설치

2. `settings.py` > `INSTALLED_APPS` > `'django_extensions',` 추가
3. `python manage.py shell_plus` : 자동으로 import가 되어있는 shell