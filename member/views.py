from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .forms import UserForm

def signup(request):
    if request.method == 'POST':        
        if request.POST['password1'] == request.POST['password2']:
            new_user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
            login(request, new_user)            
            return redirect('user_login')
        else:
            return HttpResponse('잘못 입력하였습니다')
    else:        
        return render(request, 'video/user_new.html')

def signin(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request,user)
            request.session['user_id'] = user.id           
            return redirect('/main')
        else:
            return HttpResponse('ERROR: Username or Password is incorrent.')
    else:        
        return render(request,'video/user_login.html')

def signout(request):
    logout(request)
    return redirect('user_login')        


