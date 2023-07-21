from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .db_funcs import *

# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def discover(request):
    return loadDiscoverPage(request)

@login_required
def joined(request):
    user_id = 1
    clubs = Club.objects.filter(users_id__contains=[user_id])
    return render(request, 'joined.html', {
        'Clubs' : clubs
    })

@login_required
def clubinformation(request, c_id):
    club = get_object_or_404(Club, id=c_id)
    return render(request, 'clubinformation.html', {
        'club' : club
    })

@login_required
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
                username=request.POST['username'], 
                password=request.POST['password1'],
                first_name=request.POST['fname'],
                last_name=request.POST['lname'],
                email=request.POST['email'])

                # Create a new user profile object
                profile = UserProfile()
                
                # Set user field to the user being created
                profile.user = user
                
                # Add user data
                profile.City = request.POST['city']
                profile.Country = request.POST['country']
                profile.School = request.POST['school']
                
                # Save
                profile.save()

                #login
                login(request, user)

                #Redirect to the page shown after logging in.
                return loadDiscoverPage(request)
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
    return render(request, 'auth/signin.html')


def signin(request):
    if request.method == 'GET':
        print("Get Method Reached")
        return render(request, 'auth/signin.html')
    else:
        print("POST Method Reached")
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth/signin.html')
        else:
            login(request, user)
            return loadDiscoverPage(request)
        
def profile(request):
    return render(request, 'profile.html')