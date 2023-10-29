from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'tapcord/home.html', context)


def about_us(request):
    return render(request, 'tapcord/about.html')



def contact(request):
    context = {}
    return render(request, 'tapcord/contact.html', context)


def gallery(request):
    context = {}
    return render(request, 'tapcord/gallery.html', context)


def services(request):
    context = {}
    return render(request, 'tapcord/services.html', context)



def team(request):
    context = {}
    return render(request, 'tapcord/team.html', context)