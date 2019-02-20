### Separate URL for multiple apps

* 새로운 APP(utilities) 생성

  ```
  python manage.py startapp utilities
  ```

* views 중복 방지

1. home에서 urls.py 생성

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('static_example/', views.static_example, name='static_example'),
       path('template_example/', views.template_example, name='template_example'),
       path('user_create/', views.user_create, name='user_create'),
       path('user_new/', views.user_new, name='user_new'),
       path('pong/', views.pong, name='pong'),
       path('ping/', views.ping, name='ping'),
       path('cube/<int:num>', views.cube, name='cube'),
       path('hello/<name>/', views.hello, name='hello'),
       path('dinner/', views.dinner, name='dinner'),
       path('index/', views.index, name='index'), # views 에 index함수 실행
   ]
   ```

2. home의 urls.py 수정

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('utilities/', include('utilities.urls'))
       path('home/', include('home.urls')), # views 에 index함수 실행
       path('admin/', admin.site.urls),
   ]
   ```

-----------



