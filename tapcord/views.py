from django.shortcuts import render
from .models import Gallery

from blog.models import BlogPost










# Create your views here.

def home(request):
    posts = BlogPost.objects.all()

    context = {'posts':posts}
    return render(request, 'tapcord/home.html', context)


def about_us(request):
    return render(request, 'tapcord/about.html')



def contact(request):
    context = {}
    return render(request, 'tapcord/contact.html', context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {'gallery':gallery}
    return render(request, 'tapcord/gallery.html', context)


def services(request):
    context = {}
    return render(request, 'tapcord/services.html', context)



def team(request):
    context = {}
    return render(request, 'tapcord/team.html', context)