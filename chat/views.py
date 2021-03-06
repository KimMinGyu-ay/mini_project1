from django.shortcuts import redirect, render
from .models import User, Room, Message
from django.db.models import Q

# 메인 화면으로 지정 - 채팅 방 검색
def index(request):

    return render(request, 'chat/index.html',)

def room(request, room_name):
    # 세션에서 로그인된 사용자 id 가져오기
    username = request.session.get('user_id')
    messages = Message.objects.filter(room=room_name)[0:25]

    
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': username,
        'messages': messages
    })