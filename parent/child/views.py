from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1><font color='blue'> Hello, world!</font></h1><br>I am Mummy Jay")

# Create your views here.
