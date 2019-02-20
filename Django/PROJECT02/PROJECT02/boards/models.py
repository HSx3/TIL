from django.db import models

# Create your models here.
class Board(models.Model):   # 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현
    title = models.CharField(max_length=10)     # max_length는 charfield의 필수인자
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # default = UTC, Asia/Seoul 시간을 사용하기 위해 settings.py의 use_TZ를 False로 바꿔주자
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now_add=True : 장고 모델의 최초 저장시 현재 날짜를 적용
    # auto_now : 장고 모델을 save 할때마다 현재날짜로 갱신
    
    def __str__(self):
        return f"{self.id}: {self.title}"