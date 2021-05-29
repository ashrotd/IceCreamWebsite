from re import A
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Contact
from django.http import JsonResponse;
from .models import Product
from math import ceil
import json
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from rest_framework.parsers import JSONParser


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

def product(request,myid):
    prod = Product.objects.filter(id=myid)
    parameter = {'prod':prod[0]}

    return render(request,'product.html',parameter)

def cartItem(request):
    global finalValue
    if request.method == 'POST':
        data = request.body
        myData = json.loads(data)
    dataKey = myData
    dataDict = dataKey['localId']
    def getList(dict):
        list = []
        for key in dict.keys():
            list.append(key)
            
        return list
    finalValue = getList(dataDict)
    
    return JsonResponse('Checked', safe=False)

class ProductList(APIView):
    
    finalProd = {}
    def get(self, request, format=None):
     
        params = []
        for i in finalValue:
            products = Product.objects.filter(id=i) 
            params += products
        serializers = ProductSerializer(params, many=True)
        return Response(serializers.data)

    
def cartPage(request):
        params = []
        for i in finalValue:
            productItem = Product.objects.filter(id=i)
            params += productItem
        serializers = ProductSerializer(params, many = True)
        parameter = {'finalProd':serializers.data}
        return render(request,'cart.html',parameter)

