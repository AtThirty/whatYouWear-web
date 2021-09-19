from django.contrib import admin
from .models import Clothes, Rooms


class RoomAdmin(admin.ModelAdmin):
    list_display = ['room', 'number', 'created_at']

admin.site.register(Rooms, RoomAdmin)
admin.site.register(Clothes)
