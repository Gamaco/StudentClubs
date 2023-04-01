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
        'Clubs' : clubs
    })

def clubinformation(request):
    return render(request, 'clubinformation.html')

def club_creation(request):
    if request.method == 'POST':
        data = request.POST
        club_name = data.get("club_name")
        club_category = data.get("category")
        club_description = data.get("description")
        school_name = data.get("school_name")
        club_country = data.get("country")

        # Get the uploaded image file
        image_file = request.FILES.get('image')

        # Create a new Club instance
        new_club = Club.objects.create(
        name=club_name,
        category=club_category,
        description=club_description,
        school=school_name,
        country=club_country,
        image=image_file  # Set the image field to the uploaded file path.
        )
        return render(request, 'joined.html')
    else:
        return render(request, 'club-creation.html')