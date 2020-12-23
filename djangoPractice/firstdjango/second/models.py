from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) #이 post 데이터가 생성될 때 자동으로 현재 시간을 추가
    updated_at = models.DateTimeField(auto_now=True) #최근 수정일

    
