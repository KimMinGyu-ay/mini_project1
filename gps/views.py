import re
from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request,'gpsapp/shop.html')

def nav(request):
    return render(request,'gpsapp/nav.html')

