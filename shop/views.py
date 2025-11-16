from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("This is About Page of My Shop")

def contact(request):
    return HttpResponse("This is Contact Page")

def tracker(requsest):
    return HttpResponse("This is Tracker Page")

def search(requsest):
    return HttpResponse("This is Search Page")

def productview(requsest):
    return HttpResponse("This is Product View Page")

def checkout(request):
    return HttpResponse("This is Checkout Page")