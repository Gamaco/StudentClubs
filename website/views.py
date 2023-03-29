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

def joined(request):
    user_id = 1
    clubs = Club.objects.filter(users_id__contains=[user_id])
    return render(request, 'joined.html', {
        'Clubs' : clubs
    })