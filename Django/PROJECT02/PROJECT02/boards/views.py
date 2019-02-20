# 모듈 import 순서
# 1. 파이썬 표준 라이브러리 ex) os, random..
# 2. core django : 장고 프레임워크에 내장되어 있는 것
# 3. 3rd party library ex) pip로 설치한 것들. Beautifulsoup, djangoextension.. 
# 4. 장고 프로젝트 app

from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    # boards = Board.objects.all()[::-1]    # 원래 결과를 파이썬이 변경하는 방식
    boards = Board.objects.order_by('-id')  # db가 정렬을 바꿔서 보내주는 방식
    return render(request, 'boards/index.html', {'boards': boards})
    
def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    board = Board(title=title, content=content)
    board.save()
    
    # Board.objects.create(title=title, content=content)
    
    return redirect('/boards/') # 주소로 이동 가능
    # return redirect(index)    # view 함수명으로 이동 가능