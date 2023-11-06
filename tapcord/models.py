from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField()
    featuredimage = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    

class NewsLetterMember(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email