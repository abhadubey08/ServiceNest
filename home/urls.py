from atexit import register
from django.urls import path
from .views import about, contact, home, services, electrician, appliance, plumber, painter, cleaning, carpenter, salon, Login, register, booking_view, custom_logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('about/', about, name='about'),  # About page
    path('services/', services, name='services'),  # Services page
    path('contact', contact, name='contact'),
    path('services/electrician/', electrician, name='electrician'),  # Corrected URL path
     path('services/appliance/', appliance, name='appliance'),
     path('services/plumber/', plumber, name='plumber'),
      path('services/carpenter/', carpenter, name='carpenter'),
     path('services/painter/', painter, name='painter'),
     
     path('services/cleaning/', cleaning, name='cleaning'),
     
     path('services/salon/', salon, name='salon'),
     path('Login/', Login, name='Login'),
     path('register/', register, name='register'),
     path('logout/', custom_logout, name='logout'),
     path('book/', booking_view, name='book_service'),
]