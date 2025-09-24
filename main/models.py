import uuid
from django.db import models
from django.contrib.auth.models import User
#Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    product_views = models.IntegerField(default=0)
    #artinya setiap produk dimiliki oleh satu user (relasi many-to-one).
    #kalau user dihapus, semua produk miliknya juga ikut dihapus.
    #biar produk yang sudah ada sebelumnya (yang belum punya user) tidak error waktu migrasi. Field ini bisa kosong.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    


    def increment_views(self):
        self.product_views += 1
        self.save()

    def __str__(self):
        return self.name
    



#ngerubah schema kak (lupa) 