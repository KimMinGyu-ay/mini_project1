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
<<<<<<< HEAD
    path('post/<int:id>/edit/', views.board_eitd, name='board_update'),
=======
    path('post/<int:id>/update/', views.board_update, name='board_update'),
>>>>>>> parent of c804160 (feat: templates,urls,vies.board_edit 취소구현)
=======
    path('post/<int:id>/update/', views.board_update, name='board_update'),
>>>>>>> parent of c804160 (feat: templates,urls,vies.board_edit 취소구현)
]