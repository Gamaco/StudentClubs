from .models import *
from django.shortcuts import render

# CRUD and common database interaction functions.

def loadDiscoverPage(request):
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