from django.db import models
from datetime import datetime



class Author(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    post = models.ForeignKey('BlogPost', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    featuredpost = models.BooleanField(default=False)
    important_post = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.title
    

    def shotend_desc(self):
        return self.description[:200] + '...'

    def mid_shotend_desc(self):
        return self.content[:1000] + '...'

    def get_comments(self):
        return self.comments.all().order_by('-time_stamp')

    
    def comment_count(self):
        return BlogPost.objects.filter(post=self).count()