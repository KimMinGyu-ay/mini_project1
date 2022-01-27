from unicodedata import name
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('cancel/', views.cancel, name='cancel'),
    path('post/<int:id>', views.detail, name='detail'),
    path('post/<int:id>/delete', views.board_delete, name='board_delete'),
<<<<<<< HEAD
=======
    path('main/', views.main, name='main'),
>>>>>>> 7118e6b06698354108defd2429a26a6dc7c21dc5
    path('post/<int:id>/edit/', views.board_edit, name='board_edit'),
    path('main/',views.main, name='main')
]