from django.shortcuts import render
from .models import Clothes

# Create your views here.

def index(request):
    return render(request, 'room/index.html')

def room(request, room_name):
    users = Clothes.objects.filter(room=room_name)

    return render(request, 'room/room.html', {'room_name':room_name, 'users':users})