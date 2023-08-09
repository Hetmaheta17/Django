from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contect
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'index.html')
    # return HttpResponse("This is services page")

def contect(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phonenumber = request.POST.get('Phonenumber')
        contect = Contect(name=name, email=email, Phonenumber=Phonenumber, date = datetime.today())
        contect.save()
        messages.success(request, 'your messages sent')
    return render(request, 'contect.html')
    # return HttpResponse("This is contact page")
