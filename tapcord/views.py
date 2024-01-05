from django.shortcuts import render, redirect
from .models import Gallery, NewsLetterMember

from blog.models import BlogPost
from .forms import ContactForm
from django.core.mail import send_mail





def home(request):
    

    featured_posts = BlogPost.objects.filter(featuredpost=True)
    important_posts = BlogPost.objects.filter(important_post=True)
    
    featured_galary = Gallery.objects.filter(featuredimage=True)
    success_msg = ""
    e= ""
    msg=""
    myform = ContactForm()

    
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
            e= "Your message was successfully sent we would reply you shortly"
            msg=e
            return redirect('home')
        else:
            myform = ContactForm()
    if msg:
        success_msg = msg
    
    # news_letter_form = NewsLetterMember()
    
    if request.method == "POST":
        news_letter_form=NewsLetterMember(request.POST)
        
        news_letter_form.save()

        return redirect('home')
        
    else:
        news_letter_form = NewsLetterMember()

    news_letter_form = NewsLetterMember()
    context = {
        'featured_galary':featured_galary,
        'news_letter_form':news_letter_form,
        'featured_posts':featured_posts,
        "important_posts":important_posts,
        'myform':myform,
        'success_msg':success_msg
        }
    return render(request, 'tapcord/home.html', context)


def about_us(request):
    return render(request, 'tapcord/about.html')



def contact(request):
    msg = ""
    success_msg = ""
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
            e= "Your message was successfully sent we would reply you shortly"
            msg=e
            return redirect('home')
        else:
            myform = ContactForm()
    if msg:
        success_msg = msg
    
    myform = ContactForm()

    context = {
        'success_msg':success_msg,
        'myform':myform,
    }
    return render(request, 'tapcord/contact.html', context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {'gallery':gallery}
    return render(request, 'tapcord/gallery.html', context)


def services(request):
    context = {}
    return render(request, 'tapcord/services.html', context)



def electrical(request):
    context = {}
    return render(request, 'tapcord/electrical.html', context)


def plumbing(request):
    context = {}
    return render(request, 'tapcord/plumbing.html', context)


def facility(request):
    context = {}
    return render(request, 'tapcord/facility.html', context)