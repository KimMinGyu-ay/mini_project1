from django.db import models
from django.contrib.auth.models import User

# 채팅방 모델
class Room(models.Model):
    id = models.AutoField(primary_key=True) # 방 id
    name = models.CharField(max_length=20, default="") # 방 이름
    class Meta:
        db_table = 'room'
        app_label = 'chat'

# 메시지 모델
class Message(models.Model):
    id = models.AutoField(primary_key=True) # 메시지 id
    username = models.CharField(max_length=255) # 송신자 이름
    room = models.CharField(max_length=255) # 방 이름
    content = models.TextField(default="") # 내용
    date_added = models.DateTimeField(auto_now_add=True)    # 생성 날짜

    class Meta:
        ordering = ('date_added',)
        db_table = 'message'
        app_label = 'chat'