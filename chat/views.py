from django.shortcuts import redirect, render
from .models import User


# Create your views here.
def index(request):
    user_id = request.session.get('user_id')
    user_name = User.objects.get(id = user_id)

    ul = User.objects.exclude(id = user_id)

    rl = {}

    # 고유한 주소 생성
    # for u in ul:
    #     s = str(user_name) + str(u.username) 
    #     sorted(s)
    #     rl[u.id] = s     

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