'''Определяет URL схемы для learning_logs'''
from django.conf.urls import url
from . import views

urlpatterns = [
    #URl домашней страницы
    url(r'^$', views.index, name='index'),
    #URL страницы тем
    url(r'^topics/$', views.topics, name='topics'),
    #Страница с подробной информацией по каждой теме
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Страница для создания формы.
    url(r'^new_form/$', views.new_topic, name='new_topic'),
    #Страница для создания записей
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #Cтраница для редактирования записей
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]