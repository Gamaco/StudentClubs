from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def discover(request):
    objects = Club.objects.all()
    return render(request, 'discover.html', {
        'clubs' : objects
    })