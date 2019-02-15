### 0. 준비사항

1. pyenv / python / pyenv-virtualenv 설치 및 설정

   * python 3.6.7
   * git

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

2. 가상환경 생성

   ```
   python -V : 버전 3.6.7인지 확인
   pyenv virtualenv 3.6.7 django-venv
   pyenv virtualenvs : 목록에서 확인
   ~/workspace 에서 mkdir PROJECT01 만들고 이동, README.md 삭제
   pyenv local django-venv : 가상환경 액티브
   ```

3. 프로젝트 폴더 생성 및 이동

   ```
   
   ```

4. local 가상환경 활성화

   ```
   python -V : 버전 3.6.7인지 확인
   pyenv virtualenv 3.6.7 django-venv
   pyenv virtualenvs : 목록에서 확인
   ~/workspace 에서 mkdir PROJECT01 만들고 이동, README.md 삭제
   pyenv local django-venv : 가상환경 액티브
   ```

5. Django 설치

   ```
   pip install django
   pip install --upgrade pip
   ```

----------------------------------------------

### 1. Django start

##### 1.1 장고 프로젝트

1. 프로젝트 생성

   ```
   django-admin startproject django_intro . : django_intro 폴더와 manage.py 생성 확인
   ```

   > django, test, class, django-test 등은, 프로젝트 이름으로 사용하면 안됩니다.

2.  서버 실행

   ```
   python manage.py runserver $IP:$PORT : manage.py가 있는 위치에서 명령어 입력
   /django_intro/settings.py에서 
   ALLOWED_HOSTS = ['django-intro-hsx3.c9users.io'] 추가 or ['*']
   ```

   > ALLOWED_HOSTS = ['*']
   >
   > ALLOWED_HOSTS = ['example-username.c9users.io']

3.  .gitignore 설정

   ```
   touch .gitignore
   ls -al : 숨김파일까지 확인
   gitignore.io에서 django 검색 후 내용 복사
   .gitignore에 붙여넣기
   ```

4. TIMEZONE / LANGUAGE_CODE 설정

   ```
   LANGUAGE_CODE = 'ko-kr'
   TIME_ZONE = 'Asia/Seoul'
   ```

5. 로켓 페이지 한글화 확인

6. 프로젝트 구조

   `manage.py` : 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

   `프로젝트이름 폴더` : 디렉토리 내부에는 프로젝트를 위한 실제 파이썬 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여 프로젝트 어디서나 파이썬 패키지들을 import 할 수 있습니다.

   `settings.py` : 현재 장고 프로젝트의 모든 환경과 구성을 저장합니다.

   `__init__.py` : 파이썬으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일

   `urls.py` : 현재 장고 프로젝트의 URL 선언을 저장. 사이트의 URL과 VIEWS의 연결을 지정.

   `wsgi.py` : 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점.

----------------------------------------------

##### 1.2 장고 어플리케이션(APP)

* 실제로 특정한 역할을 하는 친구가 바로 APP
* 프로젝트는 이러한 어플리케이션의 집합
* 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있다.
* 각각의 어플리케이션은 MTV 패턴으로 구성되어있다.

1. 어플리케이션 만들기

   ```
   python manage.py startapp home : home 폴더 생성, manage.py가 있는 위치에서 명령어 입력
   ```

2. 어플리케이션 구조

* `admin.py` : 관리자용 페이지 커스터마이징 장소
* `apps.py ` : 앱의 정보가 있는 곳, 우리는 수정할 일이 없습니다.
* `models.py` : 앱에서 사용하는 Model을 정의하는 곳
* `test.py` : 테스트 코드를 작성하는 곳
* `views.py` : 뷰들이 정의되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현하는 곳

3. 어플리케이션 등록

> home > apps.py > class HomeConfig()
>
> `home.apps.HomeConfig`를 settings.py에 등록
>
> 혹은 그냥 `home`이라고 작성 가능. 다만, 추후에 자세한 설정을 할 수 없다.

```
app을 만들면 가장 먼저 수행
settings.py에서 INSTALLED_APPS에 'home.apps.HomeConfig', 추가
> home/apps.py에 HomeConfig 클래스가 있음
```

--------------------

### 2. MTV 패턴

-------------

### 3. view - urls

우리는 앞으로

1. views
2. urls
3. template 순으로 코드를 작성할 겁니다.

* HttpResponse로 첫 리턴값 출력해보기 

