from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Clothes(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    top = ColorField(default='#000000')
    bot = ColorField(default='#FFFFFF')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room+"/"+self.username

    class Meta:
        ordering = ('created_at',)