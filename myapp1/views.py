from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>HELLO EVERY ONE</h1>")

def home(request):
    return render(request,"sample.html")

def child(request):
    return render(request,"child.html")