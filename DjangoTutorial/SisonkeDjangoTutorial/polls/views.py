#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><body><h1>Hello Team</h1></body></html>")

def about(request):
    return HttpResponse("<html><body><h2>We are Sisonke Rising</h2></body></html>")
    
def tefo(regust):
	return HttpResponse("<html><body><h2>i'm tefo and i'm rising</h2></body></html>")

def jessy(request):
    return HttpResponse("<html><body><h3>Jessy</h3></body></html>")

def brian(request):
    return HttpResponse("<html><body><h3>Brian</h3></body></html>")

def florah (request):
    return HttpResponse("<html><body><h3>I am Florah Weni , a Sisonke Riser .</h3></body></html>")

def vuyisile (request):
    return HttpResponse("<html><body><h3>I am Vuyisile Weni , a Sisonke Riser .</h3></body></html>")
