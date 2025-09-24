from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

#function bawaan yakni decorator to make sure fungsi ini oonly accesible fot those who login
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.all() 
    filter_type = request.GET.get("filter", "all") 

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    context = {
        'app_name': 'Toko Futsal Kalcerz',
        'name': 'Syafiq Faqih', 
        'class': 'PBP C',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never')  
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        #false biar gak langsung post tapi nunggu adjust dari user
        news_entry = form.save(commit = False)
        news_entry.user = request.user
        news_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

#get itu buat ambil data dari database
#post itu buat add data
#delete 
#put
##patch

#masih sama dengan yang ada di tutorial bedanya ini namanya products bukan newqs
@login_required(login_url='/login')
def show_products(request):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_details.html", context)

def show_xml(request):
     news_list = Product.objects.all()
     xml_data = serializers.serialize("xml", news_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    news_list = Product.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")



def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()#abis validasi input datanya di save deh
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

'''METHOD HTTP apa aja?'''
#GET buat baca doang, gak amil or rubah apa apa
#POST masukkin data baru
#PUT itu sebenernya sama kek post tapi dia lebih ke buat ganti ke spesifik data yg alr exist
#PATCH mirip put tapi bedanya dia cuma data yg mau kt ganti aj gak perlu semuanya
#DELETE BUAT NGAPUS
#HEAD → Sama kayak GET tapi cuma ambil header responsenya, tanpa body. Cocok buat cek resource ada atau tidak.
#OPTIONS → Nanya ke server: "Endpoint ini support method apa aja?"
#CONNECT / TRACE → Lebih teknis, jarang dipakai di web app biasa.

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        #ini buat save attempt waktunya
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    #berfungsi untuk menghapus cookie last_login dari daftar cookies di response.
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response