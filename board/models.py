from django.db import models

# Create your models here.


# Create your models here.
class Board(models.Model):
    #board_id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=10, null=False) # 작성자 이름 
    title = models.CharField(max_length=100, null=False) # 게시판 제목
    content = models.TextField(null=False) # 내용
    created_date = models.DateTimeField(auto_now_add=True) # 게시물 시간
    modified_date = models.DateTimeField(auto_now=True) # 수정된 시간

    #number = models.IntegerField(default=0)
    # image 넣어야하는데....

