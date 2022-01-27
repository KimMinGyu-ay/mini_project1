from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.signin, name='user_login'),
    path('signup/', views.signup, name='user_signup'),
    path('logout/', views.signout, name='user_logout'),
   
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)