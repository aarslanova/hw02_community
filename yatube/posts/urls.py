from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница:
    # если получен запрос без относительного адреса
    # (то есть это запрос к имени домена, например anfisa.com),
    # будет вызвана функция index() из файла views.py
    path('', views.index, name='index'),
    # Страница со списком групп
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
