from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    return render(request, 'index.html')


def discover(request):
    gaming_count = Club.objects.filter(category='Gaming')
    hobbies_count = Club.objects.filter(category='Hobbies')
    academic_count = Club.objects.filter(category='Academic')
    sports_count = Club.objects.filter(category='Sports')
    social_count = Club.objects.filter(category='Social')
    objects = Club.objects.all()
    return render(request, 'discover.html', {
        'clubs': objects,
        'social_count': len(social_count),
        'hobbies_count': len(hobbies_count),
        'academic_count': len(academic_count),
        'gaming_count': len(gaming_count),
        'sports_count': len(sports_count),
    })


def joined(request):
    user_id = 1
    clubs = Club.objects.filter(users_id__contains=[user_id])
    return render(request, 'joined.html', {

