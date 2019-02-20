### STATIC

home에서 static 폴더 생성 > img 파일과 css 만들기

* views.py

```python
def static_example(request):
    return render(request, 'static_example.html')
```

* urls.py

```python
path('home/static_example/', views.static_example, name='static_example'),
```

* static_example.html

```html
{% extends 'base.html' %} <!-- extends는 항상 맨 위에! -->

{% load static %}

{% block title %}STATIC{% endblock %}

{% block css %}
    <link rel="stylesheet" href="{% static 'style.css' %}" type="text/css" />
{% endblock %}

{% block body %}
    <img src="{% static 'Django.jpg' %}" alt="image"></img>
{% endblock %}
```

* style.css

```css
h1 {
    color: crimson;
}
```

