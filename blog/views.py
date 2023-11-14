from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Comment
from .forms import CommentForm

from django.urls.base import reverse
# Create your views here.


def posts(request):
    posts = BlogPost.objects.all()
    most_recent_post = BlogPost.objects.order_by("-post_date")[0:1]

    
    context = {
        
        'posts':posts,
        'most_recent_post':most_recent_post
        }
    # return render(request, 'blog/posthome.html', context)
    return render(request, 'blog/boostrapbloghome.html', context)


def postView(request, post_id):
    # post = BlogPost.objects.get(pk=post_id)
    post = get_object_or_404(BlogPost, id=post_id)

    commentform = CommentForm(request.POST or None)
    if request.method == "POST":
        if commentform.is_valid():
            commentform.instance.post = post
            commentform.save()
            print(f"this is the comment{commentform}")
            return redirect("post", post.id)
            # return redirect(reverse("post", kwargs={
            #     'id':post.pk
            # }))

    
    context = {
        "post":post,
        'commentform':commentform
        }
    return render(request, 'blog/boostrapblogpost.html', context)



