from django.shortcuts import render, redirect
from .models import Gallery

from blog.models import BlogPost
from .forms import ContactForm
from django.core.mail import send_mail





def home(request):
    
    success_msg = ""
    msg=""
    myform = ContactForm()


    posts = BlogPost.objects.all()
    
    if request.method == 'POST':
        myform = ContactForm(request.POST)
        if myform.is_valid():
            subject = myform.cleaned_data['name']
            
            message = myform.cleaned_data['message']
            print(message)
            contact_number = myform.cleaned_data['contact_number']
            sender = myform.cleaned_data['email']
            print(sender)
            
            
            
            recipients = ['frank4everreal@gmail.com', 'myfran4everreal@gmail.com']
            
            # if message:
                # recipients.append(sender)
            send_mail(f'{subject}', f'{message}', f'{sender}', ['frankmadu2live@gmail.com'])



            print('form is save successfully')
            msg= "Your message was successfully sent we would reply you shortly"
            
            return redirect('home')
        else:
            myform = ContactForm()
    
    success_msg = msg
    context = {
        'posts':posts,
        'myform':myform,
        'success_msg':success_msg
        }
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