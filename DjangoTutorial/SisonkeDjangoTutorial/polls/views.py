#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><body><h1>Hello Team</h1></body></html>")

def about(request):
    return HttpResponse("<html><body><h2>We are Sisonke Rising</h2></body></html>")