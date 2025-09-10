import uuid
from django.db import models
#Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
