from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    featuredpost = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.title
    

    def shotend_desc(self):
        return self.description[:200] + '...'
