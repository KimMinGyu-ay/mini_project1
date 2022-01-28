from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    class Meta:
        db_table = 'room'
        app_label = 'chat'

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
        db_table = 'message'
        app_label = 'chat'