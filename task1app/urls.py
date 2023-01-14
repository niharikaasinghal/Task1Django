from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='index'), 
    path('login',views.login, name='login'),
    path('register',views.register , name='register')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)