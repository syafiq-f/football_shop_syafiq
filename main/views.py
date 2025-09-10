from django.shortcuts import render
from main.models import Product

# ini function untuk dikembalikan ke dalam sebuah template HTML
# yang menampilkan nama aplikasi serta nama dan kelas kamu
def show_main(request):

    if not Product.objects.exists():
        Product.objects.create(
            name="Sepatu Bola",
            price=250000,
            description="Sepatu bola berkualitas tinggi",
            thumbnail="https://senikersku.com/wp-content/uploads/2025/04/Sporty-Rich-adidas-Handball-Spezial-2048x1024.jpg",
            category="Sepatu",
            is_featured=True
        )

    items = Product.objects.all()

    context = {
        "app_name": "Football Shop",   # nama aplikasi
        "name": "Syafiq Faqih",      # ganti dengan nama asli
        "class": "PBP C",    
        "items": items,
    }

    return render(request, "main.html", context)
