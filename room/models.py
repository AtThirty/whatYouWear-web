from django.db import models
from colorfield.fields import ColorField

class Rooms(models.Model):
    room = models.CharField(max_length=255)
    number = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room
    class Meta:
        ordering = ('created_at',)

# Create your models here.
class Clothes(models.Model):
    number = models.IntegerField()
    username = models.CharField(max_length=255)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    top = ColorField(default='#000000')
    bot = ColorField(default='#ffffff')

    def __str__(self):
        return str(self.room)+"/"+self.username
