from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def post(request):
    posts = BlogPost.objects.all()
    most_recent_post = BlogPost.objects.order_by("-post_date")[0:1]


    context = {
        'posts':posts,
        'most_recent_post':most_recent_post
        }
    # return render(request, 'blog/posthome.html', context)
    return render(request, 'blog/boostrapbloghome.html', context)