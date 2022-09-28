from django.shortcuts import render

# Create your views here.

def index(request, room_name):
    
    render(request, "index.html")

def room(request, room_name):
    
    return render(request, 'chatroom.html', {
        'room_name' : room_name
    })
