from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Contact
from datetime import datetime
# Create your views here.
def index(request):
    context = {
        
    }
    return render(request, 'index.html', context)

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