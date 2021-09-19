from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Clothes, Rooms
import json

# Create your views here.

def index(request):
    return render(request, 'room/index.html')

def room(request, room_name):
    users = Clothes.objects.filter(room__room=room_name)
    return render(request, 'room/room.html', {'room_name':room_name, 'users':users})

def detail(request, room_name, number):
    user = Clothes.objects.filter(room__room=room_name).get(number=number)
    return render(request, 'room/detail.html', {'room_name':room_name, 'user':user})

def add_user(request, room_name):
    if request.method == "POST":
        users = Clothes.objects.filter(room__room=room_name)
        max = -1
        for u in users:
            if max < u.number:
                max = u.number
        number = max + 1

        rooms = Rooms.objects.get(room=room_name)
        clothes = Clothes()
        clothes.number = number
        clothes.username = "민수"
        clothes.room = rooms
        clothes.save()

        return HttpResponse(status=200)

    else:
        return HttpResponse(status=404)

def modify_user(request, room_name, number):
    if request.method == "PUT":
        body = json.loads(request.body)
        name = body["name"]
        color1 = body["color1"]
        color2 = body["color2"]
        user = Clothes.objects.filter(room__room=room_name).get(number=number)
        user.username = name
        user.top = color1
        user.bot = color2
        user.save()
        return HttpResponse(status=200)    

    elif request.method == "DELETE":
        user = Clothes.objects.filter(room__room=room_name).get(number=number)
        user.delete()
        room = Rooms.objects.get(room=room_name)
        room.number -= 1
        room.save()
        return HttpResponse(status=200)
        
    else:
        return HttpResponse(status=404)

def make_room(request):
    name_li = ["은종", "서빈", "진호", "동훈"]
    if request.method == "POST":
        body = json.loads(request.body)
        room = body["room"]
        number = body["number"]

        rooms = Rooms()
        rooms.room = room
        rooms.number = number
        rooms.save()

        for i in range(int(number)):
            rooms = Rooms.objects.get(room=room)
            clothes = Clothes()
            clothes.number = i
            clothes.username = name_li[i]
            clothes.room = rooms
            clothes.save()

        return HttpResponse(status=200)
    
    else:

        return HttpResponse(status=404)