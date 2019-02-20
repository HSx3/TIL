### Django_DTL

* template_example

  ```python
  # views.py
  def template_example(request):
      my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
      my_sentence = 'Life is short. you need python'
      messages = ['apple', 'banana', 'cucumber', 'mango']
      empty_list = []
      return render(request, 'template_example.html', 
                    {'my_list': my_list, 'my_sentence': my_sentence, 
                     'messages': messages, 'empty_list': empty_list})
  ```

  ```python
  # urls.py
  path('home/template_example/', views.template_example, name='template_example'),
  ```

  ```html
  <!-- template_example.html -->
  <body>
      <h3>1. 반복문</h3>
      {% for menu in my_list %}
          <p>{{ menu }}</p>
      {% endfor %}
      <hr>
      {% for menu in my_list %}
          {{ forloop.counter }} <!-- 앞에 번호를 붙여줌 -->
          {% if forloop.first %} <!-- first와 last만 가능 -->
              <p>짜장면+고춧가루</p> 
              <!-- 번호와 붙이고 싶다면, <p>{{ forloop.counter }}. 짜장면 + 고춧가루</p> -->
          {% else %}
              <p>{{ menu }}</p>
          {% endif %}
      {% endfor %}
      <hr>
      {% for user in empty_list %}
          <p>{{ user }}</p>
      {% empty %}
          <p>지금 가입한 회원이 없습니다.</p>
      {% endfor %}
      <hr>
      
      <h3>2. 조건문</h3>
      {% if '짜장면' in my_list %}
          <p>짜장면엔 고춧가루지!</p>
      {% endif %}
      <hr>
      
      <h3>3. length filter 활용</h3>
      {% for message in messages %}
          {% if message|length > 5 %}
              <p>글씨가 너무 길어요.</p>
          {% else %}
              <p>{{ message }}, {{ message|length }}</p>
          {% endif %}
      {% endfor %}
      <hr>
      
      <h3>4. lorem ipsum</h3>
      {% lorem %} <!-- 내장변수이기때문에 %% 필요 -->
      <hr>
      {% lorem 3 w %} <!-- lorem의 세 단어만 출력 -->
      <hr>
      {% lorem 4 w random %} <!-- random으로 lorem 출력 -->
      <hr>
      {% lorem 2 p %} <!-- 문단으로 -->
      <hr>
      
      <h3>5. 글자수 제한</h3>
      <p>{{ my_sentence|truncatewords:3 }}</p>
      <p>{{ my_sentence|truncatechars:5 }}</p> <!-- 공백 ...이 기본값이므로 5부터 첫글자를 출력 -->
      <p>{{ my_sentence|truncatechars:10 }}</p>
      <hr>
      
      <h3>6. 글자 관련 filter</h3>
      <p>{{ 'abc'|length }}</p>
      <p>{{ 'ABC'|lower }}</p>
      <p>{{ my_sentence|title }}</p>
      <p>{{ 'abc def'|capfirst }}</p>
      <p>{{ my_list|random }}</p>
      <hr>
      
      <h3>7. 연산</h3>
      <p>{{ 4|add:6 }}</p>
      <hr>
      
      <h3>8. 날짜 표현</h3>
      {% now "DATETIME_FORMAT" %}       <br>
      {% now "SHORT_DATETIME_FORMAT" %} <br>
      {% now "DATE_FORMAT" %}           <br>
      {% now "SHORT_DATE_FORMAT" %}     <br>
      <hr>
      {% now "Y년 m월 d일 (D) h:i" %}
      <hr>
      {% now "Y" as current_year %}
      Copyright {{ current_year }}
      <hr>
      {{ datetimenow }} <br>
      {{ datetimenow|date:"SHORT_DATE_FORMAT" }}
      <hr>
      
      <h3>9. 기타</h3>
      {{ 'google.com'|urlize }}
  </body>
  ```

  

