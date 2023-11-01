
from django.urls import path
from . import views



urlpatterns = [
    path("Post/", views.post, name='posts'),
    
]


