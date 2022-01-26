from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserForm

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():                              
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            form.save()
            return redirect('user_login')
        else:
            return HttpResponse('잘못 입력하였습니다')
    else:
        form = UserForm()
        return render(request, 'video/user_new.html')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request,user)            
            return redirect('/index')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        form = LoginForm()
        return render(request,'video/user_login.html')

def signout(request):
    logout(request)
    return redirect('user_login')        


