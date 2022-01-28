from django.shortcuts import redirect, render
from .models import User, Room, Message
from django.db.models import Q

# Create your views here.
def index(request):
    # 세션에서 로그인된 사용자 id 가져오기
    user_id = request.session['user_id']
    rooms = Room.objects.all()

    return render(request, 'chat/index.html', {})

def room(request, room_name):
    user_id = request.session.get('user_id')
    username =  User.objects.get(id = user_id).username
    messages = Message.objects.filter(room=room_name)[0:25]

    
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': username,
        'messages': messages
    })

def blank(request):
    return render(request, 'chat/blank.html')