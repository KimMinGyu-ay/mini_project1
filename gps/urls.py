from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop_location'),
    path('nav/', views.nav),
] 