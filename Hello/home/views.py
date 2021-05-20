from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Contact
from .models import Product
from math import ceil
from datetime import datetime
# Create your views here.
def index(request):
    most_popular = Product.objects.filter(most_popular=True)
    hot_selling = Product.objects.filter(hot_selling = True)
    params = {'product': most_popular, 'products':hot_selling}
    return render(request, 'index.html', params)

def about(request):
    return render(request,'about.html')
     
def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('first')
        name1 = request.POST.get('last')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        contact = Contact(name=name, name1=name1, phone=phone, city=city, date=datetime.today())
        contact.save()
        messages.success(request,'We will contact you soon!!!')
    return render(request, 'contact.html')

def test(request):
    
    most_popular = Product.objects.filter(most_popular=True)
    hot_selling = Product.objects.filter(hot_selling = True)
    params = {'product': most_popular, 'products':hot_selling}
    return render(request, 'test.html', params)

def product(request,myid):
    prod = Product.objects.filter(id=myid)
    parameter = {'prod':prod[0]}
    return render(request,'product.html',parameter)
