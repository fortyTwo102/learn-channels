from turtle import xcor
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from chat.views import room

# helpers
import random, string

# generate random room name
def generate_room_name():
    global room_name
    room_name = ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + "/"

    return room_name

room_name = ''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', lambda request: redirect(generate_room_name(), permanent=False)),
    path('chat/<str:room_name>/', include("chat.urls")),
]