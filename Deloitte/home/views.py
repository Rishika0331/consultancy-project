from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render (request,'index.html')

def aboutus(request):
    return render (request,'about.html')

def services(request):
    return render (request,'services.html')

def career(request):
    return render (request,'career.html')

def signup(request):
    return render (request,'login.html')

def login(request):
    return render (request,'login.html')

def contactus(request):
    return render (request,'contact.html')


