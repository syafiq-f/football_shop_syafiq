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
    product_views = models.IntegerField(default=0)

    #sempet ada error krn pas add product gak nambah nambah
    #ternyata harus dibuat function yang ngesave dulu productnya plus ditambahin ke product_views
    def increment_views(self):
        self.product_views += 1
        self.save()

    def __str__(self):
        return self.name
