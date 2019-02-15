### Django

MTV 구조 - model, template, view

하나의 프로젝트가 여러 개의 앱을 가지고 있는 구조. 앱도 MTV 구조

django의 마무리는 , (쉼표)

@app.route() > urls.py

def index() > view.py



순서 : 처리할 views(controller) > 요청 urls > 결과 보여줄 templates



* zzu.li/djpy2_c9 에서 세팅

```
# install pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
pyenv rehash


# install pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
```

* git 설정

```
git config --global --list : user.name / user.email 체크
```


* 가상환경 설정

```
python -V : 버전 3.6.7인지 확인
pyenv virtualenv 3.6.7 django-venv
pyenv virtualenvs : 목록에서 확인
~/workspace 에서 mkdir PROJECT01 만들고 이동, README.md 삭제
pyenv local django-venv : 가상환경 액티브
```

* django 설치

```
pip install django
pip install --upgrade pip
```

------------------------------

* 프로젝트 생성

```
django-admin startproject django_intro . : django_intro 폴더와 manage.py 생성 확인
```

* 서버 on

```
python manage.py runserver $IP:$PORT : manage.py가 있는 위치에서 명령어 입력
/django_intro/settings.py에서 
ALLOWED_HOSTS = ['django-intro-hsx3.c9users.io'] 추가 or ['*']
```

* git ignore

```
touch .gitignore
ls -al : 숨김파일까지 확인
gitignore.io에서 django 검색 후 내용 복사
.gitignore에 붙여넣기
```

* 서버 설정 on settings.py

```
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

* 폴더정리

```
tree
```

---------------------------------

* app 생성

```
python manage.py startapp home : home 폴더 생성, manage.py가 있는 위치에서 명령어 입력
```

* home 구조

```
admin.py : 관리자용 페이지를 커스터마이징하는 곳
apps.py : 앱의 정보가 있는 곳
models.py : db 정의하는 곳
tests.py : testcode 작성하는 곳, model에 반영 x
views.py : view들이 정의되며, 사용자들에게 어떻게 보여질지 정의되는 곳
```

* app 등록

```
app을 만들면 가장 먼저 수행
settings.py에서 INSTALLED_APPS에 'home.apps.HomeConfig', 추가
> home/apps.py에 HomeConfig 클래스가 있음
```

-------------------

* view 작성

```python
from django.shortcuts import render, HttpResponse
# from pprint import pprint

# Create your views here.
def index(request):     # request
    # print(request)
    # print(type(request))
    # pprint(request.META)    # http 정보 확인
    return HttpResponse('Welcome to Django!') 
	# view를 만들었지만 url이 없으므로 urls.py로 이동
```

* url 등록

```python
# 위로 쌓아나가자
from django.contrib import admin
from django.urls import path
from home import views # home 디렉토리에 있는 views 불러오기

urlpatterns = [
    path('home/index/', views.index, name='index'), # views에 index함수 실행
    path('admin/', admin.site.urls),
]
```

----------

* dinner 추가

```python
# views.py
from django.shortcuts import render, HttpResponse
import random

def dinner(request):
    menu = ['한식', '중식', '일식', '양식']
    return HttpResponse(random.choice(menu))
```

```python
# urls.py
from django.contrib import admin
from django.urls import path
from home import views # home 디렉토리에 있는 views 불러오기

urlpatterns = [
    path('home/dinner/', views.dinner, name='dinner'), # name 없어도 ok, name='test' ok
    path('home/index/', views.index, name='index'), # views 에 index함수 실행
    path('admin/', admin.site.urls),
]
```

----------------

* cube 페이지

```python
# views.py
def cube(request, num):
    nums = num ** 3
    return render(request, 'cube.html', {'num': num, 'nums': nums})

# urls.py
path('home/cube/<int:num>', views.cube, name='cube'),

# cube.html
# <h1>{{ num }}의 세제곱은 {{ nums }}</h1>
```

------------

* ping-pong

```python
# views.py
def ping(request):
    return render(request, 'ping.html')

def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data': data})

# urls.py
path('home/pong/', views.pong, name='pong'),
spath('home/ping/', views.ping, name='ping'),
```

```html
<!-- ping -->
<body>
    <form action="/home/pong">
        <input type="text" name="data"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
    
<!-- pong -->
<body>
	<h1>퐁~! {{ data }}</h1>    
</body>
```

-----------

* POST 방식으로 user 생성 (ping-pong)

```python
# views.py
def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'nickname': nickname, 'pwd': pwd})

# urls.py
path('home/user_create/', views.user_create, name='user_create'),
path('home/user_new/', views.user_new, name='user_new'),
```

```html
<!-- user_new.html -->
<form action="/home/user_create/" method="POST"> <!-- POST 방식은 url 뒤에 / 필수! -->
    {% csrf_token %}
    <input type="text" name="nickname"/>
    <input type="password" name="pwd"/>
    <input type="submit" value="Submit"/>
</form>

<!-- user_create.html -->
<h1>닉네임 : {{ nickname }}</h1>
<h2>비밀번호 : {{ pwd }}</h2>
```



