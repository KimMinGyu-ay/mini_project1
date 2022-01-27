from django.shortcuts import render
from .models import Room, User


# Create your views here.
def index(request):
    user_id = request.session.get('user')
    user_name = User.objects.get(id = user_id)

    ul = User.objects.exclude(id = user_id)

    rl = {}

    for u in ul:
        s = user_name + u.username 
        sorted(s)
        rl[u.id] = s     
    # user에 따른 고유한 채팅방 주소 생성

    return render(request, 'chat/index.html', {
        'me' : user_id,
        'ul' : ul,
        'rl' : rl
    })

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def blank(request):
    return render(request, 'chat/blank.html')