* path(route, views,  name) 2개의 필수인수와 1개의 선택 인수

  ```python
  # views.py - 뷰 작성
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

  ```python
  # urls.py - url 등록
  # 위로 쌓아나가자
  from django.contrib import admin
  from django.urls import path
  from home import views # home 디렉토리에 있는 views 불러오기
  
  urlpatterns = [
      path('home/index/', views.index, name='index'), # views에 index함수 실행
      path('admin/', admin.site.urls),
  ]
  ```

* 저녁 메뉴 리턴 실습

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

  ```html
  <!-- templates -->
  <body>
      {% for menu in menus %}
          <p>{{ menu }}</p>    
      {% endfor %}
      <hr>
      {% if menu == '일식' %}
          <p>계란 초밥!</p>
      {% else %}
          <p>{{ menu }}</p>
      {% endif %}
  </body>
  ```

---------------

### 4. Template

- 장고에서 사용되는 템플릿은 DTL(Django Template Language) 이다.
- jinja2와 문법이 유사하지만 다르다.

##### 4.1  Template Variable

* render()
  * render(request, template_name, context=None, 								content_type=None, status=None, using=None)

-------

##### 4.2 Variable Routing

* hello

  ```python
  # views.py
  def hello(request, name):
      return render(request, 'hello.html', {'name': name})
  ```

  ```python
  # urls.py
  path('home/hello/<name>', views.hello, name='hello'),
  ```

  ```html
  <!-- hello.html -->
  <body>
      <h1>{{ name }}, 안녕??</h1>
  </body>
  ```

----------

### 5. Form data (get / post)

request.GET.get('data')

request.POST.get('data')

{% csrf_token %}를 form 안에서 같이 보내줘야 합니다.

> csrf 공격과 같은 보안과 관련된 사항은 settings에 MIDDLEWARE에 있습니다.
>
> 실제로 요청은 MIDDLEWARE 설정 사항들을 순차적으로 거친다.
>
> 응답은 아래에서 위로 거쳐서 응답이 리턴된다.

* PING-PONG 실습 (get)

  ```python
  # views.py - ping
  def ping(request):
      return render(request, 'ping.html')
  ```

  ```python
  # views.py - pong
  def pong(request):
      print(request.GET)
      data = request.GET.get('data')
      return render(request, 'pong.html', {'data': data})
  ```

  ```python
  # urls.py
  path('home/pong/', views.pong, name='pong'),
  path('home/ping/', views.ping, name='ping'),
  ```

  ```html
  <!-- ping -->
  <body>
      <form action="/home/pong">
          <input type="text" name="data"/>
          <input type="submit" value="Submit"/>
      </form>
  </body>
  ```

  ```html
  <!-- pong -->
  <body>
      <h1>퐁~! {{ data }}</h1>
  </body>
  ```

* user 생성 실습 (post)

  ```python
  # views.py - user_new
  def ping(request):
      return render(request, 'ping.html')
  ```

  ```python
  # views.py - user_create
  def pong(request):
      print(request.GET)
      data = request.GET.get('data')
      return render(request, 'pong.html', {'data': data})
  ```

  ```python
  # urls.py
  path('home/user_create/', views.user_create, name='user_create'),
  path('home/user_new/', views.user_new, name='user_new'),
  ```

  ```html
  <!-- user_new.html -->
  <body>
      <!-- POST 방식은 url 뒤에 / 필수! -->
      <form action="/home/user_create/" method="POST">
          {% csrf_token %}
          <input type="text" name="nickname"/>
          <input type="password" name="pwd"/>
          <input type="submit" value="Submit"/>
      </form>
  </body>
  ```

  ```html
  <!-- user_create.html -->
  <body>
      <h1>닉네임 : {{ nickname }}</h1>
      <h2>비밀번호 : {{ pwd }}</h2>
  </body>
  ```

  

------------

### 6. Template Inheritance

* 상속을 위한 base.html 생성

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %}{% endblock %}</title> <!-- 상속을 위해서 -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>
<body>
    <h1>장고 연습</h1>
    <hr>
    <div class="container">
        {% block body %}
        {% endblock %}    
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>
</html
```

* 상속 예시

```html
<!-- inheritance example -->
<!-- hello.html -->
{% extends 'base.html' %}
{% block title %}hello{% endblock %}
{% block body %}
    <h1>{{ name }}, 안녕??</h1>
{% endblock %}
```

