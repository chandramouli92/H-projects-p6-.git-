from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>HELLO EVERY ONE</h1>")

def home(request):
    return render(request,"myapp1/sample.html")

def child(request):
    return render(request,"child.html")
def base(request):
    return render(request,"myapp1/base.html")

def cm(request):
    return render(request,"myapp1/cm.html")
