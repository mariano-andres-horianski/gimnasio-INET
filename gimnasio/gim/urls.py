from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'gim'

urlpatterns = [
    path('', views.index, name='index'),
    path('clases', views.lessons, name="lessons"),
    path('rooms',views.rooms, name='rooms'),
    path('new_lesson', views.new_lesson, name="new_lesson"),
    path('new_room', views.new_room, name="new_room")
]