from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discover/', views.discover, name='discover'),
    path('joined/', views.joined, name='joined'),
    path('club-creation/', views.club_creation, name='club-creation')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)