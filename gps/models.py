from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


#메시지 내용
# class Message(models.Model):
#     from_id = models.ForeignKey(
#         User, related_name='chat1', on_delete=models.CASCADE) # 보낸 사람
#     to_id = models.ForeignKey(
#         User, related_name='chat2', on_delete=models.CASCADE) # 보낸 사람
#     content = models.TextField() # 메시지 내용
#     read = models.BooleanField()
#     timestamp = models.DateTimeField(auto_now_add=True) # 메시지 날짜

#     def __str__(self):
#         return self.contact.user.name


# #채팅방

# class Room(models.Model):
#     id = models.BigAutoField(primary_key=True, verbose_name=("Id"))
#     join1 = models.ForeignKey(User, on_delete=models.CASCADE)
#     join2 = models.ForeignKey(User,  on_delete=models.CASCADE) # 방이름
    # timestamp = models.DateTimeField(auto_now_add=True)

# # 메시지
# class Message(models.Model):
#     text = models.TextField()
#     sender = models.ForeignKey(User)
#     thread = models.ForeignKey(Room)
#     datetime = models.DateTimeField(auto_now_add=True, db_index=True)

# user 모델 확장