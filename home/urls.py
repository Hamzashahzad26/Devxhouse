# manually creeated file

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('portfolio', views.portfolio, name='portfolio' ),
    path('contact', views.contact, name='contact' ),
    path('about', views.about, name='about' ),
    path('services', views.services, name='services' )

    
]