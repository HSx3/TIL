```bash
hsx3:~/workspace $ cd PROJECT02
(django-venv) hsx3:~/workspace/PROJECT02 $ c9 open .gitignore
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py startapp boards
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py makemigrations boards                                                                                                                   
Migrations for 'boards':
  boards/migrations/0001_initial.py
    - Create model Board
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py sqlmigrate boards 0001
BEGIN;
--
-- Create model Board
--
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
COMMIT;
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py makemigrations boards
No changes detected in app 'boards'
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py makemigrations boards
Migrations for 'boards':
  boards/migrations/0002_board_updated_at.py
    - Add field updated_at to board
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, boards, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying boards.0001_initial... OK
  Applying boards.0002_board_updated_at... OK
  Applying sessions.0001_initial... OK
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py sqlmigrate boards 0002
BEGIN;
--
-- Add field updated_at to board
--
ALTER TABLE "boards_board" RENAME TO "boards_board__old";
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "updated_at" datetime NOT NULL, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
INSERT INTO "boards_board" ("id", "title", "content", "created_at", "updated_at") SELECT "id", "title", "content", "created_at", '2019-02-20 10:12:21.043529' FROM "boards_board__old";
DROP TABLE "boards_board__old";
COMMIT;
(django-venv) hsx3:~/workspace/PROJECT02 $ sqlite3 db.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
auth_group                  boards_board              
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session            
auth_user_user_permissions
sqlite> .schema boards_board
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
sqlite> .exit
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py shell
Python 3.6.7 (default, Feb 13 2019, 00:35:42) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from boards.models import Board
>>> Board.objects.all()
<QuerySet []>
>>> board = Board()
>>> board.title = 'first'
>>> board.content = 'django!'
>>> board.save()
>>> Board.objects.all()
<QuerySet [<Board: Board object (1)>]>
>>> exit()
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py shell
Python 3.6.7 (default, Feb 13 2019, 00:35:42) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from boards.models import Board
>>> Board.objects.all()
<QuerySet [<Board: 1: first>]>
>>> exit()
(django-venv) hsx3:~/workspace/PROJECT02 $ pip install django-extensions
Collecting django-extensions
  Downloading https://files.pythonhosted.org/packages/bf/91/840de20b263525af1585194eb8339a8f6d077f8b9698c80332d28f7a3200/django_extensions-2.1.5-py2.py3-none-any.whl (218kB)
    100% |████████████████████████████████| 225kB 7.7MB/s 
Collecting six>=1.2 (from django-extensions)
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Installing collected packages: six, django-extensions
Successfully installed django-extensions-2.1.5 six-1.12.0
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py shell_plus
# Shell Plus Model Imports
from boards.models import Board
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.6.7 (default, Feb 13 2019, 00:35:42) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> board = Board(title='second', content='django!!')
>>> board.save()
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>]>
>>> Board.objects.create(title='third', content='django!!!')
<Board: 3: third>
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>]>
>>> board = Board()
>>> board.title = 'fourth'
>>> board.content = 'django!!!!'
>>> board.id
>>> board.created_at
>>> board.save()
>>> board.id
4
>>> board.created_at
datetime.datetime(2019, 2, 20, 10, 35, 32, 151972)
>>> board.title = 'asdfjlkadflkn'
>>> board.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/ubuntu/.pyenv/versions/django-venv/lib/python3.6/site-packages/django/db/models/base.py", line 1152, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 13 자).']}
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
>>> Board.objects.filter(title='first').all()
<QuerySet [<Board: 1: first>]>
>>> Board.objects.filter(title='first').first()
<Board: 1: first>
>>> Board.objects.filter(title='missing').first()
>>> board = Board.objects.get(pk=1)
>>> board
<Board: 1: first>
>>> board = Board.objects.filter(id=1)
>>> board
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(title__contains='fi').all()
>>> boards
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(title__startswith='fi')
>>> boards
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(title__endswith='!')
>>> boards
<QuerySet []>
>>> boards = Board.objects.filter(content__endswith='!')
>>> boards
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
>>> boards = Board.objects.order_by('-title').all()
>>> boards
<QuerySet [<Board: 3: third>, <Board: 2: second>, <Board: 4: fourth>, <Board: 1: first>]>
>>> board = Board.objects.get(pk=1)
>>> board.title = 'hello'
>>> board.save()
>>> board.title
'hello'
>>> board.delete()
(1, {'boards.Board': 1})
>>> exit()
(django-venv) hsx3:~/workspace/PROJECT02 $ python manage.py createsuperuser
사용자 이름 (leave blank to use 'ubuntu'): admin
이메일 주소: hs.ssafy@gmail.com
Password: 
Password (again): 
비밀번호가 너무 일상적인 단어입니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(django-venv) hsx3:~/workspace/PROJECT02 $ 
```

