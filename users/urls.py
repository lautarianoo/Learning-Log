#Схемы URl для пользователей
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    #Страница входа
    url(r'^login/$', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    #Страницы выхода
    url(r'^logout/$', views.logout_view, name='logout'),
    #Страница регистрации
    url(r'^register/$', views.register, name='register')
]