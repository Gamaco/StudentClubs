from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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

def clubinformation(request, c_id):
    club = get_object_or_404(Club, id=c_id)
    return render(request, 'clubinformation.html', {
        'club' : club
    })

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
    

def signup(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register
            try:

                #Crear User
                user = User.objects.create_user(
                username=request.POST['email'], 
                password=request.POST['password1'])

                user.save()

                #login
                login(request, user)

                #Redirect to the page shown after logging in.
                return render(request, 'discover.html', {
                    'message': f"User created succesfully {user.get_username()}"
                })
            except:
                #if the username already exists throws exception.
                return render(request, 'auth/signup.html', {
                    'error': 'Username already exists.'
                })
        #In the event that passwords do not match.
        return render(request, 'signup.html', {
            'error': 'Passwords do not match'
        })

@login_required   
def signout(request):
    logout(request)
    return render(request, 'signin.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error' : "Username or password is incorrect"
            })
        else:
            login(request, user)
            return render(request, 'index.html', {
                'form': AuthenticationForm,
                'message' : f"Welcome back {user.get_username()}!"
            })