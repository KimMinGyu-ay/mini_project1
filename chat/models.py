from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# class Room(models.Model):
#     id = models.BigAutoField(primary_key=True, verbose_name=("Id"))
#     join1 = models.ForeignKey(User, on_delete=models.CASCADE)
#     join2 = models.ForeignKey(User,  on_delete=models.CASCADE) # 방이름