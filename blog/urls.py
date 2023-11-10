
from django.urls import path
from . import views




urlpatterns = [
    path("posts/", views.posts, name='viewposts'),
    path("<int:post_id>/", views.postView, name='post'),
]


