
from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name='home'),
    path("about-us", views.about_us, name='about_us'),
    path("contact-us", views.contact, name='contact'),
    path("gallery-view", views.gallery, name='gallery'),
    path("our-services", views.services, name='services'),
    # path("team", views.team, name='team'),

    # services
    path("Electrical-services", views.electrical, name='electrical'),
    path("Plumbing-services", views.plumbing, name='plumbing'),
    path("Facility-management-services", views.facility, name='facility'),
    

]



